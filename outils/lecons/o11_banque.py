"""O11 (« Les noms en [sjɔ̃] » : -tion, -sion, -ssion) : BANQUE d'exercices écrite à la main (16/11/2026). État : intégré dans index.html par `python3 o11_banque.py --integrer` (relançable : repart des 2 exercices d'origine par écran).

Avant : 3 exercices par écran. Ici : 12 de plus par écran (donc 14 avec les 2 d'origine, plus l'exercice « atoi » d'origine).
Sources des mots : docs/dispositif-orthographe-ce2-cm1-cm2.md (règles O11 : -tion le plus fréquent ; -sion après voyelle quand on entend [z] ; -ssion entre deux voyelles pour [s] ;
le verbe de la famille décide : -quer → -cation, -ter → -tion, -mettre → -mission, -der / -clure / -ser → -sion). Mots courants du cycle 3 seulement ; -xion abandonné (décision du 11/11/2026).
Jamais d'écriture fausse : les propositions sont des FINS de mots (trou de lettres) ou des phrases justes sur la règle.
Aperçu : python3 o11_banque.py"""
H = 'hl'
ASK = 'Complète avec la bonne fin.'
def Q(p, bon, autres, hint, ask=ASK, fill=H):
    t = {'choose': [bon] + autres, 'ok': 0, 'hint': hint, 'ask': ask}
    if fill: t['fill'] = fill
    return {'p': p, 'tasks': [t]}
def F(bon, p, hint):
    autres = [x for x in ('tion', 'sion', 'ssion') if x != bon]
    return Q(p, bon, autres, hint)

# écran 1 : -tion (l'écriture la plus fréquente) ; les verbes en -er donnent -tion
TION = [F('tion', p, h) for p, h in [
 ('une réac___', 'Le plus fréquent : -tion.'), ('une collec___', 'Le plus fréquent : -tion.'), ('la popula___', 'Le plus fréquent : -tion.'),
 ('la direc___', 'Le plus fréquent : -tion.'), ('la situa___', 'Le plus fréquent : -tion.'), ('une récréa___', 'Le plus fréquent : -tion.'),
 ('une invita___', 'Pense à inviter.'), ('la prépara___', 'Pense à préparer.'), ('la décora___', 'Pense à décorer.'),
 ('la créa___', 'Pense à créer.'), ('une répara___', 'Pense à réparer.'), ('une construc___', 'Le plus fréquent : -tion.')]]
# écran 2 : -sion (après une voyelle, j'entends [z]) ; après n : quelques mots à mémoriser
SION = [F('sion', p, h) for p, h in [
 ('la télévi___', 'Après i, j’entends [z].'), ('une révi___', 'Après i, j’entends [z]. Pense à réviser.'), ('la vi___', 'Après i, j’entends [z].'),
 ('une conclu___', 'Après u, j’entends [z]. Pense à conclure.'), ('une explo___', 'Après o, j’entends [z]. Pense à exploser.'), ('une colli___', 'Après i, j’entends [z].'),
 ('une confu___', 'Après u, j’entends [z]. Pense à confondre.'), ('une éva___', 'Après a, j’entends [z]. Pense à s’évader.'), ('une illu___', 'Après u, j’entends [z].'),
 ('une occa___', 'Après a, j’entends [z].'), ('la ten___', 'Après n : un mot en -sion à mémoriser.'), ('la pen___', 'Après n : un mot en -sion à mémoriser.')]]
# écran 3 : -ssion (entre deux voyelles, pour [s])
SSION = [F('ssion', p, h) for p, h in [
 ('une pa___', 'Entre deux voyelles : [s] → ss.'), ('une expre___', 'Entre deux voyelles : [s] → ss.'), ('une impre___', 'Entre deux voyelles : [s] → ss.'),
 ('une se___', 'Entre deux voyelles : [s] → ss.'), ('une commi___', 'Pense à commettre : -ssion.'), ('une émi___', 'Pense à émettre : -ssion.'),
 ('une permi___', 'Pense à permettre : -ssion.'), ('une posse___', 'Entre deux voyelles : [s] → ss. Pense à posséder.'), ('une agre___', 'Entre deux voyelles : [s] → ss.'),
 ('une progre___', 'Entre deux voyelles : [s] → ss.'), ('une dépre___', 'Entre deux voyelles : [s] → ss.'), ('la transmi___', 'Pense à transmettre : -ssion.')]]
