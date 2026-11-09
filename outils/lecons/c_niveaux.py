from niveaux_lib import *
from conj import *
import random
TN = {'pr': 'au présent', 'fu': 'au futur', 'im': 'à l’imparfait', 'pc': 'au passé composé', 'pqp': 'au plus-que-parfait', 'ps': 'au passé simple'}
TNOM = {'pr': 'le présent', 'fu': 'le futur', 'im': 'l’imparfait', 'pc': 'le passé composé', 'pqp': 'le plus-que-parfait', 'ps': 'le passé simple'}
COMPL = {
 'jouer': ('au ballon', 'au ballon dans la cour de récréation'), 'chanter': ('une chanson', 'une chanson pour la fête de l’école'), 'regarder': ('un film', 'un film passionnant à la télévision'),
 'laver': ('les mains', 'soigneusement les mains avant le repas'), 'sauter': ('très haut', 'par-dessus le ruisseau'), 'danser': ('toute la soirée', 'toute la soirée au son de la musique'),
 'parler': ('à la maîtresse', 'calmement à la maîtresse'), 'manger': ('une pomme', 'une pomme bien mûre au goûter'), 'commencer': ('une leçon', 'une nouvelle leçon de grammaire'),
 'lever': ('la main', 'la main pour répondre à la maîtresse'), 'appeler': ('un ami', 'un ami depuis le jardin'), 'acheter': ('du pain', 'du pain frais à la boulangerie'),
 'nettoyer': ('la table', 'la table de la cuisine'), 'essuyer': ('la vaisselle', 'la vaisselle après le repas'), 'ranger': ('la chambre', 'la chambre avant le dîner'),
 'finir': ('les devoirs', 'les devoirs avant le dîner'), 'choisir': ('un livre', 'un livre à la bibliothèque'), 'grandir': ('vite', 'vite pendant l’été'), 'réussir': ('un examen', 'un examen difficile'),
 'être': ('en retard', 'en retard à l’école ce jour-là'), 'avoir': ('un chien', 'un grand chien noir'), 'aller': ('à la piscine', 'à la piscine municipale'), 'faire': ('du sport', 'du sport chaque semaine'),
 'dire': ('bonjour', 'bonjour à tout le monde'), 'venir': ('avec nous', 'avec nous au marché'), 'pouvoir': ('venir', 'venir à la fête'), 'vouloir': ('un gâteau', 'un gros gâteau au chocolat'),
 'voir': ('un oiseau', 'un oiseau sur la branche'), 'prendre': ('le bus', 'le bus de huit heures'), 'arriver': ('à l’heure', 'à l’heure à l’école'), 'partir': ('en vacances', 'en vacances au bord de la mer'),
 'tomber': ('dans l’escalier', 'dans l’escalier de la cave'), 'entrer': ('dans la classe', 'dans la classe sans bruit'), 'marcher': ('à pied', 'à pied jusqu’au village'),
 'inviter': ('des amis', 'des amis pour l’anniversaire'), 'fermer': ('la porte', 'la porte du garage'), 'oublier': ('un cahier', 'un cahier à l’école'), 'préparer': ('le dîner', 'le dîner pour toute la famille'),
 'nager': ('dans la mer', 'dans la mer chaque été'), 'écouter': ('la radio', 'la radio dans la cuisine'), 'surgir': ('du buisson', 'soudain du buisson'), 'bondir': ('sur le mur', 'sur le mur du jardin'),
}
ADV = {'pr': (['Aujourd’hui,', 'En ce moment,', 'Chaque matin,', 'Tous les jours,'], ['Chaque matin avant l’école,', 'En ce moment même,', 'Tous les samedis,', 'D’habitude,']),
       'fu': (['Demain,', 'Bientôt,', 'Samedi prochain,', 'L’été prochain,'], ['Dans quelques jours,', 'L’année prochaine,', 'Dans un mois,', 'Pendant les prochaines vacances,']),
       'im': (['Autrefois,', 'Quand j’étais petit,', 'Avant,', 'Chaque été,'], ['Autrefois, dans ce village,', 'Quand ils étaient enfants,', 'Pendant les vacances d’autrefois,', 'Il y a longtemps,']),
       'pc': (['Hier,', 'Ce matin,', 'Hier soir,', 'Lundi dernier,'], ['Hier après-midi,', 'Le week-end dernier,', 'Pendant les vacances,', 'L’année dernière,']),
       'pqp': (['Avant notre arrivée,', 'Avant le déjeuner,', 'Avant la nuit,', 'Déjà hier,'], ['Avant que les invités n’arrivent,', 'Avant le début du spectacle,', 'Longtemps avant l’orage,', 'Bien avant la fin de l’hiver,']),
       'ps': (['Soudain,', 'Alors,', 'Tout à coup,', 'Un jour,'], ['Soudain, dans le silence de la nuit,', 'Alors, sans hésiter un instant,', 'Tout à coup, au détour du chemin,', 'Un matin, très tôt,'])}
