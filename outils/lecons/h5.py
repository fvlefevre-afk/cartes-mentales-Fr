import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from mapgen import build, TL, TC, TR
from lhelp import *
from hlib import R, rows, table

# H5 — la, c’est. Jumeaux interdits : là, l’a, l’as, s’est (et les sons voisins ses / ces).
boxes = [
 dict(id='det', col='bleu', geom=TL, title='la devant un nom', html=rows([
   ('la', '<b>déterminant</b>, devant un nom féminin', 'je dis <b>une</b>, ou je mets au pluriel : <b>les</b>', f'{R("la")} porte → une porte, les portes')]) +
   f'<span class="exl" style="margin-top:6px">{R("la")} ~table · {R("la")} fenêtre</span>'.replace('~', '')),
 dict(id='pro', col='vert', geom=TC, title='la devant un verbe', html=rows([
   ('la', '<b>pronom</b>, remplace un nom féminin', 'avec un nom masculin, je dis <b>le</b>', f'Ma poupée ? Je {R("la")} coiffe.')]) +
   f'<span class="exl" style="margin-top:6px">Mon ballon ? Je le lance.</span>'),
 dict(id='cest', col='orange', geom=TR, title='c’est', avatar=('girl', 1250, 122), html=rows([
   ('c’est', '= cela est', 'je mets au passé : <b>c’était</b>', f'{R("C’est")} mon ami.<br>→ C’était mon ami.')], pr=110) +
   '<p class="txt" style="margin-top:6px;padding-right:110px">Toujours avec une <b>apostrophe</b>.</p>'),
 dict(id='mix', col='violet', geom=(18, 568, 560, 350), title='Je prouve', style='padding-top:52px', avatar=('boy', 445, 610), html=
   '<p class="txt" style="padding-right:110px">Je fais une manipulation pour trouver le bon mot.</p>' + table([
     ('la', '→ une, les (devant un nom)'), ('la', '→ le, les (devant un verbe)'), ('c’est', '→ c’était, cela est')])),
 dict(id='att', col='rouge', geom=(612, 568, 770, 350), title='Attention !', style='padding-top:52px', html='''
  <ul style="font-size:22px;line-height:1.5">
   <li><b>la</b> peut être devant un verbe : <i>Je la regarde</i> (= ma sœur).</li>
   <li><b>c’est</b> s’écrit toujours avec une <b>apostrophe</b>.</li>
   <li>Au passé, <b>c’est</b> devient <b>c’était</b>.</li></ul>'''),
]
out, zones = build('H5', 'la, c’est', 'Homophones — H5 — CM1', None, boxes, title_size=40, sub='homophones')

