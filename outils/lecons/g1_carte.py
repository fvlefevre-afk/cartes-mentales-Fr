"""Carte de G1 (Qu'est-ce qu'une phrase ?) refaite avec les mêmes outils que G2 à G7 (14/11/2026) : trois cadres autour du nuage (le sujet, le verbe, et « une phrase, c'est… » en bas).
Mêmes zones (sujet, verbe, phrase) que l'ancienne image. Usage : python3 lecons/g_cartes.py G1   (ce fichier ne fait que décrire la carte)."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from mapgen import build, TL, TC, TR

S, V = '<span class="s">{}</span>', '<span class="v">{}</span>'
EX = lambda s, fs=21: f'<div class="ex" style="font-size:{fs}px;line-height:1.5;margin-top:8px">{s}</div>'
BAS = (330, 568, 740, 350)
boxes = [
 dict(id='sujet', col='bleu', geom=TL, title='Le sujet', html='''<p class="txt" style="padding-right:110px;margin-top:-6px">Le <b>sujet</b> peut être :</p>
  <ul style="font-size:20px;line-height:1.35;margin-top:0;padding-right:66px"><li>un <b>seul mot</b> : <span class="s">Il</span>, <span class="s">Charles</span>, <span class="s">la pluie</span>…</li>
  <li>un <b>groupe de mots</b> : <span class="s">Toutes les dames du salon</span>, <span class="s">mon petit chat</span>…</li></ul>
  <p class="txt" style="font-size:19px;margin:6px 0 0">Il répond à la question : <b>« qui est-ce qui… ? »</b></p>''' + EX(f'{S.format("Il")} regarde la télé.<br>{S.format("Toutes les dames du salon")} discutent.<br>{S.format("Charles et sa mère")} discutent.', 19),
      figs=[('girl', 352, 98, 84)]),
 dict(id='verbe', col='rouge', geom=TR, title='Le verbe', html='''<ul style="font-size:20px;line-height:1.35;padding-right:100px;margin-top:-6px"><li>Le verbe, c’est <b>l’action</b>.</li><li>Il nous dit <b>ce que fait le sujet</b>.</li></ul>
  <p class="txt" style="font-size:19px;margin:6px 0 0">Pour le trouver, je demande : <b>« qu’est-ce qu’il / elle fait ? »</b></p>''' + EX(f'Il {V.format("regarde")} la télé.<br>Toutes les dames du salon {V.format("discutent")}.', 19),
      figs=[('boy', 1244, 106, 112)]),
 dict(id='phrase', col='vert', geom=BAS, title='Une phrase, c’est…', style='padding-top:50px', html='''<p class="txt" style="font-size:25px;text-align:center;margin:0">Une phrase, c’est un <span class="s">sujet</span> ET un <span class="v">verbe</span>.</p>''' + EX(f'{S.format("Il")} {V.format("regarde")} la télé.', 24).replace('margin-top:8px', 'margin-top:10px;text-align:center') + '''<p class="small" style="text-align:center;margin:10px 0 0;font-size:19px">Une phrase a du <b>sens</b> et raconte quelque chose !</p>''',
      figs=[('duo', 392, 566, 120), ('ampoule', 950, 733, 50)]),
]
legend = f'{S.format("sujet")} · {V.format("verbe")}'
out, zones = build('G1', 'Qu’est-ce<br>qu’une phrase ?', 'Grammaire — G1 — CM1', legend, boxes, title_size=34)
