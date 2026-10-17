import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from mapgen import build, TL, TC, TR
from lhelp import *
from hlib import R, rows, table

# H3 — ce, ces, à. Jumeaux interdits : se, ses, a (verbe avoir), et les sons voisins c’est / s’est.
boxes = [
 dict(id='ce', col='bleu', geom=TL, title='ce, cet, cette', avatar=('girl', 322, 122), html=f'''
  <p class="txt" style="padding-right:100px">Des <b>déterminants</b> : je <b>montre</b> une chose ou une personne.</p>
  <div class="exl" style="font-size:21px;line-height:1.6;margin-top:12px;margin-right:110px">{R("ce")} chien<br>{R("cet")} arbre <span class="small">(voyelle, h)</span><br>{R("cette")} fleur</div>'''),
 dict(id='ces', col='vert', geom=TC, title='ces : au pluriel', html=rows([
   ('ces', 'déterminant, devant un nom au pluriel', 'je mets au <b>singulier</b> : ce, cet, cette', f'{R("ces")} chiens → ce chien')]) +
   f'<span class="exl" style="margin-top:6px">{R("ces")} fleurs → cette fleur</span>'),
 dict(id='a', col='orange', geom=TR, title='à : le petit mot', html=rows([
   ('à', 'un petit mot qui ne change jamais', 'je mets la phrase au <b>passé</b> : <b>à</b> ne bouge pas', f'Je vais {R("à")} la piscine.<br>→ Hier, j’allais {R("à")} la piscine.')]) +
   f'<p class="txt" style="margin-top:6px">{R("à")} + le = <b>au</b> : je vais au marché.</p>'),
 dict(id='mix', col='violet', geom=(18, 568, 560, 350), title='Je prouve', style='padding-top:52px', avatar=('boy', 445, 610), html=
   '<p class="txt" style="padding-right:110px">Je fais une manipulation pour trouver le bon mot.</p>' + table([
     ('ce', '→ au pluriel : ces'), ('ces', '→ au singulier : ce, cet, cette'), ('à', '→ au passé, il ne change pas')])),
 dict(id='att', col='rouge', geom=(612, 568, 770, 350), title='Attention !', style='padding-top:52px', html='''
  <ul style="font-size:22px;line-height:1.5">
   <li><b>cet</b> devant une voyelle ou un h muet : <i>cet ami, cet hiver</i>.</li>
   <li><b>ces</b> est toujours suivi d’un nom au <b>pluriel</b>.</li>
   <li>En majuscule, <b>À</b> garde son accent : <i>À demain !</i></li></ul>'''),
]
out, zones = build('H3', 'ce, ces, à', 'Homophones — H3 — CM1', None, boxes, title_size=40, sub='homophones')

