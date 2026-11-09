"""Petit conjugueur (présent, futur, imparfait, participe passé, passé composé, plus-que-parfait, passé simple) pour fabriquer des exercices justes.
Personnes : 0 je, 1 tu, 2 il/elle, 3 nous, 4 vous, 5 ils/elles."""
import random
VOY = 'aeiouyéèêàâîïôûhAEIOUH'
IRR = {  # présent, radical du futur, radical de l'imparfait, participe passé, passé simple (3 personnes utiles : 2, 5), auxiliaire
 'être':   dict(pr=['suis','es','est','sommes','êtes','sont'], fu='ser', im='ét', pp='été', ps=['fut','furent'], aux='avoir'),
 'avoir':  dict(pr=['ai','as','a','avons','avez','ont'], fu='aur', im='av', pp='eu', ps=['eut','eurent'], aux='avoir'),
 'aller':  dict(pr=['vais','vas','va','allons','allez','vont'], fu='ir', im='all', pp='allé', ps=['alla','allèrent'], aux='être'),
 'faire':  dict(pr=['fais','fais','fait','faisons','faites','font'], fu='fer', im='fais', pp='fait', ps=['fit','firent'], aux='avoir'),
 'dire':   dict(pr=['dis','dis','dit','disons','dites','disent'], fu='dir', im='dis', pp='dit', ps=['dit','dirent'], aux='avoir'),
 'venir':  dict(pr=['viens','viens','vient','venons','venez','viennent'], fu='viendr', im='ven', pp='venu', ps=['vint','vinrent'], aux='être'),
 'pouvoir':dict(pr=['peux','peux','peut','pouvons','pouvez','peuvent'], fu='pourr', im='pouv', pp='pu', ps=['put','purent'], aux='avoir'),
 'vouloir':dict(pr=['veux','veux','veut','voulons','voulez','veulent'], fu='voudr', im='voul', pp='voulu', ps=['voulut','voulurent'], aux='avoir'),
 'voir':   dict(pr=['vois','vois','voit','voyons','voyez','voient'], fu='verr', im='voy', pp='vu', ps=['vit','virent'], aux='avoir'),
 'prendre':dict(pr=['prends','prends','prend','prenons','prenez','prennent'], fu='prendr', im='pren', pp='pris', ps=['prit','prirent'], aux='avoir'),
}
ETRE_VERBES = {'aller', 'venir', 'arriver', 'partir', 'tomber', 'entrer', 'sortir', 'rester', 'monter', 'descendre'}
ER_PR = ['e', 'es', 'e', 'ons', 'ez', 'ent']
IR_PR = ['is', 'is', 'it', 'issons', 'issez', 'issent']
FU = ['ai', 'as', 'a', 'ons', 'ez', 'ont']
IM = ['ais', 'ais', 'ait', 'ions', 'iez', 'aient']
SPEC = {  # radicaux particuliers : (présent je/tu/il/ils, présent nous/vous, futur, imparfait)
 'lever':    ('lèv', 'lev', 'lèver', 'lev'),
 'acheter':  ('achèt', 'achet', 'achèter', 'achet'),
 'appeler':  ('appell', 'appel', 'appeller', 'appel'),
 'nettoyer': ('nettoi', 'nettoy', 'nettoier', 'nettoy'),
 'essuyer':  ('essui', 'essuy', 'essuier', 'essuy'),
 'manger':   ('mang', 'mang', 'manger', 'mange'),   # nous mangeons, imparfait mangeais
 'nager':    ('nag', 'nag', 'nager', 'nage'),
 'ranger':   ('rang', 'rang', 'ranger', 'range'),
 'commencer':('commenc', 'commenc', 'commencer', 'commenç'),
}
def groupe(v):
    if v in IRR: return 0
    return 2 if v.endswith('ir') else 1
def ger_cer(v, ending):
    """mangeons, mangeais, commençons, commençais : -ge-/-ç- devant a et o."""
    return ending[:1] in 'aoâ'
def pr(v, p):
    if v in IRR: return IRR[v]['pr'][p]
    g = groupe(v)
    if g == 2: return v[:-2] + IR_PR[p]
    if v in SPEC:
        a, b, _, _ = SPEC[v]
        r = a if p in (0, 1, 2, 5) else b
        if v in ('manger', 'ranger', 'nager'):
            r = v[:-2]
            return r + ('e' if p == 3 else '') + ER_PR[p]
        if v == 'commencer':
            return ('commenç' if p == 3 else 'commenc') + ER_PR[p]
        return r + ER_PR[p]
    return v[:-2] + ER_PR[p]
def fu(v, p):
    if v in IRR: return IRR[v]['fu'] + FU[p]
    g = groupe(v)
    if g == 2: return v + FU[p]
    if v in SPEC: return SPEC[v][2] + FU[p]
    return v + FU[p]
def im(v, p):
    if v in IRR: 
        r = IRR[v]['im']; return r + IM[p]
    g = groupe(v)
    if g == 2: return v[:-2] + 'iss' + IM[p]
    if v in ('manger', 'ranger', 'nager'): return v[:-2] + ('e' if p in (0, 1, 2, 5) else '') + IM[p]
    if v == 'commencer': return ('commenç' if p in (0, 1, 2, 5) else 'commenc') + IM[p]
    if v in SPEC: return SPEC[v][3] + IM[p]
    return v[:-2] + IM[p]
def pp(v, g='m', n=1):
    if v in IRR: b = IRR[v]['pp']
    elif groupe(v) == 2: b = v[:-2] + 'i'
    else: b = v[:-2] + 'é'
    if v in IRR: b = IRR[v]['pp']
    if g == 'f': b += 'e'
    if n > 1: b += 's'
    return b
def aux_de(v):
    return IRR[v]['aux'] if v in IRR else ('être' if v in ETRE_VERBES else 'avoir')
def aux_pr(a, p): return pr(a, p)
def aux_im(a, p): return im(a, p)
def pc(v, p, g='m', n=None):
    a = aux_de(v)
    plur = p in (3, 4, 5) if n is None else n > 1
    part = pp(v, g if a == 'être' else 'm', (2 if plur else 1) if a == 'être' else 1)
    return aux_pr(a, p) + ' ' + part
def pqp(v, p, g='m', n=None):
    a = aux_de(v)
    plur = p in (3, 4, 5) if n is None else n > 1
    part = pp(v, g if a == 'être' else 'm', (2 if plur else 1) if a == 'être' else 1)
    return aux_im(a, p) + ' ' + part
def ps(v, p):
    if v in IRR: 
        t = IRR[v]['ps']
        return t[0] if p == 2 else t[1]
    if groupe(v) == 2: return v[:-2] + ('it' if p == 2 else 'irent')
    return v[:-2] + ('a' if p == 2 else 'èrent')
def forme(v, t, p, g='m', n=None):
    return {'pr': pr, 'fu': fu, 'im': im}[t](v, p) if t in ('pr', 'fu', 'im') else (pc(v, p, g, n) if t == 'pc' else pqp(v, p, g, n) if t == 'pqp' else ps(v, p))
