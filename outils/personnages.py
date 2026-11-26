#!/usr/bin/env python3
"""Met dans index.html le bloc /*PERSOS-JS*/…/*PERSOS-JS-FIN*/ : les dessins d'origine (outils/img/persos/*.png, réduits en WebP, dans la page : un seul fichier)
puis le code d'outils/personnages.js. À relancer après toute modification de l'un ou de l'autre (relance sans effet sinon)."""
import base64, io, json, pathlib, re
from PIL import Image
ICI = pathlib.Path(__file__).resolve().parent
FICHIERS = {"det":"determinant","nom":"nom","adj":"adjectif","verbe":"verbe","pron":"pronom-personnel","adv":"adverbe","conj":"conjonction","prep":"preposition","prel":"pronom-relatif","nompropre":"nom-propre","nomcommun":"nom-commun"}
def dessin(nom):
    im = Image.open(ICI/"img"/"persos"/(nom+".png")).convert("RGBA"); im = im.crop(im.getbbox()); im.thumbnail((400, 240), Image.LANCZOS)
    b = io.BytesIO(); im.save(b, "WEBP", quality=85, method=6)
    return "data:image/webp;base64," + base64.b64encode(b.getvalue()).decode()
bloc = ("/*PERSOS-JS*/\nconst PERSOS_DEF=" + json.dumps({k: dessin(v) for k, v in FICHIERS.items()}, separators=(",", ":")) + ";\n"
        + (ICI/"personnages.js").read_text(encoding="utf-8") + "/*PERSOS-JS-FIN*/\n")
p = ICI.parent/"index.html"; s = p.read_text(encoding="utf-8")
s = re.sub(r"/\*PERSOS-JS\*/\n.*?/\*PERSOS-JS-FIN\*/\n", "", s, flags=re.S)
ancre = "/* Couleurs des classes de mots (17/11/2026"
assert s.count(ancre) == 1
i = s.index(ancre); p.write_text(s[:i] + bloc + s[i:], encoding="utf-8")
print("personnages : bloc posé (%d Ko)" % (len(bloc)//1024))