sections = [
 {'id': 'ce', 'nom': 'ce, cet, cette', 'couleur': '#1f5fc4'},
 {'id': 'ces', 'nom': 'ces : au pluriel', 'couleur': '#23845a'},
 {'id': 'a', 'nom': 'à : le petit mot', 'couleur': '#e67e22'},
 {'id': 'mix', 'nom': 'Je prouve', 'couleur': '#7b3fa0'},
 {'id': 'att', 'nom': 'Attention !', 'couleur': '#c62828'},
]
ecrans = [
 E('ce', 'doigt', 'ce, cet, cette', 'girl', 'Je montre une chose : ce, cet, cette sont des déterminants.',
   [('|ce| chien · |cette| fleur', 'Ils sont devant un nom : je montre.'),
    ('|cet| arbre · |cet| hiver', 'cet devant une voyelle ou un h muet.'),
    ('|ce| ~petit~ chien', 'Un adjectif peut être placé entre les deux.')],
   Q('___ arbre est très vieux.', ['Cet', 'Ce', 'Cette'], 'Arbre commence par une voyelle.', fill='circ'),
   [Q('___ fleur sent bon.', ['Cette', 'Ce', 'Cet'], 'Fleur est féminin.', fill='circ'),
    Q('___ chien aboie.', ['Ce', 'Cet', 'Cette'], 'Chien est masculin et commence par une consonne.', fill='circ'),
    C('J’aime <cette> chanson.', 'Clique sur le déterminant.', 'Il est devant le nom « chanson ».')]),
 E('ces', 'wagon', 'ces : au pluriel', 'boy', 'Au pluriel, ce, cet et cette deviennent ces.',
   [('|ce| chien → |*ces*| chiens', 'Plusieurs chiens : ces.'),
    ('|cette| fleur → |*ces*| fleurs', 'Au pluriel, toujours ces.'),
    ('|ces| ~grands~ arbres', 'ces est suivi d’un nom au pluriel.')],
   Q('J’aime ___ chansons.', ['ces', 'ce', 'cette'], 'Chansons : pluriel.', fill='circ'),
   [Q('Regarde ___ nuages !', ['ces', 'ce', 'cet'], 'Nuages : pluriel.', fill='circ'),
    Q('___ enfants jouent dehors.', ['Ces', 'Cet', 'Ce'], 'Enfants : pluriel.', fill='circ')]),
 E('ces', 'remplacer', 'Je change le nombre', 'boy', 'Je prouve : je passe du singulier au pluriel.',
   [('|cet| oiseau chante. → |ces| oiseaux chantent.', 'singulier → pluriel'),
    ('|ces| vélos → |ce| vélo', 'pluriel → singulier')],
   Q2('___ oiseau chante. ___ oiseaux chantent.',
      ('Premier trou :', ['Cet', 'Ce', 'Ces'], 'Oiseau commence par une voyelle.', 'circ'),
      ('Deuxième trou :', ['Ces', 'Cet', 'Ce'], 'Oiseaux : pluriel.', 'circ')),
   [Q2('___ maison est grande. ___ maisons sont grandes.',
      ('Premier trou :', ['Cette', 'Ce', 'Ces'], 'Maison : féminin singulier.', 'circ'),
      ('Deuxième trou :', ['Ces', 'Cette', 'Ce'], 'Maisons : pluriel.', 'circ'))]),
 E('a', 'attention', 'à : le petit mot', 'girl', 'À est un petit mot qui ne change jamais.',
   ['Je vais |à| la piscine.',
    ('Hier, j’allais |à| la piscine.', 'Je prouve : je mets au passé. Le verbe change, à ne change pas.'),
    ('|à| Paris · |à| midi · |à| vélo', 'à indique souvent un lieu ou un moment.')],
   Q('Je pars ___ midi.', ['à', 'ce', 'ces'], 'Un petit mot devant un moment.', fill='circ'),
   [Q('Il habite ___ Lyon.', ['à', 'ce', 'ces'], 'Un petit mot devant un lieu.', fill='circ'),
    Q('Nous rentrons ___ pied.', ['à', 'ce', 'ces'], 'Un petit mot qui ne change jamais.', fill='circ')]),
 E('a', 'tableau', 'à ne change jamais', 'girl', 'Le sujet change, le temps change… à reste le même.',
   ['Tom joue |à| la balle.',
    ('Les enfants jouent |à| la balle.', 'Le sujet change : à ne change pas.'),
    ('|à| + le = |*au*| : je vais au marché.', 'à et le deviennent au.')],
   Q('Elle pense ___ son anniversaire.', ['à', 'ce', 'ces'], 'Un petit mot qui ne change jamais.', fill='circ'),
   [Q('Demain, nous irons ___ marché.', ['au', 'à le', 'ces'], 'à + le = au.', fill='circ'),
    Q('Je donne un dessin ___ Léa.', ['à', 'ce', 'ces'], 'Un petit mot qui ne change jamais.', fill='circ')]),
 E('mix', 'liste', 'Je choisis le bon mot', 'boy', 'Je prouve chaque mot avec une manipulation.',
   [('|Ce| matin, je vais |à| l’école.', 'ce matin → ces matins · à ne change pas'),
    ('|Ces| enfants jouent |à| cache-cache.', 'ces enfants → cet enfant · à ne change pas')],
   Q2('___ soir, nous allons ___ la fête.',
      ('Premier trou :', ['Ce', 'Ces', 'À'], 'Soir est un nom masculin singulier.', 'circ'),
      ('Deuxième trou :', ['à', 'ce', 'ces'], 'Un petit mot qui ne change jamais.', 'circ')),
   [Q2('Je prête ___ livres ___ mon cousin.',
      ('Premier trou :', ['ces', 'ce', 'à'], 'Livres : pluriel.', 'circ'),
      ('Deuxième trou :', ['à', 'ce', 'ces'], 'Un petit mot qui ne change jamais.', 'circ'))]),
 E('att', 'attention', 'Les pièges', 'girl', 'Attention à cet, et à la majuscule !',
   [('|cet| ami · |cet| hiver', 'cet devant une voyelle ou un h muet.'),
    ('|À| demain !', 'En majuscule, À garde son accent.')],
   Q('', ['Cet ami est gentil.', 'Ce ami est gentil.'], 'Ami commence par une voyelle.', 'Quelle phrase est bien écrite ?'),
   [Q('', ['Ces voitures roulent vite.', 'Ces voiture roulent vite.'], 'Après ces, le nom est au pluriel.', 'Quelle phrase est bien écrite ?')]),
]
save('H3', {'id': 'H3', 'f': 'H', 'ceinture': 'Jaune', 'titre': 'ce, ces, à', 'sous': 'les démonstratifs · le petit mot à', 'lesson': True}, sections, ecrans, zones)
