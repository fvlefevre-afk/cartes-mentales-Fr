def R(t): return f'<span class="rond">{t}</span>'
A='<span class="arrow">→</span>'
def rows(items, pr=0, lab="Je prouve"):
    out=''
    for mot, expl, ast, ex in items:
        out += f'<div class="hrow" style="padding-right:{pr}px">{R(mot)} {expl}<span class="ast">{lab} : {ast}</span><span class="exl">{ex.replace('→', A)}</span></div>'
    return out
def table(pairs):
    return '<table class="tr">'+''.join(f'<tr><td style="width:90px">{R(a)}</td><td>{b.replace("→", A)}</td></tr>' for a,b in pairs)+'</table>'
