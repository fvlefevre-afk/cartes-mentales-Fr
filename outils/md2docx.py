import re, sys, html, shutil, os, subprocess
src, base_dir, out = sys.argv[1], sys.argv[2], sys.argv[3]
lines = open(src, encoding='utf-8').read().split('\n')
# saute l'en-tête YAML
if lines[0] == '---':
    k = lines.index('---', 1); title = re.search(r'title: "(.*)"', '\n'.join(lines[:k])).group(1); lines = lines[k+1:]
E = lambda t: html.escape(t, quote=False).replace("'", '&apos;')
def runs(t, base_b=False, ital=False):
    out = ''
    for i, part in enumerate(re.split(r'\*\*(.+?)\*\*', t)):
        if not part: continue
        b = (i % 2 == 1) or base_b
        out += (f'<w:r><w:rPr>{"<w:b/><w:bCs/>" if b else "<w:b w:val=\"false\"/><w:bCs w:val=\"false\"/>"}'
                f'{"<w:i/><w:iCs/>" if ital else "<w:i w:val=\"false\"/><w:iCs w:val=\"false\"/>"}</w:rPr><w:t xml:space="preserve">{E(part)}</w:t></w:r>')
    return out
P = lambda t, after=160, ital=False: f'<w:p><w:pPr><w:spacing w:after="{after}"/></w:pPr>{runs(t, ital=ital)}</w:p>'
H1 = lambda t: f'<w:p><w:pPr><w:pStyle w:val="Heading1"/><w:spacing w:after="160" w:before="360"/></w:pPr><w:r><w:t xml:space="preserve">{E(t)}</w:t></w:r></w:p>'
LI = lambda t: f'<w:p><w:pPr><w:pStyle w:val="ListParagraph"/><w:numPr><w:ilvl w:val="0"/><w:numId w:val="2"/></w:numPr><w:spacing w:after="100"/></w:pPr>{runs(t)}</w:p>'
MAR = '<w:tcMar><w:top w:type="dxa" w:w="70"/><w:left w:type="dxa" w:w="90"/><w:bottom w:type="dxa" w:w="70"/><w:right w:type="dxa" w:w="90"/></w:tcMar>'
def table(rows):
    n = len(rows[0]); total = 9906
    lens = [max(max(len(r[i]) for r in rows[1:]) if len(rows) > 1 else 1, max(len(x) for x in rows[0][i].split()) * 1.6, 5) ** 0.75 for i in range(n)]
    w = [int(total * l / sum(lens)) for l in lens]; w[-1] = total - sum(w[:-1])
    x = ('<w:tbl><w:tblPr><w:tblW w:type="dxa" w:w="9906"/><w:tblBorders>' + ''.join(f'<w:{b} w:val="single" w:color="auto" w:sz="4"/>' for b in ['top','left','bottom','right','insideH','insideV']) +
         '</w:tblBorders></w:tblPr><w:tblGrid>' + ''.join(f'<w:gridCol w:w="{c}"/>' for c in w) + '</w:tblGrid>')
    for ri, r in enumerate(rows):
        x += '<w:tr>' + ('<w:trPr><w:tblHeader/></w:trPr>' if ri == 0 else '')
        for ci, c in enumerate(r):
            shd = '<w:shd w:fill="D9E2F3" w:val="clear"/>' if ri == 0 else ''
            x += f'<w:tc><w:tcPr><w:tcW w:type="dxa" w:w="{w[ci]}"/>{shd}{MAR}</w:tcPr><w:p><w:pPr><w:spacing w:after="40"/></w:pPr>{runs(c, base_b=(ri == 0))}</w:p></w:tc>'
        x += '</w:tr>'
    return x + '</w:tbl><w:p><w:pPr><w:spacing w:after="120"/></w:pPr></w:p>'
body = f'<w:p><w:pPr><w:pStyle w:val="Title"/></w:pPr><w:r><w:t xml:space="preserve">{E(title)}</w:t></w:r></w:p>'
i = 0; first = True
while i < len(lines):
    l = lines[i].rstrip()
    if not l: i += 1; continue
    if l.startswith('# '): body += H1(l[2:]); i += 1; continue
    if l.startswith('|'):
        rows = []
        while i < len(lines) and lines[i].startswith('|'):
            cells = [c.strip() for c in lines[i].strip().strip('|').split('|')]
            if not all(re.fullmatch(r'-+', c) for c in cells): rows.append(cells)
            i += 1
        body += table(rows); continue
    if l.startswith('- '): body += LI(l[2:]); i += 1; continue
    if first and l == 'Classe de CM1':
        body += f'<w:p><w:pPr><w:pStyle w:val="Heading2"/><w:spacing w:after="200"/></w:pPr><w:r><w:t xml:space="preserve">Classe de CM1</w:t></w:r></w:p>'; i += 1; continue
    body += P(l, ital=first and l.startswith('Version')); i += 1
    if l.startswith('Version'): first = False
doc = open(os.path.join(base_dir, 'word/document.xml'), encoding='utf-8').read()
a = doc.index('<w:body>') + len('<w:body>'); b = doc.index('<w:sectPr')
open(os.path.join(base_dir, 'word/document.xml'), 'w', encoding='utf-8').write(doc[:a] + body + doc[b:])
if os.path.exists(out): os.remove(out)
subprocess.run(['zip', '-qXr', os.path.abspath(out), '.'], cwd=base_dir, check=True)
print('ok', out)
