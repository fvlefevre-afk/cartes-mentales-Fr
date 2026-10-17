"""Remplit la partie CM1 (parcours B) des fiches du cahier de progrès à partir de cahiers_donnees.py.
Usage :  python3 cahiers.py G H C V     (familles à mettre à jour)
         python3 cahiers.py 2026        (cahiers « 2026 » de grammaire et de conjugaison, tableau CM1)
Ensuite, pour refaire un PDF :  soffice --headless --convert-to pdf "fichier.odt" """
import os, sys
from odttool import set_table, table_after, rewrite_odt
from cahiers_donnees import DATA
R = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
CM1 = os.path.join(R, 'Cahier de progrès cm1') + '/'
TRI = os.path.join(R, 'Cahier de progrès - CE2 - CM1 - CM2') + '/'
args = sys.argv[1:] or sys.exit(__doc__)
for fam in args:
    if fam == '2026':
        for name, f in [('Ceintures de grammaire et orth gram 2026 - cahier de progrès.odt', 'G'), ('Ceintures de conjugaison 2026 - cahier de progrès A REFAIRE.odt', 'C')]:
            rows, codes = [], []
            for c, code, txt in DATA[f]:
                rows.append((c, code, txt, ', '.join(codes), c.capitalize())); codes.append(code)
            rewrite_odt(CM1 + name, CM1 + name, lambda s, rows=rows: set_table(s, 'Tableau1', rows, extra=3)); print('maj', name)
        continue
    for d, name in [(CM1, f'{fam} - cahier de progrès.odt'), (TRI, f'{fam} - cahier de progrès - CE2 - CM1 - CM2.odt')]:
        if os.path.exists(d + name):
            rewrite_odt(d + name, d + name, lambda s, fam=fam: set_table(s, table_after(s, 'Parcours B'), DATA[fam])); print('maj', name)
