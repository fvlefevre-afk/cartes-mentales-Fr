#!/usr/bin/env python3
"""Accès enseignant depuis la page d'accueil « Mes ceintures » seulement (27/11/2026, demande de l'enseignante).
Ajoute à la fin de la page un bloc qui : cache les boutons enseignant des cartes ; ouvert avec « ?reglages » (par la fenêtre de l'accueil), montre directement les réglages.
Rejouable (le bloc est remplacé). Usage : python3 outils/acces_accueil.py [fichier …]"""
import os, pathlib, sys

MATIERE = "francais"   # préfixe des clés de sessionStorage de cette page
DEB, FIN = "<!--ACCES-ACCUEIL-DEBUT-->", "<!--ACCES-ACCUEIL-FIN-->"
BLOC = DEB + """<style id="accesAccueil">
/* plus de bouton enseignant dans les cartes : un seul, discret, sur la page d'accueil */
#ensBtn,#regBtn,[data-rail="ens"]{display:none!important}
body:not(.mode-ens) [data-cu="enseignante"]{display:none!important}
html.reglages-seuls body{background:#fff!important;overflow:hidden}
html.reglages-seuls body>:not(#regDlg){visibility:hidden!important}
html.reglages-seuls #regDlg{position:fixed;inset:0;margin:0;width:100%;max-width:none;height:100%;max-height:none;border-radius:0;box-shadow:none;box-sizing:border-box;overflow:auto}
html.reglages-seuls #regDlg::backdrop{background:#fff}
html.reglages-seuls #regDlg>h2{display:none}
</style>
<script>
(function(){
const M="@MATIERE@",lire=k=>{try{return sessionStorage.getItem(M+"-"+k);}catch(e){return null;}};
const ens=!!lire("enseignant")&&lire("apercu")!=="1";
document.body.classList.toggle("mode-ens",ens);
/* élèves : le bouton « Enseignante » des activités affichées dans un cadre est caché aussi */
if(!ens){const surCharge=e=>{if(e.target&&e.target.tagName==="IFRAME")cacher(e.target);};
 const cacher=f=>{try{const d=f.contentDocument;if(!d||!d.head||d.getElementById("sansEns"))return;const s=d.createElement("style");s.id="sansEns";s.textContent="#ensT{display:none!important}";d.head.appendChild(s);d.addEventListener("load",surCharge,true);d.querySelectorAll("iframe").forEach(cacher);}catch(e){}};
 document.addEventListener("load",surCharge,true);document.querySelectorAll("iframe").forEach(cacher);}
if(!/[?&]reglages\\b/.test(location.search))return;
const bouton=document.getElementById("regBtn"),dlg=document.getElementById("regDlg");if(!bouton||!dlg)return;   /* sans le mot de passe : la page ordinaire */
const dansCadre=parent!==window,adresse=location.href.split(/[?#]/)[0],dire=(m,u)=>{if(dansCadre)parent.postMessage({reglagesCartes:m,url:u},"*");};
document.documentElement.classList.add("reglages-seuls");
/* « Voir comme un élève » : la page entière, pas le cadre des réglages */
document.addEventListener("click",e=>{if(!(e.target.closest&&e.target.closest("#regDlg [data-rgap]")))return;e.preventDefault();e.stopPropagation();
 try{sessionStorage.setItem(M+"-apercu","1");}catch(x){}if(dansCadre)dire("apercu",adresse);else location.href=adresse;},true);
dlg.addEventListener("close",()=>{if(dansCadre)dire("fermer");else location.replace(adresse);});
bouton.onclick();dire("pret");
/* ouvertures.json arrive après la page : les réglages sont redessinés avec lui */
if(location.protocol!=="file:")fetch("ouvertures.json",{cache:"no-store"}).catch(()=>{}).finally(()=>setTimeout(()=>{if(dlg.open)bouton.onclick();},500));
})();
</script>""".replace("@MATIERE@", MATIERE) + FIN + "\n"

def poser(f):
    s = f.read_text(encoding="utf8")
    if DEB in s:
        a = s.index(DEB); b = s.index(FIN, a) + len(FIN)
        s = s[:a] + s[b:].lstrip("\n")
    i = s.rfind("</body>")
    if i < 0 or 'id="ensBtn"' not in s: sys.exit("page non reconnue : %s" % f)
    f.write_text(s[:i] + BLOC + s[i:], encoding="utf8")
    print("accès enseignant depuis l'accueil :", f)

if __name__ == "__main__":
    ici = pathlib.Path(__file__).resolve().parent.parent
    for f in sys.argv[1:] or [os.environ.get("HABILLAGE_FICHIER") or ici / "index.html"]:
        poser(pathlib.Path(f))
