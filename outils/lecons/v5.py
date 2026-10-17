import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from mapgen import build, TL, TC, TR
from lhelp import *
from hlib import R, table, A

G = lambda t: f'<b style="color:#23845a">{t}</b>'   # synonyme
O = lambda t: f'<b style="color:#c62828">{t}</b>'   # contraire
P = lambda t: f'<span class="e">{t}</span>'
D = '<span class="arrow">↔</span>'
boxes = [
 dict(id='syn', col='vert', geom=TL, title='Les synonymes', avatar=('girl', 322, 122), html=f'''
  <p class="txt" style="padding-right:100px">Des mots qui ont le <b>même sens</b>, ou presque.</p>
  <div class="exl" style="font-size:21px;line-height:1.6;margin-top:36px">{G("content")} = {G("joyeux")}<br>{G("commencer")} = {G("débuter")}<br>{G("une maison")} = {G("une habitation")}</div>'''),
 dict(id='choix', col='bleu', geom=TC, title='Le bon synonyme', html=f'''
  <p class="txt">Je choisis le synonyme qui va avec <b>la phrase</b>.</p>
  <div class="exl" style="font-size:20px;line-height:1.6">un <u>gros</u> chien {A} un chien {G("énorme")}<br>une <u>grosse</u> voix {A} une voix {G("grave")}<br>un <u>gros</u> rhume {A} un rhume {G("fort")}</div>'''),
 dict(id='con', col='rouge', geom=TR, title='Les contraires', html=f'''
  <p class="txt">Des mots de <b>sens opposé</b>.</p>
  <div class="exl" style="font-size:20px;line-height:1.5">{O("grand")} {D} {O("petit")}<br>{O("monter")} {D} {O("descendre")}</div>
  <p class="txt" style="margin-top:6px;font-size:18px">Parfois, un <b>préfixe</b> fabrique le contraire :</p>
  <div class="exl" style="font-size:20px;line-height:1.5">heureux {D} {P("mal")}heureux<br>connu {D} {P("in")}connu</div>'''),
 dict(id='classe', col='violet', geom=(18, 568, 560, 350), title='La même classe de mots', style='padding-top:52px', avatar=('boy', 445, 610), html=f'''
  <p class="txt" style="padding-right:110px">Le synonyme ou le contraire est de la <b>même classe</b> que le mot.</p>
  <table class="tr" style="font-size:20px;margin-right:110px;width:auto"><tr><td>verbe</td><td>courir {D} marcher</td></tr>
  <tr><td>nom</td><td>la joie {D} la tristesse</td></tr><tr><td>adjectif</td><td>joyeux {D} triste</td></tr></table>'''),
 dict(id='reb', col='orange', geom=(612, 568, 770, 350), title='Avec une famille de mots', style='padding-top:52px', html=f'''
  <p class="txt" style="font-size:22px">Je trouve le contraire de chaque mot de la famille.</p>
  <table class="tr" style="font-size:22px;width:auto"><tr><td><b style="color:#1f5fc4">joie</b></td><td>{D} tristesse</td></tr>
  <tr><td><b style="color:#1f5fc4">joy</b>eux</td><td>{D} triste</td></tr><tr><td><b style="color:#1f5fc4">joy</b>eusement</td><td>{D} tristement</td></tr></table>'''),
]
out, zones = build('V5', 'Synonymes<br>et contraires', 'Vocabulaire — V5 — CM1', None, boxes, title_size=34)

