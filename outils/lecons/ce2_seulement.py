"""Ceintures CE2 seulement : C6 (verbes irréguliers au présent), C7 (verbes irréguliers au futur, à l'imparfait,
au passé composé), O7 (les sons « o », « é », « è » et les accents). Identifiants : C6-CE2, C7-CE2, O7-CE2."""
import os, sys, re
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from mapgen import build, TL, TC, TR
from lhelp import *
from hlib import A
from clib import T, conj

BL = (18, 568, 560, 350)
H = 'hl'
BR = (612, 568, 770, 350)
SEC = lambda *l: [{'id': i, 'nom': n, 'couleur': c} for (i, n), c in zip(l, ['#1f5fc4', '#23845a', '#7b3fa0', '#e67e22', '#c62828'])]


def tab(verbe, rows, size=20):
    """rows : (pronom, radical, terminaison)"""
    return f'<p class="txt" style="margin:0 0 4px;font-size:21px"><b>{verbe}</b></p>' + conj(rows, size)


# ================================================================ C6 : verbes irréguliers au présent
def fv(verbe, f):
    """f : 6 couples (radical, terminaison) pour je, tu, il, nous, vous, ils"""
    p = ['je', 'tu', 'il', 'nous', 'vous', 'ils']
    x = [f"{p[i]} {r}{T(e) if e else ''}" for i, (r, e) in enumerate(f)]
    x[0] = x[0].replace('je a', 'j’a')
    return f'<b style="font-size:20px">{verbe}</b><br>' + ' · '.join(x[:3]) + '<br>' + ' · '.join(x[3:])
def bx(*vs, pr=0):
    return f'<div class="exl" style="font-size:17.5px;line-height:1.5;margin-top:4px;margin-right:{pr}px">' + '<br>'.join(vs) + '</div>'
