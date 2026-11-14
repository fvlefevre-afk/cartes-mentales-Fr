"""Cartes mentales de G2 (types et formes de phrase) pour les TROIS classes, fabriquées par le même outil pour avoir la même apparence (13/11/2026 :
  la carte du CM1 était une image faite à part, les cartes CE2 et CM2 en différaient).
  - G2 (CM1) : la carte d'origine, refaite à l'identique pour le texte (3 façons de poser une question, ne… pas / jamais / plus / rien / personne) ;
  - G2-CE2 : deux façons de poser une question (? seul, est-ce que), négation ne… pas seulement ;
  - G2-CM2 : comme le CM1, avec en plus la phrase simple / complexe sous la déclarative (même titre, mêmes six cadres).
Mêmes six zones que G2 (decl, inter, imp, aff, neg, excl) : les leçons n'ont pas à changer de zones.
Usage : python3 lecons/g2_cartes.py   → sortie/G2_carte.jpeg, G2-CE2_carte.jpeg, G2-CM2_carte.jpeg (puis les copier dans images/G2.jpg, G2-CE2.jpg, G2-CM2.jpg)."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from mapgen import build, TL, TC, TR

AFF = (18, 618, 420, 302); NEG = (452, 618, 470, 302); EXC = (952, 618, 430, 302)
EX = lambda s, fs=20: f'<div class="ex" style="font-size:{fs}px;line-height:1.45;margin-top:8px">{s}</div>'
S, V = '<span class="s">{}</span>', '<span class="v">{}</span>'


def carte(lid, chip, niveau):
    ce2, cm2 = niveau == 'CE2', niveau == 'CM2'  # CM1 : ni l'un ni l'autre
    decl = '''<ul style="padding-right:104px;font-size:20px;margin-top:-14px">
  <li>Elle raconte, elle informe.</li>
  <li>Elle se termine par un point <b>.</b> ou par <b>!</b></li></ul>''' + EX('Léa range sa chambre.', 21)
    if cm2:
        decl = decl.replace('font-size:20px;margin-top:-14px', 'font-size:19px;line-height:1.25;margin-top:-14px') + \
            '<p class="small" style="margin:10px 0 0;font-size:17px;line-height:1.4"><b>Phrase simple</b> : un seul <span class="v">verbe conjugué</span>.<br><b>Phrase complexe</b> : plusieurs verbes conjugués, reliés par <b>et</b>, <b>mais</b>, <b>car</b> ou une virgule.</p>'
    tl_title = 'Déclarative'
    if ce2:
        inter = '''<ul style="font-size:19.5px;line-height:1.3;margin-top:-12px"><li>Elle pose une question.</li><li>Elle se termine par <b>?</b></li><li><b>2 façons</b> de la poser :</li></ul>''' + \
                EX('Tu ranges ta chambre ?<br>Est-ce que tu ranges ta chambre ?', 19)
        inter_t = 'Interrogative'
    else:
        inter = '''<ul style="font-size:19.5px;line-height:1.3;margin-top:-12px"><li>Elle pose une question.</li><li>Elle se termine par <b>?</b></li><li><b>3 façons</b> de la poser :</li></ul>''' + \
                EX('Tu ranges ta chambre ?<br>Est-ce que tu ranges ta chambre ?<br>Ranges-tu ta chambre ?', 18)
        inter_t = 'Interrogative'
    imp = '''<ul style="font-size:19.5px;padding-right:104px;line-height:1.3;margin-top:-14px"><li>Elle donne un ordre, un conseil.</li><li>Elle se termine par <b>.</b> ou <b>!</b></li><li><b>Pas de sujet écrit</b></li></ul>''' + \
          EX('Vous rangez votre chambre. <span style="font-size:14px">(polie)</span><br>Rangez votre chambre. <span style="font-size:14px">(directe)</span>', 17)
    aff = '<ul style="font-size:20px;margin-top:-10px"><li>Elle affirme quelque chose.</li></ul>' + EX('Léa range sa chambre.<br>Léa aime le chocolat.', 20)
    if ce2:
        neg = '''<ul style="font-size:19.5px;line-height:1.3;margin-top:-10px"><li>La négation <b>encadre le verbe</b> :</li></ul><div class="ex" style="font-size:21px;margin-top:4px;text-align:center"><b>ne</b> … <b>pas</b></div>''' + \
              EX('Léa <b>ne</b> range <b>pas</b> sa chambre.<br>Devant une voyelle : <b>n’</b> <span class="arrow">→</span> Léa <b>n’</b>aime <b>pas</b> le thé.', 18)
    else:
        neg = '''<ul style="font-size:19px;line-height:1.3;margin-top:-10px"><li>La négation <b>encadre le verbe</b> :</li></ul><div class="ex" style="font-size:19px;margin-top:4px;text-align:center">ne… pas, ne… jamais, ne… plus,<br>ne… rien, ne… personne</div>''' + \
              EX('Léa <b>ne</b> range <b>jamais</b> sa chambre.<br>Devant une voyelle : <b>n’</b> <span class="arrow">→</span> Léa <b>n’</b>écrit <b>rien</b>.', 18)
    exc = '''<ul style="padding-right:84px;font-size:19px;line-height:1.3;margin-top:-10px"><li>Elle exprime une émotion (surprise, colère, joie…).</li><li>Elle se termine par <b>!</b></li><li>Elle s’ajoute à n’importe quel type de phrase :</li></ul>''' + \
          EX('Le chien renverse sa gamelle ! <span style="font-size:15px">(déclarative)</span><br>Range ta chambre ! <span style="font-size:15px">(impérative)</span>', 17)
    boxes = [
     dict(id='decl', col='bleu', geom=TL, ext=24, title=tl_title, figs=[('girl', 352, 98, 84)], html=decl, hstyle='top:30px'),
     dict(id='inter', col='vert', geom=TC, ext=24, title=inter_t, hstyle='top:30px', html=inter, figs=[('q', 800, 92, 90)]),
     dict(id='imp', col='violet', geom=TR, ext=24, title='Impérative', hstyle='top:30px', figs=[('boy', 1244, 106, 112)], html=imp),
     dict(id='aff', ext=24, col='rose', geom=AFF, title='Affirmative', hstyle='top:30px', html=aff, figs=[('thumb', 340, 785, 62)], style='padding-top:50px'),
     dict(id='neg', ext=24, col='turquoise', geom=NEG, title='Négative', hstyle='top:30px', html=neg, figs=[('no', 850, 632, 54)], style='padding-top:50px'),
     dict(id='excl', ext=24, col='orange', geom=EXC, title='Exclamative', hstyle='top:30px', html=exc, figs=[('burst', 1290, 700, 74)], style='padding-top:50px'),
    ]
    legend = ''
    titre = 'Les types<br>et les formes<br>de phrase'
    bulle = lambda x, y, w, h, txt, tail: f'<div style="position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{h}px;background:#fff;border:3.5px solid #1f5fc4;border-radius:34px;display:flex;align-items:center;justify-content:center;text-align:center;padding:10px 18px;font-size:18.5px;line-height:1.3;color:#1f2a44"><span>{txt}</span><i style="position:absolute;{tail}"></i></div>'
    note = ('<div style="position:absolute;left:18px;top:436px;width:392px;height:132px;background:#fff9e0;border:3.5px dashed #e6a700;border-radius:24px;display:flex;align-items:center;gap:12px;padding:6px 12px 6px 92px;font-size:19.5px;line-height:1.3;color:#1f2a44">'
            '<img src="file://' + os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'img', 'g2', 'ampoule.png') + '" style="position:absolute;left:14px;top:14px;width:72px">'
            '<span><b>À retenir :</b> une phrase a <b>toujours un type</b>. Elle peut en plus être <b>négative</b> et/ou <b>exclamative</b>.</span></div>')
    duo = ('<img src="file://' + os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'img', 'g2', 'duo.png') + '" style="position:absolute;left:1200px;top:462px;width:180px">'
           + bulle(964, 440, 238, 126, 'Quel est son type ?<br>Elle <b>raconte</b>, elle <b>demande</b> ou elle <b>ordonne</b> ?', 'right:-22px;bottom:30px;border:11px solid transparent;border-left:18px solid #1f5fc4;border-right:0'))
    extra_html = note + duo
    return build(lid, titre, chip, legend, boxes, extra_html=extra_html, sub='', title_size=34, legend_pos='right:26px;top:540px', cloud_dy=26)


if __name__ == '__main__':
    carte('G2', 'Grammaire — G2 — CM1', 'CM1')
    carte('G2-CE2', 'Grammaire — G2 — CE2', 'CE2')
    carte('G2-CM2', 'Grammaire — G2 — CM2', 'CM2')
    print('cartes G2 : sortie/G2_carte.jpeg, G2-CE2_carte.jpeg, G2-CM2_carte.jpeg')
