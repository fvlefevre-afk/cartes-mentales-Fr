import json, os
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'sortie'); os.makedirs(D, exist_ok=True)


def C(p, ask, hint, n=None):
    t = {'click': 'x', 'ask': ask, 'hint': hint}
    if n: t['n'] = n
    return {'p': p, 'tasks': [t]}


def SV(p):
    return {'p': p, 'tasks': [{'click': 's'}, {'click': 'v'}]}


def V(p):
    return {'p': p, 'tasks': [{'click': 'v'}]}


def S(p):
    return {'p': p, 'tasks': [{'click': 's'}]}


def Q(p, choices, hint, ask=None, fill=None):
    t = {'choose': choices, 'ok': 0, 'hint': hint}
    if ask: t['ask'] = ask
    if fill: t['fill'] = fill
    return {'p': p, 'tasks': [t]}


def Q2(p, *qs):
    """plusieurs questions sur la même phrase : qs = (ask, choices, hint[, fill])"""
    ts = []
    for q in qs:
        t = {'ask': q[0], 'choose': q[1], 'ok': 0, 'hint': q[2]}
        if len(q) > 3: t['fill'] = q[3]
        ts.append(t)
    return {'p': p, 'tasks': ts}


def E(sec, picto, titre, guide, bulle, steps, atoi, plus):
    st = []
    for s in steps:
        if isinstance(s, str): st.append({'p': s})
        else: st.append({'p': s[0], 'c': s[1]})
    return {'sec': sec, 'picto': picto, 'titre': titre, 'guide': guide, 'bulle': bulle, 'steps': st, 'atoi': atoi, '_plus': plus}


def save(lid, trace, sections, ecrans, zones):
    for s in sections:
        s['zone'] = zones[s['id']]
    plus = [e.pop('_plus') for e in ecrans]
    data = {'trace': trace, 'lesson': {'sections': sections, 'ecrans': ecrans}, 'plus': plus}
    json.dump(data, open(os.path.join(D, f'{lid}.json'), 'w'), ensure_ascii=False, indent=1)
    print(lid, len(ecrans), 'écrans', sum(len(p) for p in plus), 'exercices en plus')
