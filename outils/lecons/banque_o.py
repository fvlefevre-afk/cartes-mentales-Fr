"""Outils communs aux banques d'exercices des ceintures O (19/11/2026) : contrôles avant intégration et intégration relançable.

Contrôles bloquants (rien n'est écrit sinon) :
  - chaque mot recomposé (début + bonne réponse + fin) est cherché dans /usr/share/dict/french (dernier mot du trou, sans l'article) ;
  - aucun exercice ajouté ne reprend un exercice déjà dans la leçon (exercices d'origine, « À toi ! », exemples) ;
  - aucun doublon dans la banque ; aucune proposition « un / une / la / le … » qui ne soit un vrai mot ;
  - aucun signe phonétique ([…]) dans les phrases, questions, propositions et aides ajoutées."""
import json, os, re

H = 'hl'
CHEMIN = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'index.html')


def Q(p, bon, autres, hint, ask='Complète avec la bonne fin.'):
    return {'p': p, 'tasks': [{'choose': [bon] + list(autres), 'ok': 0, 'hint': hint, 'ask': ask, 'fill': H}]}


def C(ask, bon, a, b, hint, p=''):
    return {'p': p, 'tasks': [{'choose': [bon, a, b], 'ok': 0, 'hint': hint, 'ask': ask}]}


def recompose(e):
    t = e['tasks'][0]
    return e['p'].replace('___', t['choose'][t.get('ok', 0)]) if '___' in e['p'] else None


def _lire(s, nom):
    m = re.search(r'const %s=(\{.*\});\n' % nom, s)
    return m, json.loads(m.group(1))


def _ecrire(s, m, obj):
    return s[:m.start(1)] + json.dumps(obj, ensure_ascii=False) + s[m.end(1):]


def _lecon(s, code):
    d = s.find('const LESSONS=')
    i = max(s.find('\n%s:{' % code, d), s.find('\n"%s":{' % code, d)); assert i > 0, code
    return s[i:re.search(r'\n"?[A-Z][A-Za-z0-9_-]*"?:\{', s[i + 5:]).start() + i + 5]


def controler(s, code, banque, ordre, origine, cm2=None):
    dico = set(open('/usr/share/dict/french', encoding='utf-8').read().split('\n'))
    dico |= {w.replace('oe', 'œ') for w in dico if 'oe' in w}          # le dictionnaire écrit « coeur »
    _, PLUS = _lire(s, 'PLUS')
    lecon = _lecon(s, code)
    deja = [x for k, L in enumerate(PLUS[code]) for x in L[:origine[k]]]
    tout = [e for c in ordre for e in banque[c]]
    if cm2:
        _, C2 = _lire(s, 'CM2_PLUS')
        ec = next(e for e in C2[code]['ecrans'] if e['titre'] == cm2[0])
        deja += ec['plus'][:cm2[1]] + [ec['atoi']]
        tout += cm2[2]
    err = []
    for e in tout:
        w = recompose(e)
        if w:
            dernier = re.split(r'[\s’\']', w.strip(' .!?'))[-1]
            if dernier not in dico: err.append('absent du dictionnaire : ' + w)
        for t in e['tasks']:
            for c in t['choose']:
                if c.startswith(('un ', 'une ', 'la ', 'le ', 'l’')) and re.split(r'[\s’]', c)[-1] not in dico: err.append('proposition inconnue : ' + c)
            if re.search(r'\[[^\]\s]{1,4}\]', ' '.join([e['p'], t.get('ask', ''), t.get('hint', '')] + t['choose'])): err.append('signe phonétique : ' + (e['p'] or t['ask']))
    cles = [json.dumps(e, ensure_ascii=False) for e in tout]
    err += ['doublon dans la banque : ' + c[:90] for c in set(cles) if cles.count(c) > 1]
    for e in tout:
        if e['p'] and ('"p": "%s"' % e['p'] in lecon or any(o['p'] == e['p'] for o in deja)):
            err.append('déjà dans la leçon : ' + e['p'])
        if not e['p'] and any(not o['p'] and o['tasks'][0].get('ask') == e['tasks'][0]['ask'] and o['tasks'][0]['choose'][0] == e['tasks'][0]['choose'][0] for o in deja):
            err.append('question déjà dans la leçon : ' + e['tasks'][0]['ask'])
    return err


def integrer(code, banque, ordre, origine, cm2=None):
    """cm2 = (titre de l'écran du CM2, nombre d'exercices d'origine gardés, exercices ajoutés) ou None."""
    s = open(CHEMIN, encoding='utf-8').read()
    m, PLUS = _lire(s, 'PLUS')
    assert len(PLUS[code]) == len(ordre), (code, len(PLUS[code]))
    PLUS[code] = [PLUS[code][k][:origine[k]] for k in range(len(ordre))]          # repart des exercices d'origine
    s = _ecrire(s, m, PLUS)
    if cm2:
        m2, C2 = _lire(s, 'CM2_PLUS')
        ec = next(e for e in C2[code]['ecrans'] if e['titre'] == cm2[0])
        ec['plus'] = ec['plus'][:cm2[1]]
        s = _ecrire(s, m2, C2)
    err = controler(s, code, banque, ordre, origine, cm2)
    if err:
        print('\n'.join(err)); raise SystemExit('%s : rien n’est intégré.' % code)
    m, PLUS = _lire(s, 'PLUS')
    PLUS[code] = [PLUS[code][k] + banque[c] for k, c in enumerate(ordre)]
    s = _ecrire(s, m, PLUS)
    if cm2:
        m2, C2 = _lire(s, 'CM2_PLUS')
        next(e for e in C2[code]['ecrans'] if e['titre'] == cm2[0])['plus'] += cm2[2]
        s = _ecrire(s, m2, C2)
    open(CHEMIN, 'w', encoding='utf-8').write(s)
    print(code, ': exercices en plus par écran :', {c: len(banque[c]) for c in ordre}, *(['; CM2 « %s » : %d' % (cm2[0], len(cm2[2]))] if cm2 else []))


def lister(banque, cm2=None):
    for k, L in list(banque.items()) + ([('CM2 ' + cm2[0], cm2[2])] if cm2 else []):
        print('==', k, len(L))
        for e in L:
            t = e['tasks'][0]
            print('  ', recompose(e) or (e['p'] + ' ' if e['p'] else '') + t['ask'], '→', t['choose'][0], '| autres :', t['choose'][1:], '|', t['hint'])


def main(code, banque, ordre, origine, cm2=None):
    import sys
    if '--integrer' in sys.argv:
        integrer(code, banque, ordre, origine, cm2)
    else:
        lister(banque, cm2)
        s = open(CHEMIN, encoding='utf-8').read()
        print('\n'.join(controler(s, code, banque, ordre, origine, cm2)) or 'contrôles : aucun problème')
