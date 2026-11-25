#!/usr/bin/env python3
"""« Je retiens » par cadre de la carte (25/11/2026, demande de l'enseignante) : chaque point de CE2_PLUS, CM1_PLUS et CM2_PLUS reçoit
data-sec="id du cadre" (un ou plusieurs, séparés par une espace) ; un point sans cadre n'apparaît que dans « Je retiens tout ».
Clé = « NIVEAU|ceinture|n° du point » ; valeur = ids des cadres (sections de LESSONS). Rejouable (data-sec déjà posé = remplacé).
Usage : python3 outils/retiens_cadres.py"""
import json, pathlib, re, sys
P = pathlib.Path(__file__).resolve().parent.parent / "index.html"

def T(niv, code, *secs):
    return {f"{niv}|{code}|{i}": s for i, s in enumerate(secs, 1) if s}

M = {}
for d in [
 # ---- CM1 ----
 T("CM1","G1","phrase","sujet","verbe"), T("CM1","G2","decl inter imp","aff neg","excl"),
 T("CM1","G3","gn","noyau","adj","accord","att"), T("CM1","G4","gn det","verbe","adv","conj","inv"),
 T("CM1","G5","regle","pronom","pieges","groupe2","methode"), T("CM1","G6","phrase","cod","cc","tests"),
 T("CM1","G7","gn sv chaine","etre","etre","methode"), T("CM1","H1","avoir etre","choisir","forme","retenir"),
 T("CM1","H2","on","la","ou"), T("CM1","H3","ce ces","mix","a"), T("CM1","H4","et","ou","mais","inv"),
 T("CM1","H5","det","pro","cest"), T("CM1","H6","son ses mes","son ses mes","acc"), T("CM1","H7","se pers","sest","acc"),
 T("CM1","C1","rad","g1 g2","verbes","att"), T("CM1","C2","form term","term","form","etre irr"),
 T("CM1","C3","quand","radical term","etre","att"), T("CM1","C4","deux avoir","pp","neg","att"),
 T("CM1","C5","deux verbes","accord","att"), T("CM1","C6","aller dire pouvoir voir","aller dire pouvoir voir","att"),
 T("CM1","C7","futur","imparfait","pp etre","att"),
 T("CM1","V1","etiq precis ex","echelle","att","sert"), T("CM1","V2","phrase mot","methode","att"),
 T("CM1","V3","mot","pre suf","sens","att"), T("CM1","V4","fam","trouver","intrus","ortho"),
 T("CM1","V5","syn choix","con","classe","reb"), T("CM1","V6","def","ecrit pareil","contexte","reb"),
 T("CM1","O1","regle ailleurs","sons","prouve","attention"), T("CM1","O2","muette","famille feminin","prouve","memo"),
 T("CM1","O3","s ss c cedille","prouve"), T("CM1","O4","c consonne","qu","k"), T("CM1","O5","g gu","gj","ge"),
 T("CM1","O6","ill ille","y","oi oy"), T("CM1","O8","masc fem","te","tie","prouve"),
 T("CM1","O9","debut","exceptions","famille","verif prouve"), T("CM1","O10","eur exc","verbe","coeur"),
 T("CM1","O11","tion","sion","ssion","famille"), T("CM1","O12","fem","voyelle","adj","mem"),
 # ---- CM2 ----
 T("CM2","G1","sujet","sujet"), T("CM2","G3","gn","adj"), T("CM2","G4","inv","det","verbe","conj","verbe"),
 T("CM2","G5","pieges","regle"), T("CM2","G6","cod","cc","att"), T("CM2","G7","chaine","etre"),
 T("CM2","H1","choisir","forme"), T("CM2","V1","etiq","echelle"), T("CM2","V2","methode","methode","methode"),
 T("CM2","V3","mot","pre suf"), T("CM2","V4","fam"), T("CM2","V6","def","def","contexte"),
 T("CM2","C1","rad"), T("CM2","C2","term"), T("CM2","C3","quand","term","etre"), T("CM2","C4","pp","neg"), T("CM2","C5","accord"),
 T("CM2","O2","famille"), T("CM2","O8","fem"), T("CM2","O9","debut"), T("CM2","O11","famille"), T("CM2","O12","adj"),
 # ---- CE2 ----
 T("CE2","G1","phrase","sujet","sujet"), T("CE2","G2","decl inter imp","neg excl"), T("CE2","G3","gn","accord","accord"),
 T("CE2","G4","gn det","inv"), T("CE2","G5","regle","pronom"), T("CE2","G6","phrase","tests"), T("CE2","G7","chaine"),
 T("CE2","C1","verbes","rad","verbes"), T("CE2","C2","form","irr"), T("CE2","C3","quand","etre"), T("CE2","C4","deux avoir"),
 T("CE2","C5","deux verbes"), T("CE2","V1","etiq precis"), T("CE2","V2","phrase mot"), T("CE2","V3","pre","suf"),
 T("CE2","V4","fam","trouver"), T("CE2","V5","syn con","choix"), T("CE2","V6","def","contexte"),
 T("CE2","O1","regle"), T("CE2","O2","famille"), T("CE2","O3","s ss c cedille"), T("CE2","O4","c qu k"), T("CE2","O5","g gu"), T("CE2","O6","ill"),
]:
    M.update(d)

CIBLES = {"CE2": "CE2_PLUS", "CM1": "CM1_PLUS", "CM2": "CM2_PLUS"}

def etiqueter(niv, k, html, stat):
    n = [0]
    def f(m):
        n[0] += 1
        sec = M.get(f"{niv}|{k}|{n[0]}")
        corps = re.sub(r'^<li(?: data-sec="[^"]*")?>', '', m.group(0))
        stat["tot"] += 1
        if sec: stat["tag"] += 1
        return f'<li data-sec="{sec}">' + corps if sec else '<li>' + corps
    # seuls les <li> de premier niveau (le bloc d'exemples n'a plus de <li>)
    return re.sub(r'<li(?: data-sec="[^"]*")?>', f, html)

def main():
    L = P.read_text(encoding="utf-8").split("\n"); stat = {"tot": 0, "tag": 0}
    for niv, nom in CIBLES.items():
        i = next(i for i, l in enumerate(L) if l.startswith(f"const {nom}="))
        l = L[i]; fin = l.rindex("};") + 1
        data = json.loads(l[len(f"const {nom}="):fin])
        for k, v in data.items():
            if isinstance(v, str): data[k] = etiqueter(niv, k, v, stat)
            else: v["html"] = etiqueter(niv, k, v.get("html", ""), stat)
        L[i] = f"const {nom}=" + json.dumps(data, ensure_ascii=False) + l[fin:]
    P.write_text("\n".join(L), encoding="utf-8")
    print(stat["tag"], "points rattachés à un cadre sur", stat["tot"])

main()
