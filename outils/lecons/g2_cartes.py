"""Cartes mentales de G2 (types et formes de phrase) pour le CE2 et le CM2 (28/10/2026) ; la carte du CM1 est images/G2.jpg.
  - G2-CE2 : deux façons de poser une question (? seul, est-ce que), négation ne… pas seulement ;
  - G2-CM2 : la carte du CM1, avec la phrase simple / complexe (verbes conjugués, et, mais, car) dans la case de la déclarative.
Mêmes six zones que G2 (decl, inter, imp, aff, neg, excl) : les leçons n'ont pas à changer de zones.
Usage : python3 lecons/g2_cartes.py   → sortie/G2-CE2_carte.jpeg, sortie/G2-CM2_carte.jpeg (puis les copier dans images/G2-CE2.jpg, G2-CM2.jpg)."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from mapgen import build, TL, TC, TR

AFF = (18, 618, 420, 302); NEG = (452, 618, 470, 302); EXC = (952, 618, 430, 302)
EX = lambda s, fs=20: f'<div class="ex" style="font-size:{fs}px;line-height:1.45;margin-top:8px">{s}</div>'
S, V = '<span class="s">{}</span>', '<span class="v">{}</span>'


def carte(lid, chip, niveau):
    ce2, cm2 = niveau == 'CE2', niveau == 'CM2'
    if cm2:
        decl = '''<ul style="padding-right:104px;font-size:19px;line-height:1.28;margin-top:-16px">
  <li><b>Phrase simple</b> : un seul verbe conjugué.</li>
  <li><b>Phrase complexe</b> : plusieurs verbes conjugués.</li></ul>''' + EX('Le chat <span class="v">dort</span>. <span style="font-size:15px">(1 verbe)</span><br>Le chat <span class="v">dort</span> et le chien <span class="v">aboie</span>. <span style="font-size:15px">(2 verbes)</span>', 17) + \
        '<p class="small" style="margin:6px 0 0;font-size:16px">On relie avec <b>et</b>, <b>mais</b>, <b>car</b> ou une virgule.<br>L’infinitif ne compte pas : Léa veut <i>chanter</i>.</p>'
        tl_title = 'Simple ou complexe'
    else:
        decl = '''<ul style="padding-right:104px;font-size:20px;margin-top:-14px">
  <li>Elle raconte, elle informe.</li>
  <li>Elle se termine par un point <b>.</b> ou par <b>!</b></li></ul>''' + EX('Léa range sa chambre.', 21)
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
    exc = '''<ul style="font-size:19px;line-height:1.3;margin-top:-10px"><li>Elle exprime une émotion (surprise, colère, joie…).</li><li>Elle se termine par <b>!</b></li><li>Elle s’ajoute à n’importe quel type de phrase :</li></ul>''' + \
          EX('Le chien renverse sa gamelle ! <span style="font-size:15px">(déclarative)</span><br>Range ta chambre ! <span style="font-size:15px">(impérative)</span>', 17)
    boxes = [
     dict(id='decl', col='bleu', geom=TL, title=tl_title, avatar=('girl', 322, 122), html=decl, hstyle='font-size:30px' if cm2 else ''),
     dict(id='inter', col='vert', geom=TC, title=inter_t, html=inter),
     dict(id='imp', col='violet', geom=TR, title='Impérative', avatar=('boy', 1250, 122), html=imp),
     dict(id='aff', col='rose', geom=AFF, title='Affirmative', html=aff, style='padding-top:50px'),
     dict(id='neg', col='turquoise', geom=NEG, title='Négative', html=neg, style='padding-top:50px'),
     dict(id='excl', col='orange', geom=EXC, title='Exclamative', html=exc, style='padding-top:50px'),
    ]
    legend = '<span class="v">verbe conjugué</span>' if cm2 else ''
    titre = 'La phrase :<br>simple ou<br>complexe' if cm2 else 'Les types<br>et les formes<br>de phrase'
    return build(lid, titre, chip, legend, boxes, sub='', title_size=34, legend_pos='right:26px;top:540px')


if __name__ == '__main__':
    carte('G2-CE2', 'Grammaire — G2 — CE2', 'CE2')
    carte('G2-CM2', 'Grammaire — G2 — CM2', 'CM2')
    print('cartes G2 : sortie/G2-CE2_carte.jpeg, G2-CM2_carte.jpeg')