SUBJ = {
 0: {1: [('je', 'm')], 2: [('je', 'm')]}, 1: {1: [('tu', 'm')], 2: [('tu', 'm')]},
 2: {1: [('Léa', 'f'), ('mon frère', 'm'), ('le chat', 'm'), ('elle', 'f'), ('Tom', 'm'), ('ma sœur', 'f')], 2: [('mon grand-père', 'm'), ('la petite sœur de mon ami', 'f'), ('le chien de mes voisins', 'm'), ('la boulangère du quartier', 'f')]},
 3: {1: [('nous', 'm'), ('mon frère et moi', 'm')], 2: [('ma sœur et moi', 'f'), ('mes amis et moi', 'm'), ('nous', 'm')]},
 4: {1: [('vous', 'm'), ('toi et ton frère', 'm')], 2: [('vous', 'm'), ('toi et ta cousine', 'f')]},
 5: {1: [('les enfants', 'm'), ('mes sœurs', 'f'), ('ils', 'm'), ('mes cousins', 'm')], 2: [('les enfants de ma voisine', 'm'), ('mes deux cousines', 'f'), ('tous les élèves de la classe', 'm'), ('les filles de la classe', 'f')]},
}
def sujet(p, lvl, k):
    L = SUBJ[p][2 if lvl >= 3 else 1]
    return L[k % len(L)]
def avec_elision(s, form):
    if s == 'je' and form[:1] in VOY: return 'j’'
    return s
def phr(adv, s, form, compl, blank=True):
    s2 = avec_elision(s, form)
    sp = '' if s2 == 'j’' else ' '
    body = (s2 + sp + ('___' if blank else form) + (' ' + compl if compl else '')).strip()
    txt = (adv + ' ' + body if adv else body)
    return txt[0].upper() + txt[1:] + '.'
def autres(forms, p, bon, n=2, ordre=None):
    ordre = ordre or [(p + 1) % 6, (p + 5) % 6, (p + 2) % 6, (p + 4) % 6, (p + 3) % 6, p]
    out = []
    for q in ordre:
        f = forms[q]
        if f != bon and f not in out: out.append(f)
    return out[:n]
def X(t, v, p, lvl, k, ask=None, fill='t', sub=None, g=None, explic=False, adv_i=None):
    cm = lvl >= 3
    adv = ADV[t][1 if cm else 0][(k if adv_i is None else adv_i) % 4]
    s, gen = sujet(p, lvl, k) if sub is None else sub
    forms = [forme(v, t, q, gen, None) if t in ('pc', 'pqp') else forme(v, t, q) for q in range(6)]
    bon = forms[p]
    compl = COMPL[v][1 if cm else 0]
    if t in ('pc', 'pqp'):
        # participe passé : le complément suit
        pass
    mal = autres(forms, p, bon)
    if t == 'ps':
        mal = [m for m in dict.fromkeys([ps(v, 2 if p == 5 else 5), im(v, p), fu(v, p)]) if m != bon][:2]
    tx = phr(adv, s, bon, compl)
    ask = ask or (f'Complète avec « {v} » {TN[t]}.' if explic else f'Complète avec le verbe {TN[t]}.' if t in ('pr', 'fu', 'im', 'ps') else f'Complète avec le {TNOM[t][3:] if False else "passé composé" if t == "pc" else "plus-que-parfait"}.')
    h = {'pr': 'Je cherche le sujet, puis la terminaison du présent.', 'fu': 'Au futur : le r, puis la terminaison -ai, -as, -a, -ons, -ez, -ont.', 'im': 'À l’imparfait : le radical de « nous », puis -ais, -ais, -ait, -ions, -iez, -aient.',
         'pc': 'Au passé composé : l’auxiliaire au présent + le participe passé.', 'pqp': 'Au plus-que-parfait : l’auxiliaire à l’imparfait + le participe passé.', 'ps': 'Je cherche le sujet, puis la terminaison du passé simple.'}[t]
    return C(tx, ask, bon, mal, h, 'v' if t in ('pc', 'pqp', 'ps') else fill)
