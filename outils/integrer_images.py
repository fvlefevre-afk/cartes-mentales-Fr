#!/usr/bin/env python3
"""Met les images des cartes et la police Andika DANS index.html (17/11/2026, demande de l'enseignante :
« comme pour les maths, ne pas avoir de fichier supplémentaire autre que index pour fonctionner »).

Les outils continuent de travailler comme avant : les cartes sont fabriquées dans images/<id>.jpg et
l'objet IMG de index.html garde leur CHEMIN (« images/G3-CM2.jpg »). Ce script ajoute, juste après la
ligne `const IMG=`, un bloc

    /*IMAGES-INTEGREES*/const IMG_DATA={"images/G3-CM2.jpg":"data:image/webp;base64,…",…};…/*IMAGES-INTEGREES-FIN*/

qui remplace, au chargement de la page, chaque chemin par l'image elle-même. Les images sont
recompressées en WebP (qualité 82) : 12 Mo de JPEG → ~5 Mo. La police (url(polices/…)) est intégrée de même.

À relancer après tout changement d'une image (carte refaite, nouvelle leçon) : il est appelé tout seul à la fin
de inserer.py, inserer_cm2.py, lecons/g_cartes.py, lecons/g2_cartes.py, lecons/g3_cartes.py et par publier-forge.sh ;
outils/tester.py signale un bloc qui n'est plus à jour.

Usage : python3 outils/integrer_images.py [chemin/vers/index.html]      (sans argument : index.html de ce dépôt)
        python3 outils/integrer_images.py --verifier                    (dit seulement s'il est à jour ; code 1 sinon)"""
import base64, hashlib, io, json, os, re, sys

ICI = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
args = [a for a in sys.argv[1:] if not a.startswith('--')]
VERIFIER = '--verifier' in sys.argv
page = os.path.abspath(args[0]) if args else os.path.join(ICI, 'index.html')
racine = os.path.dirname(page)
DEBUT, FIN = '/*IMAGES-INTEGREES*/', '/*IMAGES-INTEGREES-FIN*/'
QUALITE = 82
CACHE = os.path.join(ICI, 'outils', 'sortie', 'images-webp')     # conversions déjà faites (même image = même résultat, plus rapide)

def webp(chemin):
    brut = open(chemin, 'rb').read()
    cle = hashlib.md5(brut).hexdigest() + f'-q{QUALITE}'
    f = os.path.join(CACHE, cle + '.webp')
    if os.path.isfile(f):
        return open(f, 'rb').read()
    from PIL import Image
    im = Image.open(io.BytesIO(brut))
    if im.mode not in ('RGB', 'RGBA'):
        im = im.convert('RGBA' if 'A' in im.getbands() or 'transparency' in im.info else 'RGB')
    b = io.BytesIO(); im.save(b, 'WEBP', quality=QUALITE, method=6)
    os.makedirs(CACHE, exist_ok=True); open(f, 'wb').write(b.getvalue())
    return b.getvalue()

texte = open(page, encoding='utf-8').read()
lignes = texte.split('\n')
k = next(i for i, l in enumerate(lignes) if 'const IMG=' in l and DEBUT not in l)

# 1. IMG garde des chemins simples (plus de « ?v=… » : une image intégrée change avec la page)
lignes[k] = re.sub(r'(images/[A-Za-z0-9_.\-]+)\?v=[0-9a-f]+', r'\1', lignes[k])
IMG = json.loads(lignes[k].split('const IMG=', 1)[1].rstrip().rstrip(';'))
chemins = sorted({c for d in IMG.values() for c in d.values() if isinstance(c, str) and c.startswith('images/')})

# 2. bloc des images
manque, data = [], {}
for c in chemins:
    f = os.path.join(racine, c)
    if not os.path.isfile(f):
        manque.append(c); continue
    data[c] = 'data:image/webp;base64,' + base64.b64encode(webp(f)).decode()