sections = [
 {'id': 'det', 'nom': 'la devant un nom', 'couleur': '#1f5fc4'},
 {'id': 'pro', 'nom': 'la devant un verbe', 'couleur': '#23845a'},
 {'id': 'cest', 'nom': 'c’est', 'couleur': '#e67e22'},
 {'id': 'mix', 'nom': 'Je prouve', 'couleur': '#7b3fa0'},
 {'id': 'att', 'nom': 'Attention !', 'couleur': '#c62828'},
]
ecrans = [
 E('det', 'etiquette', 'la : un déterminant', 'girl', 'Devant un nom féminin, la est un déterminant.',
   [('|la| porte · |la| table', 'la est devant un nom féminin : c’est un déterminant.'),
    ('|*une*| porte · |*les*| portes', 'Je prouve : je dis « une », ou je mets au pluriel.'),
    ('|la| ~petite~ fille', 'Un adjectif peut se glisser entre les deux.')],
   Q('Ferme ___ fenêtre.', ['la', 'le', 'les'], 'Fenêtre : féminin singulier.', fill='circ'),
   [Q('Je lave ___ voiture.', ['la', 'le', 'les'], 'Voiture : féminin singulier.', fill='circ'),
    C('Léa ouvre <la> boîte.', 'Clique sur le déterminant.', 'Il est devant le nom « boîte ».')]),
 E('pro', 'remplacer', 'la : un pronom', 'girl', 'Devant un verbe, la remplace un nom féminin.',
   [('Ma poupée ? Je |la| coiffe.', 'la est devant un verbe : il remplace « ma poupée ».'),
    ('Mon ballon ? Je |*le*| lance.', 'Avec un nom masculin : le.'),
    ('Mes poupées ? Je |*les*| coiffe.', 'Au pluriel : les.')],
   Q('Cette chanson, je ___ connais.', ['la', 'le', 'les'], 'Chanson : féminin singulier.', fill='circ'),
   [Q('Ta sœur ? Je ___ vois demain.', ['la', 'le', 'les'], 'Ta sœur : féminin singulier.', fill='circ'),
    Q('Mon vélo ? Je ___ répare.', ['le', 'la', 'les'], 'Vélo : masculin singulier.', fill='circ')]),
 E('cest', 'tableau', 'c’est : cela est', 'boy', 'C’est veut dire « cela est ».',
   ['|C’est| mon ami.',
    ('|*Cela est*| mon ami.', 'c’est = cela est.'),
    ('|*C’était*| mon ami.', 'Je prouve : je mets au passé → c’était.')],
   Q('', ['C’est mon tour !', 'Cest mon tour !', 'C’es mon tour !'], 'c’est s’écrit avec une apostrophe.', 'Quelle phrase est bien écrite ?'),
   [Q('', ['C’est très joli.', 'Cest très joli.'], 'c’est s’écrit avec une apostrophe.', 'Quelle phrase est bien écrite ?'),
    C('Regarde : <c’est> un écureuil !', 'Clique sur c’est.', 'Cela est un écureuil.')]),
 E('cest', 'horloge', 'c’est au passé : c’était', 'boy', 'Au passé, c’est devient c’était.',
   [('|C’est| la fin.', 'aujourd’hui'),
    ('Hier, |c’était| la fin.', 'au passé : c’était')],
   Q('C’est la récré. Hier, ___ la récré.', ['c’était', 'c’étais', 'cétait'], 'Au passé : c’était.', fill='circ'),
   [Q('C’est mon anniversaire. L’an dernier, ___ un lundi.', ['c’était', 'c’étais', 'cétait'], 'Au passé : c’était.', fill='circ')]),
 E('mix', 'liste', 'Je choisis le bon mot', 'boy', 'Je prouve chaque mot avec une manipulation.',
   [('|C’est| |la| maison de Léa.', 'c’était · une maison'),
    ('Cette robe ? Je |la| mets : |c’est| ma préférée.', 'je le mets → la · c’était → c’est')],
   Q2('___ ma sœur : je ___ vois souvent.',
      ('Premier trou :', ['C’est', 'La', 'Le'], 'Cela est ma sœur.', 'circ'),
      ('Deuxième trou :', ['la', 'le', 'c’est'], 'Elle : féminin → la.', 'circ')),
   [Q2('Prends ___ clé : ___ celle de la cave.',
      ('Premier trou :', ['la', 'le', 'c’est'], 'Une clé.', 'circ'),
      ('Deuxième trou :', ['c’est', 'la', 'le'], 'Cela est celle de la cave.', 'circ'))]),
 E('att', 'attention', 'Les pièges', 'girl', 'La devant un verbe, et l’apostrophe de c’est !',
   [('Je |la| regarde.', 'la devant un verbe : il remplace un nom féminin.'),
    ('|C’est| · |C’était|', 'Toujours une apostrophe.')],
   Q('', ['Ma lampe, je la répare.', 'Ma lampe, je le répare.'], 'Lampe est féminin : la.', 'Quelle phrase est bien écrite ?'),
   [Q('', ['C’était une belle journée.', 'Cétait une belle journée.'], 'C’était : avec une apostrophe.', 'Quelle phrase est bien écrite ?')]),
]
save('H5', {'id': 'H5', 'f': 'H', 'ceinture': 'Verte', 'titre': "la, c'est", 'sous': 'la déterminant et pronom · c’est', 'lesson': True}, sections, ecrans, zones)