def XP(t, v, p, lvl, k, **kw):  # phrase bien écrite
    cm = lvl >= 3
    s, gen = sujet(p, lvl, k)
    forms = [forme(v, t, q, gen, None) if t in ('pc', 'pqp') else forme(v, t, q) for q in range(6)]
    bon = forms[p]; compl = COMPL[v][1 if cm else 0]
    adv = ADV[t][1 if cm else 0][k % 4]
    mal = [phr(adv, s, f, compl, False) for f in autres(forms, p, bon)]
    return C('', 'Quelle phrase est bien écrite ?', phr(adv, s, bon, compl, False), mal, 'Je trouve le sujet, puis j’écris la bonne terminaison.')
def XT(v, p, lvl, k, t='pr', ask=None):   # terminaison
    cm = lvl >= 3
    s, gen = sujet(p, lvl, k); f = forme(v, t, p); stem = v[:-2]
    fin = f[len(stem):] if f.startswith(stem) else None
    if fin is None or not fin: return XP(t, v, p, lvl, k)
    return C(f'{avec_elision(s, f) if s == "je" else s} {f}'.replace('j’ ', 'j’'), 'Quelle est la terminaison ?', '-' + fin, [stem + '-', s], 'Le radical reste, la terminaison change avec le sujet.')
def XPS(v, t, p, lvl, k, other, ask=None):  # le bon temps : forme du temps voulu / de l'autre temps
    cm = lvl >= 3
    s, gen = sujet(p, lvl, k)
    adv = ADV[t][1 if cm else 0][k % 4]; compl = COMPL[v][1 if cm else 0]
    bon = forme(v, t, p, gen) 
    mal = [forme(v, o, p, gen) for o in other]
    return C(phr(adv, s, bon, compl), ask or 'Complète avec le bon temps.', bon, mal, 'Je regarde les mots qui disent quand.', 't' if t in ('pr', 'fu', 'im') else 'v')
def XQ(v, t, p, lvl, k, options):  # quel temps ?
    cm = lvl >= 3
    s, gen = sujet(p, lvl, k)
    adv = ADV[t][1 if cm else 0][k % 4]; compl = COMPL[v][1 if cm else 0]
    f = forme(v, t, p, gen)
    return C(phr(adv, s, f, compl, False), 'Quel est le temps de cette phrase ?', TNOM[t], [TNOM[o] for o in options if o != t][:2], 'Je regarde les mots qui disent quand et la forme du verbe.')
def XAUX(v, t, p, lvl, k):  # auxiliaire
    cm = lvl >= 3
    s, gen = sujet(p, lvl, k); a = aux_de(v)
    auxf = [aux_pr(a, q) if t == 'pc' else aux_im(a, q) for q in range(6)]
    bon = auxf[p]
    part = pp(v, gen if a == 'être' else 'm', (2 if p in (3, 4, 5) else 1) if a == 'être' else 1)
    adv = ADV[t][1 if cm else 0][k % 4]; compl = COMPL[v][1 if cm else 0]
    tx = phr(adv, s, '___ ' + part, compl, False).replace('___ ' + part, '___ ' + part)
    s2 = avec_elision(s, bon)
    sp = '' if s2 == 'j’' else ' '
    tx2 = (adv + ' ' + s2 + sp + '___ ' + part + ' ' + compl).strip()
    return C(tx2[0].upper() + tx2[1:] + '.', 'Complète avec l’auxiliaire.', bon, autres(auxf, p, bon), 'L’auxiliaire se conjugue ' + ('au présent.' if t == 'pc' else 'à l’imparfait.'), 'v')
