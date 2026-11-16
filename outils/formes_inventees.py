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
 # G5, G3, V5
 ('grandissent', 'grandent', 'grandit'): ['grandissent', 'grandit', 'grandissons'],
 ('grandissent', 'grandit', 'grandent'): ['grandissent', 'grandit', 'grandissons'],
 ('choisissez', 'choisisez', 'choisissons'): ['choisissez', 'choisissons', 'choisissent'],
 ('choisissez', 'choisissons', 'choisisez'): ['choisissez', 'choisissons', 'choisissent'],
 ('finissent', 'finit', 'finisent'): ['finissent', 'finit', 'finissons'],
 ('grosse', 'grose', 'gros'): ['grosse', 'gros', 'grosses'],
 ('impossible', 'repossible', 'possiblement'): ['impossible', 'possibilité', 'possiblement'],
 ('mécontent', 'recontent', 'contentement'): ['mécontent', 'contenter', 'contentement'],
 ('illisible', 'relisible', 'lisiblement'): ['illisible', 'lire', 'lisiblement'],
 ('impatient', 'dépatient', 'repatient'): ['impatient', 'patience', 'patiemment'],
 ('désagréable', 'malagréable', 'reagréable'): ['désagréable', 'agrément', 'agréablement'],
 ('malhonnête', 'inhonnête', 'déshonnête'): ['malhonnête', 'honnêteté', 'honnêtement'],
 ('inatteignable', 'désatteignable', 'malatteignable'): ['inatteignable', 'atteindre', 'atteinte'],
 # V3 : mots de la même famille, jamais des mots inventés
 ('refermer', 'défermer', 'fermeur'): ['refermer', 'fermer', 'fermeture'],
 ('maladroit', 'readroit', 'adroitement'): ['maladroit', 'adroitement', 'adresse'],
 ('malheureux', 'reheureux', 'heureusement'): ['malheureux', 'heureusement', 'bonheur'],
 ('impatient', 'dépatient', 'malpatient'): ['impatient', 'patiemment', 'patience'],
 ('illisible', 'délisible', 'mallisible'): ['illisible', 'lisiblement', 'lecture'],
 ('démonter', 'immonter', 'malmonter'): ['démonter', 'montée', 'montagne'],
 ('un nageur', 'une nageoire', 'un nageage'): ['un nageur', 'une nageoire', 'une nage'],
 ('un guitariste', 'une guitare', 'un guitarage'): ['un guitariste', 'une guitare', 'une guirlande'],
 ('buvable', 'buveuse', 'reboire'): ['buvable', 'buveuse', 'boisson'],
 ('un garçonnet', 'un garçonnier', 'un garçonnable'): ['un garçonnet', 'un garçon', 'un garage'],
 ('un chaton', 'un chatier', 'un chatable'): ['un chaton', 'un chat', 'un chantier'],
 ('une maisonnette', 'une maisonner', 'une maisonnable'): ['une maisonnette', 'une maison', 'une maisonnée'],
 ('invisible', 'revisible', 'visiblement'): ['invisible', 'visiblement', 'vision'],
 ('malhonnête', 'déshonnête', 'inhonnête'): ['malhonnête', 'honnêtement', 'honnêteté'],
 ('lisible', 'lisant', 'liser'): ['lisible', 'lecteur', 'lecture'],
 ('mangeable', 'mangeur', 'mangement'): ['mangeable', 'mangeur', 'mangeoire'],
 ('prudemment', 'prudence', 'prudentable'): ['prudemment', 'prudence', 'prudent'],
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
# exercices « Quel GN est bien accordé ? » / « Quelle phrase est bien accordée ? » : on choisit parmi des écritures fausses -> un trou avec de vraies formes
# clé : (question, bonne réponse) ; valeur : (phrase à trou, propositions)
TROUS = {
 ('Quel GN est bien accordé ?', 'les grandes maisons'): ('les ___ maisons', ['grandes', 'grand', 'grande']),
 ('Quel GN est bien accordé ?', 'de jolies fleurs'): ('de ___ fleurs', ['jolies', 'jolie', 'joli']),
 ('Quelle phrase est bien accordée ?', 'Les grandes sœurs sont venues.'): ('Les grandes sœurs sont ___.', ['venues', 'venue', 'venus']),
 ('Quelle phrase est bien accordée ?', 'Les vieux chats sont rentrés.'): ('Les vieux chats sont ___.', ['rentrés', 'rentré', 'rentrées']),
 ('Quelle phrase est bien accordée ?', 'Ma petite cousine est arrivée.'): ('Ma petite cousine est ___.', ['arrivée', 'arrivé', 'arrivées']),
 ('Quelle phrase est bien accordée ?', 'Mes petites sœurs sont arrivées.'): ('Mes petites sœurs sont ___.', ['arrivées', 'arrivée', 'arrivés']),
 ('Quelle phrase est bien accordée ?', 'Les vieilles maisons sont tombées.'): ('Les vieilles maisons sont ___.', ['tombées', 'tombée', 'tombés']),
 ('Quelle phrase est bien accordée ?', 'La grande fille est partie.'): ('La grande fille est ___.', ['partie', 'parti', 'parties']),
 ('Quelle phrase est bien accordée ?', 'Les petits chats sont rentrés.'): ('Les petits chats sont ___.', ['rentrés', 'rentré', 'rentrées']),
 ('Quelle phrase est bien accordée ?', 'Les deux jeunes voisines de ma cousine sont arrivées hier.'): ('Les deux jeunes voisines de ma cousine sont ___ hier.', ['arrivées', 'arrivée', 'arrivés']),
 ('Quelle phrase est bien accordée ?', 'Mes vieux amis du village sont venus me voir.'): ('Mes vieux amis du village sont ___ me voir.', ['venus', 'venu', 'venues']),
 ('Quelle phrase est bien accordée ?', 'Les petites filles de la voisine sont allées au parc.'): ('Les petites filles de la voisine sont ___ au parc.', ['allées', 'allée', 'allés']),
 ('Quelle phrase est bien accordée ?', 'Ma grande sœur et sa meilleure amie sont parties ensemble.'): ('Ma grande sœur et sa meilleure amie sont ___ ensemble.', ['parties', 'partie', 'partis']),
 ('Quelle phrase est bien accordée ?', 'Les petits chiens aboient.'): ('Les petits chiens ___.', ['aboient', 'aboie', 'aboyons']),
 ('Quelle phrase est bien accordée ?', 'Mes jolies fleurs poussent.'): ('Mes jolies fleurs ___.', ['poussent', 'pousse', 'poussons']),
}
EXO = re.compile(r'\{"p": "[^"]*", "tasks": \[\{[^{}]*\}\]\}')
def _trou(m):
    ex = json.loads(m.group(0)); t = ex['tasks'][0]
    r = TROUS.get((t.get('ask'), (t.get('choose') or [''])[0]))
    if not r: return m.group(0)
    return json.dumps({'p': r[0], 'tasks': [{'choose': r[1], 'ok': 0, 'hint': t['hint'], 'ask': 'Complète avec la bonne forme.', 'fill': 'hl'}]}, ensure_ascii=False)
def corriger(chemin=None, bavard=True):
    chemin = chemin or os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'index.html')
    t = open(chemin, encoding='utf-8').read(); n = 0
    for ancien, neuf in REMPLACEMENTS.items():
        a = '"choose": ' + json.dumps(list(ancien), ensure_ascii=False)
        c = t.count(a)
        if c: t = t.replace(a, '"choose": ' + json.dumps(neuf, ensure_ascii=False)); n += c
    t2 = EXO.sub(_trou, t)
    ex = sum(1 for a, b in zip(EXO.findall(t), EXO.findall(t2)) if a != b)
    t = t2; n += ex
    if n: open(chemin, 'w', encoding='utf-8').write(t)
    if bavard or n: print(f'Formes inventées : {n} listes ou exercices remplacés.')
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
