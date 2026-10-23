"""Joue toutes les animations et tous les exercices des leçons, dans un vrai navigateur.
Usage :  python3 tester.py O1 G4-CE2 ...   (quelques leçons)
         python3 tester.py tout            (toutes les leçons des trois classes, CE2, CM1, CM2)
         python3 tester.py tout CE2        (toutes les leçons d'une classe)
Il faut Playwright (pour Python) et Chromium.
La date du navigateur est mise en fin d'année scolaire : toutes les leçons sont ouvertes, même celles
dont la date d'ouverture n'est pas encore arrivée.
Vérifie aussi : la carte et les personnages s'affichent (dossier images/), la carte a des zones, la leçon a des écrans.
Termine par « TOUT EST BON » ou par la liste des problèmes (et un code d'erreur)."""
import datetime, os, re, sys
from playwright.sync_api import sync_playwright

f = 'file://' + os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'index.html'))
args = sys.argv[1:] or sys.exit(__doc__)
auj = datetime.date.today()
fin_annee = datetime.datetime(auj.year + (1 if auj.month >= 7 else 0), 6, 30, 12)   # 30 juin de l'année scolaire en cours

IMAGES_OK = "[...document.querySelectorAll('.sheet img')].every(i=>i.complete&&i.naturalWidth>0)"

with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={'width': 1300, 'height': 900})
    pg.clock.set_system_time(fin_annee)
    errs = []; pg.on('pageerror', lambda e: errs.append(str(e)))
    manquants = []; pg.on('requestfailed', lambda r: manquants.append(r.url.rsplit('/', 1)[-1]))

    if args[0] == 'tout':   # leçons du sommaire de chaque classe
        ids = []
        for niv in (args[1:] or ['CE2', 'CM1', 'CM2']):
            pg.goto(f + '#niveau=' + niv); pg.wait_for_timeout(400)
            ids += pg.evaluate("[...new Set([...document.querySelectorAll('a[href^=\"#t=\"]')].map(a=>a.getAttribute('href').slice(3).split('/')[0]))]")
        ids = list(dict.fromkeys(ids))
    else:
        ids = args

    bad = []; raw = []; pb = []; total_ex = total_ok = 0
    for lid in ids:
        pg.goto(f + '#t=' + lid); pg.wait_for_timeout(250)
        if not pg.query_selector('.sheet.lesson'):
            pb.append(f'{lid} : la leçon ne s’ouvre pas'); print(f'{lid}: ne s’ouvre pas'); continue
        nz = pg.evaluate("document.querySelectorAll('.zone').length")
        if not nz: pb.append(f'{lid} : carte sans zone')
        if not pg.evaluate(IMAGES_OK): pb.append(f'{lid} : la carte ne s’affiche pas')
        n = ok = i = 0
        while True:
            pg.goto(f + f'#t={lid}/{i}'); pg.wait_for_timeout(120)
            if not pg.query_selector('.scr-head'): break
            if not pg.evaluate(IMAGES_OK): pb.append(f'{lid} écran {i} : personnage absent')
            while pg.is_visible('#nextStep'):
                t = pg.inner_text('#ph')
                if re.search(r'[\[\]{}^~%#|*§]', t): raw.append((lid, i, t))   # marque restée visible
                pg.click('#nextStep'); pg.wait_for_timeout(40)
            seen = 0
            while True:
                for _ in range(4):
                    if pg.query_selector('#atoi .after'): break
                    ch = pg.query_selector_all('#choices .choice')
                    if ch:
                        for c in ch:
                            c.click(); pg.wait_for_timeout(420)
                            if 'right' in (c.get_attribute('class') or ''): break
                    else:
                        for tk in pg.query_selector_all('#tok .tk:not(.found)'):
                            tk.click(); pg.wait_for_timeout(30)
                            if pg.query_selector('#atoi .after'): break
                n += 1
                if pg.query_selector('#atoi .after'): ok += 1
                else: bad.append((lid, i, pg.inner_text('#exNum'), pg.inner_text('#ask')))
                btn = pg.query_selector('.ex-autre'); seen += 1
                if not btn or seen >= 6: break
                btn.click(); pg.wait_for_timeout(120)
                if pg.inner_text('#exNum').startswith('· exercice 1 '): break
            i += 1
        if not i: pb.append(f'{lid} : aucun écran')
        total_ex += n; total_ok += ok
        print(f'{lid}: {nz} zones, {i} écrans, {ok}/{n} exercices réussis')
    b.close()

print(f'\n{len(ids)} leçons, {total_ok}/{total_ex} exercices réussis')
print('exercices non réussis :', bad or 'aucun')
print('marques visibles :', raw or 'aucune')
print('images introuvables :', sorted(set(manquants)) or 'aucune')
print('autres problèmes :', pb or 'aucun')
print('erreurs :', errs or 'aucune')
if bad or raw or manquants or pb or errs:
    print('À CORRIGER'); sys.exit(1)
print('TOUT EST BON')
