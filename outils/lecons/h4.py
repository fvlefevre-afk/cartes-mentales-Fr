import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from mapgen import build, TL, TC, TR
from lhelp import *
from hlib import R, rows, table

# H4 — et, ou, mais : les conjonctions de coordination. Jumeaux interdits : est, où, mes.
W = ['et', 'ou', 'mais']
boxes = [
 dict(id='et', col='bleu', geom=TL, title='et : j’ajoute', html=rows([
   ('et', 'relie deux mots ou deux parties de phrase', 'j’ajoute quelque chose', f'du pain {R("et")} du beurre')]) +
   f'<span class="exl" style="margin-top:6px">Il prend son sac {R("et")} il part.</span>'),
 dict(id='ou', col='vert', geom=TC, title='ou : je choisis', html=rows([
   ('ou', 'propose un choix', 'je dis <b>ou bien</b>', f'Tu veux du lait {R("ou")} du jus ?')]) +
   f'<span class="exl" style="margin-top:6px">pile {R("ou")} face</span>'),
 dict(id='mais', col='orange', geom=TR, title='mais : je m’oppose', html=rows([
   ('mais', 'oppose deux idées', 'les deux idées vont dans des sens <b>contraires</b>', f'Il pleut, {R("mais")} je sors.')]) +
   f'<span class="exl" style="margin-top:6px">Il paraît petit, {R("mais")} il court vite.</span>'),
 dict(id='inv', col='violet', geom=(18, 568, 560, 350), title='Des mots qui relient', style='padding-top:52px', avatar=('girl', 445, 610), html=f'''
  <p class="txt" style="padding-right:110px">Ce sont des <b>conjonctions de coordination</b> : elles relient, et elles ne changent <b>jamais</b>.</p>
  <div class="exl" style="font-size:22px;text-align:center;margin-right:110px">{R("et")} · {R("ou")} · {R("mais")}<br><span class="small">et aussi : donc, or, ni, car</span></div>'''),
 dict(id='att', col='rouge', geom=(612, 568, 770, 350), title='Attention !', style='padding-top:52px', avatar=('boy', 1250, 610), html='''
  <ul style="font-size:22px;line-height:1.5;padding-right:110px">
   <li>Souvent, une <b>virgule</b> avant <b>mais</b> : <i>Il pleut, mais je sors.</i></li>
   <li>En général, pas de virgule avant <b>et</b> ni avant <b>ou</b>.</li>
   <li>Pour choisir le bon mot, je pense au <b>sens</b> : ajouter, choisir ou opposer.</li></ul>'''),
]
out, zones = build('H4', 'et, ou, mais', 'Homophones — H4 — CM1', None, boxes, title_size=40, sub='homophones')