ALLER = fv('aller', [('v','ais'),('v','as'),('v','a'),('all','ons'),('all','ez'),('v','ont')])
FAIRE = fv('faire', [('fai','s'),('fai','s'),('fai','t'),('fais','ons'),('fai','tes'),('f','ont')])
DIRE = fv('dire', [('di','s'),('di','s'),('di','t'),('dis','ons'),('di','tes'),('dis','ent')])
VENIR = fv('venir', [('vien','s'),('vien','s'),('vien','t'),('ven','ons'),('ven','ez'),('vienn','ent')])
POUV = fv('pouvoir', [('peu','x'),('peu','x'),('peu','t'),('pouv','ons'),('pouv','ez'),('peuv','ent')])
VOUL = fv('vouloir', [('veu','x'),('veu','x'),('veu','t'),('voul','ons'),('voul','ez'),('veul','ent')])
VOIR = fv('voir', [('voi','s'),('voi','s'),('voi','t'),('voy','ons'),('voy','ez'),('voi','ent')])
PREN = fv('prendre', [('prend','s'),('prend','s'),('prend',''),('pren','ons'),('pren','ez'),('prenn','ent')])
boxes = [
 dict(id='aller', col='bleu', geom=TL, title='aller, faire', html=bx(ALLER, FAIRE), style='padding-top:62px'),
 dict(id='dire', col='vert', geom=TC, title='dire, venir', html=bx(DIRE, VENIR), style='padding-top:54px'),
 dict(id='pouvoir', col='violet', geom=TR, title='pouvoir, vouloir', html=bx(POUV, VOUL), style='padding-top:62px'),
 dict(id='voir', col='orange', geom=BL, title='voir, prendre', style='padding-top:52px', avatar=('boy', 445, 610), html=bx(VOIR, PREN, pr=100)),
 dict(id='att', col='rouge', geom=BR, title='Attention !', style='padding-top:52px', avatar=('girl', 1250, 790), html=f'''
  <ul style="font-size:21px;line-height:1.5;padding-right:20px">
   <li>Le <b>radical change</b> : je viens, nous venons, ils viennent.</li>
   <li>tu <b>peux</b>, tu <b>veux</b> : avec un x.</li>
   <li>vous <b>faites</b>, vous <b>dites</b> ; ils <b>vont</b>, ils <b>font</b> : à connaître par cœur.</li>
   <li>il <b>prend</b> : pas de t.</li></ul>'''),
]
legend = '<span class="t">terminaison</span>'
out, zones = build('C6-CE2', 'Les verbes<br>irréguliers', 'Conjugaison — C6 — CE2', legend, boxes, title_size=36, sub='au présent', legend_pos='right:18px;top:470px')
sections = SEC(('aller', 'aller, faire'), ('dire', 'dire, venir'), ('pouvoir', 'pouvoir, vouloir'), ('voir', 'voir, prendre'), ('att', 'Attention !'))
ecrans = [
 E('aller', 'liste', 'aller et faire', 'girl', 'aller et faire ne suivent pas la règle du 1er groupe : je les apprends par cœur.',
   ['je v§ais§ · tu v§as§ · il v§a§', 'nous all§ons§ · vous all§ez§ · ils v§ont§',
    ('je fai§s§ · nous fais§ons§ · vous fai§tes§ · ils f§ont§', 'Je les apprends par cœur.')],
   Q('Ils ___ à la piscine.', ['vont', 'allent', 'vas'], 'aller, avec ils : ils vont.', 'Complète avec « aller » au présent.', fill='v'),
   [Q('Vous ___ un gâteau.', ['faites', 'faisez', 'font'], 'faire, avec vous : vous faites.', 'Complète avec « faire » au présent.', fill='v'),
    Q('Je ___ à l’école.', ['vais', 'vas', 'va'], 'aller, avec je : je vais.', 'Complète avec « aller » au présent.', fill='v'),
    Q('Les enfants ___ du vélo.', ['font', 'faisent', 'fait'], 'faire, avec ils : ils font.', 'Complète avec « faire » au présent.', fill='v')]),
 E('dire', 'bulle', 'dire et venir', 'boy', 'dire et venir : attention aux radicaux qui changent.',
   ['je di§s§ · il di§t§ · vous di§tes§ · ils dis§ent§', 'je vien§s§ · nous ven§ons§ · ils vienn§ent§',
    ('Le radical de venir change : vien-, ven-, vienn-.', '')],
   Q('Vous ___ merci.', ['dites', 'disez', 'disent'], 'dire, avec vous : vous dites.', 'Complète avec « dire » au présent.', fill='v'),
   [Q('Mes cousins ___ ce soir.', ['viennent', 'venent', 'vienent'], 'venir, avec ils : ils viennent.', 'Complète avec « venir » au présent.', fill='v'),
    Q('Nous ___ à pied.', ['venons', 'viennons', 'venont'], 'venir, avec nous : nous venons.', 'Complète avec « venir » au présent.', fill='v')]),
 E('pouvoir', 'attention', 'pouvoir et vouloir', 'girl', 'pouvoir et vouloir : un x avec je et tu.',
   ['je peu§x§ · tu peu§x§ · il peu§t§', 'je veu§x§ · tu veu§x§ · il veu§t§',
    ('nous pouv§ons§ · ils peuv§ent§ · nous voul§ons§ · ils veul§ent§', 'Le radical change avec nous et ils.')],
   Q('Tu ___ venir avec nous.', ['peux', 'peut', 'peus'], 'pouvoir, avec tu : un x.', 'Complète avec « pouvoir » au présent.', fill='v'),
   [Q('Les filles ___ jouer.', ['veulent', 'voulent', 'veut'], 'vouloir, avec ils : ils veulent.', 'Complète avec « vouloir » au présent.', fill='v'),
    Q('Je ___ un verre d’eau.', ['veux', 'veut', 'veus'], 'vouloir, avec je : un x.', 'Complète avec « vouloir » au présent.', fill='v')]),
 E('voir', 'loupe', 'voir et prendre', 'boy', 'voir et prendre : le radical change avec nous et ils.',
   ['je voi§s§ · nous voy§ons§ · ils voi§ent§', 'je prend§s§ · il prend · nous pren§ons§ · ils prenn§ent§',
    ('il prend : pas de t !', '')],
   Q('Ils ___ le bus.', ['prennent', 'prenent', 'prendent'], 'prendre, avec ils : ils prennent.', 'Complète avec « prendre » au présent.', fill='v'),
   [Q('Nous ___ la mer.', ['voyons', 'voions', 'voyont'], 'voir, avec nous : nous voyons.', 'Complète avec « voir » au présent.', fill='v'),
    Q('Léo ___ son goûter.', ['prend', 'prent', 'prends'], 'prendre, avec il : il prend, sans t.', 'Complète avec « prendre » au présent.', fill='v')]),
 E('att', 'attention', 'Les pièges', 'girl', 'Quelques formes sont à connaître par cœur.',
   [('vous |faites| · vous |dites|', 'Pas de -ez !'), ('ils |vont| · ils |font|', 'Pas de -ent !'), ('tu |peux| · tu |veux|', 'Un x avec tu.')],
   Q('', ['Vous dites bonjour.', 'Vous disez bonjour.'], 'vous dites : pas de -ez.', 'Quelle phrase est bien écrite ?'),
   [Q('', ['Ils vont au parc.', 'Ils allent au parc.'], 'ils vont.', 'Quelle phrase est bien écrite ?'),
    Q('', ['Tu peux entrer.', 'Tu peus entrer.'], 'tu peux : un x.', 'Quelle phrase est bien écrite ?')]),
]
save('C6-CE2', {'id': 'C6-CE2', 'code': 'C6', 'niveau': 'CE2', 'f': 'C', 'ceinture': 'Rouge', 'titre': 'Les verbes irréguliers au présent', 'sous': 'aller, faire, dire, venir, pouvoir, vouloir, voir, prendre', 'lesson': True}, sections, ecrans, zones)