def XPP(v, t, p, lvl, k, accord=True):  # participe passé
    cm = lvl >= 3
    s, gen = sujet(p, lvl, k); a = aux_de(v)
    plur = p in (3, 4, 5)
    bon = pp(v, gen if a == 'être' else 'm', (2 if plur else 1) if a == 'être' else 1)
    adv = ADV[t][1 if cm else 0][k % 4]; compl = COMPL[v][1 if cm else 0]
    af = aux_pr(a, p) if t == 'pc' else aux_im(a, p)
    s2 = avec_elision(s, af); sp = '' if s2 == 'j’' else ' '
    tx = (adv + ' ' + s2 + sp + af + ' ___ ' + compl).strip()
    if a == 'être':
        mal = [pp(v, 'm', 1) if bon != pp(v, 'm', 1) else pp(v, 'f', 1), pp(v, 'f', 2)] ; mal = [x for x in dict.fromkeys(mal) if x != bon][:2]
        if len(mal) < 2: mal.append(v)
        hint = 'Avec être, le participe passé s’accorde avec le sujet.'
    else:
        mal = [v, forme(v, 'pr', 5)]; mal = [x for x in dict.fromkeys(mal) if x != bon][:2]
        hint = 'Avec avoir, le participe passé ne s’accorde pas avec le sujet.'
    return C(tx[0].upper() + tx[1:] + '.', 'Complète avec le participe passé.', bon, mal, hint, 't')
NEGC = {'manger': ('la pomme', 'la pomme bien mûre du goûter'), 'finir': ('les devoirs', 'les devoirs avant le dîner'), 'regarder': ('le film', 'le film passionnant de ce soir'), 'jouer': ('au ballon', 'au ballon dans la cour de récréation')}
def XNEG(v, t, p, lvl, k):
    cm = lvl >= 3
    s, gen = sujet(p, lvl, k); a = aux_de(v)
    af = aux_pr(a, p) if t == 'pc' else aux_im(a, p)
    part = pp(v, gen if a == 'être' else 'm', (2 if p in (3, 4, 5) else 1) if a == 'être' else 1)
    adv = ADV[t][1 if cm else 0][k % 4]; compl = NEGC.get(v, COMPL[v])[1 if cm else 0]
    s2 = avec_elision(s, 'n' + af[:1] if af[:1] in VOY else af)
    ne = 'n’' if af[:1] in VOY else 'ne '
    s1 = 'je' if s == 'je' else s
    def mk(body): 
        t_ = (adv + ' ' + body + ' ' + compl).strip(); return t_[0].upper() + t_[1:] + '.'
    sj = s if s != 'je' else 'je'
    if sj == 'je' and af[:1] in VOY: sj = 'je'
    good = mk(f'{sj} {ne}{af} pas {part}'.replace('je n’', 'je n’')); b1 = mk(f'{sj} {af} {part} pas'); b2 = mk(f'{sj} {af} pas {part}')
    return C('', 'Quelle phrase est bien écrite ?', good, [b1, b2], 'Ne… pas encadre l’auxiliaire.')

def XE(v, p, lvl, k):   # é ou er ?
    cm = lvl >= 3
    s, gen = sujet(p, lvl, k); compl = COMPL[v][1 if cm else 0]
    af = aux_pr('avoir', p); s2 = avec_elision(s, af); sp = '' if s2 == 'j’' else ' '
    adv = ADV['pc'][1 if cm else 0][k % 4]
    tx = (adv + ' ' + s2 + sp + af + ' ___ ' + compl).strip()
    return C(tx[0].upper() + tx[1:] + '.', 'Complète avec le bon mot.', pp(v), [v, forme(v, 'pr', 4)], 'Après l’auxiliaire avoir : le participe passé. Je vérifie avec « vendu ».', 't')
