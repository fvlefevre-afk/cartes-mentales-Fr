import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from mapgen import build, TL, TC, TR
from lhelp import *
from hlib import R, table, A

O = lambda t: f'<b style="color:#d9730d">{t}</b>'
boxes = [
 dict(id='def', col='bleu', geom=TL, title='Même son, autre sens', avatar=('girl', 322, 122), html=f'''
  <p class="txt" style="padding-right:100px">Les <b>homonymes</b> se prononcent <b>pareil</b>, mais n’ont <b>pas le même sens</b>.</p>
  <div class="exl" style="font-size:21px;line-height:1.6;margin-top:16px">la {R("mer")} · ma {R("mère")} · le {R("maire")}</div>
  <div class="exl" style="font-size:21px;line-height:1.6;margin-top:8px">du {R("pain")} · un {R("pin")}</div>'''),
 dict(id='ecrit', col='vert', geom=TC, title='Écrits autrement', html=f'''
  <p class="txt" style="margin-bottom:2px">L’<b>orthographe change</b> avec le sens.</p>
  <div class="exl" style="font-size:19px;line-height:1.5">un {R("verre")} d’eau · un {R("ver")} de terre<br>un pull {R("vert")}</div>
  <div class="exl" style="font-size:19px;line-height:1.5;margin-top:6px">{R("cent")} euros · du {R("sang")}<br>{R("sans")} sucre</div>'''),
 dict(id='pareil', col='orange', geom=TR, title='Écrits pareil', html=f'''
  <p class="txt">Parfois, ils s’écrivent <b>pareil</b> : le <b>déterminant</b> et la phrase m’aident.</p>
  <div class="exl" style="font-size:20px;line-height:1.55">{O("un")} livre de contes<br>{O("une")} livre de cerises<br>{O("un")} tour de manège<br>{O("une")} tour de château</div>'''),
 dict(id='contexte', col='violet', geom=(18, 568, 560, 350), title='La phrase m’aide', style='padding-top:52px', avatar=('boy', 445, 610), html=f'''
  <p class="txt" style="padding-right:110px">Pour trouver le sens, je lis <b>toute la phrase</b> : les autres mots m’aident.</p>
  <div class="exl" style="font-size:21px;line-height:1.6;margin-right:110px">J’ai <span class="e">faim</span> : je mange.<br>C’est la <span class="e">fin</span> du film.</div>
  <div class="exl" style="font-size:21px;line-height:1.6;margin-right:110px;margin-top:8px">Je mange du <span class="e">pain</span>.<br>Le <span class="e">pin</span> est un arbre.</div>'''),
 dict(id='reb', col='rouge', geom=(612, 568, 770, 350), title='Homonyme ou synonyme ?', style='padding-top:52px', html=f'''
  <table class="tr" style="font-size:21px"><tr><td><b>homonymes</b></td><td>même son, sens différent<br><i>mer · mère</i></td></tr>
  <tr><td><b>synonymes</b></td><td>sons différents, même sens<br><i>content · joyeux</i></td></tr>
  <tr><td><b>contraires</b></td><td>sens opposé<br><i>chaud · froid</i></td></tr></table>'''),
]
out, zones = build('V6', 'Les<br>homonymes', 'Vocabulaire — V6 — CM1', None, boxes, title_size=38)

