"""Joue toutes les animations et tous les exercices des leçons, dans un vrai navigateur.
Usage :  python3 tester.py O1 G4-CE2 ...   (quelques leçons)
         python3 tester.py tout            (toutes les leçons des trois classes, CE2, CM1, CM2)
         python3 tester.py tout CE2        (toutes les leçons d'une classe)
Il faut Playwright (pour Python) et Chromium.
La date du navigateur est mise en fin d'année scolaire : toutes les leçons sont ouvertes, même celles
dont la date d'ouverture n'est pas encore arrivée.
Vérifie aussi : la carte et les personnages s'affichent (dossier images/), la carte a des zones, la leçon a des écrans.
Chaque écran : l'animation (Je regarde), puis les séries « Avec aide », « Seul » et « Je corrige » (présentation du 14/11/2026, 4 étapes).
Termine par « TOUT EST BON » ou par la liste des problèmes (et un code d'erreur)."""
import datetime, os, re, sys
from playwright.sync_api import sync_playwright

f = 'file://' + os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'index.html'))
args = sys.argv[1:] or sys.exit(__doc__)
auj = datetime.date.today()
fin_annee = datetime.datetime(auj.year + (1 if auj.month >= 7 else 0), 6, 30, 12)   # 30 juin de l'année scolaire en cours

IMAGES_OK = "[...document.querySelectorAll('.sheet img')].every(i=>i.complete&&i.naturalWidth>0)"

with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={'width': 1300, 'height': 900}, reduced_motion='reduce')   # pas d'animation : sinon Playwright juge les boutons « instables »
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
            if not pg.query_selector('#main .cu-et'): break          # plus d'écran : la page n'a plus la barre des 4 étapes (présentation du 14/11/2026)
            if not pg.evaluate(IMAGES_OK): pb.append(f'{lid} écran {i} : personnage absent')
            # étape 1, Je regarde : l'animation pas à pas
            while pg.is_visible('#nextStep'):
                t = pg.inner_text('#ph')
                if re.search(r'[\[\]{}^~%#|*§]', re.sub(r'\[[^\[\]\s*%|§^~#{}]{1,4}\]', '', t)): raw.append((lid, i, t))   # marque restée visible (un son noté [é], [sjɔ̃] n'en est pas une)
                pg.click('#nextStep'); pg.wait_for_timeout(40)
            # étapes 2 à 4 : Avec aide, Seul, Je corrige ; chaque exercice est joué jusqu'à « fait » (CartesExo.derniere, bibliothèque commune)
            for etape in ('Avec aide', 'Seul', 'Je corrige'):
                bt = pg.locator('#main .cu-et', has_text=etape).first
                if not bt.count() or bt.is_disabled(): continue
                pg.goto(f + f'#t={lid}/{i}'); pg.wait_for_timeout(100)
                bt = pg.locator('#main .cu-et', has_text=etape).first; bt.click(); pg.wait_for_timeout(150)
                vus = 0
                while vus < 14:
                    fait = lambda: pg.evaluate("(() => { const s = CartesExo.derniere; return !!(s && s.cur() && s.cur().fait); })()")
                    for _ in range(6):
                        if fait(): break
                        mots = pg.query_selector_all('#choices .mot:not(.used)')     # remets les mots dans l'ordre : data-n = place dans la phrase
                        if mots:
                            for k in sorted(int(m.get_attribute('data-n')) for m in mots):
                                pg.click(f'#choices .mot[data-n="{k}"]:not(.used)'); pg.wait_for_timeout(30)
                            pg.wait_for_timeout(250); continue
                        sa = pg.query_selector('#saisie')                              # dictée à trous : la réponse est dans data-attendu
                        if sa and sa.is_visible():
                            sa.fill(sa.get_attribute('data-attendu')); pg.click('#valSaisie'); pg.wait_for_timeout(300); continue
                        ch = pg.query_selector_all('#choices .choice')
                        if ch:
                            for c in ch:
                                if fait(): break
                                try: c.click(timeout=1500)
                                except Exception: continue
                                pg.wait_for_timeout(350)
                                if 'right' in (c.get_attribute('class') or '') or fait(): break
                            continue
                        for tk in pg.query_selector_all('#tok .tk:not(.found)'):
                            try: tk.click(timeout=1500)
                            except Exception: continue
                            pg.wait_for_timeout(30)
                            if fait(): break
                    n += 1; vus += 1
                    if fait(): ok += 1
                    else:
                        bad.append((lid, i, etape, pg.inner_text('#exNum'), pg.inner_text('#ask'))); break
                    if pg.query_selector('#atoi .after'): break                       # fin de la série (bilan, « Refaire une série »)
                    pg.evaluate("CartesExo.derniere.autre()"); pg.wait_for_timeout(120)  # sans attendre le passage automatique (1,6 s)
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