# ================================================================ C7 : verbes irréguliers aux autres temps
boxes = [
 dict(id='futur', col='bleu', geom=TL, title='Au futur', avatar=('girl', 322, 122), html=f'''
  <p class="txt" style="padding-right:100px">Le <b>radical</b> change, la terminaison reste.</p>
  <div class="exl" style="font-size:19px;line-height:1.5;margin-top:6px;padding-right:96px">j’i{T("rai")} · je fe{T("rai")}<br>je di{T("rai")} · je viend{T("rai")}<br>je pour{T("rai")} · je ver{T("rai")}<br>je voud{T("rai")} · je prend{T("rai")}</div>'''),
 dict(id='imparfait', col='vert', geom=TC, title='À l’imparfait', html=f'''
  <p class="txt">Je pars du radical de <b>nous</b> au présent.</p>
  <div class="exl" style="font-size:20px;line-height:1.55">nous fais<b>ons</b> → je fais{T("ais")}<br>nous all<b>ons</b> → j’all{T("ais")}<br>nous pren<b>ons</b> → je pren{T("ais")}</div>'''),
 dict(id='pp', col='violet', geom=TR, title='Le participe passé', html=f'''
  <div class="exl" style="font-size:20px;line-height:1.6">aller → all{T("é")} · faire → fai{T("t")}<br>dire → di{T("t")} · venir → ven{T("u")}<br>pouvoir → p{T("u")} · voir → v{T("u")}<br>vouloir → voul{T("u")} · prendre → pri{T("s")}</div>'''),
 dict(id='etre', col='orange', geom=BL, title='Avec avoir ou être', style='padding-top:52px', avatar=('boy', 445, 610), html=f'''
  <p class="txt" style="padding-right:110px">Avec <b>avoir</b> : j’ai fait, il a dit, nous avons pris.</p>
  <p class="txt" style="padding-right:110px">Avec <b>être</b> : je suis allé, il est venu.</p>'''),
 dict(id='att', col='rouge', geom=BR, title='Attention !', style='padding-top:52px', html='''
  <ul style="font-size:21px;line-height:1.5">
   <li>je <b>pourrai</b>, je <b>verrai</b> : deux r au futur.</li>
   <li>il <b>fait</b> (présent) · il a <b>fait</b> (passé composé) : l’auxiliaire m’aide.</li>
   <li>pris, fait, dit : une lettre muette à la fin.</li></ul>'''),
]
out, zones = build('C7-CE2', 'Les verbes<br>irréguliers', 'Conjugaison — C7 — CE2', legend, boxes, title_size=36, sub='futur, imparfait, passé composé', legend_pos='right:18px;top:470px')
sections = SEC(('futur', 'Au futur'), ('imparfait', 'À l’imparfait'), ('pp', 'Le participe passé'), ('etre', 'Avec avoir ou être'), ('att', 'Attention !'))
ecrans = [
 E('futur', 'horloge', 'Au futur', 'girl', 'Au futur, le radical change, mais la terminaison reste : -rai, -ras, -ra…',
   ['aller → j’i§rai§ · faire → je fe§rai§', 'venir → je viend§rai§ · prendre → je prend§rai§',
    ('pouvoir → je pour§rai§ · voir → je ver§rai§', 'Deux r !')],
   Q('Demain, nous ___ au cinéma.', ['irons', 'allerons', 'allons'], 'aller au futur : nous irons.', 'Complète avec « aller » au futur.', fill='v'),
   [Q('Demain, tu ___ tes devoirs.', ['feras', 'faireras', 'fais'], 'faire au futur : tu feras.', 'Complète avec « faire » au futur.', fill='v'),
    Q('Ce soir, je ___ la lune.', ['verrai', 'voirai', 'verai'], 'voir au futur : deux r.', 'Complète avec « voir » au futur.', fill='v'),
    Q('Ils ___ le train.', ['prendront', 'prenront', 'prendent'], 'prendre au futur : ils prendront.', 'Complète avec « prendre » au futur.', fill='v')]),
 E('imparfait', 'remplacer', 'À l’imparfait', 'boy', 'À l’imparfait, je pars du radical de « nous » au présent.',
   ['nous fais§ons§ → je fais§ais§', 'nous all§ons§ → j’all§ais§',
    ('nous pren§ons§ → je pren§ais§', 'Les terminaisons sont les mêmes que pour tous les verbes.')],
   Q('Autrefois, je ___ du piano.', ['faisais', 'fesais', 'fairais'], 'nous faisons → je faisais.', 'Complète avec « faire » à l’imparfait.', fill='v'),
   [Q('Avant, nous ___ à la plage.', ['allions', 'vions', 'irions'], 'nous allons → nous allions.', 'Complète avec « aller » à l’imparfait.', fill='v'),
    Q('Il ___ toujours le bus.', ['prenait', 'prendait', 'prennait'], 'nous prenons → il prenait.', 'Complète avec « prendre » à l’imparfait.', fill='v')]),
 E('pp', 'etiquette', 'Le participe passé', 'girl', 'Au passé composé, il faut connaître le participe passé.',
   ['aller → all§é§ · faire → fai§t§ · dire → di§t§', 'venir → ven§u§ · pouvoir → p§u§ · voir → v§u§',
    ('vouloir → voul§u§ · prendre → pri§s§', 'Je les apprends par cœur.')],
   Q('J’ai ___ mon lit.', ['fait', 'fais', 'faire'], 'faire → fait.', 'Complète avec le participe passé de « faire ».', fill='t'),
   [Q('Nous avons ___ un film.', ['vu', 'voir', 'vus'], 'voir → vu.', 'Complète avec le participe passé de « voir ».', fill='t'),
    Q('Elle a ___ son manteau.', ['pris', 'prit', 'prendu'], 'prendre → pris.', 'Complète avec le participe passé de « prendre ».', fill='t')]),
 E('etre', 'wagon', 'Avec avoir ou être', 'boy', 'aller et venir se conjuguent avec être ; les autres avec avoir.',
   [('j’(ai) fai§t§ · il (a) di§t§', 'Avec avoir.'), ('je (suis) all§é§ · il (est) ven§u§', 'Avec être : aller et venir.')],
   Q('Hier, Léo ___ au parc.', ['est allé', 'a allé', 'allait'], 'aller se conjugue avec être.', 'Complète avec le passé composé.', fill='v'),
   [Q('Hier, j’___ bonjour.', ['ai dit', 'suis dit', 'disais'], 'dire se conjugue avec avoir.', 'Complète avec le passé composé.', fill='v'),
    Q('Ma tante ___ nous voir.', ['est venue', 'a venu', 'venait'], 'venir se conjugue avec être.', 'Complète avec le passé composé.', fill='v')]),
 E('att', 'attention', 'Les pièges', 'girl', 'Quelques pièges à connaître.',
   [('je |pourrai| · je |verrai|', 'Deux r au futur.'), ('il |fait| · il a |fait|', 'Présent, puis passé composé : l’auxiliaire m’aide.')],
   Q('', ['Je pourrai venir.', 'Je pourai venir.', 'Je pouvrai venir.'], 'pouvoir au futur : deux r.', 'Quelle phrase est bien écrite ?'),
   [Q('', ['Il a pris son sac.', 'Il a prit son sac.'], 'prendre → pris.', 'Quelle phrase est bien écrite ?')]),
]
save('C7-CE2', {'id': 'C7-CE2', 'code': 'C7', 'niveau': 'CE2', 'f': 'C', 'ceinture': 'Violette', 'titre': 'Les verbes irréguliers aux autres temps', 'sous': 'futur, imparfait, passé composé', 'lesson': True}, sections, ecrans, zones)


