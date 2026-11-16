"""Jamais d'écriture fausse montrée aux élèves (décision de l'enseignante, 15/11/2026).
Les exercices « Quelle phrase est bien écrite ? » (et « Laquelle est bien écrite ? », « Choisis la phrase bien écrite. »,
« Quelle question est bien écrite ? », « Quelle phrase déclarative est bien écrite ? ») faisaient choisir la bonne phrase
parmi des phrases fausses. Ce script les remplace, dans index.html, par des exercices sans écriture fausse :
  - un trou à compléter avec de vraies formes (« Les enfants ___ dehors. » : jouent / joue / jouez) ;
  - un trou de quelques lettres (« Je pou___ai venir. » : rr / r) quand la faute était une forme inventée ;
  - une question sur la règle, la phrase juste sous les yeux (virgules, « ne… pas »).
Il est appelé tout seul à la fin de inserer.py, inserer_cm2.py, lecons/niveaux_lib.py et lecons/g2_enrichi.py ;
à la main : python3 outils/sans_ecriture_fausse.py. Il ne change rien quand il n'y a plus rien à remplacer.
Une phrase nouvelle qu'il ne sait pas traiter (forme inventée sans remplacement) est signalée : l'ajouter dans REGLES_FIXES."""
import json, os, re, sys
import re
ASKS = ['Quelle phrase est bien écrite ?', 'Laquelle est bien écrite ?', 'Choisis la phrase bien écrite.', 'Quelle question est bien écrite ?', 'Quelle phrase déclarative est bien écrite ?']
CPL = 'Complète la phrase.'
# formes inventées (jamais montrées) : remplacées par des formes justes, ou par un trou de quelques lettres
VRAIES = {'disez': None, 'allent': ['vont', 'va', 'vas'], 'peus': ['peux', 'peut', 'pouvons'], 'pourai': None, 'pouvrai': None,
          'voirons': None, 'verons': None, 'nagais': None, 'lancais': None}
def fin_signe(s):
    return re.sub(r'\s*[.?!]$', '', s)
def nepas(bon, hint):
    m = re.search(r'\bn’(\S+) (pas|jamais|rien|plus) (\S+?)[ .]', bon)
    if not m: return None
    aux, neg, pp = m.groups()
    return {'p': bon, 'choose': [f'l’auxiliaire « {aux} »', f'le participe passé « {pp} »'], 'ask': f'Dans cette phrase, « ne… {neg} » encadre…', 'hint': hint}