sections = [
 {'id': 'syn', 'nom': 'Les synonymes', 'couleur': '#23845a'},
 {'id': 'choix', 'nom': 'Le bon synonyme', 'couleur': '#1f5fc4'},
 {'id': 'con', 'nom': 'Les contraires', 'couleur': '#c62828'},
 {'id': 'classe', 'nom': 'La même classe de mots', 'couleur': '#7b3fa0'},
 {'id': 'reb', 'nom': 'Avec une famille de mots', 'couleur': '#e67e22'},
]
ecrans = [
 E('syn', 'remplacer', 'Même sens : les synonymes', 'girl', 'Des synonymes ont le même sens, ou presque.',
   ['Léa est |contente|.',
    ('Léa est |*joyeuse*|.', 'Le sens ne change pas : joyeux est un synonyme de content.'),
    ('|commencer| = |débuter|', 'Je peux remplacer l’un par l’autre.')],
   Q('', ['construire', 'casser', 'tomber'], 'Même sens que bâtir.', 'Un synonyme de « bâtir » :'),
   [Q('', ['effrayé', 'courageux', 'calme'], 'Même sens qu’apeuré.', 'Un synonyme de « apeuré » :'),
    Q('', ['un vélo', 'une voiture', 'un camion'], 'Même sens que bicyclette.', 'Un synonyme de « une bicyclette » :'),
    Q('Tom ___ la porte.', ['ferme', 'ouvre', 'pousse'], 'Même sens que « clôt ».', 'Remplace « clôt » par un synonyme :', fill='pr')]),
 E('choix', 'loupe', 'Le bon synonyme pour la phrase', 'boy', 'Selon la phrase, le synonyme change.',
   [('un ~gros~ chien → un chien |énorme|', 'gros = très grand.'),
    ('une ~grosse~ voix → une voix |grave|', 'Ici, gros veut dire grave.'),
    ('un ~gros~ rhume → un rhume |fort|', 'Je choisis selon la phrase.')],
   Q('Une forte pluie', ['violente', 'musclée', 'solide'], 'Ici, forte parle de la pluie.', 'Un synonyme de « forte » dans cette phrase :'),
   [Q('Un homme fort', ['musclé', 'violent', 'bruyant'], 'Ici, fort parle d’une personne.', 'Un synonyme de « fort » dans cette phrase :'),
    Q('Un vieux livre', ['ancien', 'âgé', 'fatigué'], 'Un livre n’est pas une personne.', 'Un synonyme de « vieux » dans cette phrase :')]),
 E('con', 'non', 'Sens opposé : les contraires', 'boy', 'Des contraires ont des sens opposés.',
   ['|grand| ↔ |petit|',
    ('|monter| ↔ |descendre|', 'Deux verbes de sens opposé.'),
    ('|chaud| ↔ |froid|', 'Je les range par paires.')],
   Q('', ['fermer', 'pousser', 'entrer'], 'Le sens opposé d’ouvrir.', 'Le contraire de « ouvrir » :'),
   [Q('', ['sale', 'lavé', 'beau'], 'Le sens opposé de propre.', 'Le contraire de « propre » :'),
    Q('', ['perdre', 'jouer', 'finir'], 'Le sens opposé de gagner.', 'Le contraire de « gagner » :')]),
 E('con', 'ciseaux', 'Un préfixe pour le contraire', 'boy', 'Parfois, un préfixe fabrique le contraire.',
   [('visible ↔ %in%visible', 'in- : pas.'),
    ('faire ↔ %dé%faire', 'dé- : le contraire.'),
    ('heureux ↔ %mal%heureux', 'mal- : pas.')],
   Q('', ['inconnu', 'reconnu', 'connaître'], 'in- fabrique le contraire.', 'Le contraire de « connu » :'),
   [Q('', ['déboucher', 'reboucher', 'bouchon'], 'dé- fabrique le contraire.', 'Le contraire de « boucher » :'),
    Q('', ['impossible', 'repossible', 'possiblement'], 'im- devant p.', 'Le contraire de « possible » :')]),
 E('classe', 'etiquette', 'La même classe de mots', 'girl', 'Le synonyme ou le contraire garde la même classe.',
   [('courir ↔ marcher', 'Un verbe ↔ un verbe.'),
    ('la joie ↔ la tristesse', 'Un nom ↔ un nom.'),
    ('joyeux ↔ triste', 'Un adjectif ↔ un adjectif.')],
   Q('', ['le froid', 'froid', 'refroidir'], 'Je cherche un nom, avec un déterminant.', 'Le contraire du nom « la chaleur » :'),
   [Q('', ['rire', 'triste', 'tristesse'], 'Je cherche un verbe.', 'Le contraire du verbe « pleurer » :'),
    Q('', ['lent', 'lenteur', 'ralentir'], 'Je cherche un adjectif.', 'Le contraire de l’adjectif « rapide » :')]),
 E('reb', 'mots', 'Avec une famille de mots', 'girl', 'Je trouve le contraire de chaque mot de la famille.',
   [('|joie| · |joy|eux · |joy|eusement', 'Une famille de mots.'),
    ('joie ↔ tristesse · joyeux ↔ triste · joyeusement ↔ tristement', 'Chaque mot a son contraire, de la même classe.')],
   Q('', ['lentement', 'lent', 'lenteur'], 'Je cherche un mot en -ment, comme rapidement.', 'Le contraire de « rapidement » :'),
   [Q('', ['la faiblesse', 'faible', 'faiblement'], 'Je cherche un nom, comme la force.', 'Dans la famille de « fort », le contraire de « la force » :'),
    Q('', ['propreté ↔ saleté', 'propre ↔ sale', 'proprement ↔ salement'], 'Je cherche les deux noms.', 'Quelle paire est faite de deux noms ?')]),
]
save('V5', {'id': 'V5', 'f': 'V', 'ceinture': 'Verte', 'titre': 'Synonymes et contraires', 'sous': 'même sens · sens opposé', 'lesson': True}, sections, ecrans, zones)
