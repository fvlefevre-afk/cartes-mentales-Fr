"""Joue toutes les animations et tous les exercices d'une ou plusieurs leçons, dans un vrai navigateur.
Usage :  python3 tester.py O1 O2 ...   (il faut Playwright et Chromium)"""
import os, re, sys
from playwright.sync_api import sync_playwright
f = 'file://' + os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'index.html'))
ids = sys.argv[1:] or sys.exit(__doc__)
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={'width': 1300, 'height': 900})
    errs = []; pg.on('pageerror', lambda e: errs.append(str(e)))
    bad = []; raw = []
    for lid in ids:
        pg.goto(f + '#t=' + lid); pg.wait_for_timeout(250)
        nz = pg.evaluate("document.querySelectorAll('.zone').length")
        n = ok = i = 0
        while True:
            pg.goto(f + f'#t={lid}/{i}'); pg.wait_for_timeout(120)
            if not pg.query_selector('.scr-head'): break
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
        print(f'{lid}: {nz} zones, {i} écrans, {ok}/{n} exercices réussis')
    print('exercices non réussis :', bad or 'aucun'); print('marques visibles :', raw or 'aucune'); print('erreurs :', errs or 'aucune')
    b.close()
