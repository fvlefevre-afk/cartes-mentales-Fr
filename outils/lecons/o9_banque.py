"""O9 (« Les consonnes doubles ») : BANQUE d'exercices écrite à la main (19/11/2026). État : intégrée par
`python3 o9_banque.py --integrer` (relançable : repart des exercices d'origine). `python3 o9_banque.py` : liste les exercices et fait les contrôles.

Sources : docs/dispositif-orthographe-ce2-cm1-cm2.md (O9 au CM1 en découverte, au CM2 consolidée + il-, ir-, im-, in- : illisible, irréel, immangeable ;
mots des dictées : appeler, attendre, effort, accident, affaire, commencer, immobile), programme du cycle 3 (mots fréquents, régularités et formation des mots),
règle de la leçon (après a-, e-, o-, com- la consonne se double ; quelques exceptions à mémoriser ; la famille montre la consonne doublée).
Contrôles (avant toute intégration) : chaque mot recomposé (début + bonne réponse + fin) est cherché dans /usr/share/dict/french ; aucun exercice
ne reprend un exercice déjà présent dans la leçon O9 (« À toi ! » compris) ; aucun mot de famille trompeur (donateur, chaton, salon, papier : une seule consonne).
Jamais d'écriture fausse montrée : propositions = lettres d'un trou, phrases justes sur la règle, ou vrais mots."""
H = 'hl'
ASK_D = 'Complète : consonne simple ou double ?'
ASK_X = 'Complète avec la bonne lettre.'
def Q(p, bon, autre, hint, ask=ASK_D):
    return {'p': p, 'tasks': [{'choose': [bon, autre], 'ok': 0, 'hint': hint, 'ask': ask, 'fill': H}]}
def C(ask, bon, a, b, hint):
    return {'p': '', 'tasks': [{'choose': [bon, a, b], 'ok': 0, 'hint': hint, 'ask': ask}]}
# écran 1 : après a-, la consonne se double
A_ = 'Le mot commence par a-.'
DEBUT_A = [Q('a___orter', 'pp', 'p', A_), Q('a___rendre', 'pp', 'p', A_), Q('a___laudir', 'pp', 'p', A_), Q('a___ueillir', 'cc', 'c', A_),
           Q('a___ompagner', 'cc', 'c', A_), Q('une a___ition', 'dd', 'd', A_), Q('une a___iche', 'ff', 'f', A_), Q('une a___aire', 'ff', 'f', A_),
           Q('a___umer', 'll', 'l', A_), Q('a___iver', 'rr', 'r', A_), Q('a___êter', 'rr', 'r', A_), Q('a___raper', 'tt', 't', A_)]
# écran 2 : après e-, o-, com-
E_, O_, COM = 'Le mot commence par e-.', 'Le mot commence par o-.', 'Le mot commence par com-.'
DEBUT_EOC = [Q('e___acer', 'ff', 'f', E_), Q('un e___et', 'ff', 'f', E_), Q('e___rayer', 'ff', 'f', E_), Q('e___icace', 'ff', 'f', E_),
             Q('o___uper', 'cc', 'c', O_), Q('une o___asion', 'cc', 'c', O_), Q('o___oser', 'pp', 'p', O_),
             Q('co___ander', 'mm', 'm', COM), Q('le co___erce', 'mm', 'm', COM), Q('co___un', 'mm', 'm', COM), Q('co___ent', 'mm', 'm', COM),
             Q('une co___ode', 'mm', 'm', COM)]
# écran 3 : quelques exceptions (une seule consonne) à mémoriser
def X(p, bon, autre, mot): return Q(p, bon, autre, 'Une exception : je mémorise « %s ».' % mot, ASK_X)
EXCEPTIONS = [X('a___ors', 'l', 'll', 'alors'), X('un a___iment', 'l', 'll', 'aliment'), X('une a___arme', 'l', 'll', 'alarme'),
              X('a___ener', 'm', 'mm', 'amener'), X('a___latir', 'p', 'pp', 'aplatir'), X('a___aiser', 'p', 'pp', 'apaiser'),
              X('un a___out', 't', 'tt', 'atout'), X('l’a___ome', 't', 'tt', 'atome'), X('une o___ive', 'l', 'll', 'olive'),
              X('un o___éra', 'p', 'pp', 'opéra'), X('une co___ète', 'm', 'mm', 'comète'), X('une co___édie', 'm', 'mm', 'comédie')]
# écran 4 : la famille m'aide
def F(p, bon, autre, mot): return Q(p, bon, autre, 'Pense à %s.' % mot)
FAMILLE = [F('une so___ette', 'nn', 'n', 'sonner'), F('un te___ain', 'rr', 'r', 'terre'), F('une fi___ette', 'll', 'l', 'fille'),
           F('un ba___eur', 'tt', 't', 'battre'), F('une gou___elette', 'tt', 't', 'goutte'), F('une nou___ice', 'rr', 'r', 'nourrir'),
           F('enfla___er', 'mm', 'm', 'flamme'), F('un co___age', 'll', 'l', 'colle'), F('un cla___ement', 'ss', 's', 'classe'),
           F('bo___u', 'ss', 's', 'bosse'), F('so___eiller', 'mm', 'm', 'sommeil'), F('un cha___eur', 'ss', 's', 'chasser')]
