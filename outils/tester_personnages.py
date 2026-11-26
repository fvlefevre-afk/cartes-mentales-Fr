#!/usr/bin/env python3
"""Personnages des classes de mots (G3, G4, G7) : repérage des natures sur des phrases témoins, affichage dans « Je regarde », « Avec aide » (après réussite), jamais dans « Seul ».
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
    d = pathlib.Path(tempfile.mkdtemp()); (d / "t.html").write_text(s.replace(k, k + "setTimeout(()=>{window.__T={natures,naturesEcrites,persosPoser,phraseHTML,atoiTokens,LESSONS,PERSOS_PHRASES};},0);"), encoding="utf-8")
    b = p.chromium.launch(); pg = b.new_page(viewport={"width": 1280, "height": 800}); err = []
    pg.on("pageerror", lambda e: err.append(str(e)))
    import datetime; pg.clock.set_system_time(datetime.datetime(2027, 6, 1, 10, 0))   # toutes les leçons ouvertes
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
    # G4 et G7 : chaque phrase affichée des leçons (trois classes) est dans la table, et tous ses mots repérés reçoivent leur personnage
    pg.goto((d / "t.html").as_uri()); pg.wait_for_timeout(900)
    r = pg.evaluate(r"""()=>{ const T=window.__T, manque=[], mauvais=[]; let n=0, mots=0;
      for(const id of Object.keys(T.LESSONS).filter(k=>/^G[47](-|$)/.test(k))){ const c=id.slice(0,2), niv=id.endsWith('-CE2')?'CE2':id.endsWith('-CM2')?'CM2':'CM1', lv=niv==='CE2'?1:niv==='CM2'?3:2;
        const voir=(html,texte)=>{ const d=document.createElement('div'); if(html!==null) d.innerHTML=html; else d.textContent=texte; d.querySelectorAll('small,.sr-only').forEach(x=>x.remove());
          const avant=d.textContent, cle=avant.replace(/\s+/g,' ').trim(); if(!cle) return; n++; const ligne=T.PERSOS_PHRASES[c][cle]; if(ligne===undefined){ manque.push(id+' : '+cle); return; }
          const tous=T.naturesEcrites(avant,c,'CM2').length, vus=T.naturesEcrites(avant,c,niv); T.persosPoser(d,c,niv); const k=d.querySelectorAll('.mp img').length; mots+=k;
          if(tous!==ligne.split(' ').filter(Boolean).length||k!==vus.length||d.textContent!==avant) mauvais.push(id+' : '+cle+' ('+k+'/'+vus.length+'/'+tous+')'); };
        T.LESSONS[id].ecrans.forEach(e=>{ (e.steps||[]).forEach(s=>voir(T.phraseHTML(s.p),null));
          ((e.niv&&lv>1?e.niv[lv]:[e.atoi,...(e.plus||[])])||[]).forEach(a=>{ if(!a||!a.p) return; const F=(a.tasks||[]).filter(k=>k.choose&&k.fill).map(k=>k.choose[k.ok]); let f=0;
            voir(null,T.atoiTokens(a.p).map(x=>x.sp!=null?x.sp:x.blank?(F[f]!==undefined?F[f++]:'___'):x.t).join('')); }); }); }
      return {n,mots,manque,mauvais}; }""")
    ok(not r["manque"], f"G4 / G7 : les {r['n']} phrases affichées sont toutes repérées " + " ; ".join(r["manque"][:5]))
    ok(not r["mauvais"], f"G4 / G7 : {r['mots']} personnages posés sans changer le texte " + " ; ".join(r["mauvais"][:5]))
    t = pg.evaluate(r"""()=>{ const T=window.__T, f=(c,n,p)=>T.naturesEcrites(p,c,n).map(x=>p.slice(x.d,x.f)+'/'+x.n).join(' ');
      return [f('G4','CE2','Je voulais sortir mais il pleuvait.'), f('G4','CM1','Je voulais sortir mais il pleuvait.'), f('G4','CM1','Le chat dort sur le canapé.'), f('G4','CM2','Je reste parce qu’il pleut.'), f('G4','CM1','tu élèves · elles élèventdes élèves')]; }""")
    ok("mais/conj" not in t[0] and "mais/conj" in t[1], "G4 : pas de conjonction au CE2, oui au CM1")
    ok("/prep" not in t[2], "G4 : pas de préposition au CM1")
    ok(t[3] == "Je/pron reste/verbe il/pron pleut/verbe", "G4 : « parce que » sans personnage : " + t[3])
    ok(t[4] == "tu/pron élèves/verbe elles/pron élèvent/verbe des/det élèves/nom", "G4 : mots collés : " + t[4])
    for c, ecran in (("G4", "G4/1"), ("G7", "G7/0")):
        pg.goto(page_url + "#t=" + ecran); pg.wait_for_timeout(900)
        for _ in range(5):
            if "Avec aide" in pg.locator("#nextStep").inner_text(): break
            pg.locator("#nextStep").click(force=True); pg.wait_for_timeout(300)
        ok(pg.locator("#ph .mp img").count() >= 3, f"{c} « Je regarde » : personnages ({pg.locator('#ph .mp img').count()})")
        pg.locator(".cu-et").nth(2).click(force=True); pg.wait_for_timeout(500)
        ok(pg.locator("#atoi .mp").count() == 0, f"{c} « Seul » : aucun personnage")
    ok(not err, "aucune erreur : " + " | ".join(err[:3]))
    b.close()
print("Tout est bon." if not ko else f"{ko} problème(s)"); raise SystemExit(bool(ko))