# écran 4 : le verbe de la même famille m'aide (verbe → nom)
FAMILLE = [
 Q('décider → une déci___', 'sion', ['tion', 'ssion'], 'Les verbes en -der donnent -sion.'), Q('diviser → une divi___', 'sion', ['tion', 'ssion'], 'diviser : -sion.'),
 Q('conclure → une conclu___', 'sion', ['tion', 'ssion'], 'Les verbes en -clure donnent -sion.'), Q('exploser → une explo___', 'sion', ['tion', 'ssion'], 'exploser : -sion.'),
 Q('émettre → une émi___', 'ssion', ['tion', 'sion'], 'Les verbes en -mettre donnent -ssion.'), Q('transmettre → une transmi___', 'ssion', ['tion', 'sion'], 'Les verbes en -mettre donnent -ssion.'),
 Q('discuter → une discu___', 'ssion', ['tion', 'sion'], 'discuter : -ssion.'), Q('inviter → une invita___', 'tion', ['sion', 'ssion'], 'Les verbes en -er donnent le plus souvent -tion.'),
 Q('animer → une anima___', 'tion', ['sion', 'ssion'], 'animer : -tion.'), Q('organiser → une organisa___', 'tion', ['sion', 'ssion'], 'organiser : -sation, donc -tion.'),
 Q('expliquer → une explica___', 'tion', ['sion', 'ssion'], 'Les verbes en -quer donnent -cation : on écrit -tion après ca.'), Q('communiquer → une communica___', 'tion', ['sion', 'ssion'], 'Les verbes en -quer donnent -cation.'),
]
# écran 5 : je prouve (la bonne règle et deux règles qui ne conviennent pas à ce mot)
def P(mot, bon, a, b, hint, fin):
    return {'p': '', 'tasks': [{'choose': [bon, a, b], 'ok': 0, 'hint': hint, 'ask': 'Pourquoi %s dans « %s » ?' % (fin, mot)}]}
R_Z = 'Parce qu’après la voyelle, j’entends [z].'
R_S = 'Parce qu’entre deux voyelles, [s] s’écrit ss.'
R_T = 'Parce que c’est l’écriture la plus fréquente.'
def verbe(v): return 'Parce que le verbe de la famille est « %s ».' % v
PROUVE = [
 P('télévision', R_Z, R_S, R_T, 'Écoute le son avant -ion.', '-sion'), P('passion', R_S, R_Z, R_T, 'Un seul s ferait [z].', '-ssion'), P('collection', R_T, R_Z, R_S, 'Le plus fréquent.', '-tion'),
 P('permission', verbe('permettre'), R_Z, R_T, 'Cherche le verbe de la famille.', '-ssion'), P('invention', verbe('inventer'), R_Z, R_S, 'Cherche le verbe de la famille.', '-tion'),
 P('discussion', verbe('discuter'), R_Z, R_T, 'Cherche le verbe de la famille.', '-ssion'), P('explosion', R_Z, R_S, R_T, 'Écoute le son avant -ion.', '-sion'),
 P('révision', verbe('réviser'), R_S, R_T, 'Cherche le verbe de la famille.', '-sion'), P('communication', verbe('communiquer'), R_Z, R_S, 'Cherche le verbe de la famille.', '-tion'),
 P('expression', R_S, R_Z, R_T, 'Un seul s ferait [z].', '-ssion'), P('vision', R_Z, R_S, R_T, 'Écoute le son avant -ion.', '-sion'), P('population', R_T, R_Z, R_S, 'Le plus fréquent.', '-tion'),
]
BANQUE = {'tion': TION, 'sion': SION, 'ssion': SSION, 'famille': FAMILLE, 'prouve': PROUVE}
ORDRE = ['tion', 'sion', 'ssion', 'famille', 'prouve']   # les 5 écrans de la leçon, dans l'ordre de PLUS['O11']
PLUS_ORIGINE = 2
def integrer():
    import json, os, re
    chemin = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'index.html')
    s = open(chemin, encoding='utf-8').read()
    m = re.search(r'const PLUS=(\{.*\});\n', s); PLUS = json.loads(m.group(1))
    assert len(PLUS['O11']) == 5, len(PLUS['O11'])
    for k, cle in enumerate(ORDRE):
        orig = PLUS['O11'][k][:PLUS_ORIGINE]
        vus = {json.dumps(e, ensure_ascii=False) for e in orig}
        nouv = [e for e in BANQUE[cle] if json.dumps(e, ensure_ascii=False) not in vus]
        assert len(nouv) == len(BANQUE[cle]), ('doublon avec un exercice d’origine', cle)
        PLUS['O11'][k] = orig + nouv
    s = s[:m.start(1)] + json.dumps(PLUS, ensure_ascii=False) + s[m.end(1):]
    open(chemin, 'w', encoding='utf-8').write(s)
    print('O11 : %d exercices en plus par écran.' % len(BANQUE['tion']))

if __name__ == '__main__':
    import sys
    if '--integrer' in sys.argv:
        integrer(); sys.exit(0)
    for k, L in BANQUE.items():
        print('==', k, len(L))
        for e in L:
            t = e['tasks'][0]
            print('  ', e['p'] or '(question)', '→', t['choose'][0], '|', t.get('ask', '') if not e['p'] else '', '|', t['hint'])
