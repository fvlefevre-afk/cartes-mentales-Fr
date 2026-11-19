"""O12 (« Les adverbes en -ment ») : BANQUE d'exercices écrite à la main (16/11/2026, revue le 19/11/2026 d'après les programmes). État : intégrée par
`python3 o12_banque.py --integrer` (relançable : repart des exercices d'origine).

Décisions d'après les sources (programme du cycle 3 du 17/04/2025 et annexe du cycle 2 : « orthographier les adverbes en -ment » dès la fin du CE2 ; cycle 3 : mots fréquents,
régularités et formation des mots ; docs/dispositif-orthographe-ce2-cm1-cm2.md : O12 en CM1 = découverte avec lentement, vraiment, doucement, poliment ; CM2 = consolidation
+ -amment / -emment avec évidemment, constamment, prudemment) :
  - CM1 : adverbes en -ment fréquents seulement ; AUCUN -emment / -amment (réservés au CM2) ; exceptions -ément limitées à quelques mots (peu de mots fréquents) ;
  - CM2 : l'écran « -emment et -amment » (CM2_PLUS['O12']) reçoit 12 exercices de plus ;
  - mots rares retirés (hardiment, éperdument, obscurément…) ; jamais d'écriture fausse : propositions = FINS de mots (trou de lettres) ou phrases justes sur la règle.
Mots : exercices partagés par CM1 et CM2 dans PLUS['O12'] (5 écrans) ; extras du CM2 dans CM2_PLUS['O12']."""
H = 'hl'
ASK = 'Complète avec la bonne fin.'
def Q(p, bon, autres, hint, ask=ASK):
    return {'p': p, 'tasks': [{'choose': [bon] + autres, 'ok': 0, 'hint': hint, 'ask': ask, 'fill': H}]}
def MENT(p, hint): return Q(p, 'ment', ['ement', 'mant'], hint)
def EMENT(p, hint): return Q(p, 'ément', ['ement', 'ment'], hint)
# écran 1 : le féminin de l'adjectif + -ment
FEM = [MENT('%s___' % f, 'Le féminin « %s » + -ment.' % f) for f in
       ('froide', 'fière', 'sèche', 'fraîche', 'complète', 'joyeuse', 'courageuse', 'naturelle', 'seule', 'certaine', 'sincère', 'longue')]
# écran 2 : l'adjectif finit par une voyelle : + -ment
VOYELLE = [MENT('%s___' % a, 'L’adjectif « %s » finit par %s.' % (a, 'u' if a[-1] == 'u' else 'i' if a[-1] == 'i' else 'é')) for a in
           ('joli', 'poli', 'infini', 'absolu', 'aisé', 'forcé', 'spontané', 'modéré', 'assuré', 'décidé', 'carré', 'passionné')]
# écran 3 : je cherche l'adjectif (il finit par e : le féminin est le même)
ADJ = [MENT('%s___' % a, 'L’adjectif est « %s ».' % a) for a in
       ('rapide', 'facile', 'difficile', 'tranquille', 'utile', 'riche', 'sage', 'juste', 'large', 'libre', 'timide', 'rare')]
# écran 4 : les exceptions en -ément (peu de mots fréquents : seulement quelques exercices de plus)
EXC = [EMENT('profond___', 'profond → profondément.'), EMENT('immens___', 'immense → immensément.'), EMENT('intens___', 'intense → intensément.'),
       EMENT('conform___', 'conforme → conformément.'), EMENT('confus___', 'confus → confusément.')]
# CM2 seulement : -emment (adjectif en -ent) et -amment (adjectif en -ant)
def EM(p, bon, hint): return Q(p, bon, [x for x in ('emment', 'amment', 'ement' if bon == 'emment' else 'ament')], hint)
CM2_EXTRA = [EM('pati___', 'emment', 'L’adjectif « patient » finit par -ent.'), EM('viol___', 'emment', 'L’adjectif « violent » finit par -ent.'),
             EM('réc___', 'emment', 'L’adjectif « récent » finit par -ent.'), EM('fréqu___', 'emment', 'L’adjectif « fréquent » finit par -ent.'),
             EM('appar___', 'emment', 'L’adjectif « apparent » finit par -ent.'), EM('différ___', 'emment', 'L’adjectif « différent » finit par -ent.'),
             EM('innoc___', 'emment', 'L’adjectif « innocent » finit par -ent.'), EM('élég___', 'amment', 'L’adjectif « élégant » finit par -ant.'),
             EM('brill___', 'amment', 'L’adjectif « brillant » finit par -ant.'), EM('méch___', 'amment', 'L’adjectif « méchant » finit par -ant.'),
             EM('cour___', 'amment', 'L’adjectif « courant » finit par -ant.'), EM('puiss___', 'amment', 'L’adjectif « puissant » finit par -ant.')]
