import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from mapgen import build, TL, TC, TR
from lhelp import *
from hlib import R, table, A

B = lambda t: f'<b style="color:#1f5fc4">{t}</b>'
P = lambda t: f'<span class="e">{t}</span>'
boxes = [
 dict(id='fam', col='bleu', geom=TL, title='Une famille de mots', avatar=('girl', 322, 122), html=f'''
  <p class="txt" style="padding-right:100px">Des mots qui ont une <b>partie commune</b> et qui parlent de la <b>même chose</b>.</p>
  <div class="exl" style="font-size:21px;line-height:1.6;margin-top:14px">{B("dent")} · {B("dent")}iste<br>{B("dent")}ifrice · é{B("dent")}é</div>
  <div class="exl" style="font-size:21px;line-height:1.6;margin-top:8px">{B("jardin")} · {B("jardin")}ier · {B("jardin")}age</div>'''),
 dict(id='trouver', col='vert', geom=TC, title='Je fabrique des mots', html=f'''
  <p class="txt">J’ajoute des morceaux <b>devant</b> ou <b>derrière</b> le mot de base.</p>
  <div class="exl" style="font-size:21px;line-height:1.6">{B("terre")} {A} {B("terr")}ain · {B("terr")}ier<br>en{B("terr")}er · sou{B("terr")}ain</div>'''),
 dict(id='intrus', col='orange', geom=TR, title='L’intrus', html=f'''
  <p class="txt">Un mot qui <b>ressemble</b>, mais qui ne parle pas de la même chose, n’est pas de la famille.</p>
  <div class="exl" style="font-size:21px;line-height:1.6">{B("chant")} · {B("chant")}er · {B("chant")}eur<br><span class="barre">champ</span> {A} l’intrus</div>
  <div class="exl" style="font-size:21px;line-height:1.6;margin-top:8px">{B("lait")} · {B("lait")}ier · <span class="barre">laid</span></div>'''),
 dict(id='ortho', col='violet', geom=(18, 568, 560, 350), title='La famille m’aide à écrire', style='padding-top:52px', avatar=('boy', 445, 610), html=f'''
  <p class="txt" style="padding-right:110px">J’entends la lettre muette dans un mot de la famille.</p>
  <div class="exl" style="font-size:23px;line-height:1.7;margin-right:110px">un lai{P("t")} {A} une lai{P("t")}ière<br>un galo{P("p")} {A} galo{P("p")}er<br>bavar{P("d")} {A} bavar{P("d")}er</div>'''),
 dict(id='reb', col='rouge', geom=(612, 568, 770, 350), title='Préfixes et suffixes', style='padding-top:52px', html=f'''
  <p class="txt" style="font-size:22px">Dans une famille, je retrouve les préfixes et les suffixes que je connais.</p>
  <div class="exl" style="font-size:25px;line-height:1.8;padding:8px 14px">{P("en")}{B("terr")}{P("er")} · {P("dé")}{B("terr")}{P("er")}<br>{B("jardin")}{P("ier")} · {B("jardin")}{P("age")}</div>'''),
]
out, zones = build('V4', 'Les familles<br>de mots', 'Vocabulaire — V4 — CM1', None, boxes, title_size=36)

