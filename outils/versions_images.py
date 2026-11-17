#!/usr/bin/env python3
"""Ajoute à chaque image de index.html une marque de version tirée de son contenu
(« images/G3-CM2.jpg?v=1a2b3c4d »).

Pourquoi : quand une carte est refaite, elle garde le même nom de fichier. Le navigateur
(ordinateur, tablette, téléphone) peut alors garder l'ancienne image en mémoire, alors que
la page, elle, est nouvelle : les cadres en pointillés ne tombent plus sur les cadres de la
carte (constaté le 17/11/2026 sur G3 CM2). Avec la marque, une image modifiée change
d'adresse et elle est rechargée ; une image inchangée garde la sienne (pas de téléchargement inutile).

Usage : python3 outils/versions_images.py [chemin/vers/index.html]
(sans argument : index.html de ce dépôt). Peut être relancé autant de fois qu'on veut.
Appelé tout seul par outils/publier-forge.sh sur la copie publiée."""
import hashlib, os, re, sys

ICI = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
page = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else os.path.join(ICI, 'index.html')
racine = os.path.dirname(page)
texte = open(page, encoding='utf-8').read()
manque, cache = set(), {}

def marque(m):
    chemin = m.group(1)
    if chemin not in cache:
        f = os.path.join(racine, chemin)
        if not os.path.isfile(f):
            manque.add(chemin); cache[chemin] = None
        else:
            cache[chemin] = hashlib.md5(open(f, 'rb').read()).hexdigest()[:8]
    v = cache[chemin]
    return m.group(0) if v is None else f'{chemin}?v={v}'

nouveau = re.sub(r'(images/[A-Za-z0-9_.\-]+\.(?:jpe?g|png|webp|svg))(?:\?v=[0-9a-f]+)?', marque, texte)
if nouveau != texte:
    open(page, 'w', encoding='utf-8').write(nouveau)
print(f'versions des images : {len([c for c in cache.values() if c])} images marquées'
      + (f' ; introuvables : {", ".join(sorted(manque))}' if manque else ''))
