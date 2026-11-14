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

SCRIPTS = {'G1': 'g1_carte.py', **{f'O{k}': 'o1_a_o6.py' for k in range(1, 7)}, 'O7-CE2': 'o7_o12.py', **{f'O{k}': 'o7_o12.py' for k in range(8, 13)}, 'G4': 'g4.py', 'G5': 'g5.py', 'G6': 'g6.py', 'G6-CE2': 'g6_ce2.py', 'G7': 'g7.py', **{f'H{k}': f'h{k}.py' for k in range(2, 8)}, **{f'V{k}': f'v{k}.py' for k in range(3, 7)}, **{f'C{k}': f'c{k}.py' for k in range(1, 6)}, 'C6': 'ce2_seulement.py', 'C6-CE2': 'ce2_seulement.py', 'C7': 'ce2_seulement.py', 'C7-CE2': 'ce2_seulement.py', 'C8-CM2': 'c8_c9_cm2.py', 'C9-CM2': 'c8_c9_cm2.py'}
PAL_DE = {'indigo': ('#5e35b1', '#ece6fa', '#cdbff0', '#5e35b1'), 'marron': ('#8d5524', '#f6e9dc', '#e5c9a8', '#8d5524')}
MARGE = 24
ZMAX = {'C2': 1.0, 'C8-CM2': 1.1, 'C3': 1.1}   # cartes dont un tableau déborderait du cadre si le texte était plus grand
ZOOM = [1]   # agrandissement du texte des cadres (cartes aux petits caractères : H) ; choisi par auto()
ECART_MIN = 205   # espace minimum, entre les cadres du haut et ceux du bas, pour le nuage
# retouches propres à une carte : (carte, cadre) -> (titre en plus, [(texte à remplacer, remplaçant)])
RETOUCHES = {('G4', 'inv'): ('font-size:25px;', []), ('G6', 'phrase'): ('font-size:24px;', []),
             ('G6-CE2', 'cc'): ('', [('font-size:20px;padding-right:96px', 'font-size:20px;padding-right:150px')]),
             ('G6-CE2', 'tests'): ('', [('<p class="txt"><b>Je supprime', '<p class="txt" style="font-size:18px;white-space:nowrap;margin-right:-12px"><b>Je supprime')])}


