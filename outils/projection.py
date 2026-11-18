#!/usr/bin/env python3
"""Cartes interactives de français au tableau (vidéoprojecteur), 18/11/2026, demande de l'enseignante :
mêmes réglages que les cartes de mathématiques (dépôt cartes-mentales-maths, outils-dev/projection.py). Rejouable sans effet.

  - titre de l'activité centré dans sa pastille (avant : collé en bas) ;
  - cartes d'activités : toute la largeur, même quand il y en a peu.
Bloc entre /*PROJECTION*/ et /*PROJECTION-FIN*/ à la fin de la feuille de style (ne pas le modifier à la main).
Usage : python3 outils/projection.py
"""
import pathlib, re

P = pathlib.Path(__file__).resolve().parent.parent / "index.html"
s = P.read_text(encoding="utf-8")
avant = s
CSS = ("/*PROJECTION*/"
       ".cu-cartes{grid-template-columns:repeat(auto-fit,minmax(min(100%,15rem),1fr))}"
       ".cu-titre{display:flex;align-items:center;padding-top:.12em;padding-bottom:.2em}"
       "/*PROJECTION-FIN*/\n")
s = re.sub(r"/\*PROJECTION\*/.*?/\*PROJECTION-FIN\*/\n", "", s, flags=re.S)
i = s.find("</style>\n</head>")
assert i > 0, "fin de la feuille de style introuvable"
s = s[:i] + CSS + s[i:]
if s != avant:
    P.write_text(s, encoding="utf-8")
print("index.html", "modifié" if s != avant else "déjà à jour")
