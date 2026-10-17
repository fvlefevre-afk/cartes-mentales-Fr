import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from mapgen import build, TL, TC, TR
from lhelp import *
from hlib import R, rows, table

# H2 — on, là, où. Jumeaux interdits dans toute la ceinture : ont, la, l’a, l’as, ou.
W = ['on', 'là', 'où']
boxes = [
 dict(id='on', col='bleu', geom=TL, title='Le pronom on', avatar=('girl', 322, 122), html=f'''
  <p class="txt" style="padding-right:100px"><b>on</b> est un <b>pronom</b> : il remplace des personnes.</p>
  <span class="exl" style="font-size:20px;margin-top:10px;margin-right:100px">{R("On")} joue dehors.</span>
  <p class="txt" style="margin-top:10px">Je prouve : je dis <b>quelqu’un</b>.<br><span class="small">Quelqu’un joue dehors.</span></p>
  <p class="small" style="margin:0">Le verbe est au <b>singulier</b> : on chante, on finit.</p>'''),
 dict(id='la', col='vert', geom=TC, title='là : un lieu', html=rows([
   ('là', 'indique un lieu', 'je dis <b>ici</b>', f'Pose ton sac {R("là")}. → Pose ton sac ici.')]) +
   f'<p class="txt" style="margin-top:6px">Je le retrouve dans : {R("là")}-bas, voi{R("là")}, celui-{R("là")}.</p>'),
 dict(id='ou', col='orange', geom=TR, title='où : le lieu', html=rows([
   ('où', 'indique un lieu', 'je réponds par un <b>lieu</b>', f'{R("Où")} vas-tu ? → Au parc.')]) +
   f'<span class="exl" style="margin-top:6px">Le parc {R("où")} je joue est grand.</span>'),
 dict(id='mix', col='violet', geom=(18, 568, 560, 350), title='Je prouve', style='padding-top:52px', avatar=('boy', 445, 610), html=
   '<p class="txt" style="padding-right:110px">Je fais une manipulation : si ma phrase garde son sens, j’ai trouvé le bon mot.</p>' + table([
     ('on', '→ quelqu’un'), ('là', '→ ici'), ('où', '→ je réponds par un lieu')])),
 dict(id='att', col='rouge', geom=(612, 568, 770, 350), title='Attention !', style='padding-top:52px', html='''
  <ul style="font-size:22px;line-height:1.5">
   <li>Avec <b>on</b>, le verbe se conjugue comme avec <b>il</b> : on jou<span class="e">e</span>, on fini<span class="e">t</span>.</li>
   <li>Ces mots gardent l’accent : <b>là-bas</b>, <b>voilà</b>, <b>celui-là</b>.</li>
   <li><b>où</b> commence souvent une question : <i style="white-space:nowrap">Où habites-tu ?</i></li></ul>'''),
]
out, zones = build('H2', 'on, là, où', 'Homophones — H2 — CM1', None, boxes, title_size=40, sub='homophones')

