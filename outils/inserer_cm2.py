"""Met les écrans CM2 en plus (sortie/CM2_PLUS.json, fabriqué par lecons/cm2_ajouts.py) dans index.html.
Usage :  python3 inserer_cm2.py        (CM2)
         python3 inserer_cm2.py CE2    (CE2 : sortie/CE2_PLUS.json, fabriqué par lecons/ce2_ajouts.py)"""
import json, os, sys
NIV = (sys.argv[1:] or ['CM2'])[0]
D = os.path.dirname(os.path.abspath(__file__))
P = os.path.join(D, '..', 'index.html')
data = json.load(open(os.path.join(D, 'sortie', f'{NIV}_PLUS.json')))
L = open(P, encoding='utf-8').read().split('\n')
line = f'const {NIV}_PLUS=' + json.dumps(data, ensure_ascii=False) + ';'
k = [n for n, l in enumerate(L) if l.startswith(f'const {NIV}_PLUS=')]
if k: L[k[0]] = line
else:
    j = [n for n, l in enumerate(L) if l.startswith('const CM2_COPIE=')][0]
    L.insert(j, line)
open(P, 'w', encoding='utf-8').write('\n'.join(L))
print(f'écrans {NIV} mis dans le site :', sum(len(v['ecrans']) for v in data.values()))
