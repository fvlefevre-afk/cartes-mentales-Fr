#!/usr/bin/env python3
"""Import du fichier d'ouvertures dans ⚙ Réglages et le menu enseignant (25/11/2026, demande de l'enseignante, comme les cartes de maths) : remet ce que le commit
« plus de dates d'ouverture dans ouvertures.json » (10/11/2026) avait retiré : les dates du fichier PRIMENT sur les dates prévues (sans date, rien ne change),
« 📂 Charger ouvertures.json » (dates, école, photo, classes, couleurs), date de chaque leçon, Ouvrir / Fermer ; le fichier téléchargé ne contient que les dates
changées ou importées (jamais les dates prévues). Rejouable. Usage : python3 outils/import_ouvertures.py"""
import pathlib
P = pathlib.Path(__file__).resolve().parent.parent / "index.html"
s = open(P, encoding="utf-8").read()
if "/*IMPORT-OUVERTURES*/" in s:
    print("déjà posé"); raise SystemExit
def une_fois(a, b, nom):
    global s
    assert s.count(a) == 1, f"« {nom} » : {s.count(a)} fois"
    s = s.replace(a, b, 1)

une_fois("""/* date d'ouverture : la date prévue (début de la période de la ceinture) (10/11/2026, demande de l'enseignante : plus de dates dans ouvertures.json,
   plus de dépôt régulier ; en cas d'écart, la clé 🔑 ouvre tout sur l'appareil) */
const dateOuverture=t=>(OUVERTURE_PREVUE[niveauDe(t)]||{})[code(t)]||'';;""",
"""/*IMPORT-OUVERTURES*/
/* date d'ouverture : brouillon de l'onglet, puis ouvertures.json s'il porte une date pour cette leçon (une date vide = fermée), puis la date prévue (début de la période de la ceinture)
   (25/11/2026 : l'import du fichier du tableau de bord est revenu ; sans date dans le fichier, les dates prévues s'appliquent comme depuis le 10/11) */
const dateOuverture=t=>{const n=niveauDe(t),c=code(t);for(const src of [BROUILLON.dates,OUVERTURE_REELLE]){const r=(src||{})[n];if(r&&typeof r==='object'&&Object.prototype.hasOwnProperty.call(r,c))return r[c]||'';}return (OUVERTURE_PREVUE[n]||{})[c]||'';};""", "dateOuverture")

une_fois("const fichier=()=>{const out={maj:AUJ,classes:classesVis()},E=ecole(),C=couleursCl();if(E.nom||E.photo)out.ecole=E;if(Object.keys(C).length)out.couleurs=C;return JSON.stringify(out,null,1);};",
"""const fichier=()=>{const out={maj:AUJ,classes:classesVis()},E=ecole(),C=couleursCl();if(E.nom||E.photo)out.ecole=E;if(Object.keys(C).length)out.couleurs=C;
  NIVEAUX.forEach(n=>{const cles=new Set([...Object.keys((BROUILLON.dates||{})[n]||{}),...Object.keys(((OUVERTURE_REELLE||{})[n]&&typeof OUVERTURE_REELLE[n]==='object')?OUVERTURE_REELLE[n]:{})]),o={};
   ordreSommaire(n).filter(hasTrace).forEach(t=>{if(cles.has(code(t)))o[code(t)]=dateOuverture(t);});if(Object.keys(o).length)out[n]=o;});   /* jamais les dates prévues : seulement celles changées ou importées */
  return JSON.stringify(out,null,1);};""", "fichier")

une_fois("""  <p class="rg-note">Chaque leçon s'ouvre au début de la période de sa ceinture : rien à régler ni à déposer. En cas d'écart, la clé 🔑 ouvre toutes les leçons sur l'appareil.</p>""",
"""  <div class="rg-charge"><button type="button" data-rgld>📂 Charger ouvertures.json</button><input type="file" id="rgFic" accept=".json,application/json" hidden><span>Reprend le fichier fabriqué par le tableau de bord (ou un ancien fichier d'ici) : ses dates, le nom et la photo de l'école, les classes montrées. Sans fichier, les leçons suivent les dates prévues.</span></div>
  <div class="rg-tabs">${NIVEAUX.map(n=>`<button type="button" data-rgniv="${n}" aria-pressed="${n===nivReg}">${n}</button>`).join('')}</div>
  <div class="rg-lst">${ordreSommaire(nivReg).filter(hasTrace).map(t=>{const d=dateOuverture(t),ouv=!!d&&d<=AUJ,c=esc(code(t));return `<div class="rg-l"><b>${c}</b><span>${esc(t.titre)}</span><input type="date" value="${d}" data-rgd="${c}" aria-label="Date d'ouverture de ${c}"><em class="${ouv?'ok':''}">${ouv?'ouverte':d?'ouvre le '+dateCourte(d):'fermée'}</em><button type="button" data-rgo="${c}">Ouvrir</button><button type="button" data-rgf="${c}">Fermer</button></div>`;}).join('')}</div>""", "section dates")

