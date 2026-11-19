"""Carte mentale de G7 pour le CE2 (18/11/2026, idée 329 du tableau de bord) : la carte du CM1 (g7.py) avec « nom » au lieu de « nom noyau »
(programme : le nom noyau est une notion du CM1 ; même choix que G3-CE2) et sans le participe passé avec être dans « Je vérifie ».
Usage : python3 outils/lecons/g_cartes.py G7-CE2  → images/G7-CE2.jpg, zones dans ZONES_NIV."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from mapgen import build, TL, TC, TR
_src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'g7.py'), encoding='utf-8').read()
exec(_src[:_src.index('out, zones = build(')].replace('from lhelp import *', ''))
boxes = [dict(b, html=b['html'].replace('nom noyau', 'nom').replace('\n   <li>Avec <b>être</b>, j’accorde le participe passé.</li>', '')) for b in boxes]
# au CE2, pas de participe passé dans la chaîne (programme du cycle 2) : verbe conjugué à la place
_CE2 = [('<span class="v">sont</span> <span class="v">arrivé<span class="e">es</span></span>', '<span class="v">chant<span class="e">ent</span></span>'),
        ('les · petites · sont · arrivées : tout s’accorde !', 'les · petites · filles · chantent : tout s’accorde !'),
        ('Le petit chat est rentré.<br><span class="arrow">→</span> Les petit<span class="e">s</span> chat<span class="e">s</span> <span class="v">sont</span> rentré<span class="e">s</span>.',
         'Le petit chat dort.<br><span class="arrow">→</span> Les petit<span class="e">s</span> chat<span class="e">s</span> <span class="v">dorm<span class="e">ent</span></span>.')]
for _a, _b in _CE2:
    assert any(_a in b['html'] for b in boxes), _a
    boxes = [dict(b, html=b['html'].replace(_a, _b)) for b in boxes]
out, zones = build('G7-CE2', 'La chaîne<br>des accords', 'Grammaire — G7 — CE2', legend, boxes, title_size=38, legend_pos='right:18px;top:470px')