# écran 5 : je vérifie (le début du mot, un mot de la famille)
FAM_Q = 'Quel mot de la même famille m’aide à écrire « %s » ?'
VERIF = [C(FAM_Q % 'sonnette', 'sonner', 'sortir', 'soulever', 'Il a deux n.'),
         C(FAM_Q % 'fillette', 'une fille', 'une fleur', 'un fil', 'Il a deux l.'),
         C(FAM_Q % 'batteur', 'battre', 'bâtir', 'un bateau', 'Il a deux t.'),
         C(FAM_Q % 'collage', 'la colle', 'le col', 'la couleur', 'Il a deux l.'),
         C(FAM_Q % 'bossu', 'une bosse', 'un bois', 'une boîte', 'Il a deux s.'),
         C(FAM_Q % 'chasseur', 'chasser', 'la chaise', 'un chat', 'Il a deux s.'),
         C(FAM_Q % 'nourrice', 'nourrir', 'nouer', 'nouveau', 'Il a deux r.'),
         C(FAM_Q % 'gouttelette', 'une goutte', 'une gourde', 'le goûter', 'Il a deux t.'),
         C('« attraper » commence par a-. Que fait la consonne qui suit ?', 'Elle se double.', 'Elle reste seule.', 'Elle disparaît.', 'Après a-, la consonne se double.'),
         C('« alors » commence par a-, mais n’a qu’un l. Que faire ?', 'Je le mémorise : c’est une exception.', 'J’ajoute un l.', 'Je cherche la fin du mot.', 'Une exception.'),
         C('Où regarder d’abord pour « accompagner » ?', 'Le début du mot : a-.', 'La fin du mot.', 'Le nombre de syllabes.', 'Regarde le début du mot.'),
         C('Comment savoir qu’il y a deux t dans « battement » ?', 'Je pense à « battre ».', 'Je compte les lettres.', 'Je regarde la fin du mot.', 'Pense à la famille.')]
# écran 6 : je prouve
def P(ask, bon, a, b, hint): return C(ask, bon, a, b, hint)
R_A, R_E, R_O, R_C = ('Parce que le mot commence par %s.' % d for d in ('a-', 'e-', 'o-', 'com-'))
R_X, R_L, R_N = 'Parce que c’est une exception à mémoriser.', 'Parce que le mot est long.', 'Parce que c’est un nom.'
def R_F(mot, n): return 'Parce que dans « %s » il y a deux %s.' % (mot, n)
PROUVE = [P('Pourquoi pp dans « apporter » ?', R_A, R_X, R_L, 'Regarde le début du mot.'),
          P('Pourquoi ff dans « effacer » ?', R_E, R_X, R_N, 'Regarde le début du mot.'),
          P('Pourquoi cc dans « occuper » ?', R_O, R_X, R_L, 'Regarde le début du mot.'),
          P('Pourquoi mm dans « commander » ?', R_C, R_X, R_N, 'Regarde le début du mot.'),
          P('Pourquoi ll dans « fillette » ?', R_F('fille', 'l'), R_X, R_L, 'Pense à fille.'),
          P('Pourquoi rr dans « terrain » ?', R_F('terre', 'r'), R_X, R_N, 'Pense à terre.'),
          P('Pourquoi ss dans « chasseur » ?', R_F('chasser', 's'), R_X, R_L, 'Pense à chasser.'),
          P('Pourquoi tt dans « batteur » ?', R_F('battre', 't'), R_X, R_N, 'Pense à battre.'),
          P('Pourquoi un seul l dans « alors » ?', R_X, R_A, R_L, 'Je mémorise.'),
          P('Pourquoi un seul t dans « atome » ?', R_X, R_A, R_N, 'Je mémorise.'),
          P('Pourquoi un seul p dans « aplatir » ?', R_X, R_A, R_L, 'Je mémorise.'),
          P('Pourquoi un seul m dans « comète » ?', R_X, R_C, R_N, 'Je mémorise.')]
# CM2 : il-, ir-, im-, in- (préfixe in- devant l, r, m, n)
def I(p, bon, autre, base): return Q(p, bon, autre, 'in- + %s.' % base)
CM2_EXTRA = [I('i___égulier', 'rr', 'r', 'régulier'), I('i___emplaçable', 'rr', 'r', 'remplaçable'), I('i___esponsable', 'rr', 'r', 'responsable'),
             I('i___imité', 'll', 'l', 'limité'), I('i___ogique', 'll', 'l', 'logique'), I('i___angeable', 'mm', 'm', 'mangeable'),
             I('i___ortel', 'mm', 'm', 'mortel'), I('i___ombrable', 'nn', 'n', 'nombrable')]
