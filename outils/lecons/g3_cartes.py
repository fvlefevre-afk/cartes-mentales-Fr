"""Cartes mentales de G3 (le groupe nominal) pour le CE2 et le CM2 (27/10/2026).
La carte du CM1 (images/G3.jpg) n'a pas de script ; ce script la refait à l'identique (identifiant « G3-CM1-essai », pour comparer) et fabrique :
  - G3-CE2 : « nom » à la place de « nom noyau » (au CE2 on dit « nom », comme dans les fiches) ;
  - G3-CM2 : la carte du CM1 + le complément du nom et l'attribut du sujet, les notions du CM2.
Mêmes zones que G3 (gn, noyau, adj, accord, att) : les leçons n'ont pas à changer de zones.
Usage : python3 lecons/g3_cartes.py   → sortie/G3-CE2_carte.jpeg, sortie/G3-CM2_carte.jpeg (puis les copier dans images/ : voir LISEZMOI)."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from mapgen import build, TL, TC, TR, BL, BR
from g2_cartes import PALG, police, mesurer, mettre_dans_le_site   # même style que G2 (couleurs soutenues, Andika, cadres ajustés, zones automatiques)

SOUS = lambda c, hb, titre, x, y, w, h, html: (
    f'<div class="sub" style="--c:{c};--hb:{hb};left:{x}px;top:{y}px;width:{w}px;height:{h}px;font-size:20px;line-height:1.5"><h3>{titre}</h3>{html}</div>')


def carte(lid, chip, niveau, geo=None, cdy=26):
    geo = geo or {}
    nom = 'nom noyau' if niveau != 'CE2' else 'nom'
    titre_tc = 'Le nom noyau' if niveau != 'CE2' else 'Le nom'
    cm2 = niveau == 'CM2'
    # --- le GN, c'est…
    gn_li2 = '<span class="d">déterminant</span> + <b style="color:#e0458f">nom</b> (+ <span class="a">adjectif</span>)' + (' (+ <b style="color:#5e35b1">complément du nom</b>)' if cm2 else '')
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
  <div class="ex" style="text-align:center;padding:2px 8px;margin-top:4px;font-size:17px;line-height:1.3;white-space:nowrap">une <span class="barre">grande</span> <span class="n">maison</span> <span class="barre">blanche</span> <span class="arrow">→</span> <span class="d">une</span> <span class="n">maison</span></div>'''
    # --- l'adjectif
    epi = '' if niveau == 'CE2' else '  <ul style="font-size:19.5px;line-height:1.3;margin-top:2px"><li>Dans le GN, il est <b>épithète</b>.</li></ul>'   # épithète : notion du CM1 (idée 329)
    adj = f'''<ul style="padding-right:128px;font-size:19.5px;line-height:1.3;margin-top:-14px">
  <li>Il dit <b>comment est</b> le nom.</li>
  <li>Il se place <b>avant</b> ou <b>après</b> le nom.</li></ul>
{epi}
  <div class="exl" style="margin-top:6px;line-height:1.4;font-size:19.5px">un <span class="a">gros</span> ballon <span class="a">rouge</span><br>une souris <span class="arrow">→</span> une <span class="a">petite</span> souris <span class="a">grise</span></div>'''
    if cm2:
        adj = f'''<ul style="padding-right:128px;font-size:18.5px;line-height:1.25;margin-top:-16px">
  <li>Il dit <b>comment est</b> le nom ; il se place <b>avant</b> ou <b>après</b>.</li></ul>
  <ul style="font-size:18.5px;line-height:1.25;margin-top:2px">
  <li style="margin-right:128px">Dans le GN, il est <b>épithète</b>.</li>
  <li>Après <b>être, sembler, devenir</b>… il est <b>attribut</b> du sujet : il s’accorde avec lui.</li></ul>
  <div class="exl" style="margin-top:4px;line-height:1.35;font-size:19px">Les fleurs <span class="v">sont</span> <span class="a">fanées</span>.<br>une souris <span class="arrow">→</span> une <span class="a">petite</span> souris <span class="a">grise</span></div>'''
    # --- les accords
    accord = (f'<div class="rule" style="top:74px;font-size:19.5px">Le <b>{nom}</b> commande : le déterminant et l’adjectif s’accordent avec lui.</div>'
      + SOUS('#5f6b7a', '#eef0f3', 'Masculin → féminin', 22, 140, 410, 216, '''
  <div>J’ajoute souvent un <span class="e">e</span>.</div>
  <div style="margin-top:6px">un ami content<br>&nbsp;&nbsp;<span class="arrow">→</span> un<span class="e">e</span> ami<span class="e">e</span> content<span class="e">e</span></div>
  <div style="margin-top:6px">Parfois, le mot change :<br>&nbsp;&nbsp;gros <span class="arrow">→</span> gro<span class="e">sse</span> · doux <span class="arrow">→</span> dou<span class="e">ce</span></div>''')
      + SOUS('#00838f', '#cdeef1', 'Singulier → pluriel', 456, 140, 410, 216, '''
  <div>J’ajoute souvent un <span class="e">s</span>.</div>
  <div style="margin-top:6px">le chat noir<br>&nbsp;&nbsp;<span class="arrow">→</span> le<span class="e">s</span> chat<span class="e">s</span> noir<span class="e">s</span></div>
  <div style="margin-top:6px">une fleur jaune<br>&nbsp;&nbsp;<span class="arrow">→</span> de<span class="e">s</span> fleur<span class="e">s</span> jaune<span class="e">s</span></div>'''))
    if niveau == 'CE2':   # au CE2, les féminins qui s'entendent du programme (lecteur → lectrice, joyeux → joyeuse) ; grosse, douce : CM1 (comme les fiches, idée 329)
        accord = accord.replace('gros <span class="arrow">→</span> gro<span class="e">sse</span> · doux <span class="arrow">→</span> dou<span class="e">ce</span>',
                                'joyeux <span class="arrow">→</span> joyeu<span class="e">se</span> · lecteur <span class="arrow">→</span> lect<span class="e">rice</span>')
    att_extra = '<li style="margin-top:4px">Le complément du nom <b>ne s’accorde pas</b> : des pots <b>de confiture</b>.</li>' if cm2 else ''
    att = f'''<ul style="font-size:{'18' if cm2 else '19'}px;line-height:1.28;margin-top:-16px">
  <li>Pluriel en <span class="e">x</span> : des gâteau<span class="e">x</span>, des jeu<span class="e">x</span>.</li>
  <li><b>-al</b> <span class="arrow">→</span> <b>-aux</b> : un cheval, des chev<span class="e">aux</span>.</li>
  <li>Déjà <b>-s, -x, -z</b> : pas de changement.<br><span class="small" style="font-size:16px">une souris <span class="arrow">→</span> des souris</span></li>
  <li>Déjà <b>-e</b> au masculin : pas de changement.<br><span class="small" style="font-size:16px">un vélo rouge <span class="arrow">→</span> une moto rouge</span></li>{att_extra}</ul>'''
    boxes = [
     dict(id='gn', col='gris', pal=PAL_PERSO['gris'], geom=geo.get('gn', TL), ext=24, hstyle='top:30px', title='Le GN, c’est…', figs=[('girl', 352, 98, 84)], html=gn),
     dict(id='noyau', col='rose', pal=PAL_PERSO['nom'], geom=geo.get('noyau', TC), ext=24, hstyle='top:30px', title=titre_tc, html=tc),
     dict(id='adj', col='vert', pal=PALG['vert'], geom=geo.get('adj', TR), ext=24, hstyle='top:30px', title='L’adjectif', figs=[('boy', 1244, 106, 112)], html=adj),
     dict(id='accord', col='orange', pal=PALG['orange'], geom=geo.get('accord', BL), ext=24, hstyle='top:30px', title='Les accords dans le GN', html=accord, style='padding-top:48px'),
     dict(id='att', col='rouge', pal=PALG['rouge'], geom=geo.get('att', BR), ext=24, hstyle='top:30px', title='Attention !', style='padding-top:58px', html=att),
    ]
    legend = f'<span class="d">dét.</span> · <b style="color:#e0458f">{nom}</b> · <span class="a">adjectif</span>'
    return build(lid, 'Le groupe<br>nominal', chip, legend, boxes, extra_html=police() + CSS_PERSO, sub='le GN', title_size=40, legend_pos='right:26px;top:14px', cloud_dy=cdy)


IDS = ('gn', 'noyau', 'adj', 'accord', 'att')
# Code couleur des personnages (18/11/2026, choix de l'enseignante, comme G4) : déterminant bleu ciel, nom rose, adjectif vert ; cadre du nom noyau rose, de l'adjectif vert, du GN gris.
PAL_PERSO = {'nom': ('#e0458f', '#fde4ef', '#f7b3d2', '#d6337f'), 'gris': ('#5f6b7a', '#eef0f3', '#cfd5dd', '#4b5563')}
CSS_PERSO = '<style>.d{color:#0b8fd6}.n{color:#e0458f;border-color:#e0458f}</style>'
MARGE = 24


def auto(lid, chip, niveau):
    carte(lid, chip, niveau)
    m = mesurer(lid, IDS)
    geo = {}
    for k, g in (('gn', TL), ('noyau', TC), ('adj', TR)):
        l, t, w, h = g; geo[k] = (l, t, w, round(m[k] + MARGE - t))
    Hb = {k: round(m[k] + MARGE - (g[1] - 24)) for k, g in (('accord', BL), ('att', BR))}
    Tb = 921 - max(Hb.values())
    for k, g in (('accord', BL), ('att', BR)):
        l, t, w, h = g; geo[k] = (l, Tb + 24, w, Hb[k] - 24)
    Bi = geo['noyau'][1] + geo['noyau'][3]   # le nuage est dans la colonne du centre : seul le cadre du nom noyau est au-dessus de lui
    cdy = round((Bi + Tb) / 2 - 431)
    carte(lid, chip, niveau, geo, cdy)
    zones = {}
    for k, (l, t, w, h) in geo.items():
        T = t - 24
        zones[k] = [round(l / 14, 1), round(T / 9.33, 1), round(w / 14, 1), round((t + h - T) / 9.33, 1)]
    print(lid, 'bas des cadres du haut', Bi, 'rangée du bas à', Tb, 'nuage dy', cdy)
    return zones


if __name__ == '__main__':
    import shutil
    Z = {'G3': auto('G3', 'Grammaire — G3 — CM1', 'CM1'), 'G3-CE2': auto('G3-CE2', 'Grammaire — G3 — CE2', 'CE2'), 'G3-CM2': auto('G3-CM2', 'Grammaire — G3 — CM2', 'CM2')}
    mettre_dans_le_site(Z, 'G3')
    from g_cartes import garder_html   # loupe nette (19/11/2026) : la carte gardée en vrai texte dans cartes-html/, image recopiée dans images/
    for lid in Z:
        shutil.copy(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'sortie', f'{lid}_carte.jpeg'), os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'images', f'{lid}.jpg'))
        garder_html(lid)
    print('cartes G3 : sortie/G3_carte.jpeg, G3-CE2_carte.jpeg, G3-CM2_carte.jpeg (recopiées dans images/, pages gardées dans cartes-html/) ; zones mises dans index.html')
if __name__ == '__main__':
    import os, sys; import subprocess as _sp; _sp.run([sys.executable, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'integrer_images.py')])   # images et police dans index.html (17/11/2026)