# écran 5 : je prouve
R_FEM = lambda f: 'Parce que c’est le féminin « %s » + -ment.' % f
R_VOY = lambda a: 'Parce que « %s » finit par une voyelle : + -ment.' % a
R_EXC = 'Parce que c’est une exception à mémoriser.'
R_ENT = lambda a: 'Parce que l’adjectif « %s » finit par -ent : -emment.' % a
R_ANT = lambda a: 'Parce que l’adjectif « %s » finit par -ant : -amment.' % a
def P(mot, fin, bon, autres, hint):
    return {'p': '', 'tasks': [{'choose': [bon] + autres, 'ok': 0, 'hint': hint, 'ask': 'Pourquoi %s dans « %s » ?' % (fin, mot)}]}
PROUVE = [
 P('froidement', '-ment', R_FEM('froide'), [R_VOY('froid'), R_EXC], 'Cherche l’adjectif.'), P('joliment', '-ment', R_VOY('joli'), [R_FEM('jolie'), R_EXC], 'Cherche l’adjectif.'),
 P('sèchement', '-ment', R_FEM('sèche'), [R_VOY('sec'), R_EXC], 'Cherche l’adjectif.'), P('énormément', '-ément', R_EXC, [R_FEM('énorme'), R_VOY('énorme')], 'Une exception à mémoriser.'),
 P('profondément', '-ément', R_EXC, [R_FEM('profonde'), R_VOY('profond')], 'Une exception à mémoriser.'), P('heureusement', '-ment', R_FEM('heureuse'), [R_VOY('heureux'), R_EXC], 'Cherche l’adjectif.'),
 P('seulement', '-ment', R_FEM('seule'), [R_VOY('seul'), R_EXC], 'Cherche l’adjectif.'), P('absolument', '-ment', R_VOY('absolu'), [R_FEM('absolue'), R_EXC], 'Cherche l’adjectif.'),
 P('fièrement', '-ment', R_FEM('fière'), [R_VOY('fier'), R_EXC], 'Cherche l’adjectif.'), P('aisément', '-ment', R_VOY('aisé'), [R_FEM('aisée'), R_EXC], 'Cherche l’adjectif.'),
 P('vivement', '-ment', R_FEM('vive'), [R_VOY('vif'), R_EXC], 'Cherche l’adjectif.'), P('carrément', '-ment', R_VOY('carré'), [R_FEM('carrée'), R_EXC], 'Cherche l’adjectif.'),
]
BANQUE = {'fem': FEM, 'voyelle': VOYELLE, 'adj': ADJ, 'mem': EXC, 'prouve': PROUVE}
ORDRE = ['fem', 'voyelle', 'adj', 'mem', 'prouve']
PLUS_ORIGINE = 2
def integrer():
    import json, os, re
    chemin = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'index.html')
    s = open(chemin, encoding='utf-8').read()
    m = re.search(r'const PLUS=(\{.*\});\n', s); PLUS = json.loads(m.group(1))
    assert len(PLUS['O12']) == 5, len(PLUS['O12'])
    for k, cle in enumerate(ORDRE):
        orig = PLUS['O12'][k][:PLUS_ORIGINE]
        vus = {json.dumps(e, ensure_ascii=False) for e in orig}
        assert all(json.dumps(e, ensure_ascii=False) not in vus for e in BANQUE[cle]), ('doublon avec un exercice d’origine', cle)
        PLUS['O12'][k] = orig + BANQUE[cle]
    s = s[:m.start(1)] + json.dumps(PLUS, ensure_ascii=False) + s[m.end(1):]
    m2 = re.search(r'const CM2_PLUS=(\{.*\});\n', s); C = json.loads(m2.group(1))
    ec = C['O12']['ecrans'][0]; assert ec['titre'] == '-emment et -amment'
    base = ec['plus'][:2]
    vus = {json.dumps(e, ensure_ascii=False) for e in base + [ec['atoi']]}
    assert all(json.dumps(e, ensure_ascii=False) not in vus for e in CM2_EXTRA), 'doublon CM2'
    ec['plus'] = base + CM2_EXTRA
    s = s[:m2.start(1)] + json.dumps(C, ensure_ascii=False) + s[m2.end(1):]
    open(chemin, 'w', encoding='utf-8').write(s)
    print('O12 : exercices en plus par écran :', {k: len(v) for k, v in BANQUE.items()}, '; CM2 « -emment et -amment » :', len(CM2_EXTRA))
if __name__ == '__main__':
    import sys
    if '--integrer' in sys.argv:
        integrer(); sys.exit(0)
    for k, L in BANQUE.items():
        print('==', k, len(L))
        for e in L:
            t = e['tasks'][0]; print('  ', e['p'] or '(question)', '→', t['choose'][0], '|', t.get('ask', '') if not e['p'] else '', '|', t['hint'])