def XPPV(v, p, lvl, k):   # participe passé d'un verbe irrégulier
    cm = lvl >= 3
    s, gen = sujet(p, lvl, k); compl = COMPL[v][1 if cm else 0]
    af = aux_pr('avoir', p); s2 = avec_elision(s, af); sp = '' if s2 == 'j’' else ' '
    adv = ADV['pc'][1 if cm else 0][k % 4]
    tx = (adv + ' ' + s2 + sp + af + ' ___ ' + compl).strip()
    return C(tx[0].upper() + tx[1:] + '.', f'Complète avec le participe passé de « {v} ».', pp(v), [v, forme(v, 'pr', 2)], 'Au passé composé, il faut connaître le participe passé.', 't')
def x(t, v, p, **kw): return lambda lvl, k: X(t, v, p, lvl, k, **kw)
def xp(t, v, p): return lambda lvl, k: XP(t, v, p, lvl, k)
def xt(v, p): return lambda lvl, k: XT(v, p, lvl, k)
def xps(v, t, p, other): return lambda lvl, k: XPS(v, t, p, lvl, k, other)
def xq(v, t, p, opts): return lambda lvl, k: XQ(v, t, p, lvl, k, opts)
def xaux(v, t, p): return lambda lvl, k: XAUX(v, t, p, lvl, k)
def xpp(v, t, p): return lambda lvl, k: XPP(v, t, p, lvl, k)
def xneg(v, t, p): return lambda lvl, k: XNEG(v, t, p, lvl, k)
def xe(v, p): return lambda lvl, k: XE(v, p, lvl, k)
def xppv(v, p): return lambda lvl, k: XPPV(v, p, lvl, k)
def cu(fn): return lambda lvl, k: fn   # exercice écrit à la main (identique aux deux niveaux)
def cc(p, ask, bon, mal, h): return lambda lvl, k: C(p, ask, bon, mal, h)
def mk(specs):
    return ([f(2, i) for i, f in enumerate(specs)], [f(3, i + 1) for i, f in enumerate(specs)])
