"""Remplit les parties CE2 (parcours A), CM1 (parcours B) et CM2 (parcours C) des fiches du cahier de progrès à partir de cahiers_donnees.py.
Usage :  python3 cahiers.py G H C V O   (familles à mettre à jour)
         python3 cahiers.py 2026        (cahiers « 2026 » de grammaire et de conjugaison, tableaux CE2, CM1 et CM2)
Ensuite, pour refaire un PDF :  soffice --headless --convert-to pdf "fichier.odt" """
import os, sys
from odttool import set_table, table_after, rewrite_odt
from cahiers_donnees import DATA, DATA_CM2, DATA_CE2
R = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
CM1 = os.path.join(R, 'Cahier de progrès cm1') + '/'
TRI = os.path.join(R, 'Cahier de progrès - CE2 - CM1 - CM2') + '/'
args = sys.argv[1:] or sys.exit(__doc__)
for fam in args:
    if fam == '2026':
        def rows(data):
            out, codes = [], []
            for c, code, txt in data:
                out.append((c, code, txt, ', '.join(codes), c.capitalize())); codes.append(code)
            return out
        for name, f in [('Ceintures de grammaire et orth gram 2026 - cahier de progrès.odt', 'G'), ('Ceintures de conjugaison 2026 - cahier de progrès A REFAIRE.odt', 'C')]:
            # Tableau2 = CE2, Tableau1 = CM1, Tableau3 = CM2
            fn = lambda s, f=f: set_table(set_table(set_table(s, 'Tableau1', rows(DATA[f]), extra=3), 'Tableau3', rows(DATA_CM2[f]), extra=3), 'Tableau2', rows(DATA_CE2[f]), extra=3)
            rewrite_odt(CM1 + name, CM1 + name, fn); print('maj', name)
        continue
    if fam == 'O' and not os.path.exists(TRI + 'O - cahier de progrès - CE2 - CM1 - CM2.odt'):
        # première fois : la fiche O (CE2-CM1-CM2) est fabriquée à partir de la fiche V
        def neuf(s):
            s = s.replace('ceintures de vocabulaire', 'ceintures d’orthographe')
            return set_table(s, table_after(s, 'Parcours A'), [(c, '', '') for c, _, _ in DATA['O']])
        rewrite_odt(TRI + 'V - cahier de progrès - CE2 - CM1 - CM2.odt', TRI + 'O - cahier de progrès - CE2 - CM1 - CM2.odt', neuf); print('créé O (CE2-CM1-CM2)')
    for d, name in [(CM1, f'{fam} - cahier de progrès.odt'), (TRI, f'{fam} - cahier de progrès - CE2 - CM1 - CM2.odt')]:
        if os.path.exists(d + name):
            def fn(s, fam=fam):
                s = set_table(s, table_after(s, 'Parcours B'), DATA[fam])
                if fam in DATA_CE2: s = set_table(s, table_after(s, 'Parcours A'), DATA_CE2[fam])
                return set_table(s, table_after(s, 'Parcours C'), DATA_CM2[fam]) if fam in DATA_CM2 else s
            rewrite_odt(d + name, d + name, fn); print('maj', name)
