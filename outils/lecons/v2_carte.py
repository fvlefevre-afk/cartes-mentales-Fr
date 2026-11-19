"""Carte de V2 (comprendre un mot inconnu) refaite avec les mêmes outils que les autres cartes (19/11/2026). Mêmes rubriques que l'ancienne image
(phrase, mot, methode, att), même texte. Usage : python3 lecons/g_cartes.py V2   (ce fichier ne fait que décrire la carte)."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from mapgen import build, TL, TC, TR

J = lambda t: f'<span class="e">{t}</span>'
boxes = [
 dict(id='phrase', col='vert', geom=(18, 86, 600, 330), title='Les indices dans la phrase', avatar=('girl', 492, 122), html=f'''
  <p class="txt" style="padding-right:100px">Je lis <b>toute la phrase</b> : les autres mots m’aident.</p>
  <div class="ex" style="font-size:20px;line-height:1.5">Le boulanger sort le pain du {J("fournil")} encore brûlant.<br>→ le <b>fournil</b> : la pièce où l’on cuit le pain.</div>'''),
 dict(id='mot', col='orange', geom=(782, 86, 600, 330), title='Les indices dans le mot', html=f'''
  <p class="txt">Je cherche un <b>mot que je connais</b>, caché dans le mot.</p>
  <div class="ex" style="font-size:20px;line-height:1.55">in{J("cass")}able → qu’on ne peut pas casser<br>{J("chocolat")}ier → une personne qui fabrique du chocolat</div>'''),
 dict(id='methode', col='bleu', geom=(18, 568, 640, 350), title='Ma méthode', style='padding-top:52px', html='''
  <ol style="font-size:20px;line-height:1.4;margin:0;padding-left:28px"><li>Je <b>lis</b> toute la phrase.</li><li>Je <b>cherche des indices</b> dans la phrase et dans le mot.</li>
  <li>Je <b>propose</b> un sens.</li><li>Je <b>vérifie</b> : je remplace le mot par mon explication ; la phrase doit garder son sens.</li></ol>
  <div class="ex" style="font-size:19px;margin-top:8px">Le chat lape son lait. → Le chat boit son lait en tirant la langue.</div>'''),
 dict(id='att', col='rouge', geom=(702, 568, 680, 350), title='Attention !', style='padding-top:52px', avatar=('boy', 1270, 610), html='''
  <p class="txt" style="padding-right:110px">Parfois, <b>la phrase ne suffit pas</b> :</p>
  <div class="ex" style="font-size:19px;line-height:1.5;margin-right:110px">Le tamanoir est un animal.<br>→ je sais seulement que c’est un animal.</div>
  <p class="txt" style="margin-top:10px;padding-right:110px">Je lis alors <b>la suite du texte</b>, ou je <b>demande</b>.</p>'''),
]
out, zones = build('V2', 'Comprendre<br>un mot inconnu', 'Vocabulaire — V2 — CM1', None, boxes, sub='avec les indices', title_size=34)
