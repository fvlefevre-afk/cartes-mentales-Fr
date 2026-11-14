"""Cartes de G4, G5, G6 (CM1), G6-CE2 et G7 dans le même style que G2 et G3 (14/11/2026) : couleurs soutenues, Andika, titres noirs, cadres ajustés à
leur contenu, zones cliquables écrites dans index.html, nuage entre les cadres du haut et ceux du bas.
Le texte de chaque carte reste celui de son script d'origine (g4.py, g5.py…) : ce script en lit les cadres SANS rien exécuter d'autre
(pas de save : les leçons de index.html ne sont pas touchées, seules les zones le sont).
Usage : python3 outils/lecons/g_cartes.py [G4 G5 G6 G6-CE2 G7]  → sortie/<id>_carte.jpeg copié dans images/<id>.jpg ; zones mises dans index.html."""
import os, sys, ast, shutil
D = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(D, '..'))
from mapgen import build, CY
from g2_cartes import PALG, police, mesurer, mettre_dans_le_site

SCRIPTS = {'G4': 'g4.py', 'G5': 'g5.py', 'G6': 'g6.py', 'G6-CE2': 'g6_ce2.py', 'G7': 'g7.py'}
PAL_DE = {'indigo': ('#5e35b1', '#ece6fa', '#cdbff0', '#5e35b1'), 'marron': ('#8d5524', '#f6e9dc', '#e5c9a8', '#8d5524')}
MARGE = 24
# retouches propres à une carte : (carte, cadre) -> (titre en plus, [(texte à remplacer, remplaçant)])
RETOUCHES = {('G4', 'inv'): ('font-size:25px;', []), ('G6', 'phrase'): ('font-size:24px;', []),
             ('G6-CE2', 'cc'): ('', [('font-size:20px;padding-right:96px', 'font-size:20px;padding-right:150px')]),
             ('G6-CE2', 'tests'): ('', [('<p class="txt"><b>Je supprime', '<p class="txt" style="font-size:18px;white-space:nowrap;margin-right:-12px"><b>Je supprime')])}


def lire(fichier):
    """(boxes, args du build) d'un script de leçon : tout le texte avant l'appel à build() est exécuté, rien après."""
    src = open(os.path.join(D, fichier)).read().split('\n')
    i = next(k for k, l in enumerate(src) if 'build(' in l and not l.startswith(' '))
    ns = {'__file__': os.path.join(D, fichier)}
    exec('\n'.join(src[:i]), ns)
    call = ast.parse(src[i].split('=', 1)[-1].strip() if src[i].lstrip().startswith('out') else src[i].strip()).body[0].value
    a = [eval(compile(ast.Expression(x), 'a', 'eval'), ns) for x in call.args]
    kw = {k.arg: eval(compile(ast.Expression(k.value), 'a', 'eval'), ns) for k in call.keywords}
    return ns['boxes'], a, kw


def style(boxes, lid=''):
    """Mêmes réglages que G2 / G3 : palette soutenue, cadre prolongé de 24 px vers le haut, titre à 30 px, dessins détourés."""
    res = []
    for b in boxes:
        b = dict(b)
        b['pal'] = PALG.get(b['col']) or PAL_DE[b['col']]
        b['ext'] = 24
        b['hstyle'] = 'top:30px;' + b.get('hstyle', '').rstrip(';') + ';'
        ht, rep = RETOUCHES.get((lid, b['id']), ('', []))
        b['hstyle'] = ht + b['hstyle']
        for x, y in rep: b['html'] = b['html'].replace(x, y, 1)
        av = b.pop('avatar', None)
        if av:
            who, x, y = av
            b['figs'] = [('girl', x + 30, y - 24, 84)] if who == 'girl' else [('boy', x - 6, y - 16, 112)]
        res.append(b)
    return res