def lire(fichier, lid=None):
    """(boxes, args du build) de la carte `lid` d'un script de leçon. Les instructions qui précèdent sont exécutées, SAUF celles qui appellent
    build() ou save() (rien n'est écrit, les autres cartes du même script ne sont pas refaites) ; celle de la carte voulue donne les arguments."""
    if fichier.startswith('o'):   # leçons O : une fonction lesson() appelle build() et save() pour chaque carte ; on enregistre les appels de build() sans rien écrire
        rec = {}
        def faux_build(l, *a, **k): rec[l] = (k.pop('boxes', None) or a[3], (l,) + a, k); return '', {}
        src = open(os.path.join(D, fichier)).read().replace('from mapgen import build, TL, TC, TR', 'from mapgen import TL, TC, TR').replace('from lhelp import *', 'from lhelp import *\nsave = lambda *a, **k: None')
        ns = {'__file__': os.path.join(D, fichier), 'build': faux_build}
        exec(compile(src, fichier, 'exec'), ns)
        return rec[lid]
    tree = ast.parse(open(os.path.join(D, fichier)).read())
    ns = {'__file__': os.path.join(D, fichier)}
    appelle = lambda n, noms: any(isinstance(x, ast.Call) and getattr(x.func, 'id', '') in noms for x in ast.walk(n))
    for st in tree.body:
        if appelle(st, ('build',)):
            call = next(x for x in ast.walk(st) if isinstance(x, ast.Call) and getattr(x.func, 'id', '') == 'build')
            if lid is None or (call.args and getattr(call.args[0], 'value', None) == lid):
                a = [eval(compile(ast.Expression(x), 'a', 'eval'), ns) for x in call.args]
                kw = {k.arg: eval(compile(ast.Expression(k.value), 'a', 'eval'), ns) for k in call.keywords}
                return ns['boxes'], a, kw
            continue
        if appelle(st, ('save',)): continue
        exec(compile(ast.Module([st], []), fichier, 'exec'), ns)
    raise SystemExit('carte introuvable : ' + str(lid))


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
    bx = []
    for b in boxes:
        g = (geo or {}).get(b['id'], b['geom']); dy = g[1] - b['geom'][1]   # les dessins suivent leur cadre quand la rangée du bas monte ou descend
        bx.append(dict(b, geom=g, figs=[(n, x, y + dy, w) for n, x, y, w in b.get('figs', [])]))
    titre, chip, legend = a[1], a[2], a[3]
    kw = dict(kw); kw.pop('cloud_dy', None); kw.pop('legend_pos', None) if lid[0] == 'O' else None
    if lid in ('O8', 'O10'): kw['title_size'] = 33
    if lid == 'C5': kw['legend_pos'] = 'right:18px;top:520px'
    kw['extra_html'] = police() + (f'<style>.box.tint>*:not(h2){{zoom:{ZOOM[0]} !important}}</style>' if ZOOM[0] != 1 else '')
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
    """Pour H : texte agrandi au plus grand facteur (≤ 1,5) qui laisse la place du nuage."""
    if lid[0] not in 'HVCO': ZOOM[0] = 1; return auto1(lid, a, kw, boxes)
    for z in [x for x in [1.5, 1.45, 1.4, 1.35, 1.3, 1.25, 1.2, 1.15, 1.1, 1.05, 1.0] if x <= ZMAX.get(lid, 1.5)]:
        ZOOM[0] = z; r = auto1(lid, a, kw, boxes, silencieux=True)
        if (r[1] >= ECART_MIN and r[2] >= 40) or z == 1.0: break
    print(lid, 'zoom', z, 'écart', r[1]); return r[0]


def auto1(lid, a, kw, boxes, silencieux=False):
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
    Bi = max(geo[b['id']][1] + geo[b['id']][3] for b in centre) if centre else min(geo[b['id']][1] + geo[b['id']][3] for b in haut)
    cdy = round((Bi + Tb) / 2 - 431)
    carte(lid, a, kw, boxes, geo, cdy)
    zones = {k: [round(l / 14, 1), round((t - 24) / 9.33, 1), round(w / 14, 1), round((t + h - (t - 24)) / 9.33, 1)] for k, (l, t, w, h) in geo.items()}
    return (zones, Tb - Bi, Tb - max(g[1] + g[3] for k, g in geo.items() if g[1] < CY)) if silencieux else zones


if __name__ == '__main__':
    voulus = sys.argv[1:] or list(SCRIPTS)
    Z = {}
    for lid in voulus:
        boxes, a, kw = lire(SCRIPTS[lid], lid); Z[lid] = auto(lid, a, kw, style(boxes, lid))
        shutil.copy(os.path.join(D, '..', 'sortie', f'{lid}_carte.jpeg'), os.path.join(D, '..', '..', 'images', f'{lid}.jpg'))
    # zones : une leçon qui a son bloc dans index.html les reçoit directement ; une carte par niveau (G6-CE2…) va dans ZONES_NIV
    site = open(os.path.join(D, '..', '..', 'index.html')).read()
    for lid, z in Z.items():
        if lid == 'G1':   # leçon écrite en JS (pas en JSON) : zones remplacées une à une
            import re
            t = open(os.path.join(D, '..', '..', 'index.html')).read()
            for k, v in z.items(): t = re.sub(r"(\{id:'%s',[^}]*?zone:)\[[^\]]*\]" % k, lambda m: m.group(1) + str(v), t, count=1)
            open(os.path.join(D, '..', '..', 'index.html'), 'w').write(t); continue
        if ('\n%s:{"sections"' % lid) in site or ('\n"%s":{"sections"' % lid) in site: mettre_dans_le_site({lid: z}, lid)
        else: mettre_dans_le_site({lid.split('-')[0]: {}, lid: z}, lid.split('-')[0])