sections = [
 {'id': 'et', 'nom': 'et : j’ajoute', 'couleur': '#1f5fc4'},
 {'id': 'ou', 'nom': 'ou : je choisis', 'couleur': '#23845a'},
 {'id': 'mais', 'nom': 'mais : je m’oppose', 'couleur': '#e67e22'},
 {'id': 'inv', 'nom': 'Des mots qui relient', 'couleur': '#7b3fa0'},
 {'id': 'att', 'nom': 'Attention !', 'couleur': '#c62828'},
]
ecrans = [
 E('et', 'mots', 'et : j’ajoute', 'girl', 'Et relie deux mots ou deux parties de phrase : j’ajoute.',
   ['du pain |et| du beurre',
    ('Léa |et| Tom jouent.', 'et relie deux mots.'),
    ('Il prend son sac |et| il part.', 'et relie deux parties de phrase.')],
   Q('J’ai un chat ___ un chien.', W, 'J’ai les deux : j’ajoute.', fill='circ'),
   [Q('Nous rions ___ nous chantons.', W, 'Les deux à la fois : j’ajoute.', fill='circ'),
    C('Papa <et> moi faisons un gâteau.', 'Clique sur le mot qui relie.', 'Quel mot ajoute « moi » à « Papa » ?')]),
 E('ou', 'question', 'ou : je choisis', 'girl', 'Ou propose un choix : je peux dire « ou bien ».',
   ['Tu veux du lait |ou| du jus ?',
    ('Tu veux du lait |*ou bien*| du jus ?', 'Je prouve : je dis « ou bien » : un choix.'),
    ('pile |ou| face', 'Il faut choisir l’un ou l’autre.')],
   Q('Tu préfères le rouge ___ le bleu ?', W, 'Il faut choisir.', fill='circ'),
   [Q('Lundi ___ mardi, je viendrai.', W, 'L’un ou bien l’autre.', fill='circ'),
    Q('Tu prends le vélo ___ le bus ?', W, 'Il faut choisir.', fill='circ')]),
 E('mais', 'remplacer', 'mais : je m’oppose', 'boy', 'Mais relie deux idées qui s’opposent.',
   ['Il pleut. Je sors.',
    ('Il pleut, |*mais*| je sors.', 'mais oppose les deux idées.'),
    ('Il paraît petit, |mais| il court vite.', 'On s’attend à une chose… et c’est le contraire.')],
   Q('Il fait froid, ___ il y a du soleil.', W, 'Les deux idées s’opposent.', fill='circ'),
   [Q('Je voulais jouer, ___ il faisait nuit.', W, 'Les deux idées s’opposent.', fill='circ'),
    Q('C’était difficile, ___ j’ai réussi.', W, 'Les deux idées s’opposent.', fill='circ')]),
 E('inv', 'mots', 'Des mots qui ne changent jamais', 'girl', 'Et, ou, mais sont des conjonctions de coordination.',
   [('Léa |et| Tom · Léa |et| ses amies', 'et ne change pas, même au pluriel.'),
    ('|et| · |ou| · |mais| · donc · or · ni · car', 'La famille des mots qui relient.')],
   Q('', ['mais, ou, et', 'très, bien, vite', 'le, la, les'], 'Les mots qui relient.', 'Quelle liste contient des conjonctions de coordination ?'),
   [Q('', ['car', 'chat', 'courir'], 'Un mot qui relie, comme et, ou, mais.', 'Quel autre mot relie, comme et, ou, mais ?')]),
 E('inv', 'liste', 'Je choisis selon le sens', 'girl', 'J’ajoute ? Je choisis ? Je m’oppose ?',
   [('Nous rions |et| nous chantons.', 'j’ajoute : et'),
    ('Tu prends le vélo |ou| le bus ?', 'je choisis : ou'),
    ('Je voulais sortir, |mais| il pleuvait.', 'je m’oppose : mais')],
   Q2('Tu veux une pomme ___ une poire ? J’ai faim, ___ pas soif.',
      ('Premier trou :', W, 'Il faut choisir.', 'circ'),
      ('Deuxième trou :', ['mais', 'et', 'ou'], 'Faim et soif s’opposent ici.', 'circ')),
   [Q2('Je mets un bonnet ___ des gants, ___ j’ai encore froid.',
      ('Premier trou :', W, 'J’ajoute les gants.', 'circ'),
      ('Deuxième trou :', ['mais', 'et', 'ou'], 'Les deux idées s’opposent.', 'circ'))]),
 E('att', 'attention', 'Les pièges', 'boy', 'Une virgule avant mais, et je pense au sens.',
   [('Il pleut*,* |mais| je sors.', 'Souvent une virgule avant mais.'),
    ('Je prends du pain |et| du lait.', 'En général, pas de virgule avant et.')],
   Q('', ['Il fait beau, mais il fait froid.', 'Il fait beau mais, il fait froid.'], 'La virgule se place avant mais.', 'Choisis la phrase bien écrite.'),
   [Q('', ['Tu viens ou tu restes ?', 'Tu viens, ou, tu restes ?'], 'En général, pas de virgule avec ou.', 'Choisis la phrase bien écrite.')]),
]
save('H4', {'id': 'H4', 'f': 'H', 'ceinture': 'Orange', 'titre': 'et, ou, mais', 'sous': 'les mots qui relient', 'lesson': True}, sections, ecrans, zones)
