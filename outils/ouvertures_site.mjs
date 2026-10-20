#!/usr/bin/env node
/* Dates d'ouverture prévues des leçons (OUVERTURE_PREVUE dans index.html), comme pour le site de maths (20/10/2026).
   Date prévue = premier jour de la période de la ceinture (colonne « Période » du fichier « Langue - ceintures »), pour chaque niveau
   concerné (colonne « Niveaux »), d'après le calendrier du tableau de bord (dépôt « ressources », branche branche-propre, modèle
   « Fichiers à déposer/Langue - ceintures-1.odt », classe de test CE2 + CM1 + CM2).
   Les dates jour par jour viennent du fichier ouvertures.json fabriqué par le tableau de bord (Planning › Français (année),
   bouton « Leçons ouvertes sur le site de français ») : il est prioritaire. Pas la suite d'origine du tableau de bord ici : avec les
   réglages d'origine, elle prend du retard sur les périodes du dispositif (H6 à H8, O5, O6 ne commencent pas dans l'année).
   À relancer après tout changement du fichier « Langue - ceintures » ou du calendrier.
   Usage : node outils/ouvertures_site.mjs [chemin du dépôt ressources, par défaut ../ressources] */
import { dirname, join, resolve } from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";
import { execSync } from "node:child_process";
import { createRequire } from "node:module";
import { readFileSync, writeFileSync } from "node:fs";

const RACINE = join(dirname(fileURLToPath(import.meta.url)), "..");
const RESS = resolve(process.argv[2] || join(RACINE, "..", "ressources"));
async function chargerPlaywright(){
  try{ return await import("playwright"); }
  catch(e){ const g = execSync("npm root -g").toString().trim(); return createRequire(join(g, "x.js"))("playwright"); }
}
const { chromium } = await chargerPlaywright();
const navigateur = await chromium.launch(process.env.PW_CHROMIUM ? {executablePath: process.env.PW_CHROMIUM} : {});
const page = await navigateur.newPage();
const erreurs = [];
page.on("pageerror", e => erreurs.push(e.message));
page.on("dialog", d => d.accept());
await page.goto(pathToFileURL(join(RESS, "tableau-de-bord.html")).href);
await page.click('[data-v="creer"]');
await page.fill("#vMdp1", "girafe-crayon-orage-velo");
await page.fill("#vMdp2", "girafe-crayon-orage-velo");
await page.click('#vFormCreer button[type="submit"]');
await page.check("#vNote", {timeout: 30000});
await page.click("#vContinuer");
await page.waitForSelector("#verrou", {state: "hidden"});
await page.evaluate(`S.eleves[0].prenom = "A"; S.eleves[1].prenom = "B"; S.eleves[2].prenom = "C"; S.eleves[0].niveau = "CE2"; S.eleves[2].niveau = "CM2"; sauver(); rendre();`);
const modeles = ["Langue - ceintures-1.odt", "Langue - jeux.odt", "Langue - phrases.odt"]
  .map(f => [f, readFileSync(join(RESS, "Fichiers à déposer", f)).toString("base64")]);
const O = await page.evaluate(async M => { const acc = accConfLangue();
  for(const [nom, b64] of M){ const f = new File([Uint8Array.from(atob(b64), c => c.charCodeAt(0))], nom); analyserConfLangue(await lignesRessource(f, extRess(nom)), acc); }
  S.confLangue = reglageConfLangue({...confLangueDepuis(acc), src: acc.src, maj: isoDepuis(new Date())}); structSig = null; sauver(); rendre();
  return {per:ZONE_B.periodes, L:DOM_CODES.flatMap(dl=>repartLangue(dl).map(([c,p])=>[c, p, nivsStruct(dl, c)]))}; }, modeles);
await navigateur.close();
if(erreurs.length){ console.error(erreurs.join("\n")); process.exit(1); }
const P = {};
["CE2", "CM1", "CM2"].forEach(n => { P[n] = {};
  O.L.forEach(([c, p, nv]) => { const per = O.per[p-1]; if(per && (!nv.length || nv.includes(n))) P[n][c] = per[1]; }); });
const f = join(RACINE, "index.html"), s = readFileSync(f, "utf8");
const re = /(\/\* OUVERTURE_PREVUE[^\n]*\*\/\n)const OUVERTURE_PREVUE=[^\n]*\n/;
if(!re.test(s)){ console.error("Bloc OUVERTURE_PREVUE introuvable dans index.html"); process.exit(1); }
writeFileSync(f, s.replace(re, (m, c) => c + "const OUVERTURE_PREVUE=" + JSON.stringify(P) + ";\n"));
for(const n of ["CE2", "CM1", "CM2"]) console.log(n, Object.keys(P[n]).length, "ceintures :", Object.entries(P[n]).map(([c, d]) => c + " " + d.slice(5)).join(", "));
