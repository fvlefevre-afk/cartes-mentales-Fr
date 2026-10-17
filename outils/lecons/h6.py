import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from mapgen import build, TL, TC, TR
from lhelp import *
from hlib import R, rows, table

# H6 — son, ses, mes : les déterminants possessifs. Jumeaux interdits : sont, ces, mais (et c’est / s’est).
W = ['son', 'ses', 'mes']
boxes = [
 dict(id='son', col='bleu', geom=TL, title='son : à lui, à elle', html=rows([
   ('son', '<b>déterminant possessif</b> : une chose à lui ou à elle', 'je change la personne : <b>mon</b>', f'Léa prend {R("son")} sac.<br>→ Je prends mon sac.')])),
 dict(id='ses', col='vert', geom=TC, title='ses : plusieurs', html=rows([
   ('ses', 'plusieurs choses à lui ou à elle', 'je mets au singulier : <b>son</b>, <b>sa</b>', f'Léa range {R("ses")} livres.<br>→ son livre')])),
 dict(id='mes', col='orange', geom=TR, title='mes : à moi', html=rows([
   ('mes', 'plusieurs choses à moi', 'je mets au singulier : <b>mon</b>, <b>ma</b>', f'{R("mes")} crayons → mon crayon')]) +
   f'<span class="exl" style="margin-top:6px">{R("mes")} trousses → ma trousse</span>'),
 dict(id='acc', col='violet', geom=(18, 568, 560, 350), title='Un ou plusieurs ?', style='padding-top:52px', avatar=('girl', 445, 610), html='''
  <p class="txt" style="padding-right:110px">Le possessif s’accorde avec le nom : un seul ou plusieurs ?</p>
  <table class="tr" style="font-size:19px;margin-right:110px;width:auto"><tr><td>à moi</td><td>mon, ma → <b>mes</b></td></tr>
  <tr><td>à toi</td><td>ton, ta → <b>tes</b></td></tr><tr><td>à lui, à elle</td><td>son, sa → <b>ses</b></td></tr>
  <tr><td>à nous · à eux</td><td>notre → <b>nos</b> · leur → <b>leurs</b></td></tr></table>'''),
 dict(id='att', col='rouge', geom=(612, 568, 770, 350), title='Attention !', style='padding-top:52px', avatar=('boy', 1250, 610), html='''
  <ul style="font-size:22px;line-height:1.5;padding-right:110px">
   <li>Devant une voyelle, on dit <b>son</b>, même au féminin : <i>son amie, son école</i>.</li>
   <li>Après <b>ses</b> et <b>mes</b>, le nom est toujours au <b>pluriel</b>.</li></ul>'''),
]
out, zones = build('H6', 'son, ses, mes', 'Homophones — H6 — CM1', None, boxes, title_size=38, sub='homophones')

