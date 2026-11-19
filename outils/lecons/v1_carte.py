"""Carte de V1 (le mot-étiquette et les mots précis) refaite avec les mêmes outils que les autres cartes (19/11/2026, demande de l'enseignante :
« V1, V2 utilisent l'ancienne présentation »). Mêmes six rubriques que l'ancienne image (etiq, precis, ex, echelle, att, sert), même texte.
Usage : python3 lecons/g_cartes.py V1   (ce fichier ne fait que décrire la carte)."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from mapgen import build, TL, TC, TR

E = lambda t: f'<b style="color:#d9730d">{t}</b>'     # mot-étiquette : orange
P = lambda t: f'<b style="color:#23845a">{t}</b>'     # mot précis : vert
BAS = [(18, 568, 440, 350), (480, 568, 440, 350), (942, 568, 440, 350)]
boxes = [
 dict(id='etiq', col='orange', geom=TL, title='Le mot-étiquette', html=f'''
  <ul style="font-size:20px;line-height:1.38"><li>C’est un mot <b>général</b> qui <b>regroupe</b> d’autres mots.</li><li>Je l’écris en {E("orange")}.</li></ul>
  <div class="ex" style="font-size:21px;text-align:center">{E("fruits")} · {E("couleurs")} · {E("jours")}</div>'''),
 dict(id='precis', col='vert', geom=TC, title='Les mots précis', html=f'''
  <ul style="font-size:20px;line-height:1.38"><li>Ce sont les mots <b>rangés sous</b> l’étiquette.</li><li>Je les écris en {P("vert")}.</li></ul>
  <div class="ex" style="font-size:21px;text-align:center">{P("pomme")}, {P("poire")}, {P("cerise")}</div>'''),
 dict(id='ex', col='violet', geom=TR, title='Exemples', html=f'''
  <div class="ex" style="font-size:19px;line-height:1.6">{E("fruits")} → {P("pomme, poire, cerise")}<br>{E("couleurs")} → {P("rouge, bleu, jaune")}<br>{E("jours")} → {P("lundi, mardi…")}</div>'''),
 dict(id='echelle', col='bleu', geom=BAS[0], title='L’échelle des mots', style='padding-top:52px', html=f'''
  <p class="txt">Du <b>général</b> au <b>précis</b> :</p>
  <div class="ex" style="font-size:21px;text-align:center">{E("animal")} → <b>chien</b> → {P("caniche")}</div>
  <p class="txt" style="font-size:18px;margin-top:8px">Un même mot peut être les deux : « chien » est <b>précis</b> sous « animal », et c’est l’<b>étiquette</b> de « caniche ».</p>'''),
 dict(id='att', col='rouge', geom=BAS[1], title='Attention !', style='padding-top:52px', html=f'''
  <p class="txt">L’étiquette doit <b>convenir à tous</b> les mots, et être la plus <b>précise</b> possible.</p>
  <div class="ex" style="font-size:19px;line-height:1.5">✓ pomme, poire, cerise → {E("fruits")}<br><span class="small">(et pas « aliments » ni « choses »)</span><br>✗ pomme, couteau, pain : un couteau n’est pas un aliment !</div>'''),
 dict(id='sert', col='turquoise', geom=BAS[2], title='À quoi ça sert ?', style='padding-top:52px', avatar=('girl', 1290, 610), html=f'''
  <ul style="font-size:20px;line-height:1.38;padding-right:80px"><li>À <b>ranger</b> les mots de mon carnet de mots.</li><li>À <b>éviter les répétitions</b> :</li></ul>
  <div class="ex" style="font-size:19px;line-height:1.5">Tom croque une {P("pomme")}.<br>Il savoure le {E("fruit")}.</div>'''),
]
out, zones = build('V1', 'Le mot-étiquette<br>et les mots précis', 'Vocabulaire — V1 — CM1', None, boxes, title_size=30)