def carte(lid, a, kw, boxes, geo=None, cdy=26):
    bx = [dict(b, geom=(geo or {}).get(b['id'], b['geom'])) for b in boxes]
    titre, chip, legend = a[1], a[2], a[3]
    kw = dict(kw); kw.pop('cloud_dy', None); kw['extra_html'] = police()
    return build(lid, titre, chip, legend, bx, cloud_dy=cdy, **kw)


def titres(lid, boxes):
    """Réduit le titre d'un cadre qui irait sous la pastille de son numéro (50 px de chaque côté du titre centré)."""
    from playwright.sync_api import sync_playwright
    hp = os.path.join(D, '..', 'sortie', f'{lid}map.html')
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page(viewport={'width': 1400, 'height': 933}); pg.goto('file://' + os.path.abspath(hp)); pg.wait_for_timeout(300)
        r = pg.evaluate("""() => [...document.querySelectorAll('.box h2')].map(h => [h.getBoundingClientRect().width, parseFloat(getComputedStyle(h).fontSize)])""")
        b.close()
    out = []
    for bx, (w, fs) in zip(boxes, r):
        dispo = bx['geom'][2] - 104
        if w > dispo: bx = dict(bx, hstyle=bx['hstyle'] + f'font-size:{fs * dispo / w:.1f}px;')
        out.append(bx)
    return out


def auto(lid, a, kw, boxes):
    """Mesure le contenu de chaque cadre, ajuste les hauteurs, aligne la rangée du bas tout en bas, place le nuage au milieu ; renvoie les zones (en %)."""
    ids = [b['id'] for b in boxes]
    carte(lid, a, kw, boxes)
    boxes = titres(lid, boxes)
    carte(lid, a, kw, boxes)
    m = dict(zip(ids, mesurer(lid, ids).values()))
    geo = {}
    haut = [b for b in boxes if b['geom'][1] < CY]; bas = [b for b in boxes if b['geom'][1] >= CY]
    for b in haut:
        l, t, w, h = b['geom']; geo[b['id']] = (l, t, w, round(m[b['id']] + MARGE - t))
    Hb = {b['id']: round(m[b['id']] + MARGE - (b['geom'][1] - 24)) for b in bas}
    Tb = 921 - max(Hb.values())
    for b in bas:
        l, t, w, h = b['geom']; geo[b['id']] = (l, Tb + 24, w, Hb[b['id']] - 24)
    centre = [b for b in haut if b['geom'][0] < 840 and b['geom'][0] + b['geom'][2] > 560]
    Bi = max(geo[b['id']][1] + geo[b['id']][3] for b in centre)
    cdy = round((Bi + Tb) / 2 - 431)
    carte(lid, a, kw, boxes, geo, cdy)
    print(lid, 'bas du centre', Bi, 'rangée du bas à', Tb, 'écart', Tb - Bi, 'nuage dy', cdy)
    return {k: [round(l / 14, 1), round((t - 24) / 9.33, 1), round(w / 14, 1), round((t + h - (t - 24)) / 9.33, 1)] for k, (l, t, w, h) in geo.items()}


if __name__ == '__main__':
    voulus = sys.argv[1:] or list(SCRIPTS)
    Z = {}
    for lid in voulus:
        boxes, a, kw = lire(SCRIPTS[lid]); Z[lid] = auto(lid, a, kw, style(boxes, lid))
        shutil.copy(os.path.join(D, '..', 'sortie', f'{lid}_carte.jpeg'), os.path.join(D, '..', '..', 'images', f'{lid}.jpg'))
    # zones : une leçon (CM1) par appel ; G6-CE2 va dans ZONES_NIV
    for lid in [x for x in voulus if x != 'G6-CE2']:
        mettre_dans_le_site({lid: Z[lid], **({'G6-CE2': Z['G6-CE2']} if lid == 'G6' and 'G6-CE2' in Z else {})}, lid)
    if 'G6-CE2' in Z and 'G6' not in voulus: mettre_dans_le_site({'G6': {}, 'G6-CE2': Z['G6-CE2']}, 'G6')