sections = [
 {'id': 'son', 'nom': 'son : à lui, à elle', 'couleur': '#1f5fc4'},
 {'id': 'ses', 'nom': 'ses : plusieurs', 'couleur': '#23845a'},
 {'id': 'mes', 'nom': 'mes : à moi', 'couleur': '#e67e22'},
 {'id': 'acc', 'nom': 'Un ou plusieurs ?', 'couleur': '#7b3fa0'},
 {'id': 'att', 'nom': 'Attention !', 'couleur': '#c62828'},
]
ecrans = [
 E('son', 'etiquette', 'son : à lui, à elle', 'girl', 'Son est un déterminant possessif : une chose à lui ou à elle.',
   ['Léa prend |son| sac.',
    ('Je prends |*mon*| sac.', 'Je prouve : je change la personne. son devient mon.'),
    ('|son| ~gros~ chien', 'Un adjectif peut se glisser entre les deux.')],
   Q('Tom cherche ___ ballon.', W, 'Un seul ballon, à Tom.', fill='circ'),
   [Q('Le chat mange ___ repas.', W, 'Un seul repas, au chat.', fill='circ'),
    C('Ma sœur prête <son> vélo.', 'Clique sur le déterminant possessif.', 'Il dit à qui est le vélo.')]),
 E('ses', 'wagon', 'ses : plusieurs choses', 'girl', 'Plusieurs choses à lui ou à elle : ses.',
   [('|son| vélo → |*ses*| vélos', 'Plusieurs vélos : ses.'),
    ('|sa| robe → |*ses*| robes', 'Au pluriel, son et sa deviennent ses.'),
    ('Léa range |ses| livres.', 'Je prouve : au singulier, son livre.')],
   Q('Le chat lèche ___ pattes.', W, 'Plusieurs pattes, au chat.', fill='circ'),
   [Q('Papa lave ___ mains.', W, 'Plusieurs mains, à Papa.', fill='circ'),
    Q('Ma voisine arrose ___ fleurs.', W, 'Plusieurs fleurs, à ma voisine.', fill='circ')]),
 E('mes', 'etiquette', 'mes : à moi', 'boy', 'Plusieurs choses à moi : mes.',
   [('|mon| crayon → |*mes*| crayons', 'Plusieurs crayons à moi : mes.'),
    ('|ma| trousse → |*mes*| trousses', 'Au pluriel, mon et ma deviennent mes.'),
    ('J’ai rangé |mes| livres.', 'Je prouve : au singulier, mon livre.')],
   Q('J’ai rangé ___ jouets.', W, 'Plusieurs jouets, à moi.', fill='circ'),
   [Q('Je cherche ___ chaussures.', W, 'Plusieurs chaussures, à moi.', fill='circ'),
    Q('J’invite ___ amis.', W, 'Plusieurs amis, à moi.', fill='circ')]),
 E('acc', 'wagon', 'Un ou plusieurs ?', 'boy', 'Le possessif s’accorde avec le nom.',
   ['mon · ton · son → |mes| · tes · |ses|',
    ('notre → nos · leur → leurs', 'Au pluriel, le possessif change aussi.')],
   Q('Tu as oublié ___ lunettes.', ['tes', 'ton', 'ta'], 'Lunettes : pluriel.', fill='circ'),
   [Q('Les enfants rangent ___ affaires.', ['leurs', 'leur'], 'Plusieurs affaires.', fill='circ'),
    Q('Nous aimons ___ école.', ['notre', 'nos'], 'Une seule école.', fill='circ')]),
 E('acc', 'loupe', 'À qui ? Combien ?', 'boy', 'Je regarde à qui est la chose, et s’il y en a une ou plusieurs.',
   [('Léa a perdu |ses| gants.', 'à elle · plusieurs : ses'),
    ('Moi, j’ai perdu |mes| gants.', 'à moi · plusieurs : mes'),
    ('Tom a perdu |son| bonnet.', 'à lui · un seul : son')],
   Q2('Léa range ___ jouets, et moi ___ livres.',
      ('Premier trou :', W, 'À Léa, plusieurs jouets.', 'circ'),
      ('Deuxième trou :', ['mes', 'son', 'ses'], 'À moi, plusieurs livres.', 'circ')),
   [Q2('Tom promène ___ chien, et moi ___ chiens.',
      ('Premier trou :', W, 'À Tom, un seul chien.', 'circ'),
      ('Deuxième trou :', ['mes', 'son', 'ses'], 'À moi, plusieurs chiens.', 'circ'))]),
 E('att', 'attention', 'Les pièges', 'girl', 'Son devant une voyelle, et le nom au pluriel après ses et mes !',
   [('|son| amie · |son| école', 'Devant une voyelle : son, même au féminin.'),
    ('|ses| livre*s* · |mes| ami*s*', 'Après ses et mes, le nom est au pluriel.')],
   Q('', ['Léa invite son amie.', 'Léa invite sa amie.'], 'Devant une voyelle : son.', 'Quelle phrase est bien écrite ?'),
   [Q('', ['Tom range ses cahiers.', 'Tom range ses cahier.'], 'Après ses, le nom est au pluriel.', 'Quelle phrase est bien écrite ?')]),
]
save('H6', {'id': 'H6', 'f': 'H', 'ceinture': 'Bleue', 'titre': 'son, ses, mes', 'sous': 'les possessifs et leur accord', 'lesson': True}, sections, ecrans, zones)
