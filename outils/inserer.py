"""Met une ou plusieurs leçons dans le site (index.html).
Usage :  python3 inserer.py O1 O2 ...
Lit sortie/O1.json et sortie/O1_carte.jpeg (fabriqués par un script de lecons/).
Une leçon déjà présente est remplacée ; une nouvelle est ajoutée à la fin de sa liste."""
import json, base64, os, sys
D = os.path.dirname(os.path.abspath(__file__))
P = os.path.join(D, '..', 'index.html')
SORTIE = os.path.join(D, 'sortie')
ids = sys.argv[1:]
if not ids: sys.exit(__doc__)
b64 = lambda f: 'data:image/jpeg;base64,' + base64.b64encode(open(f, 'rb').read()).decode()
data = {i: json.load(open(os.path.join(SORTIE, f'{i}.json'))) for i in ids}
L = open(P, encoding='utf-8').read().split('\n')

def line_of(prefix):
    k = [n for n, l in enumerate(L) if l.startswith(prefix)]
    return k[0] if k else None

for i in ids:
    tr = json.dumps(data[i]['trace'], ensure_ascii=False) + ','
    k = line_of('{"id": "' + i + '"')
    if k is not None: L[k] = tr
    else:
        k = line_of('/* ================= À venir')
        L[k:k] = [f'/* ================= {i} ================= */', tr]
    le = f'{i}:' + json.dumps(data[i]['lesson'], ensure_ascii=False)
    k = line_of(i + ':{')
    if k is not None:
        L[k] = le + (',' if L[k].rstrip().endswith(',') else '')
    else:
        # dernière leçon : la ligne juste avant « }; » qui précède le « Moteur »
        m = line_of('/* ---------- Moteur')
        end = max(n for n in range(m) if L[n].startswith('};'))
        L[end - 1] = L[end - 1].rstrip().rstrip(',') + ','
        L.insert(end, le)
k = line_of('const IMG=')
IMG = json.loads(L[k][len('const IMG='):].rstrip().rstrip(';'))
for i in ids: IMG[i] = {'carte': b64(os.path.join(SORTIE, f'{i}_carte.jpeg')), 'girl': IMG['G2']['girl'], 'boy': IMG['G2']['boy']}
L[k] = 'const IMG=' + json.dumps(IMG) + ';'
k = line_of('const PLUS=')
PL = json.loads(L[k][len('const PLUS='):].rstrip().rstrip(';'))
for i in ids: PL[i] = data[i]['plus']
L[k] = 'const PLUS=' + json.dumps(PL, ensure_ascii=False) + ';'
open(P, 'w', encoding='utf-8').write('\n'.join(L))
print('mis dans le site :', ', '.join(ids))
print('Penser : nouvelle famille → FAMILLES ; période → PERIODE_CEINTURE (dans index.html).')
