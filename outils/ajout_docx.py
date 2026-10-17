"""Ajoute (ou remplace) une partie à la fin d'un dispositif .docx, avec les styles du document.
Usage :  python3 ajout_docx.py <document.docx> <partie.md>
La partie commence par un titre « # … ». Si un titre identique existe déjà dans le document,
tout ce qui suit ce titre est remplacé (on peut relancer sans doublon).
Markdown accepté : # titre, ## sous-titre, - liste, | tableau |, **gras**, paragraphes."""
import re, sys, html, zipfile, shutil, os, tempfile
doc_path, md_path = sys.argv[1], sys.argv[2]
E = lambda t: html.escape(t, quote=False)

def runs(t, bold=False):
    out = ''
    for i, part in enumerate(re.split(r'\*\*(.+?)\*\*', t)):
        if part: out += f'<w:r>{"<w:rPr><w:b/><w:bCs/></w:rPr>" if (i % 2 or bold) else ""}<w:t xml:space="preserve">{E(part)}</w:t></w:r>'
    return out

def build(md, bullet_num):
    body = ''; lines = md.split('\n'); i = 0
    while i < len(lines):
        l = lines[i].rstrip()
        if not l: i += 1; continue
        if l.startswith('## '): body += f'<w:p><w:pPr><w:pStyle w:val="Heading2"/></w:pPr>{runs(l[3:])}</w:p>'
        elif l.startswith('# '): body += f'<w:p><w:pPr><w:pStyle w:val="Heading1"/></w:pPr>{runs(l[2:])}</w:p>'
        elif l.startswith('- '):
            body += f'<w:p><w:pPr><w:pStyle w:val="BodyText"/><w:numPr><w:ilvl w:val="0"/><w:numId w:val="{bullet_num}"/></w:numPr><w:spacing w:after="60"/></w:pPr>{runs(l[2:])}</w:p>'
        elif l.startswith('|'):
            rows = []
            while i < len(lines) and lines[i].startswith('|'):
                cells = [c.strip() for c in lines[i].strip().strip('|').split('|')]
                if not all(re.fullmatch(r'-+', c) for c in cells): rows.append(cells)
                i += 1
            n = len(rows[0]); lens = [max(len(r[k]) for r in rows) ** 0.7 + 3 for k in range(n)]
            w = [int(9600 * x / sum(lens)) for x in lens]
            t = ('<w:tbl><w:tblPr><w:tblW w:type="dxa" w:w="9600"/><w:tblBorders>' + ''.join(f'<w:{b} w:val="single" w:color="auto" w:sz="4"/>' for b in ['top', 'left', 'bottom', 'right', 'insideH', 'insideV'])
                 + '</w:tblBorders><w:tblCellMar><w:left w:w="80" w:type="dxa"/><w:right w:w="80" w:type="dxa"/></w:tblCellMar></w:tblPr><w:tblGrid>' + ''.join(f'<w:gridCol w:w="{x}"/>' for x in w) + '</w:tblGrid>')
            for ri, r in enumerate(rows):
                t += '<w:tr>' + ('<w:trPr><w:tblHeader/></w:trPr>' if ri == 0 else '')
                for k, c in enumerate(r):
                    shd = '<w:shd w:fill="D9E2F3" w:val="clear"/>' if ri == 0 else ''
                    t += f'<w:tc><w:tcPr><w:tcW w:type="dxa" w:w="{w[k]}"/>{shd}</w:tcPr><w:p><w:pPr><w:spacing w:before="20" w:after="20"/></w:pPr>{runs(c, bold=ri == 0)}</w:p></w:tc>'
                t += '</w:tr>'
            body += t + '</w:tbl><w:p/>'; continue
        else: body += f'<w:p><w:pPr><w:pStyle w:val="BodyText"/></w:pPr>{runs(l)}</w:p>'
        i += 1
    return body

md = open(md_path, encoding='utf-8').read().strip()
title = md.split('\n')[0][2:].strip()
tmp = tempfile.mkdtemp()
with zipfile.ZipFile(doc_path) as z:
    names = z.namelist(); z.extractall(tmp)
p = os.path.join(tmp, 'word', 'document.xml'); doc = open(p, encoding='utf-8').read()
num = open(os.path.join(tmp, 'word', 'numbering.xml'), encoding='utf-8').read() if 'word/numbering.xml' in names else ''
bullet = '1'
for n, a in re.findall(r'<w:num w:numId="(\d+)"[^>]*>\s*<w:abstractNumId w:val="(\d+)"', num):
    if re.search(r'<w:abstractNum [^>]*w:abstractNumId="' + a + r'".*?<w:numFmt w:val="bullet"', num, re.S): bullet = n; break
end = doc.rfind('<w:sectPr')
# ancienne version de la même partie : on la retire
paras = [m for m in re.finditer(r'<w:p\b[^>]*>(?:(?!</w:p>).)*?<w:pStyle w:val="Heading1"/>.*?</w:p>', doc, re.S)]
ins = end
for k, m in enumerate(paras):
    if re.sub(r'<[^>]+>', '', m.group(0)).strip() == title:
        # on retire la partie jusqu'au titre de niveau 1 suivant (ou la fin), puis on remet la nouvelle au même endroit
        stop = paras[k + 1].start() if k + 1 < len(paras) else end
        doc = doc[:m.start()] + doc[stop:]; ins = m.start(); break
doc = doc[:ins] + build(md, bullet) + doc[ins:]
open(p, 'w', encoding='utf-8').write(doc)
out = doc_path + '.tmp'
with zipfile.ZipFile(out, 'w') as z:
    for n in names:
        z.write(os.path.join(tmp, n), n, compress_type=zipfile.ZIP_STORED if n == 'mimetype' else zipfile.ZIP_DEFLATED)
shutil.move(out, doc_path); shutil.rmtree(tmp)
print('partie ajoutée :', title, '→', os.path.basename(doc_path))