sections = [
 {'id': 'on', 'nom': 'Le pronom on', 'couleur': '#1f5fc4'},
 {'id': 'la', 'nom': 'là : un lieu', 'couleur': '#23845a'},
 {'id': 'ou', 'nom': 'où : le lieu', 'couleur': '#e67e22'},
 {'id': 'mix', 'nom': 'Je prouve', 'couleur': '#7b3fa0'},
 {'id': 'att', 'nom': 'Attention !', 'couleur': '#c62828'},
]
ecrans = [
 E('on', 'remplacer', 'on remplace des personnes', 'girl', 'On est un pronom : il remplace des personnes.',
   ['|On| joue dehors.',
    ('|*Quelqu’un*| joue dehors.', 'Je prouve : je dis « quelqu’un ».'),
    ('|On| frappe ! → *Quelqu’un* frappe !', 'on remplace une personne qu’on ne nomme pas.')],
   Q('Écoute ! ___ frappe.', W, 'Quelqu’un frappe : c’est un pronom.', fill='circ'),
   [C('<On> mange à midi.', 'Clique sur le pronom.', 'Quel mot remplace des personnes ?'),
    Q('Le soir, ___ regarde un film.', W, 'Quelqu’un regarde un film.', fill='circ'),
    C('Ce matin, <on> se lève tôt.', 'Clique sur le pronom.', 'Qui se lève tôt ?')]),
 E('on', 'sv', 'on : le verbe au singulier', 'girl', 'Avec on, le verbe se conjugue comme avec il.',
   [('[On] (chante).', 'on est le sujet du verbe.'),
    ('[Il] (chante) · [On] (chante)', 'Même terminaison qu’avec il.'),
    ('[On] (mange) · [On] (finit) · [On] (prend)', 'Le verbe est toujours au singulier.')],
   Q('On ___ dans le jardin.', ['joue', 'jouent', 'jouez'], 'On se conjugue comme il.', fill='v'),
   [Q('Le dimanche, on ___ tard.', ['dort', 'dorment', 'dormons'], 'On se conjugue comme il.', fill='v'),
    Q('À midi, on ___ ensemble.', ['mange', 'mangent', 'mangez'], 'On se conjugue comme il.', fill='v')]),
 E('la', 'doigt', 'là : un lieu', 'boy', 'Là indique un lieu : je peux dire « ici ».',
   ['Pose ton sac |là|.',
    ('Pose ton sac |*ici*|.', 'Je prouve : je dis « ici ». là indique un lieu.'),
    ('|là|-bas · voi|là| · celui-|là|', 'Je le retrouve dans d’autres mots.')],
   Q('Assieds-toi ___, près de moi.', W, 'Je peux dire « ici ».', fill='circ'),
   [Q('Mon chat dort ___, sur le canapé.', W, 'Je peux dire « ici ».', fill='circ'),
    Q('Tes clés ? Elles sont ___ !', W, 'Je peux dire « ici ».', fill='circ')]),
 E('ou', 'question', 'où : le lieu', 'boy', 'Où indique un lieu : je réponds par un lieu.',
   [('|Où| vas-tu ?', 'où pose une question.'),
    ('Je vais *au parc*.', 'Je prouve : je réponds par un lieu.'),
    ('Le parc |où| je joue est grand.', 'où indique un lieu.')],
   Q('___ habites-tu ?', ['Où', 'On', 'Là'], 'Je réponds par un lieu.', fill='circ'),
   [Q('Je sais ___ il habite.', W, 'C’est un lieu.', fill='circ'),
    Q('___ as-tu mis ton cahier ?', ['Où', 'On', 'Là'], 'Je réponds par un lieu.', fill='circ')]),
 E('mix', 'liste', 'Je choisis le bon mot', 'boy', 'Je prouve chaque mot avec une manipulation.',
   [('|On| part en voyage.', 'quelqu’un part : on'),
    ('|Où| allons-nous ?', 'je réponds par un lieu : où'),
    ('Nous allons |là|-bas.', 'ici : là')],
   Q2('___ cherche le chat. ___ est-il ?',
      ('Premier trou :', ['On', 'Où', 'Là'], 'Quelqu’un cherche le chat.', 'circ'),
      ('Deuxième trou :', ['Où', 'On', 'Là'], 'Je réponds par un lieu.', 'circ')),
   [Q2('Le chat ? Il dort ___, sous le lit. ___ le voit bien.',
      ('Premier trou :', ['là', 'on', 'où'], 'Il dort ici.', 'circ'),
      ('Deuxième trou :', ['On', 'Où', 'Là'], 'Quelqu’un le voit bien.', 'circ')),
    Q2('___ se retrouve ? Devant l’école, ___ où je t’attends.',
      ('Premier trou :', ['Où', 'On', 'Là'], 'Je réponds par un lieu.', 'circ'),
      ('Deuxième trou :', ['là', 'on', 'où'], 'Ici, devant l’école.', 'circ'))]),
 E('att', 'attention', 'Les pièges', 'girl', 'Attention au verbe avec on, et aux accents !',
   [('[On] (jou*e*). · [On] (fini*t*).', 'Avec on, le verbe est au singulier.'),
    ('|là|-bas · voi|là| · celui-|là|', 'Ces mots gardent l’accent.')],
   Q('', ['On danse.', 'On dansent.', 'On dansez.'], 'On se conjugue comme il.', 'Laquelle est bien écrite ?'),
   [Q('', ['Voilà mon frère.', 'Voila mon frère.'], 'Voilà garde l’accent.', 'Laquelle est bien écrite ?'),
    Q('', ['Mes amis sont là-bas.', 'Mes amis sont labas.'], 'Là-bas : accent et trait d’union.', 'Laquelle est bien écrite ?')]),
]
save('H2', {'id': 'H2', 'f': 'H', 'ceinture': 'Rose', 'titre': 'on, là, où', 'sous': 'le pronom on · là et où', 'lesson': True}, sections, ecrans, zones)
