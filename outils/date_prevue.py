#!/usr/bin/env python3
"""⚙ Réglages : bouton « Prévue » à côté de chaque leçon (25/11/2026, demande de l'enseignante : corriger une date après l'import d'un fichier d'ouvertures) :
remet la date prévue (début de la période de la ceinture, OUVERTURE_PREVUE). Rejouable ; à lancer après import_ouvertures.py. Usage : python3 outils/date_prevue.py"""
import pathlib
P = pathlib.Path(__file__).resolve().parent.parent / "index.html"
s = open(P, encoding="utf-8").read()
if 'data-rgp="' in s or "/*IMPORT-OUVERTURES*/" not in s:
    print("déjà posé ou import absent"); raise SystemExit
def une_fois(a, b):
    global s
    assert s.count(a) == 1, (a[:60], s.count(a)); s = s.replace(a, b, 1)
une_fois('<button type="button" data-rgo="${c}">Ouvrir</button><button type="button" data-rgf="${c}">Fermer</button>',
         '<button type="button" data-rgo="${c}">Ouvrir</button><button type="button" data-rgf="${c}">Fermer</button><button type="button" data-rgp="${c}" title="Remettre la date prévue (début de la période de la ceinture)">Prévue</button>')
une_fois("  else if('rgld' in d){$('#rgFic').click();}",
         "  else if('rgp' in d){BROUILLON.dates=BROUILLON.dates||{};(BROUILLON.dates[nivReg]=BROUILLON.dates[nivReg]||{})[d.rgp]=(OUVERTURE_PREVUE[nivReg]||{})[d.rgp]||'';apres();}\n  else if('rgld' in d){$('#rgFic').click();}")
open(P, "w", encoding="utf-8").write(s); print("posé")
