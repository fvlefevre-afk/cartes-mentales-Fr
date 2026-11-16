"""Jamais de forme inventée proposée aux élèves (décision du 15/11/2026, contrôle du 16/11/2026 au dictionnaire français).
Les exercices de conjugaison proposaient des formes de verbes qui n'existent pas (« prendent », « achettons », « oublirai »…).
Ce module remplace, dans index.html, chaque liste de propositions concernée par de VRAIES formes (le même verbe à une autre personne ou un autre temps),
la bonne réponse restant en premier. Il est appelé à la fin de sans_ecriture_fausse.corriger() (donc par inserer.py, niveaux_lib.py…) : une régénération
des leçons ne remet jamais les formes inventées. À la main : python3 outils/formes_inventees.py (affiche aussi ce qui reste d'inconnu au dictionnaire).
Une nouvelle liste inventée détectée par `controler()` : l'ajouter dans REMPLACEMENTS (ancienne liste -> liste juste)."""
import json, os, re, sys
REMPLACEMENTS = {
 # conjugaison : présent (C1, C6)
 ('appelles', 'appeles', 'appelle'): ['appelles', 'appelle', 'appelons'],
 ('répètent', 'répétent', 'répètes'): ['répètent', 'répète', 'répétons'],
 ('achetons', 'achètons', 'achettons'): ['achetons', 'achète', 'achetez'],
 ('mangeons', 'mangons', 'mangeont'): ['mangeons', 'mangez', 'mangent'],
 ('essuie', 'essuye', 'essuies'): ['essuie', 'essuies', 'essuyons'],
 ('commençons', 'commencons', 'commenceons'): ['commençons', 'commence', 'commencez'],
 ('nettoient', 'nettoyent', 'nettoies'): ['nettoient', 'nettoie', 'nettoyons'],
 ('finissons', 'finons', 'finirons'): ['finissons', 'finissez', 'finirons'],
 ('finissons', 'finons', 'finisons'): ['finissons', 'finissez', 'finirons'],
 ('choisissent', 'choisent', 'choisit'): ['choisissent', 'choisit', 'choisissons'],
 ('dites', 'disez', 'dittes'): ['dites', 'dis', 'disent'],
 ('dites', 'disez', 'disent'): ['dites', 'dis', 'disent'],
 ('vont', 'allent', 'vas'): ['vont', 'va', 'vas'],
 ('prennent', 'prendent', 'prenent'): ['prennent', 'prend', 'prenons'],
 ('prennent', 'prenent', 'prendent'): ['prennent', 'prend', 'prenons'],
 ('voyons', 'voions', 'voyez'): ['voyons', 'voyez', 'voient'],
 ('voyons', 'voions', 'voyont'): ['voyons', 'voyez', 'voient'],
 ('font', 'faisent', 'fait'): ['font', 'fait', 'faites'],
 ('faites', 'faisez', 'faitez'): ['faites', 'fait', 'font'],
 ('faites', 'faisez', 'font'): ['faites', 'fait', 'font'],
 ('pouvons', 'peuvons', 'pouvez'): ['pouvons', 'pouvez', 'peuvent'],
 ('viennent', 'venent', 'vienent'): ['viennent', 'vient', 'venons'],
 ('venons', 'viennons', 'venont'): ['venons', 'venez', 'viennent'],
 ('veulent', 'voulent', 'veut'): ['veulent', 'veut', 'voulons'],
 ('prend', 'prent', 'prends'): ['prend', 'prends', 'prennent'],
 # futur simple (C2, C7)
 ('oublierai', 'oublirai', 'oublie'): ['oublierai', 'oublie', 'oublierons'],
 ('irai', 'allerai', 'vais'): ['irai', 'vais', 'iras'],
 ('feras', 'faireras', 'fais'): ['feras', 'fais', 'fera'],
 ('verrons', 'voirons', 'voyons'): ['verrons', 'voyons', 'verrez'],
 ('viendront', 'veniront', 'viennent'): ['viendront', 'viennent', 'viendra'],
 ('prendrez', 'prenderez', 'prenez'): ['prendrez', 'prenez', 'prendrons'],
 ('dirai', 'direrai', 'dis'): ['dirai', 'dis', 'dira'],
 ('pourra', 'poura', 'pouvra'): ['pourra', 'peut', 'pourront'],
 ('appellerai', 'appelerai', 'appelrai'): ['appellerai', 'appelle', 'appellerons'],
 ('essuieras', 'essuyeras', 'essuiras'): ['essuieras', 'essuies', 'essuiera'],
 ('achèterons', 'acheterons', 'achetrons'): ['achèterons', 'achetons', 'achèterez'],
 ('irons', 'allerons', 'allons'): ['irons', 'allons', 'irez'],
 ('verrai', 'voirai', 'verai'): ['verrai', 'vois', 'verrons'],
 ('prendront', 'prenront', 'prendent'): ['prendront', 'prennent', 'prendra'],
 # imparfait (C3, C7)
 ('grandissaient', 'grandaient', 'grandiront'): ['grandissaient', 'grandiront', 'grandissent'],
 ('finissais', 'finais', 'finirai'): ['finissais', 'finirai', 'finis'],
 ('faisais', 'fairais', 'fais'): ['faisais', 'fais', 'feras'],
 ('voyions', 'voirions', 'voyons'): ['voyions', 'voyons', 'verrons'],
 ('appelais', 'appellais', 'appelai'): ['appelais', 'appelle', 'appellerai'],
 ('levais', 'lèvais', 'levai'): ['levais', 'lèves', 'lèveras'],
 ('essuyions', 'essuiions', 'essuyons'): ['essuyions', 'essuyons', 'essuierons'],
 ('faisais', 'fesais', 'fairais'): ['faisais', 'fais', 'ferais'],
 ('allions', 'vions', 'irions'): ['allions', 'irions', 'allons'],
 ('prenait', 'prendait', 'prennait'): ['prenait', 'prend', 'prendra'],
 # participe passé (C4, C7)
 ('rangé', 'rangi', 'ranger'): ['rangé', 'ranger', 'rangée'],
 ('choisi', 'choisé', 'choisir'): ['choisi', 'choisir', 'choisis'],
 ('remplir', 'remplier', 'remplire'): ['remplir', 'remplacer', 'rentrer'],
 ('attendu', 'attendre', 'attendé'): ['attendu', 'attendre', 'attendue'],
 ('pris', 'prit', 'prendu'): ['pris', 'prit', 'prise'],
 # passé simple (C9)
 ('fit', 'faisa', 'faisit'): ['fit', 'fait', 'fut'],
 ('prirent', 'prenèrent', 'prendirent'): ['prirent', 'prennent', 'prendront'],
 ('vit', 'voya', 'voyit'): ['vit', 'voit', 'verra'],
 ('voulut', 'voulit', 'voula'): ['voulut', 'veut', 'voudra'],
 ('vinrent', 'venirent', 'venèrent'): ['vinrent', 'viennent', 'viendront'],
 ('put', 'pouva', 'pouvit'): ['put', 'peut', 'pourra'],
 ('allèrent', 'allirent', 'allurent'): ['allèrent', 'vont', 'iront'],
 ('dirent', 'disèrent', 'durent'): ['dirent', 'disent', 'diront'],
}
def corriger(chemin=None, bavard=True):
    chemin = chemin or os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'index.html')
    t = open(chemin, encoding='utf-8').read(); n = 0
    for ancien, neuf in REMPLACEMENTS.items():
        a = '"choose": ' + json.dumps(list(ancien), ensure_ascii=False)
        c = t.count(a)
        if c: t = t.replace(a, '"choose": ' + json.dumps(neuf, ensure_ascii=False)); n += c
    if n: open(chemin, 'w', encoding='utf-8').write(t)
    if bavard or n: print(f'Formes inventées : {n} listes de propositions remplacées.')
    return n
def controler(chemin=None):
    """Mots proposés (hors trous de lettres) absents du dictionnaire français : à examiner."""
    chemin = chemin or os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'index.html')
    t = open(chemin, encoding='utf-8').read()
    W = set(l.strip().lower() for l in open('/usr/share/dict/french', encoding='utf-8', errors='ignore'))
    inc = {}
    for m in re.finditer(r'"choose": (\[[^\]]*\])([^{}]*?)(?:"fill": "(\w+)")?[,}]', t):
        try: ch = json.loads(m.group(1))
        except ValueError: continue
        if m.group(3) == 'circ': continue
        for c in ch:
            for w in re.findall(r'[a-zà-ÿœ]+', c):
                if len(w) >= 5 and w not in W: inc[w] = inc.get(w, 0) + 1
    return inc
if __name__ == '__main__':
    corriger(sys.argv[1] if len(sys.argv) > 1 else None)
    reste = controler()
    print(len(reste), 'mots proposés inconnus du dictionnaire :', ', '.join(sorted(reste)[:40]))