bloc = (DEBUT + 'const IMG_DATA=' + json.dumps(data, separators=(',', ':')) + ';'
        'for(const k in IMG)for(const c in IMG[k]){const d=IMG_DATA[IMG[k][c]];if(d)IMG[k][c]=d;}' + FIN)
if k + 1 < len(lignes) and lignes[k + 1].startswith(DEBUT):
    lignes[k + 1] = bloc
else:
    lignes.insert(k + 1, bloc)

# 2 bis. cartes en HTML pour la loupe (19/11/2026, demande de l'enseignante : « le texte n'est plus très net quand un cadre s'affiche en grand ») :
# cartes-html/<id>.html = la page qui a servi à photographier images/<id>.jpg (gardée par lecons/g_cartes.py, g2_cartes.py, g3_cartes.py).
# La loupe affiche le cadre redessiné en vrai texte (net à toute taille) ; une carte sans HTML (H1, V1, V2, dessinées) garde la photo agrandie.
DEB2, FIN2 = '/*CARTES-HTML*/', '/*CARTES-HTML-FIN*/'
HT, HIMG = {}, {}
dossier_html = os.path.join(ICI, 'cartes-html')
def fichier_img(m):
    chemin = m.group(1); rel = re.sub(r'^.*?/(outils/|images/)', r'\1', chemin)
    f = os.path.join(ICI, rel)
    if not os.path.isfile(f): manque.append(rel); return m.group(0)
    if rel not in HIMG: HIMG[rel] = 'data:image/webp;base64,' + base64.b64encode(webp(f)).decode()
    return 'src="@@' + rel + '@@"'
if os.path.isdir(dossier_html):
    for nom in sorted(os.listdir(dossier_html)):
        if not nom.endswith('.html'): continue
        c = 'images/' + nom[:-5] + '.jpg'
        if c not in chemins: continue
        h = open(os.path.join(dossier_html, nom), encoding='utf-8').read()
        h = re.sub(r'src="file://([^"]+)"', fichier_img, h)
        h = re.sub(r'url\(file://[^)]*?/(polices/[^)]+)\)', r'url(@@\1@@)', h)
        h = re.sub(r'\n\s*', '\n', h)
        HT[c] = h
bloc2 = DEB2 + 'const CARTE_HTML=' + json.dumps(HT, ensure_ascii=False, separators=(',', ':')) + ',CARTE_HTML_IMG=' + json.dumps(HIMG, separators=(',', ':')) + ';' + FIN2
if k + 2 < len(lignes) and lignes[k + 2].startswith(DEB2):
    lignes[k + 2] = bloc2
else:
    lignes.insert(k + 2, bloc2)
nouveau = '\n'.join(lignes)

# 3. police : url(polices/x.woff2) → url(data:…)/*polices/x.woff2*/ (le commentaire permet de la refaire)
def police(m):
    nom = m.group(1) or m.group(2)
    f = os.path.join(racine, nom)
    if not os.path.isfile(f):
        manque.append(nom); return m.group(0)
    return f'url(data:font/woff2;base64,{base64.b64encode(open(f, "rb").read()).decode()})/*{nom}*/'
nouveau = re.sub(r'url\(data:font/woff2;base64,[A-Za-z0-9+/=]+\)/\*(polices/[^*]+)\*/|url\((polices/[^)]+)\)', police, nouveau)

if VERIFIER:
    ok = nouveau == texte
    print('images intégrées : à jour' if ok else 'images intégrées : PAS À JOUR, lancer python3 outils/integrer_images.py')
    sys.exit(0 if ok else 1)
if nouveau != texte:
    open(page, 'w', encoding='utf-8').write(nouveau)
print(f'images intégrées dans {os.path.basename(page)} : {len(data)} images, {len(HT)} cartes en HTML pour la loupe, page de {len(nouveau.encode())/1e6:.1f} Mo'
      + (f' ; introuvables : {", ".join(manque)}' if manque else ''))
