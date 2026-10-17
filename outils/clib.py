T = lambda t: f'<span class="t">{t}</span>'
S = lambda t: f'<span class="s">{t}</span>'
def conj(rows, size=21):
    """rows: liste de (pronom, radical, terminaison)"""
    return f'<table class="cj" style="font-size:{size}px">' + ''.join(f'<tr><td>{p}</td><td>{r}{T(t)}</td></tr>' for p, r, t in rows) + '</table>'
