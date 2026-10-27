"""Cartes mentales de G3 (le groupe nominal) pour le CE2 et le CM2 (27/10/2026).
La carte du CM1 (images/G3.jpg) n'a pas de script ; ce script la refait à l'identique (identifiant « G3-CM1-essai », pour comparer) et fabrique :
  - G3-CE2 : « nom » à la place de « nom noyau » (au CE2 on dit « nom », comme dans les fiches) ;
  - G3-CM2 : la carte du CM1 + le complément du nom et l'attribut du sujet, les notions du CM2.
Mêmes zones que G3 (gn, noyau, adj, accord, att) : les leçons n'ont pas à changer de zones.
Usage : python3 lecons/g3_cartes.py   → sortie/G3-CE2_carte.jpeg, sortie/G3-CM2_carte.jpeg (puis les copier dans images/ : voir LISEZMOI)."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from mapgen import build, TL, TC, TR, BL, BR

SOUS = lambda c, hb, titre, x, y, w, h, html: (
    f'<div class="sub" style="--c:{c};--hb:{hb};left:{x}px;top:{y}px;width:{w}px;height:{h}px;font-size:20px;line-height:1.5"><h3>{titre}</h3>{html}</div>')


def carte(lid, chip, niveau):
    nom = 'nom noyau' if niveau != 'CE2' else 'nom'
    titre_tc = 'Le nom noyau' if niveau != 'CE2' else 'Le nom'
    cm2 = niveau == 'CM2'
    # --- le GN, c'est…
    gn_li2 = '<span class="d">déterminant</span> + <b style="color:#1f5fc4">nom</b> (+ <span class="a">adjectif</span>)' + (' (+ <b style="color:#5e35b1">complément du nom</b>)' if cm2 else '')
    gn = f'''<ul style="padding-right:128px;font-size:20px;margin-top:-14px">
  <li>un groupe de mots organisé autour d’un <b>nom</b>.</li>
  <li>{gn_li2}</li></ul>
  <div class="ex big" style="text-align:center;margin-top:8px"><span class="d">le</span> <span class="a">petit</span> <span class="n">chat</span> <span class="a">noir</span></div>
  <p class="small" style="margin:6px 0 0;font-size:16px">Déterminants : <span class="d" style="font-size:15px">le, la, les, un, une, des, mon, ce…</span></p>'''
    if cm2:
        gn = f'''<ul style="padding-right:128px;font-size:19px;margin-top:-18px;line-height:1.3">
  <li>un groupe de mots organisé autour d’un <b>nom</b>.</li>
  <li>{gn_li2}</li></ul>
  <div class="ex big" style="text-align:center;margin-top:6px;padding:4px 14px;font-size:25px"><span class="d">un</span> <span class="a">petit</span> <span class="n">pot</span> <span style="border:2.5px solid #5e35b1;border-radius:10px;padding:0 6px;color:#5e35b1">de confiture</span></div>
  <p class="small" style="margin:4px 0 0;font-size:15px">Déterminants : <span class="d" style="font-size:14px">le, la, les, un, une, des, mon, ce…</span></p>'''
    # --- le nom (noyau)
    tc_extra = ''
    if cm2:
        tc_extra = '<li>Le <b style="color:#5e35b1">complément du nom</b> (de, en, à…) le précise : il <b>ne change pas</b>.</li>'
    tc = f'''<ul style="font-size:20px;line-height:1.3;margin-top:-12px">
  <li>C’est le mot <b>le plus important</b> du GN. Je l’<b>entoure</b>.</li>
  <li>On ne peut <b>pas l’enlever</b>.</li>{tc_extra}</ul>
  <div class="ex" style="text-align:center;padding:4px 10px;margin-top:6px">une <span class="barre">grande</span> <span class="n">maison</span> <span class="barre">blanche</span><br><span class="arrow">→</span> <span class="d">une</span> <span class="n">maison</span></div>'''
    if cm2:
        tc = f'''<ul style="font-size:18.5px;line-height:1.25;margin-top:-14px">
  <li>C’est le mot <b>le plus important</b> du GN. Je l’<b>entoure</b>.</li>
  <li>On ne peut <b>pas l’enlever</b>.</li>{tc_extra}</ul>
  <div class="ex" style="text-align:center;padding:2px 10px;margin-top:4px;font-size:20px;line-height:1.3">une <span class="barre">grande</span> <span class="n">maison</span> <span class="barre">blanche</span> <span class="arrow">→</span> <span class="d">une</span> <span class="n">maison</span></div>'''
    # --- l'adjectif
    adj = f'''<ul style="padding-right:128px;font-size:19.5px;line-height:1.3;margin-top:-14px">
  <li>Il dit <b>comment est</b> le nom.</li>
  <li>Il se place <b>avant</b> ou <b>après</b> le nom.</li></ul>
  <ul style="font-size:19.5px;line-height:1.3;margin-top:2px"><li>Dans le GN, il est <b>épithète</b>.</li></ul>
  <div class="exl" style="margin-top:6px;line-height:1.4;font-size:19.5px">un <span class="a">gros</span> ballon <span class="a">rouge</span><br>une souris <span class="arrow">→</span> une <span class="a">petite</span> souris <span class="a">grise</span></div>'''
    if cm2:
        adj = f'''<ul style="padding-right:128px;font-size:18.5px;line-height:1.25;margin-top:-16px">
  <li>Il dit <b>comment est</b> le nom ; il se place <b>avant</b> ou <b>après</b>.</li></ul>
  <ul style="font-size:18.5px;line-height:1.25;margin-top:2px">
  <li style="margin-right:128px">Dans le GN, il est <b>épithète</b>.</li>
  <li>Après <b>être, sembler, devenir</b>… il est <b>attribut</b> du sujet : il s’accorde avec lui.</li></ul>
  <div class="exl" style="margin-top:4px;line-height:1.35;font-size:19px">Les fleurs <span class="v">sont</span> <span class="a">fanées</span>.<br>une souris <span class="arrow">→</span> une <span class="a">petite</span> souris <span class="a">grise</span></div>'''
    # --- les accords
    accord = (f'<div class="rule" style="top:46px;font-size:19.5px">Le <b>{nom}</b> commande : le déterminant et l’adjectif s’accordent avec lui.</div>'
      + SOUS('#c2185b', '#fbe0ea', 'Masculin → féminin', 22, 116, 410, 216, '''
  <div>J’ajoute souvent un <span class="e">e</span>.</div>
  <div style="margin-top:6px">un ami content<br>&nbsp;&nbsp;<span class="arrow">→</span> un<span class="e">e</span> ami<span class="e">e</span> content<span class="e">e</span></div>
  <div style="margin-top:6px">Parfois, le mot change :<br>&nbsp;&nbsp;gros <span class="arrow">→</span> gro<span class="e">sse</span> · doux <span class="arrow">→</span> dou<span class="e">ce</span></div>''')
      + SOUS('#00838f', '#cdeef1', 'Singulier → pluriel', 456, 116, 410, 216, '''
  <div>J’ajoute souvent un <span class="e">s</span>.</div>
  <div style="margin-top:6px">le chat noir<br>&nbsp;&nbsp;<span class="arrow">→</span> le<span class="e">s</span> chat<span class="e">s</span> noir<span class="e">s</span></div>
  <div style="margin-top:6px">une fleur jaune<br>&nbsp;&nbsp;<span class="arrow">→</span> de<span class="e">s</span> fleur<span class="e">s</span> jaune<span class="e">s</span></div>'''))
    att_extra = '<li style="margin-top:4px">Le complément du nom <b>ne s’accorde pas</b> : des pots <b>de confiture</b>.</li>' if cm2 else ''
    att = f'''<ul style="font-size:{'18' if cm2 else '19'}px;line-height:1.28;margin-top:-16px">
  <li>Pluriel en <span class="e">x</span> : des gâteau<span class="e">x</span>, des jeu<span class="e">x</span>.</li>
  <li><b>-al</b> <span class="arrow">→</span> <b>-aux</b> : un cheval, des chev<span class="e">aux</span>.</li>
  <li>Déjà <b>-s, -x, -z</b> : pas de changement.<br><span class="small" style="font-size:16px">une souris <span class="arrow">→</span> des souris</span></li>
  <li>Déjà <b>-e</b> au masculin : pas de changement.<br><span class="small" style="font-size:16px">un vélo rouge <span class="arrow">→</span> une moto rouge</span></li>{att_extra}</ul>'''
    boxes = [
     dict(id='gn', col='vert', geom=TL, title='Le GN, c’est…', avatar=('girl', 322, 122), html=gn),
     dict(id='noyau', col='bleu', geom=TC, title=titre_tc, html=tc),
     dict(id='adj', col='violet', geom=TR, title='L’adjectif', avatar=('boy', 1250, 122), html=adj),
     dict(id='accord', col='orange', geom=BL, title='Les accords dans le GN', html=accord, style='padding-top:48px'),
     dict(id='att', col='rouge', geom=BR, title='Attention !', style='padding-top:58px', html=att),
    ]
    legend = f'<span class="d">dét.</span> · <b style="color:#1f5fc4">{nom}</b> · <span class="a">adjectif</span>'
    return build(lid, 'Le groupe<br>nominal', chip, legend, boxes, sub='le GN', title_size=40, legend_pos='right:26px;top:14px')


if __name__ == '__main__':
    carte('G3-CM1-essai', 'Grammaire — G3 — CM1', 'CM1')
    carte('G3-CE2', 'Grammaire — G3 — CE2', 'CE2')
    carte('G3-CM2', 'Grammaire — G3 — CM2', 'CM2')
    print('cartes G3 : sortie/G3-CM1-essai_carte.jpeg, G3-CE2_carte.jpeg, G3-CM2_carte.jpeg')