sections = [
 {'id': 'def', 'nom': 'Même son, autre sens', 'couleur': '#1f5fc4'},
 {'id': 'ecrit', 'nom': 'Écrits autrement', 'couleur': '#23845a'},
 {'id': 'pareil', 'nom': 'Écrits pareil', 'couleur': '#e67e22'},
 {'id': 'contexte', 'nom': 'La phrase m’aide', 'couleur': '#7b3fa0'},
 {'id': 'reb', 'nom': 'Homonyme ou synonyme ?', 'couleur': '#c62828'},
]
ecrans = [
 E('def', 'bulle', 'Même son, autre sens', 'girl', 'Les homonymes se prononcent pareil, mais n’ont pas le même sens.',
   ['La |mer| est bleue.',
    'Ma |mère| est infirmière.',
    ('Le |maire| dirige la ville.', 'Même son, mais pas le même sens : ce sont des homonymes.')],
   Q('', ['verre', 'vent', 'rouge'], 'Il se prononce pareil.', 'Lequel est un homonyme de « vert » ?'),
   [Q('', ['pin', 'pomme', 'pied'], 'Il se prononce pareil.', 'Lequel est un homonyme de « pain » ?'),
    Q('', ['fin', 'fil', 'fou'], 'Il se prononce pareil.', 'Lequel est un homonyme de « faim » ?')]),
 E('ecrit', 'mots', 'Écrits autrement', 'girl', 'Souvent, l’orthographe change avec le sens.',
   [('un |verre| d’eau', 'pour boire'),
    ('un |ver| de terre', 'un petit animal'),
    ('un pull |vert|', 'une couleur')],
   Q('Je bois dans un ___.', ['verre', 'ver', 'vert'], 'Ce qui sert à boire.', 'Complète avec le bon mot.', fill='circ'),
   [Q('Le merle mange un ___ de terre.', ['ver', 'verre', 'vert'], 'Un petit animal.', 'Complète avec le bon mot.', fill='circ'),
    Q('Ce pull coûte ___ euros.', ['cent', 'sang', 'sans'], 'Un nombre.', 'Complète avec le bon mot.', fill='circ'),
    Q('Je bois mon thé ___ sucre.', ['sans', 'cent', 'sang'], 'Le contraire de « avec ».', 'Complète avec le bon mot.', fill='circ')]),
 E('pareil', 'etiquette', 'Écrits pareil', 'boy', 'Parfois, ils s’écrivent pareil : le déterminant m’aide.',
   [('|un| livre de contes', 'pour lire'),
    ('|une| livre de cerises', 'un poids : un demi-kilo'),
    ('|un| tour de manège · |une| tour de château', 'Le déterminant change avec le sens.')],
   Q('La tour Eiffel', ['un grand bâtiment', 'un tour de manège', 'un tour de magie'], 'Une tour : un bâtiment très haut.', 'Ici, « tour » veut dire…'),
   [Q('J’achète une livre de beurre.', ['un poids', 'un livre à lire'], 'Une livre : un demi-kilo.', 'Ici, « livre » veut dire…'),
    Q('Il fait un tour de vélo.', ['une petite promenade', 'un grand bâtiment'], 'Un tour : une petite promenade.', 'Ici, « tour » veut dire…')]),
 E('contexte', 'loupe', 'La phrase m’aide', 'boy', 'Je lis toute la phrase : les autres mots m’aident.',
   ['J’ai #faim#.',
    ('J’ai #faim# : je %mange%.', 'faim : l’envie de manger.'),
    ('C’est la #fin# du %film%.', 'fin : le moment où ça s’arrête.')],
   Q('Il s’est coupé : du ___ coule.', ['sang', 'cent', 'sans'], 'Ce qui coule quand on se coupe.', 'Complète avec le bon mot.', fill='circ'),
   [Q('Je mange du ___ au petit déjeuner.', ['pain', 'pin', 'peint'], 'Ce qu’on mange.', 'Complète avec le bon mot.', fill='circ'),
    Q('Au bord de la ___, je fais un château de sable.', ['mer', 'mère', 'maire'], 'L’endroit avec du sable et des vagues.', 'Complète avec le bon mot.', fill='circ')]),
 E('reb', 'liste', 'Homonyme ou synonyme ?', 'girl', 'Même son ? Même sens ? Je compare.',
   [('|mer| · |mère|', 'Même son, sens différent : des homonymes.'),
    ('|content| · |joyeux|', 'Sons différents, même sens : des synonymes.'),
    ('|chaud| · |froid|', 'Sens opposé : des contraires.')],
   Q('pain · pin', ['des homonymes', 'des synonymes', 'des contraires'], 'Même son, sens différent.', 'Ces deux mots sont…'),
   [Q('commencer · débuter', ['des synonymes', 'des homonymes', 'des contraires'], 'Même sens.', 'Ces deux mots sont…'),
    Q('monter · descendre', ['des contraires', 'des homonymes', 'des synonymes'], 'Sens opposé.', 'Ces deux mots sont…'),
    Q('cent · sang', ['des homonymes', 'des synonymes', 'des contraires'], 'Même son, sens différent.', 'Ces deux mots sont…')]),
]
save('V6', {'id': 'V6', 'f': 'V', 'ceinture': 'Bleue', 'titre': 'Les homonymes', 'sous': 'même son, autre sens', 'lesson': True}, sections, ecrans, zones)
