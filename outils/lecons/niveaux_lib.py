"""Outils communs : phrases d'exercice selon la classe pour les ceintures de grammaire (08/11/2026).
CE2 = exercices de base (atoi + plus), CM1 = NIV_ATOI[id][2], CM2 = NIV_ATOI[id][3] (4 exercices par écran)."""
import json, os, re, subprocess, sys

RACINE = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')
CHEMIN = os.path.join(RACINE, 'index.html')


def C(p, ask, bon, mauvais, hint, fill=None):
    """Choix : bon = bonne réponse, mauvais = liste (ou une seule chaîne)."""
    if isinstance(mauvais, str):
        mauvais = [mauvais]
    t = {'choose': [bon] + list(mauvais), 'ok': 0, 'hint': hint}
    if ask:
        t['ask'] = ask
    if fill:
        t['fill'] = fill
    return {'p': p, 'tasks': [t]}


def K(p, ask, hint, kind='x', n=None):
    """Clic sur un mot ou un groupe marqué <…> (kind x), ou sur le sujet [..] / le verbe (..)."""
    t = {'click': kind, 'ask': ask, 'hint': hint}
    if n:
        t['n'] = n
    return {'p': p, 'tasks': [t]}


def SV(p):
    return {'p': p, 'tasks': [{'click': 's'}, {'click': 'v'}]}


def lire(s):
    a = s.index('const LESSONS={')
    b = s.index('\n};', a) + 3
    return a, b


def lessons_json(g):
    js = ("const fs=require('fs');const t=fs.readFileSync(%r,'utf8');"
          "const a=t.indexOf('const LESSONS={'),b=t.indexOf('\\n};',a)+3;"
          "eval(t.slice(a,b).replace('const LESSONS','var LESSONS'));"
          "console.log(JSON.stringify(LESSONS[%r]));") % (CHEMIN, g)
    return json.loads(subprocess.run(['node', '-e', js], capture_output=True, text=True, check=True).stdout)


def appliquer(g, niv, nouveaux=(), retirer_ce2=()):
    """niv : {titre d'écran: (liste CM1, liste CM2)} ; nouveaux : [(titre_après_lequel_insérer, écran dict avec 'plus')].
    Remplace dans index.html : le bloc de la leçon g (si des écrans sont ajoutés), PLUS[g], NIV_ATOI[g], CE2_PLUS[g]['retirer']."""
    s = open(CHEMIN, encoding='utf-8').read()
    L = lessons_json(g)
    m = re.search(r'const PLUS=(\{.*\});\n', s)
    PLUS = json.loads(m.group(1))
    ecrans = L['ecrans']
    plus = list(PLUS.get(g) or [[] for _ in ecrans])
    for apres, e in nouveaux:
        k = max(i for i, x in enumerate(ecrans) if x['titre'] == apres)
        ecrans.insert(k + 1, {kk: v for kk, v in e.items() if kk != 'plus'})
        plus.insert(k + 1, e['plus'])
    manque = [e['titre'] for e in ecrans if e['titre'] not in niv]
    en_trop = [t for t in niv if t not in [e['titre'] for e in ecrans]]
    assert not manque and not en_trop, (g, 'sans niveaux :', manque, 'inconnus :', en_trop)
    for t, (a2, a3) in niv.items():
        assert len(a2) == 4 and len(a3) == 4, (g, t, len(a2), len(a3))
    if nouveaux:
        # réécrire le bloc de la leçon g dans LESSONS (entrée JSON)
        a = s.index('\n%s:{' % g) + 1
        b = s.index('\n', a) + 1   # l'entrée de G3…G7 tient sur une seule ligne
        L['ecrans'] = ecrans
        s = s[:a] + g + ':' + json.dumps(L, ensure_ascii=False) + ',\n' + s[b:]
    PLUS[g] = plus
    m = re.search(r'const PLUS=(\{.*\});\n', s)
    s = s[:m.start(1)] + json.dumps(PLUS, ensure_ascii=False) + s[m.end(1):]
    m = re.search(r'const NIV_ATOI=(\{.*\});\n', s)
    NIV = json.loads(m.group(1))
    NIV[g] = {'2': [niv[e['titre']][0] for e in ecrans], '3': [niv[e['titre']][1] for e in ecrans]}
    s = s[:m.start(1)] + json.dumps(NIV, ensure_ascii=False) + s[m.end(1):]
    if retirer_ce2:
        m = re.search(r'const CE2_PLUS=(\{.*\});\n', s)
        CE2 = json.loads(m.group(1))
        if g in CE2:
            for t in retirer_ce2:
                if t not in CE2[g]['retirer']:
                    CE2[g]['retirer'].append(t)
            s = s[:m.start(1)] + json.dumps(CE2, ensure_ascii=False) + s[m.end(1):]
    open(CHEMIN, 'w', encoding='utf-8').write(s)
    print(g, ':', len(ecrans), 'écrans,', len(ecrans) * 4, 'exercices CM1,', len(ecrans) * 4, 'exercices CM2')
