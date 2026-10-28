"""Carte mentale de G6 pour le CE2 (28/10/2026) : « Groupe sujet et groupe verbal » (programme du cycle 2 et tableau de bord), sans les compléments d'objet
ni circonstanciels de la carte du CM1 (images/G6.jpg).
Mêmes positions que G6 : les zones « phrase » et « tests » de la leçon restent valables ; les zones « cod » et « cc » portent ici « Le groupe sujet » et « Le groupe verbal »
(CE2_PLUS['G6'] les « démasque » : 'demasquer').
Usage : python3 lecons/g6_ce2.py   → sortie/G6-CE2_carte.jpeg (puis copier en images/G6-CE2.jpg et ajouter IMG['G6-CE2'] dans index.html)."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from mapgen import build, TL, TC, TR

boxes = [
 dict(id='phrase', col='turquoise', geom=TL, title='Deux groupes', avatar=('girl', 322, 122), html='''
  <p class="txt" style="padding-right:100px">Une phrase se découpe en <b>deux groupes</b>.</p>
  <div class="ex" style="font-size:21px;margin-top:14px;line-height:1.5"><span class="s">Le chat</span> <span class="v">mange sa pâtée</span>.</div>
  <p class="txt" style="font-size:18px;margin-top:8px">Groupe sujet + groupe verbal.</p>'''),
 dict(id='cod', col='indigo', geom=TC, title='Le groupe sujet', hstyle='font-size:28px', html='''
  <ul style="font-size:19px;line-height:1.3">
   <li>Il dit <b>de qui</b> ou <b>de quoi</b> on parle.</li>
   <li>Je le trouve avec <b>« qui est-ce qui ? »</b>.</li></ul>
  <div class="ex" style="font-size:20px;line-height:1.4;margin-top:6px"><span class="s">Les oiseaux</span> construisent un nid.<br><span class="arrow">→</span> <b>ils</b> construisent un nid</div>'''),
 dict(id='cc', col='marron', geom=TR, title='Le groupe verbal', hstyle='font-size:28px', avatar=('boy', 1250, 122), html='''
  <ul style="font-size:20px;padding-right:96px">
   <li>C’est le <b>verbe</b> et <b>ce qui le complète</b>.</li>
   <li>Le verbe en est le mot le plus important.</li></ul>
  <div class="ex" style="font-size:20px;line-height:1.5">Les oiseaux <span class="v">construisent un nid</span>.</div>'''),
 dict(id='tests', col='violet', geom=(18, 568, 560, 350), title='Je manipule la phrase', style='padding-top:52px', html='''
  <p class="txt"><b>Je supprime :</b> <span class="barre">Ce matin,</span> les élèves chantent <span class="barre">dans la cour</span>.</p>
  <p class="txt"><b>Je déplace :</b> <span class="cc">Dans la cour,</span> les élèves chantent.</p>
  <p class="txt"><b>J’ajoute :</b> les <span class="e">petits</span> élèves chantent <span class="e">joyeusement</span>.</p>
  <p class="txt"><b>Je remplace :</b> <span class="s">Les enfants</span> courent. <span class="arrow">→</span> <span class="s">Ils</span> courent.</p>'''),
 dict(id='att', col='rouge', geom=(612, 568, 770, 350), title='Attention !', style='padding-top:52px', html='''
  <ul style="font-size:20px;line-height:1.45">
   <li>Le groupe sujet peut avoir <b>plusieurs mots</b> : <span class="s">Mon petit frère</span> dort.</li>
   <li>Quand je supprime ou je déplace des mots, la phrase doit garder <b>son sens</b>.</li>
   <li>Le verbe ne se supprime jamais.</li></ul>'''),
]
legend = '<span class="s">groupe sujet</span> · <span class="v">groupe verbal</span>'
build('G6-CE2', 'Groupe sujet,<br>groupe verbal', 'Grammaire — G6 — CE2', legend, boxes, title_size=34, legend_pos='right:18px;top:470px')
print('carte G6 CE2 : sortie/G6-CE2_carte.jpeg')