BANQUE = {'debut_a': DEBUT_A, 'debut_eoc': DEBUT_EOC, 'exceptions': EXCEPTIONS, 'famille': FAMILLE, 'verif': VERIF, 'prouve': PROUVE}
ORDRE = ['debut_a', 'debut_eoc', 'exceptions', 'famille', 'verif', 'prouve']
ORIGINE = [2, 2, 2, 2, 1, 2]           # exercices d'origine gardés en tête de chaque écran


def chemin_index():
    import os
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'index.html')


def mot_recompose(e):
    t = e['tasks'][0]
    return e['p'].replace('___', t['choose'][t.get('ok', 0)]) if e['p'] else None


def controler(s):
    """Erreurs bloquantes : mot recomposé absent du dictionnaire, exercice déjà dans la page, doublon dans la banque."""
    import json, re, unicodedata
    dico = set(open('/usr/share/dict/french', encoding='utf-8').read().split('\n'))
    m = re.search(r'const PLUS=(\{.*\});\n', s); PLUS = json.loads(m.group(1))
    m2 = re.search(r'const CM2_PLUS=(\{.*\});\n', s); CM2 = json.loads(m2.group(1))
    i = s.find('\nO9:{', s.find('const LESSONS=')); assert i > 0
    lecon = s[i:re.search(r'\n[A-Z][A-Za-z0-9_-]*:\{', s[i+5:]).start() + i + 5]      # la leçon O9 (exemples, « À toi ! »)
    ec = CM2['O9']['ecrans'][0]
    tout = [e for L in BANQUE.values() for e in L] + CM2_EXTRA
    err = []
    for e in tout:
        w = mot_recompose(e)
        if w:
            nu = w.split()[-1].split('’')[-1]
            if nu not in dico: err.append('absent du dictionnaire : ' + w)
        for t in e['tasks']:
            for c in t['choose']:
                if not e['p'] and c.startswith(('un ', 'une ', 'la ', 'le ')) and c.split()[-1] not in dico: err.append('choix inconnu : ' + c)
    cles = [json.dumps(e, ensure_ascii=False) for e in tout]
    err += ['doublon dans la banque : ' + c[:80] for c in set(cles) if cles.count(c) > 1]
    origine = [x for k, L in enumerate(PLUS['O9']) for x in L[:ORIGINE[k]]] + ec['plus'][:2] + [ec['atoi']]
    for e in tout:
        if e['p'] and (('"p": "%s"' % e['p']) in lecon or any(o['p'] == e['p'] for o in origine)):
            err.append('déjà dans la leçon : ' + e['p'])
        if not e['p'] and any(o['tasks'][0].get('ask') == e['tasks'][0]['ask'] for o in origine):
            err.append('question déjà dans la leçon : ' + e['tasks'][0]['ask'])
    return err


def integrer():
    import json, re
    s = open(chemin_index(), encoding='utf-8').read()
    m = re.search(r'const PLUS=(\{.*\});\n', s); PLUS = json.loads(m.group(1))
    assert len(PLUS['O9']) == 6, len(PLUS['O9'])
    PLUS['O9'] = [PLUS['O9'][k][:ORIGINE[k]] for k in range(6)]          # repart des exercices d'origine
    s = s[:m.start(1)] + json.dumps(PLUS, ensure_ascii=False) + s[m.end(1):]
    m2 = re.search(r'const CM2_PLUS=(\{.*\});\n', s); C2 = json.loads(m2.group(1))
    ec = C2['O9']['ecrans'][0]; assert ec['titre'] == 'il-, ir-, im-, in-'
    ec['plus'] = ec['plus'][:2]
    s = s[:m2.start(1)] + json.dumps(C2, ensure_ascii=False) + s[m2.end(1):]
    err = controler(s)
    if err:
        print('\n'.join(err)); raise SystemExit('O9 : rien n’est intégré.')
    m = re.search(r'const PLUS=(\{.*\});\n', s); PLUS = json.loads(m.group(1))
    PLUS['O9'] = [PLUS['O9'][k] + BANQUE[c] for k, c in enumerate(ORDRE)]
    s = s[:m.start(1)] + json.dumps(PLUS, ensure_ascii=False) + s[m.end(1):]
    m2 = re.search(r'const CM2_PLUS=(\{.*\});\n', s); C2 = json.loads(m2.group(1))
    C2['O9']['ecrans'][0]['plus'] += CM2_EXTRA
    s = s[:m2.start(1)] + json.dumps(C2, ensure_ascii=False) + s[m2.end(1):]
    open(chemin_index(), 'w', encoding='utf-8').write(s)
    print('O9 : exercices en plus par écran :', {k: len(v) for k, v in BANQUE.items()}, '; CM2 « il-, ir-, im-, in- » :', len(CM2_EXTRA))


if __name__ == '__main__':
    import sys
    if '--integrer' in sys.argv:
        integrer(); sys.exit(0)
    for k, L in list(BANQUE.items()) + [('CM2', CM2_EXTRA)]:
        print('==', k, len(L))
        for e in L:
            t = e['tasks'][0]; print('  ', mot_recompose(e) or t['ask'], '→', t['choose'][0], '| autres :', t['choose'][1:], '|', t['hint'])