def ex(*a): return a
SP = {}
SP['C1'] = {
 'Radical + terminaison': [xt('jouer', 4), xt('finir', 5), xt('chanter', 3), xt('danser', 1)],
 'La terminaison change avec le sujet': [x('pr', 'jouer', 5), x('pr', 'chanter', 1), x('pr', 'regarder', 3), x('pr', 'danser', 4)],
 'Le 1er groupe : -er': [x('pr', 'laver', 4), x('pr', 'sauter', 2), x('pr', 'regarder', 5), x('pr', 'parler', 0)],
 'Des radicaux qui changent (1)': [x('pr', 'lever', 0), x('pr', 'appeler', 1), x('pr', 'acheter', 5), x('pr', 'lever', 5)],
 'Des radicaux qui changent (2)': [x('pr', 'manger', 3), x('pr', 'commencer', 3), x('pr', 'nettoyer', 0), x('pr', 'essuyer', 2)],
 'Le 2e groupe : -ir avec -iss-': [x('pr', 'finir', 3), x('pr', 'choisir', 5), x('pr', 'grandir', 1), x('pr', 'réussir', 4)],
 'être et avoir': [x('pr', 'être', 4), x('pr', 'avoir', 3), x('pr', 'être', 0), x('pr', 'avoir', 5)],
 'Les verbes à connaître': [x('pr', 'dire', 4), x('pr', 'aller', 5), x('pr', 'prendre', 5), x('pr', 'venir', 3)],
 'tu : -s ou -x': [x('pr', 'vouloir', 1), x('pr', 'pouvoir', 1), x('pr', 'jouer', 1), x('pr', 'finir', 1)],
 'Les exceptions': [x('pr', 'faire', 5), x('pr', 'faire', 4), x('pr', 'dire', 4), x('pr', 'aller', 5)],
 'Le sujet composé': [x('pr', 'jouer', 3, sub=('mon frère et moi', 'm')), x('pr', 'chanter', 5, sub=('le chat et le chien', 'm')), x('pr', 'regarder', 3, sub=('ma sœur et moi', 'f')), x('pr', 'danser', 5, sub=('Léa et Tom', 'm'))],
}
SP['C2'] = {
 'Pour parler de demain': [x('fu', 'jouer', 3), x('fu', 'nager', 0), x('fu', 'regarder', 2), x('fu', 'chanter', 5)],
 'Présent ou futur ?': [xps('regarder', 'fu', 2, ['pr']), xps('finir', 'pr', 2, ['fu']), xps('jouer', 'fu', 5, ['pr']), xps('danser', 'pr', 5, ['fu'])],
 'Les terminaisons du futur': [x('fu', 'finir', 4), x('fu', 'inviter', 1), x('fu', 'fermer', 5), x('fu', 'laver', 3)],
 '2e groupe et le e muet': [x('fu', 'choisir', 3), x('fu', 'oublier', 0), x('fu', 'finir', 5), x('fu', 'écouter', 2)],
 'être et avoir': [x('fu', 'être', 3), x('fu', 'avoir', 1), x('fu', 'être', 5), x('fu', 'avoir', 4)],
 'Les verbes irréguliers': [x('fu', 'aller', 0), x('fu', 'faire', 1), x('fu', 'voir', 3), x('fu', 'venir', 4)],
 'dire et prendre': [x('fu', 'prendre', 4), x('fu', 'dire', 0), x('fu', 'pouvoir', 2), x('fu', 'vouloir', 5)],
 'Les radicaux qui changent': [x('fu', 'appeler', 0), x('fu', 'essuyer', 1), x('fu', 'acheter', 3), x('fu', 'nettoyer', 2)],
 'Les pièges': [xp('fu', 'pouvoir', 0), xp('fu', 'voir', 3), xp('fu', 'vouloir', 0), xp('fu', 'faire', 4)],
}
SP['C3'] = {
 'Pour parler d’avant': [x('im', 'marcher', 2), x('im', 'jouer', 5), x('im', 'chanter', 0), x('im', 'regarder', 3)],
 'Présent, futur ou imparfait ?': [xps('regarder', 'im', 2, ['pr', 'fu']), xps('finir', 'pr', 2, ['fu', 'im']), xps('jouer', 'fu', 5, ['pr', 'im']), xps('danser', 'im', 5, ['pr', 'fu'])],
 'Les terminaisons de l’imparfait': [x('im', 'finir', 4), x('im', 'jouer', 3), x('im', 'laver', 5), x('im', 'parler', 1)],
 'Le radical de « nous »': [x('im', 'finir', 5), x('im', 'grandir', 5), x('im', 'faire', 2), x('im', 'choisir', 1)],
 'être et avoir': [x('im', 'être', 3), x('im', 'avoir', 4), x('im', 'être', 5), x('im', 'avoir', 0)],
 'Les verbes irréguliers': [x('im', 'aller', 0), x('im', 'faire', 2), x('im', 'dire', 1), x('im', 'voir', 4)],
 'Les radicaux qui changent': [x('im', 'appeler', 0), x('im', 'lever', 3), x('im', 'nettoyer', 4), x('im', 'acheter', 5)],
 'Les pièges': [xp('im', 'manger', 0), xp('im', 'commencer', 3), xp('im', 'nager', 2), xp('im', 'ranger', 5)],
}
SP['C4'] = {
 'Une action terminée': [x('pc', 'préparer', 3), x('pc', 'finir', 2), x('pc', 'jouer', 5), x('pc', 'regarder', 0)],
 'Quel temps ?': [xq('jouer', 'pc', 2, ['pr', 'fu', 'pc']), xq('finir', 'fu', 3, ['pr', 'fu', 'pc']), xq('regarder', 'pr', 5, ['pr', 'fu', 'pc']), xq('chanter', 'im', 1, ['pr', 'im', 'pc'])],
 'L’auxiliaire avoir': [xaux('manger', 'pc', 5), xaux('chanter', 'pc', 0), xaux('finir', 'pc', 3), xaux('jouer', 'pc', 4)],
 'Le participe passé': [xpp('finir', 'pc', 3), xpp('jouer', 'pc', 5), xpp('choisir', 'pc', 0), xpp('regarder', 'pc', 2)],
 'À la forme négative': [xneg('manger', 'pc', 0), xneg('finir', 'pc', 2), xneg('regarder', 'pc', 3), xneg('jouer', 'pc', 5)],
 'é ou er ?': [xe('fermer', 1), xe('chanter', 2), xe('laver', 5), xe('regarder', 3)],
}
SP['C5'] = {
 'être + participe passé': [x('pc', 'aller', 3), x('pc', 'venir', 5), x('pc', 'arriver', 2), x('pc', 'partir', 4)],
 'Les verbes avec être': [cc('', 'Lequel se conjugue avec être ?', 'venir', ['manger', 'chanter'], 'Surtout des verbes de mouvement.'), cc('', 'Lequel se conjugue avec être ?', 'aller', ['jouer', 'finir'], 'Surtout des verbes de mouvement.'),
   cc('', 'Lequel se conjugue avec être ?', 'tomber', ['regarder', 'choisir'], 'Surtout des verbes de mouvement.'), cc('', 'Lequel se conjugue avec être ?', 'partir', ['préparer', 'laver'], 'Surtout des verbes de mouvement.')],
 'J’accorde avec le sujet': [xpp('tomber', 'pc', 2), xpp('arriver', 'pc', 5), xpp('partir', 'pc', 3), xpp('entrer', 'pc', 2)],
 'L’auxiliaire être': [xaux('aller', 'pc', 3), xaux('venir', 'pc', 5), xaux('arriver', 'pc', 4), xaux('tomber', 'pc', 2)],
 'être ou avoir ?': [xpp('manger', 'pc', 5), xpp('finir', 'pc', 2), xpp('jouer', 'pc', 3), xpp('regarder', 'pc', 4)],
}
SP['C6'] = {
 'aller et faire': [x('pr', 'aller', 5, explic=True), x('pr', 'faire', 4, explic=True), x('pr', 'aller', 3, explic=True), x('pr', 'faire', 5, explic=True)],
 'dire et venir': [x('pr', 'dire', 4, explic=True), x('pr', 'venir', 5, explic=True), x('pr', 'dire', 2, explic=True), x('pr', 'venir', 3, explic=True)],
 'pouvoir et vouloir': [x('pr', 'pouvoir', 1, explic=True), x('pr', 'vouloir', 0, explic=True), x('pr', 'pouvoir', 5, explic=True), x('pr', 'vouloir', 4, explic=True)],
 'voir et prendre': [x('pr', 'prendre', 5, explic=True), x('pr', 'voir', 3, explic=True), x('pr', 'prendre', 4, explic=True), x('pr', 'voir', 5, explic=True)],
 'Les pièges': [xp('pr', 'dire', 4), xp('pr', 'faire', 4), xp('pr', 'prendre', 5), xp('pr', 'pouvoir', 1)],
}
SP['C7'] = {
 'Au futur': [x('fu', 'aller', 3, explic=True), x('fu', 'faire', 1, explic=True), x('fu', 'venir', 5, explic=True), x('fu', 'pouvoir', 0, explic=True)],
 'À l’imparfait': [x('im', 'faire', 0, explic=True), x('im', 'aller', 5, explic=True), x('im', 'dire', 3, explic=True), x('im', 'voir', 4, explic=True)],
 'Le participe passé': [xppv('faire', 0), xppv('dire', 2), xppv('prendre', 5), xppv('voir', 3)],
 'Avec avoir ou être': [x('pc', 'aller', 2), x('pc', 'venir', 5), x('pc', 'faire', 3), x('pc', 'voir', 0)],
 'Les pièges': [xp('fu', 'pouvoir', 0), xp('im', 'faire', 3), xp('fu', 'voir', 3), xp('pc', 'faire', 2)],
}
SP['C8-CM2'] = {
 'Encore avant': [cc('Il avait neigé toute la nuit : le jardin était blanc.', 'Qu’est-ce qui s’est passé en premier ?', 'Il a neigé.', ['Le jardin était blanc.'], 'Le plus-que-parfait dit ce qui s’est passé avant.'), cc('Quand nous sommes arrivés, le film avait commencé.', 'Qu’est-ce qui s’est passé en premier ?', 'Le film a commencé.', ['Nous sommes arrivés.'], 'Le plus-que-parfait dit ce qui s’est passé avant.'),
   cc('Elle avait oublié son cartable : elle est retournée à la maison.', 'Qu’est-ce qui s’est passé en premier ?', 'Elle a oublié son cartable.', ['Elle est retournée à la maison.'], 'Le plus-que-parfait dit ce qui s’est passé avant.'), cc('Les invités étaient partis quand nous avons rangé la salle.', 'Qu’est-ce qui s’est passé en premier ?', 'Les invités sont partis.', ['Nous avons rangé la salle.'], 'Le plus-que-parfait dit ce qui s’est passé avant.')],
 'Deux parties': [x('pqp', 'manger', 2, explic=True), x('pqp', 'finir', 5, explic=True), x('pqp', 'jouer', 3, explic=True), x('pqp', 'préparer', 0, explic=True)],
 'avoir à l’imparfait': [xaux('manger', 'pqp', 4), xaux('finir', 'pqp', 3), xaux('chanter', 'pqp', 5), xaux('jouer', 'pqp', 0)],
 'Avec être, j’accorde': [xpp('tomber', 'pqp', 5), xpp('partir', 'pqp', 2), xpp('arriver', 'pqp', 3), xpp('entrer', 'pqp', 2)],
 'À la forme négative': [xneg('manger', 'pqp', 0), xneg('finir', 'pqp', 2), xneg('regarder', 'pqp', 3), xneg('jouer', 'pqp', 5)],
 'Passé composé ou plus-que-parfait ?': [xq('jouer', 'pqp', 2, ['pc', 'pqp']), xq('finir', 'pc', 5, ['pc', 'pqp']), xq('regarder', 'pqp', 3, ['pc', 'pqp']), xq('manger', 'pc', 2, ['pc', 'pqp'])],
}
SP['C9-CM2'] = {
 'Le passé simple': [cc('', '« ils bondirent » est au…', 'passé simple', ['l’imparfait', 'futur'], 'Je regarde la terminaison : -irent.'), cc('', '« elle chanta » est au…', 'passé simple', ['présent', 'futur'], 'Je regarde la terminaison : -a.'),
   cc('', '« ils prirent » est au…', 'passé simple', ['l’imparfait', 'présent'], 'Je regarde la terminaison : -irent.'), cc('', '« il fit » est au…', 'passé simple', ['l’imparfait', 'futur'], 'Je regarde la terminaison : -it.')],
 '2e groupe : -is, -it': [x('ps', 'surgir', 5, explic=True), x('ps', 'bondir', 2, explic=True), x('ps', 'finir', 5, explic=True), x('ps', 'choisir', 2, explic=True)],
 'Des verbes en i': [x('ps', 'faire', 5, explic=True), x('ps', 'dire', 2, explic=True), x('ps', 'prendre', 5, explic=True), x('ps', 'voir', 2, explic=True)],
 'Des verbes en u, en in': [x('ps', 'pouvoir', 5, explic=True), x('ps', 'vouloir', 2, explic=True), x('ps', 'venir', 5, explic=True), x('ps', 'vouloir', 5, explic=True)],
 'Les pièges': [x('ps', 'aller', 5, explic=True), xp('ps', 'chanter', 2), xp('ps', 'finir', 5), xp('ps', 'prendre', 2)],
}
if __name__ == '__main__':
    for g in SP:
        titres = [e['titre'] for e in lessons_json(g)['ecrans']]
        manque = [t for t in titres if t not in SP[g]]
        assert not manque, (g, manque)
        appliquer(g, {t: mk(SP[g][t]) for t in titres})
