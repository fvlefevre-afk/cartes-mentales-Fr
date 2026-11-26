#!/usr/bin/env python3
"""Personnages des classes de mots (G3) : repérage des natures sur des phrases témoins, affichage dans « Je regarde », « Avec aide » (après réussite), jamais dans « Seul ».
Usage : python3 outils/tester_personnages.py"""
import pathlib
from playwright.sync_api import sync_playwright
page_url = (pathlib.Path(__file__).resolve().parent.parent / "index.html").as_uri()
TEMOINS = {"le petit chat noir": "det adj nom adj", "Elle ouvre la porte lourde.": "- - det nom adj", "Maya porte une écharpe douce.": "nom - det nom adj",
  "Une barque carrée flotte.": "det nom adj -", "La petite souris grise court.": "det adj nom adj -", "de beaux légumes": "det adj nom", "une tasse à café": "det nom - nom",
  "Le long du chemin": "- - det nom", "Cette fleur sent bon.": "det nom - -", "Hugo lit un journal.": "nom - det nom", "Un énorme chien noir.": "det adj nom adj"}
ko = 0
def ok(c, m):
    global ko; print(("✓ " if c else "✗ ") + m); ko += not c
with sync_playwright() as p:
    s = pathlib.Path(__file__).resolve().parent.parent.joinpath("index.html").read_text(encoding="utf-8")
    k = "const KEY='traces-ecrites-cm1-v1';"
    import tempfile
    d = pathlib.Path(tempfile.mkdtemp()); (d / "t.html").write_text(s.replace(k, k + "setTimeout(()=>{window.__T={natures};},0);"), encoding="utf-8")
    b = p.chromium.launch(); pg = b.new_page(viewport={"width": 1280, "height": 800}); err = []
    pg.on("pageerror", lambda e: err.append(str(e)))
    pg.goto((d / "t.html").as_uri()); pg.wait_for_timeout(900)
    for ph, att in TEMOINS.items():
        r = pg.evaluate("t=>__T.natures(t).filter(x=>/[A-Za-zÀ-ÿ]/.test(x.mot)).map(x=>x.n||'-').join(' ')", ph)
        ok(r == att, f"{ph} : {r}" + ("" if r == att else f" (attendu {att})"))
    pg.goto(page_url + "#t=G3/0"); pg.wait_for_timeout(900)
    for _ in range(3): pg.locator("#nextStep").click(force=True); pg.wait_for_timeout(400)
    ok(pg.locator("#ph .mp img").count() == 4, "Je regarde : 4 personnages sous « le petit chat noir »")
    ok(pg.evaluate("document.querySelector('#ph').textContent.replace(/\\s+/g,' ').trim()") == "le petit chat noir", "la phrase garde son texte")
    pg.locator("#nextStep").click(force=True); pg.wait_for_timeout(700)
    ok(pg.locator("#atoi .mp").count() == 0, "Avec aide : pas de personnage avant la réponse")
    pg.evaluate("document.querySelectorAll('#tok .tk').forEach(b=>b.click())"); pg.wait_for_timeout(700)
    ok(pg.locator("#tok .mp img").count() >= 2, "Avec aide : personnages après la réussite")
    pg.locator(".cu-et").nth(2).click(force=True); pg.wait_for_timeout(700)
    pg.evaluate("document.querySelectorAll('#tok .tk').forEach(b=>b.click())"); pg.wait_for_timeout(500)
    ok(pg.locator("#atoi .mp").count() == 0, "Seul : jamais de personnage, même après la réussite")
    pg.goto(page_url + "#t=G4/0"); pg.wait_for_timeout(900); pg.locator("#nextStep").click(force=True); pg.wait_for_timeout(300)
    ok(pg.locator(".mp").count() == 0, "G4 : pas encore de personnage")
    ok(not err, "aucune erreur : " + " | ".join(err[:3]))
    b.close()
print("Tout est bon." if not ko else f"{ko} problème(s)"); raise SystemExit(bool(ko))