def transformer(p, ask, ch, ok, hint):
    bon = ch[ok]; mauv = [c for i, c in enumerate(ch) if i != ok]
    R = REGLES_FIXES.get(bon)
    if R: return dict(R, hint=R.get('hint', hint))
    # questions à fabriquer à partir d'une phrase (p non vide) : trait d'union / -t-
    m = re.match(r'^(.*?\b\w+)-(t-)?(tu|il|elle|ils|elles|vous|nous|on)\b(.*)$', bon)
    if p and m:
        a, t, pr, b = m.groups()
        return {'p': f'{a}___{pr}{b}', 'choose': ['-t-' if t else '-', '-' if t else '-t-'], 'ask': 'Complète la question.', 'hint': hint}
    # majuscule et point : il ne manque que le signe de la fin
    if all(c.lower() == bon.lower() or fin_signe(c) == fin_signe(bon) for c in ch) and bon[-1] in '.?!':
        sg = bon[-1]; autres = [s for s in '.?!' if s != sg]
        return {'p': fin_signe(bon) + ('___' if sg == '.' else ' ___'), 'choose': [sg] + autres, 'ask': 'Complète avec le bon signe.', 'hint': hint}
    # virgules
    sans = lambda s: s.replace(',', '')
    if all(sans(c) == sans(bon) for c in ch):
        if ' mais ' in bon:
            return {'p': bon, 'choose': ['Avant « mais ».', 'Après « mais ».'], 'ask': 'Où se place la virgule ?', 'hint': hint}
        if ',' not in bon:
            w = 'et' if ' et ' in bon else 'ou'
            if 'aime lire' in bon:
                return {'p': bon, 'choose': ['Non : la virgule ne coupe pas le groupe verbal.', 'Oui, après « aime ».'], 'ask': 'Faut-il une virgule entre « aime » et « lire » ?', 'hint': hint}
            return {'p': bon, 'choose': [f'Non : en général, pas de virgule avec « {w} ».', f'Oui, autour de « {w} ».'], 'ask': f'Faut-il une virgule avec « {w} » ?', 'hint': hint}
        x = bon.split(',')[0]
        return {'p': bon, 'choose': [f'Elle sépare le complément « {x} », placé au début.', 'Elle sépare le sujet et le verbe.', 'Elle termine la phrase.'], 'ask': 'Pourquoi y a-t-il une virgule ?', 'hint': hint}
    # ne… pas
    if re.search(r'\bn’\S+ (pas|jamais|rien|plus)\b', bon) and any(re.search(r'\b(pas|jamais|rien)\b', c) for c in mauv) and not REGLES_NE.get(bon):
        r = nepas(bon, hint)
        if r: return r
    if bon in REGLES_NE: return dict(REGLES_NE[bon], hint=hint)
    # cas général : les mots qui changent deviennent un trou, avec de vraies formes à choisir
    fin = bon[-1] if bon[-1] in '.?!' and all(c.endswith(bon[-1]) for c in ch) else ''
    if fin: ch = [c[:-1].rstrip() for c in ch]
    T = [c.split(' ') for c in ch]
    i = 0
    while all(len(x) > i for x in T) and len(set(x[i] for x in T)) == 1: i += 1
    j = 0
    while all(len(x) - j > i for x in T) and len(set(x[len(x) - 1 - j] for x in T)) == 1: j += 1
    mil = [' '.join(x[i:len(x) - j]) for x in T]
    pre = ' '.join(T[0][:i]); suf = ' '.join(T[0][len(T[0]) - j:])
    choix = [mil[ok]] + [m for k, m in enumerate(mil) if k != ok]
    for k, m in enumerate(list(choix)):
        if m in VRAIES:
            v = VRAIES[m]
            if v is None: raise ValueError('forme inventée sans remplacement : ' + bon)
            choix = v; break
    pp = (pre + ' ' if pre else '') + '___' + (' ' + suf if suf else '') + ((' ' if fin in '?!' else '') + fin if fin else '')
    return {'p': pp, 'choose': choix, 'ask': CPL, 'hint': hint}