sections = [
 {'id': 'fam', 'nom': 'Une famille de mots', 'couleur': '#1f5fc4'},
 {'id': 'trouver', 'nom': 'Je fabrique des mots', 'couleur': '#23845a'},
 {'id': 'intrus', 'nom': 'L’intrus', 'couleur': '#e67e22'},
 {'id': 'ortho', 'nom': 'La famille m’aide à écrire', 'couleur': '#7b3fa0'},
 {'id': 'reb', 'nom': 'Préfixes et suffixes', 'couleur': '#c62828'},
]
ecrans = [
 E('fam', 'mots', 'Une famille de mots', 'girl', 'Une partie commune, et le même sujet : c’est une famille.',
   ['dent · dentiste · dentifrice',
    ('|dent| · |dent|iste · |dent|ifrice', 'Ils ont une partie commune : dent.'),
    ('|dent| · |dent|iste · |dent|ifrice · é|dent|é', 'Et ils parlent tous des dents : c’est une famille.')],
   Q('', ['dentiste', 'danse', 'dans'], 'Même partie commune et même sujet.', 'Quel mot est de la famille de « dent » ?'),
   [Q('', ['jardinier', 'jarre', 'jaune'], 'Le métier lié au jardin.', 'Quel mot est de la famille de « jardin » ?'),
    Q('', ['fleuriste', 'flèche', 'fleuve'], 'Il parle des fleurs.', 'Quel mot est de la famille de « fleur » ?'),
    Q('', ['nageur', 'neige', 'nuage'], 'Il parle de nager.', 'Quel mot est de la famille de « nager » ?')]),
 E('trouver', 'remplacer', 'Je fabrique des mots', 'girl', 'J’ajoute des morceaux devant ou derrière le mot de base.',
   ['|terre|',
    ('|terr|ain · |terr|ier', 'J’ajoute un morceau derrière.'),
    ('en|terr|er · sou|terr|ain', 'Ou devant !')],
   Q('', ['laitier', 'laid', 'laine'], 'Il parle du lait.', 'Un mot de la famille de « lait » :'),
   [Q('', ['chanteuse', 'chaise', 'champ'], 'Elle parle de chanter.', 'Un mot de la famille de « chant » :'),
    Q('', ['coiffeur', 'coin', 'coffre'], 'Il parle de coiffer.', 'Un mot de la famille de « coiffer » :')]),
 E('intrus', 'attention', 'L’intrus', 'boy', 'Il ressemble, mais il ne parle pas de la même chose.',
   ['chant · chanter · chanteur · champ',
    ('|chant| · |chant|er · |chant|eur · {champ}', 'champ ressemble, mais ne parle pas de chanter : c’est l’intrus.')],
   Q('lait · laitier · laitage · laid', ['laid', 'laitier', 'laitage'], 'Lequel ne parle pas du lait ?', 'Quel est l’intrus ?'),
   [Q('mer · marin · marine · mère', ['mère', 'marin', 'marine'], 'Lequel ne parle pas de la mer ?', 'Quel est l’intrus ?'),
    Q('fleur · fleuriste · fleurir · flûte', ['flûte', 'fleuriste', 'fleurir'], 'Lequel ne parle pas des fleurs ?', 'Quel est l’intrus ?')]),
 E('ortho', 'ampoule', 'La famille m’aide à écrire', 'boy', 'J’entends la lettre muette dans un mot de la famille.',
   [('un lai%t% → une lai%t%ière', 'J’entends le t dans laitière : lait s’écrit avec un t.'),
    ('un galo%p% → galo%p%er', 'J’entends le p dans galoper.'),
    ('bavar%d% → bavar%d%er', 'J’entends le d dans bavarder.')],
   Q('', ['tapisser', 'taper', 'tapir'], 'Je cherche un mot de la famille de « tapis ».', '« tapis » finit par s, car on dit…'),
   [Q('', ['sportif', 'sporte', 'spore'], 'Je cherche un mot de la famille de « sport ».', '« sport » finit par t, car on dit…'),
    Q('un gran___ arbre', ['d', 't', 's'], 'Pense à « grande ».', 'Quelle lettre muette ?', fill='circ'),
    Q('un chan___ de blé', ['p', 't', 'd'], 'Pense à « champêtre ».', 'Quelle lettre muette ?', fill='circ')]),
 E('reb', 'ciseaux', 'Des morceaux que je connais', 'girl', 'Dans une famille, je retrouve les préfixes et les suffixes.',
   [('%en%|terr|%er%', 'en- devant, -er derrière.'),
    ('%dé%|terr|%er%', 'dé- : le contraire d’enterrer.'),
    ('|jardin|%ier% · |jardin|%age%', '-ier : un métier.')],
   Q('jardinier', ['-ier, à la fin', 'jard-, au début'], 'Cherche le mot de base : jardin.', 'Le morceau ajouté est…'),
   [Q('replanter', ['re-, au début', 'plant-, au milieu'], 'Cherche le mot de base : plant.', 'Le préfixe est…'),
    Q('', ['qui peut être lavé', 'qui lave', 'pas lavé'], '-able : qu’on peut.', 'Dans la famille de « laver », « lavable » veut dire…')]),
]
save('V4', {'id': 'V4', 'f': 'V', 'ceinture': 'Orange', 'titre': 'Les familles de mots', 'sous': 'partie commune et même sens', 'lesson': True}, sections, ecrans, zones)