# ================================================================ O7 : les sons « o », « é », « è » et les accents
def M(t):
    t = re.sub(r'%([^%]+)%', r'<span style="background:#ffe066;border-radius:4px;padding:0 1px;font-weight:700">\1</span>', t)
    return t.replace('→', A)
ex = lambda *l, size=21: f'<div class="exl" style="font-size:{size+2}px;line-height:1.6;margin-top:10px">' + '<br>'.join(M(x) for x in l) + '</div>'
txt = lambda t, pr=0: f'<p class="txt" style="padding-right:{pr}px;font-size:22px">{M(t)}</p>'
boxes = [
 dict(id='o', col='bleu', geom=TL, title='Le son « o »', avatar=('girl', 322, 122), html=txt('o, <b>au</b> ou <b>eau</b>', 100) + ex('un vél%o% · une r%o%se', 'j%au%ne · ch%au%d', 'un bat%eau% · un gât%eau%', size=20)),
 dict(id='e', col='vert', geom=TC, title='Le son « é »', html=txt('<b>é</b>, <b>er</b>, <b>ez</b>') + ex('un caf%é% · l’%é%t%é%', 'chant%er% · un boulang%er%', 'vous chant%ez% · le n%ez%', size=19)),
 dict(id='ai', col='violet', geom=TR, title='Le son « è »', html=txt('<b>è</b>, <b>ê</b>, <b>ai</b>, <b>ei</b>') + ex('une m%è%re · une f%ê%te', 'une m%ai%son · du l%ai%t', 'la n%ei%ge · une r%ei%ne', size=19)),
 dict(id='accents', col='orange', geom=BL, title='Les accents', style='padding-top:52px', avatar=('boy', 445, 610), html=txt('L’accent change le son du e.', 110) + ex('é : accent aigu → l’%é%t%é%', 'è : accent grave → le p%è%re', 'ê : accent circonflexe → la f%ê%te', size=19)),
 dict(id='memo', col='rouge', geom=BR, title='Pour bien choisir', style='padding-top:52px', html='''
  <ul style="font-size:21px;line-height:1.5">
   <li><b>eau</b> souvent à la fin d’un nom : un bateau, un château.</li>
   <li><b>er</b> à la fin d’un verbe à l’infinitif : chanter ; <b>ez</b> avec vous : vous chantez.</li>
   <li>Une famille m’aide : la forêt → forestier, la fête → festin.</li>
   <li>Sinon, je mémorise le mot.</li></ul>'''),
]
leg = '<span style="background:#ffe066;font-weight:700;padding:0 4px">lettres étudiées</span>'
out, zones = build('O7-CE2', 'Les sons<br>o, é, è', 'Orthographe — O7 — CE2', leg, boxes, title_size=38, sub='et les accents', legend_pos='left:470px;top:880px')
sections = SEC(('o', 'Le son « o »'), ('e', 'Le son « é »'), ('ai', 'Le son « è »'), ('accents', 'Les accents'), ('memo', 'Pour bien choisir'))
ecrans = [
 E('o', 'mots', 'Le son « o »', 'girl', 'Le son « o » s’écrit o, au ou eau.',
   ['un vél%o% · une r%o%se', 'j%au%ne · ch%au%d', ('un bat%eau% · un gât%eau%', 'eau : souvent à la fin d’un nom.')],
   Q('un chap___', ['eau', 'au', 'o'], 'eau : souvent à la fin d’un nom.', 'Complète avec les bonnes lettres.', fill=H),
   [Q('une ___tomobile', ['au', 'eau', 'o'], 'Au début du mot : au.', 'Complète avec les bonnes lettres.', fill=H),
    Q('un ch___teau', ['â', 'au', 'eau'], 'château : un accent circonflexe.', 'Complète avec la bonne lettre.', fill=H)]),
 E('e', 'remplacer', 'Le son « é »', 'boy', 'Le son « é » s’écrit é, er ou ez.',
   ['un caf%é% · l’%é%t%é%', ('chant%er% · un boulang%er%', 'er : à la fin d’un verbe à l’infinitif, et de certains métiers.'), ('vous chant%ez%', 'ez : avec vous.')],
   Q('Vous mang___ une pomme.', ['ez', 'er', 'é'], 'Avec vous : ez.', 'Complète avec les bonnes lettres.', fill=H),
   [Q('Il faut ferm___ la porte.', ['er', 'ez', 'é'], 'Un verbe à l’infinitif : er.', 'Complète avec les bonnes lettres.', fill=H),
    Q('une ___cole', ['é', 'er', 'ez'], 'Au début du mot : é.', 'Complète avec la bonne lettre.', fill=H)]),
 E('ai', 'liste', 'Le son « è »', 'girl', 'Le son « è » s’écrit è, ê, ai ou ei.',
   ['une m%è%re · une f%ê%te', 'une m%ai%son · du l%ai%t', ('la n%ei%ge · une r%ei%ne', 'Je mémorise ces mots.')],
   Q('du l___t', ['ai', 'è', 'ei'], 'lait → laitier.', 'Complète avec les bonnes lettres.', fill=H),
   [Q('la n___ge', ['ei', 'ai', 'è'], 'neige : je mémorise.', 'Complète avec les bonnes lettres.', fill=H),
    Q('mon p___re', ['è', 'ai', 'ê'], 'père : accent grave.', 'Complète avec la bonne lettre.', fill=H)]),
 E('accents', 'attention', 'Les accents', 'boy', 'L’accent change le son du e.',
   [('l’%é%t%é%', 'é : accent aigu → « é ».'), ('le p%è%re', 'è : accent grave → « è ».'), ('la f%ê%te', 'ê : accent circonflexe → « è ».')],
   Q('', ['un élève', 'un elève', 'un élêve'], 'é puis è.', 'Quel mot est bien écrit ?'),
   [Q('', ['la forêt', 'la foret', 'la forèt'], 'forêt → forestier : ê.', 'Quel mot est bien écrit ?'),
    Q('', ['une rivière', 'une riviere', 'une riviêre'], 'rivière : accent grave.', 'Quel mot est bien écrit ?')]),
 E('memo', 'coche', 'Pour bien choisir', 'girl', 'Je regarde la place dans le mot, la famille, ou je mémorise.',
   [('un bat%eau%', 'eau à la fin d’un nom.'), ('la for%ê%t → forestier', 'La famille m’aide : le s caché, c’est l’accent circonflexe.'),
    ('chant%er% · vous chant%ez%', 'er : infinitif ; ez : vous.')],
   Q('', ['Parce que c’est un verbe à l’infinitif.', 'Parce que c’est un nom.', 'Parce que le mot est court.'], 'Je peux dire « il faut sauter ».', 'Pourquoi « sauter » finit-il par er ?'),
   [Q('', ['un gâteau', 'un gâtau', 'un gateau'], 'eau à la fin du nom ; â.', 'Quel mot est bien écrit ?')]),
]
save('O7-CE2', {'id': 'O7-CE2', 'code': 'O7', 'niveau': 'CE2', 'f': 'O', 'ceinture': 'Violette', 'titre': 'Les sons o, é, è et les accents', 'sous': 'o, au, eau ; é, er, ez ; è, ê, ai, ei', 'lesson': True}, sections, ecrans, zones)