une_fois("""  if('rgniv' in d){nivReg=d.rgniv;dessiner();}
  else if('rgph' in d){$('#rgPhoto').click();}""",
"""  if('rgniv' in d){nivReg=d.rgniv;dessiner();}
  else if('rgo' in d||'rgf' in d){const c=d.rgo||d.rgf;BROUILLON.dates=BROUILLON.dates||{};(BROUILLON.dates[nivReg]=BROUILLON.dates[nivReg]||{})[c]='rgo' in d?AUJ:'';apres();}
  else if('rgld' in d){$('#rgFic').click();}
  else if('rgph' in d){$('#rgPhoto').click();}""", "clics")

une_fois("  if(i.dataset.rgcoul){BROUILLON.couleurs=",
"""  if(i.id==='rgFic'){const f=i.files[0];i.value='';if(!f)return;f.text().then(tx=>{let j;try{j=JSON.parse(tx);}catch(x){j=null;}
    if(!j||typeof j!=='object'||!(NIVEAUX.some(n=>j[n]&&typeof j[n]==='object')||j.ecole||Array.isArray(j.classes))){$('#rgMsg').style.color='#b3261e';$('#rgMsg').textContent="Ce fichier n'est pas un ouvertures.json valide.";return;}
    BROUILLON.dates=BROUILLON.dates||{};let k=0;NIVEAUX.forEach(n=>{if(j[n]&&typeof j[n]==='object'){BROUILLON.dates[n]={...(BROUILLON.dates[n]||{}),...Object.fromEntries(Object.entries(j[n]).filter(([c,v])=>typeof v==='string'))};k+=Object.keys(j[n]).length;}});
    if(j.ecole&&typeof j.ecole==='object'){BROUILLON.ecole={nom:String(j.ecole.nom||'').slice(0,80),photo:photoOk(j.ecole.photo)?j.ecole.photo:''};}
    if(Array.isArray(j.classes)){const A=NIVEAUX.filter(n=>j.classes.includes(n));if(A.length){BROUILLON.classes=A;if(!A.includes(nivReg))nivReg=A[0];}}
    if(j.couleurs&&typeof j.couleurs==='object'){BROUILLON.couleurs=couleursValides(j.couleurs);}
    apres();marqueVue='';majMarque();$('#rgMsg').style.color='';$('#rgMsg').textContent=`Fichier chargé (${k} dates${j.ecole&&j.ecole.nom?', école « '+j.ecole.nom+' »':''}${j.maj?', progression du '+new Date(j.maj+'T12:00').toLocaleDateString('fr-FR'):''}). Vérifiez, puis téléchargez le fichier complet.`;});return;}
  if(i.dataset.rgd!=null&&i.type==='date'){BROUILLON.dates=BROUILLON.dates||{};(BROUILLON.dates[nivReg]=BROUILLON.dates[nivReg]||{})[i.dataset.rgd]=i.value;apres();return;}
  if(i.dataset.rgcoul){BROUILLON.couleurs=""", "fichier chargé")

# menu enseignant du bandeau
une_fois("if(b.dataset.me==='reg')$('#regBtn').click();else if(b.dataset.me==='cle')$('#ensBtn').click();",
         "if(b.dataset.me==='reg')$('#regBtn').click();else if(b.dataset.me==='import'){$('#regBtn').click();const f=$('#rgFic');if(f)f.click();}else if(b.dataset.me==='cle')$('#ensBtn').click();", "menu clic")
une_fois("""${ENS_REEL?'<button type="button" data-me="reg">⚙ Réglages</button>""",
         """${ENS_REEL?'<button type="button" data-me="import">📂 Importer un fichier d’ouvertures (tableau de bord)…</button><button type="button" data-me="reg">⚙ Réglages : école, photo, classes, dates, couleurs</button>""", "menu bouton")
open(P, "w", encoding="utf-8").write(s)
print("posé")
