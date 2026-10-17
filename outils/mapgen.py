import os, math, subprocess
D = os.path.dirname(os.path.abspath(__file__))
SORTIE = os.path.join(D, 'sortie'); os.makedirs(SORTIE, exist_ok=True)
CSS = open(os.path.join(D, 'common.css')).read()

PAL = {  # couleur: (bordure, fond, fond du titre)
    'vert': ('#23845a', '#eef8f1', '#cdeedb'),
    'bleu': ('#1f5fc4', '#eef4fd', '#d3e3fb'),
    'violet': ('#7b3fa0', '#f5effa', '#e6d6f3'),
    'orange': ('#e67e22', '#fff5ea', '#fde1c4'),
    'rouge': ('#c62828', '#fff3f2', '#fbd5d2'),
    'turquoise': ('#00838f', '#eaf7f8', '#cdeef1'),
    'rose': ('#c2185b', '#fdf0f5', '#fbe0ea'),
}
# Positions standard (comme G3)
TL = (18, 86, 430, 330)
TC = (485, 44, 430, 288)
TR = (952, 86, 430, 330)
BL = (18, 568, 892, 350)
BR = (945, 568, 437, 350)
CX, CY = 700, 440


def branch(b):
    l, t, w, h = b['geom']
    col = PAL[b['col']][0]
    bx = l + w / 2
    by = t + h if t < CY else t
    bx = min(max(bx, l + 60), l + w - 60)
    if t < CY and l < CX and l + w < CX:   # gauche haut
        ex, ey = l + w - 5, t + h * 0.65
    elif t < CY and l > CX:                # droite haut
        ex, ey = l + 5, t + h * 0.65
    elif t < CY:                            # centre haut
        ex, ey = CX, t + h - 5
    else:                                   # bas
        ex, ey = min(max(CX + (bx - CX) * 0.6, l + 80), l + w - 80), t + 5
    ang = math.atan2(ey - CY, ex - CX)
    sx, sy = CX + 115 * math.cos(ang), CY + 75 * math.sin(ang)
    mx, my = (sx + ex) / 2, (sy + ey) / 2
    return f'<path d="M{sx:.0f} {sy:.0f} Q{mx:.0f} {sy:.0f} {ex:.0f} {ey:.0f}" stroke="{col}"/>'


def build(lid, titre, chip, legend, boxes, sub='', title_size=40, legend_pos='right:18px;top:12px'):
    import re
    nb=lambda t: re.sub(r'« ', '«&nbsp;', re.sub(r' ([?!:;»])', r'&nbsp;\1', t))
    parts = []
    for b in boxes:
        b = dict(b, html=nb(b['html']), title=nb(b['title']))
        c, bg, hb = PAL[b['col']]
        l, t, w, h = b['geom']
        extra = b.get('style', '')
        parts.append(f'<div class="box" style="--c:{c};--bg:{bg};--hb:{hb};left:{l}px;top:{t}px;width:{w}px;height:{h}px;{extra}"><h2 style="{b.get('hstyle','')}">{b["title"]}</h2>{b["html"]}</div>')
        if b.get('avatar'):
            who, x, y = b['avatar']
            pos = 'left:-14%;top:-6%;width:125%;height:125%' if who == 'girl' else 'left:-22%;top:-4%;width:130%;height:130%'
            parts.append(f'<div class="avw" style="--c:{c};left:{x}px;top:{y}px"><img src="file://{D}/img/G2_{who}.jpeg" style="{pos}"></div>')
    branches = ''.join(branch(b) for b in boxes)
    html = f'''<!doctype html><html lang="fr"><head><meta charset="utf-8"><style>{CSS}</style></head><body>
<svg class="bg" width="1400" height="933" viewBox="0 0 1400 933">
<g fill="none" stroke-width="7" stroke-linecap="round">{branches}</g>
<g><g fill="#3b7dd8"><circle cx="620" cy="420" r="68"/><circle cx="700" cy="395" r="78"/><circle cx="785" cy="420" r="68"/><circle cx="600" cy="470" r="55"/><circle cx="700" cy="478" r="62"/><circle cx="805" cy="470" r="55"/></g>
<g fill="#eaf2fd"><circle cx="620" cy="420" r="64"/><circle cx="700" cy="395" r="74"/><circle cx="785" cy="420" r="64"/><circle cx="600" cy="470" r="51"/><circle cx="700" cy="478" r="58"/><circle cx="805" cy="470" r="51"/><rect x="600" y="410" width="205" height="80"/></g>
<g stroke-width="6" stroke-linecap="round"><path d="M520 400 l-26 -12" stroke="#f5b700"/><path d="M515 440 h-30" stroke="#e67e22"/><path d="M522 482 l-26 12" stroke="#c62828"/><path d="M880 400 l26 -12" stroke="#f5b700"/><path d="M885 440 h30" stroke="#23845a"/><path d="M878 482 l26 12" stroke="#7b3fa0"/></g></g>
</svg>
<div class="chip">{chip}</div>
<div class="title" style="font-size:{title_size}px"><div>{titre}{f'<small>{sub}</small>' if sub else ''}</div></div>
{''.join(parts)}
{f'<div style="position:absolute;{legend_pos};font-size:17px;background:#fff;border:2px solid #d8dde8;border-radius:14px;padding:2px 12px">{legend}</div>' if legend else ''}
</body></html>'''
    hp = os.path.join(SORTIE, f'{lid}map.html')
    open(hp, 'w').write(html)
    out = os.path.join(SORTIE, f'{lid}_carte.jpeg')
    subprocess.run(['python3', os.path.join(D, 'shot.py'), hp, out], check=True)
    zones = {}
    for b in boxes:
        l, t, w, h = b['geom']
        zones[b['id']] = [round(l / 14, 1), round((t - 24) / 9.33, 1), round(w / 14, 1), round((h + 24) / 9.33, 1)]
    return out, zones
