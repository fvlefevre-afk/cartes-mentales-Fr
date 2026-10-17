import re, os, shutil, subprocess, zipfile

def label_of(cell):
    return re.sub(r'<[^>]+>', '', cell).strip().lower()

def color_styles(s):
    """associe un nom de couleur au style de paragraphe utilisé dans la 1re colonne des tableaux"""
    m = {}
    for cell in re.findall(r'<table:table-cell table:style-name="Tableau\d\.A\d+"[^>]*>(.*?)</table:table-cell>', s, re.S):
        p = re.search(r'<text:p text:style-name="([^"]+)"', cell)
        lab = label_of(cell)
        if p and lab and lab not in m: m[lab] = p.group(1)
    return m

HEX = {'rose': '#f4a7c0', 'marron': '#8a5a3b', 'rouge': '#e53935', 'violette': '#8e5bc4', 'bleue': '#3b7dd8', 'verte': '#4caf6a', 'orange': '#f39c3d', 'jaune': '#ffff00'}

def ensure_color(s, cmap, color):
    if color in cmap: return s, cmap[color]
    # clone le style « jaune » (ou un autre) en changeant la couleur, avec une ombre pour la lisibilité
    base = cmap.get('jaune') or next(iter(cmap.values()))
    m = re.search(r'<style:style style:name="' + re.escape(base) + r'".*?</style:style>', s, re.S)
    name = 'PClaude' + color.capitalize()
    st = re.sub(r'style:name="[^"]+"', f'style:name="{name}"', m.group(0), count=1)
    st = re.sub(r'fo:color="#[0-9a-fA-F]{6}"', f'fo:color="{HEX[color]}"', st)
    if 'fo:text-shadow' not in st: st = st.replace('<style:text-properties ', '<style:text-properties fo:text-shadow="1pt 1pt" ', 1)
    s = s.replace('</office:automatic-styles>', st + '</office:automatic-styles>', 1)
    cmap[color] = name
    return s, name

def ensure_text_styles(s):
    if 'style:name="TClaudeB"' not in s:
        s = s.replace('</office:automatic-styles>',
            '<style:style style:name="TClaudeB" style:family="text"><style:text-properties fo:font-weight="bold" style:font-weight-asian="bold" style:font-weight-complex="bold"/></style:style>'
            '<style:style style:name="TClaudeN" style:family="text"><style:text-properties fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal"/></style:style>'
            '</office:automatic-styles>', 1)
    return s

def esc(t): return t.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

def set_table(s, tname, rows, extra=None):
    """rows : liste de (couleur, code, texte[, prérequis]). Reconstruit les lignes de données du tableau."""
    s = ensure_text_styles(s)
    cmap = color_styles(s)
    for r in rows: s, _ = ensure_color(s, cmap, r[0])
    a = s.index(f'<table:table table:name="{tname}"'); b = s.index('</table:table>', a)
    tab = s[a:b]
    trs = re.findall(r'<table:table-row.*?</table:table-row>', tab, re.S)
    head, tmpl = trs[0], trs[1]
    cells = re.findall(r'<table:table-cell.*?</table:table-cell>|<table:covered-table-cell[^>]*/>', tmpl, re.S)
    new = []
    for r in rows:
        color, code, text = r[0], r[1], r[2]
        s, cst = ensure_color(s, cmap, color)
        cs = list(cells)
        open_tag = re.match(r'<table:table-cell[^>]*>', cs[0]).group(0)
        cs[0] = f'{open_tag}<text:p text:style-name="{cst}">{esc(r[4] if len(r) > 4 else color)}</text:p></table:table-cell>'
        open_tag = re.match(r'<table:table-cell[^>]*>', cs[1]).group(0)
        pst = re.search(r"<text:(?:p|h) text:style-name=\"([^\"]+)\"", cs[1]).group(1)
        inner = (f'<text:span text:style-name="TClaudeB">{esc(code)}</text:span><text:span text:style-name="TClaudeN"> - {esc(text)}</text:span>' if code else '')
        cs[1] = f'{open_tag}<text:p text:style-name="{pst}">{inner}</text:p></table:table-cell>'
        if extra is not None and len(r) > 3 and r[3] is not None:
            i = extra
            open_tag = re.match(r'<table:table-cell[^>]*>', cs[i]).group(0)
            pst2 = re.search(r'<text:p text:style-name="([^"]+)"', cs[i])
            pst2 = pst2.group(1) if pst2 else pst
            cs[i] = f'{open_tag}<text:p text:style-name="{pst2}">{esc(r[3])}</text:p></table:table-cell>'
        row_open = re.match(r'<table:table-row[^>]*>', tmpl).group(0)
        new.append(row_open + ''.join(cs) + '</table:table-row>')
    first = tab.index(trs[1]); last = tab.index(trs[-1]) + len(trs[-1])
    tab = tab[:first] + ''.join(new) + tab[last:]
    s = s[:a] + tab + s[b:]
    # 8 ceintures ou plus : lignes moins hautes pour que le tableau tienne sur une page
    m = re.search(r'table:style-name="([^"]+)"', row_open)
    if m and len(rows) >= 8:
        h = round(19.3 / len(rows), 3)
        s = re.sub(r'(<style:style style:name="' + re.escape(m.group(1)) + r'"[^>]*><style:table-row-properties style:min-row-height=")[0-9.]+cm', lambda x: x.group(1) + f'{h}cm', s)
    return s

def table_after(s, marker):
    """Parcours A, B, C = 1er, 2e, 3e tableau du document"""
    names = re.findall(r'<table:table table:name="([^"]+)"', s)
    return names['ABC'.index(marker[-1])]

def rewrite_odt(src, dst, fn):
    tmp = dst + '.dir'
    shutil.rmtree(tmp, ignore_errors=True); os.makedirs(tmp)
    with zipfile.ZipFile(src) as z: z.extractall(tmp)
    p = os.path.join(tmp, 'content.xml')
    s = open(p, encoding='utf-8').read()
    s = fn(s)
    open(p, 'w', encoding='utf-8').write(s)
    if os.path.exists(dst): os.remove(dst)
    # le fichier mimetype doit être le premier, non compressé
    with zipfile.ZipFile(dst, 'w') as z:
        z.write(os.path.join(tmp, 'mimetype'), 'mimetype', compress_type=zipfile.ZIP_STORED)
        for root, _, files in os.walk(tmp):
            for f in files:
                full = os.path.join(root, f); rel = os.path.relpath(full, tmp)
                if rel == 'mimetype': continue
                z.write(full, rel, compress_type=zipfile.ZIP_DEFLATED)
    shutil.rmtree(tmp)