# n' devant une voyelle : un trou
REGLES_NE = {}
# phrases traitées une à une (formes inventées, accents, apostrophes)
F = lambda p, c, a=None, h=None: dict({'p': p, 'choose': c, 'ask': a or ('Complète avec la bonne lettre.' if len(c[0]) == 1 else 'Complète avec les bonnes lettres.')}, **({'hint': h} if h else {}))
REGLES_FIXES = {
 'Vous dites bonjour.': F('Vous ___ bonjour.', ['dites', 'disent', 'disons'], CPL),
 'Je pourrai venir.': F('Je pou___ai venir.', ['rr', 'r']),
 'Nous verrons la tour.': F('Nous v___ons la tour.', ['err', 'er', 'oir']),
 'Je nageais vite.': F('Je na___ais vite.', ['ge', 'g']),
 'Tu lançais le ballon.': F('Tu lan___ais le ballon.', ['ç', 'c']),
 'Nous n’avons rien vu.': F('Nous ___avons rien vu.', ['n’', 'ne'], 'Complète avec le bon mot.'),
 'Voilà mon frère.': F('Voil___ mon frère.', ['à', 'a']),
 'Voilà ton cartable.': F('Voil___ ton cartable.', ['à', 'a']),
 'Voilà exactement ce que je cherchais.': F('Voil___ exactement ce que je cherchais.', ['à', 'a']),
 'Mes amis sont là-bas.': F('Mes amis sont l___bas.', ['à-', 'a']),
 'Mes cousins habitent là-bas, près de ce lac.': F('Mes cousins habitent l___bas, près de ce lac.', ['à-', 'a']),
 'Il dit : « Bonjour. »': F('Il dit ___ « Bonjour. »', [':', '.', '!'], 'Complète avec le bon signe.'),
 'Il a pris son sac.': F('Il a ___ son sac.', ['pris', 'prit'], CPL),
 'Il n’aime pas la soupe.': F('Il ___aime pas la soupe.', ['n’', 'ne'], 'Complète avec le bon mot.'),
 'C’était mon tour.': F('C’ét___ mon tour.', ['ait', 'ais']),
 'Il s’est endormi.': F('Il ___ endormi.', ['s’est', 'c’est'], CPL),
 'Elle s’est blessée.': F('Elle ___ blessée.', ['s’est', 'c’est'], CPL),
 'Ma sœur s’est promenée hier soir au bord du lac.': F('Ma sœur ___ promenée hier soir au bord du lac.', ['s’est', 'c’est'], CPL),
}
for b in ['C’est mon tour !', 'C’est très joli.', 'C’est une belle journée.', 'C’est mon cartable.', 'C’est très bon.', 'C’est ma sœur.',
          'C’est la plus belle journée de l’année.', 'C’est un livre que j’ai lu trois fois.', 'C’est exactement ce que je voulais.']:
    REGLES_FIXES[b] = F('___ ' + b[6:], ['C’est', 'S’est', 'Ses'], CPL)
REGLES_FIXES['Regarde : c’est un renard !'] = F('Regarde : ___ un renard !', ['c’est', 's’est', 'ses'], CPL)
for b in ['C’était une belle journée.', 'C’était un jour de fête dans tout le village.']:
    REGLES_FIXES[b] = F('___ ' + b[8:], ['C’était', 'S’était'], CPL)

EX = re.compile(r'\{"p": "(?:[^"\\]|\\.)*", "tasks": \[(?:\{[^{}]*\}(?:, )?)+\]\}')


def corriger(chemin=None, bavard=True):
    chemin = chemin or os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'index.html')
    t = open(chemin, encoding='utf-8').read()
    n = [0]; pb = []

    def rep(m):
        ex = json.loads(m.group(0))
        if not any(tk.get('ask') in ASKS for tk in ex['tasks']): return m.group(0)
        if len(ex['tasks']) != 1: pb.append(ex['tasks'][0]['choose'][0]); return m.group(0)
        tk = ex['tasks'][0]
        try:
            r = transformer(ex['p'], tk['ask'], tk['choose'], tk['ok'], tk['hint'])
        except ValueError as e:
            pb.append(str(e)); return m.group(0)
        n[0] += 1
        nt = {'choose': r['choose'], 'ok': 0, 'hint': r['hint'], 'ask': r['ask']}
        if '___' in r['p']: nt['fill'] = 'hl'      # le mot complété apparaît surligné
        return json.dumps({'p': r['p'], 'tasks': [nt]}, ensure_ascii=False)
    t2 = EX.sub(rep, t)
    if t2 != t: open(chemin, 'w', encoding='utf-8').write(t2)
    import formes_inventees; formes_inventees.corriger(chemin, bavard=False)   # jamais de forme inventée (16/11/2026)
    reste = sum(t2.count(a) for a in ASKS)
    if bavard or pb or reste:
        print(f'Sans écriture fausse : {n[0]} exercices remplacés, {reste} restants.')
    for x in pb: print('  À traiter à la main :', x)
    return n[0], reste


if __name__ == '__main__':
    _, reste = corriger(sys.argv[1] if len(sys.argv) > 1 else None)
    sys.exit(1 if reste else 0)
