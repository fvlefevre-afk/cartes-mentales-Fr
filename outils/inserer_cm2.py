"""Met les écrans CM2 en plus (sortie/CM2_PLUS.json, fabriqué par lecons/cm2_ajouts.py) dans index.html.
Usage :  python3 inserer_cm2.py"""
import json, os
D = os.path.dirname(os.path.abspath(__file__))
P = os.path.join(D, '..', 'index.html')
data = json.load(open(os.path.join(D, 'sortie', 'CM2_PLUS.json')))
L = open(P, encoding='utf-8').read().split('\n')
line = 'const CM2_PLUS=' + json.dumps(data, ensure_ascii=False) + ';'
k = [n for n, l in enumerate(L) if l.startswith('const CM2_PLUS=')]
if k: L[k[0]] = line
else:
    j = [n for n, l in enumerate(L) if l.startswith('const CM2_COPIE=')][0]
    L.insert(j, line)
open(P, 'w', encoding='utf-8').write('\n'.join(L))
print('écrans CM2 mis dans le site :', sum(len(v['ecrans']) for v in data.values()))
