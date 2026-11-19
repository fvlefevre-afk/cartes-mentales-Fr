"""Carte de H1 (les verbes avoir et être au présent) refaite avec les mêmes outils que H2 à H7 (19/11/2026). Mêmes rubriques que l'ancienne image
(avoir, etre, choisir, forme, retenir), même texte ; sans le sujet placé après le verbe (« As-tu faim ? » : ajout du CM2, audit du 19/11/2026).
Usage : python3 lecons/g_cartes.py H1   (ce fichier ne fait que décrire la carte)."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from mapgen import build, TL, TC, TR
from hlib import R

A = lambda t: f'<b style="color:#d9730d">{t}</b>'
T = lambda t: f'<b style="color:#23845a">{t}</b>'
tab = lambda L, c: '<table class="tr" style="font-size:22px;width:66%">' + ''.join(f'<tr><td>{p}</td><td>{c(v)}</td></tr>' for p, v in L) + '</table>'
BAS = [(18, 568, 440, 350), (480, 568, 440, 350), (942, 568, 440, 350)]
boxes = [
 dict(id='avoir', col='orange', geom=TL, title='Le verbe avoir', avatar=('boy', 330, 122), html=tab([('j’', 'ai'), ('tu', 'as'), ('il, elle, on', 'a'), ('ils, elles', 'ont')], A)
      + '<p class="small" style="margin:6px 0 0">J’ai un vélo.</p>'),
 dict(id='etre', col='vert', geom=TR, title='Le verbe être', avatar=('girl', 1290, 122), html=tab([('je', 'suis'), ('tu', 'es'), ('il, elle, on', 'est'), ('ils, elles', 'sont')], T)
      + '<p class="small" style="margin:6px 0 0">Je suis content(e).</p>'),
 dict(id='choisir', col='bleu', geom=BAS[0], title='Comment bien choisir ?', style='padding-top:52px', html='''
  <p class="txt"><b>1.</b> Je dis la phrase avec <b>« hier »</b> : le mot change.</p>
  <div class="ex" style="font-size:18px;line-height:1.45">Tom a un vélo. → Hier, Tom <b>avait</b> un vélo.<br>Léa est malade. → Hier, Léa <b>était</b> malade.</div>
  <p class="txt" style="margin-top:8px"><b>2.</b> Je <b>change le sujet</b> : il a → ils ont.</p>'''),
 dict(id='forme', col='rose', geom=BAS[1], title='Quelle forme choisir ?', style='padding-top:52px', html='''
  <ul style="font-size:19px;line-height:1.38"><li>Le <b>sujet</b> me dit la personne : tu es, les enfants ont.</li><li>Le <b>sens</b> me dit le verbe : Tom a un vélo (avoir), Tom est content (être).</li>
  <li><b>Attention</b> : le sujet peut être <b>loin</b> du verbe, ou formé de <b>plusieurs mots</b> : Tom et Léa ont un chat.</li></ul>'''),
 dict(id='retenir', col='violet', geom=BAS[2], title='À retenir', style='padding-top:52px', html=f'''
  <ul style="font-size:19px;line-height:1.38"><li>{A("avoir")} sert souvent à dire ce qu’on <b>possède</b>.</li><li>{T("être")} sert souvent à dire <b>comment</b> est quelqu’un.</li></ul>
  <div class="ex" style="font-size:19px;text-align:center">Bien repérer le verbe et le sujet, c’est la clé !</div>'''),
]
out, zones = build('H1', 'Les verbes<br>avoir et être<br>au présent', 'Homophones — H1 — CM1', None, boxes, title_size=32)
