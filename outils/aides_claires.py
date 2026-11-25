#!/usr/bin/env python3
"""Aides des exercices en phrases claires (25/11/2026, demande de l'enseignante : « = » et « → » ne sont pas intuitifs pour un élève qui a besoin d'aide).
Réécrit dans index.html les textes d'aide (`hint:` des exercices) qui contiennent « = » ou « → » : « Mon frère = il : il a. » devient « Je remplace « Mon frère » par « il » : il a. ».
Règles par famille + liste à la main (AIDES_A_LA_MAIN). Rejouable : un texte déjà réécrit ne contient plus ces signes. Aucune formulation fausse n'est écrite.
Usage : python3 outils/aides_claires.py [--liste]   (--liste : affiche seulement les textes qui restent à traiter)"""
import pathlib, re, sys

P = pathlib.Path(__file__).resolve().parent.parent / "index.html"
Q = "« "; R = " »"   # guillemets français avec espaces insécables
def g(x): return f"« {x} »"

PRON = r"(il|elle|ils|elles|nous|vous)"
def maj(t): return t[:1].upper() + t[1:]

def regles(h):
    # 1. « X = il (→ -ent) (: reste). » : remplacement par un pronom
    m = re.fullmatch(r"(.+?) = " + PRON + r"(?: → (-\w+))?(?: : (.+?))?\.", h)
    if m and "Je cherche" not in m.group(1) and "Sujet" not in m.group(1):
        a, p, fin, reste = m.groups()
        t = f"Je remplace {g(a)} par {g(p)}"
        if fin: t += f" : j’écris {fin}"
        if reste:
            r = reste.rstrip(".")
            if " " not in r and not fin: r = g(p + " " + r)   # « On = il : construit. » → « il construit »
            t += (" : " if not fin else ", ") + r
        return t + "."
    m = re.fullmatch(r"(Je cherche le sujet|Sujet) : (.+?) = " + PRON + r"\.", h)
    if m:
        pre = "Je cherche le sujet" if m.group(1).startswith("Je") else "Le sujet"
        return f"{pre} : je remplace {g(m.group(2))} par {g(m.group(3))}."
    m = re.fullmatch(r"Les enfants = ils : un verbe → -ent\.", h)
    if m: return "Je remplace « Les enfants » par « ils » : le verbe prend -ent."
    # 2. « c’est = cela est »
    if re.search(r"[Cc]’est = cela est", h):
        t = re.sub(r"[Cc]’est = cela est", lambda x: g(x.group(0)[0] + "’est") + " veut dire « cela est »", h)
        t = re.sub(r"^(La) (devant|remplace)", lambda x: g("La") + " " + x.group(2), t)
        t = re.sub(r"; la (devant un verbe)", r"; « la » \1", t)
        t = re.sub(r"; la remplace", "; « la » remplace", t)
        t = re.sub(r"^« C’est » veut dire « cela est » ; la ", "« C’est » veut dire « cela est » ; « la » ", t)
        return t
    # 3. pronom → terminaison ou forme
    m = re.fullmatch(r"(Je|Tu|Il|Elle|On|Nous|Vous|Ils|Elles) → (-\w+)\.", h)
    if m: return f"Avec {g(m.group(1).lower())}, la terminaison est {m.group(2)}."
    m = re.fullmatch(r"(Je|Tu|Il|Elle|On|Nous|Vous|Ils|Elles) → (\w+)\.", h)
    if m: return f"Avec {g(m.group(1).lower())}, j’écris {g(m.group(2))}."
    # 4. noms de métier au féminin
    m = re.fullmatch(r"([Uu]n) (\w+) → une (\w+)\.", h)
    if m: return f"Au féminin, {g('un ' + m.group(2))} devient {g('une ' + m.group(3))}."
    # 5. adverbe : « x → xment. »
    m = re.fullmatch(r"(\w+) → (\w+ment)\.", h)
    if m: return f"L’adverbe de {g(m.group(1))} est {g(m.group(2))}."
    m = re.fullmatch(r"(\w+) → (\w+ment), sans e\.", h)
    if m: return f"L’adverbe de {g(m.group(1))} est {g(m.group(2))}, sans e."
    # 6. féminin en chaîne « x → xe → xement »
    m = re.fullmatch(r"(\w+) → (\w+) → (\w+ment)\.", h)
    if m: return f"Au féminin, {g(m.group(1))} devient {g(m.group(2))} ; puis l’adverbe est {g(m.group(3))}."
    # 7. féminin d'un adjectif (avec ou sans remarque)
    m = re.fullmatch(r"(\w+) → (\w+)(?: : (.+?))?\.", h)
    if m and re.search(r"(e|que)$", m.group(2)) and not re.match(r"^(dire|faire|prendre|voir|pouvoir|vouloir|venir|ranger|rangé)$", m.group(1)) and not m.group(1) in ("il", "ils", "as", "sont", "suis"):
        t = f"Au féminin, {g(m.group(1))} devient {g(m.group(2))}"
        return t + (f" : {m.group(3)}." if m.group(3) else ".")
    # 8. radical de « nous … »
    m = re.fullmatch(r"nous (\w+) → (\w+-)(?: \+ (\w+))?\.", h)
    if m: return f"Le radical de {g('nous ' + m.group(1))} est {g(m.group(2))}" + (f", puis j’ajoute -{m.group(3)}." if m.group(3) else ".")
    m = re.fullmatch(r"nous (\w+) → (je|il|nous) (\w+)\.", h)
    if m: return f"Je pars de {g('nous ' + m.group(1))} pour écrire {g(m.group(2) + ' ' + m.group(3))}."
    # 9. verbes : forme conjuguée ou participe
    m = re.fullmatch(r"(faire|prendre|voir) → (fait|pris|vu)( : je l’apprends par cœur)?\.", h)
    if m: return f"Le participe passé de {g(m.group(1))} est {g(m.group(2))}" + (" : je l’apprends par cœur." if m.group(3) else ".")
    m = re.fullmatch(r"(\w+) → ((?:il|ils|elle) \w+)\.", h)
    if m: return f"Le verbe {g(m.group(1))} s’écrit {g(m.group(2))}."
    return None

# textes particuliers, écrits à la main
AIDES_A_LA_MAIN = {
 "Après « deux » : un nom → -s.": "Après « deux », le nom prend -s.",
 "Les enfants = ils : un verbe → -ent.": "Je remplace « Les enfants » par « ils » : le verbe prend -ent.",
 "Mes voisins = ils : c’est un verbe → -ent.": "Je remplace « Mes voisins » par « ils » : le verbe prend -ent.",
 "Qui est-ce qui travaille ? Les élèves = ils.": "Qui est-ce qui travaille ? Les élèves : je remplace « Les élèves » par « ils ».",
 "Qui est-ce qui… ? Tes chaussures = elles.": "Qui est-ce qui… ? Tes chaussures : je remplace « Tes chaussures » par « elles ».",
 "Plusieurs sujets reliés par « et » = ils.": "Plusieurs sujets reliés par « et » : je dis « ils ».",
 "Tu → -as, avec le r du futur.": "Avec « tu », la terminaison est -as, avec le r du futur.",
 "Vous → -ez, avec le r du futur.": "Avec « vous », la terminaison est -ez, avec le r du futur.",
 "Au 2e groupe, nous → -issons.": "Au 2e groupe, avec « nous », la terminaison est -issons.",
 "Ce chien = énorme, avec « devenir ».": "Avec « devenir », « énorme » dit comment est le chien.",
 "Elle : féminin → la.": "« Elle » est féminin : je dis « la ».",
 "Entre deux voyelles : « s » → ss.": "Entre deux voyelles, le son « s » s’écrit ss.",
 "Entre deux voyelles : « s » → ss. Pense à posséder.": "Entre deux voyelles, le son « s » s’écrit ss. Je pense à « posséder ».",
 "Le chat est gris → les chats…": "Le chat est gris. Au pluriel : les chats…",
 "Le déterminant m’aide : un/le → masculin ; une/la → féminin.": "Le déterminant m’aide : « un » et « le » sont masculins ; « une » et « la » sont féminins.",
 "Les adjectifs en -ent donnent -emment ou -amment : prudent → prudemment.": "Les adjectifs en -ent donnent -emment ou -amment : par exemple « prudent » donne « prudemment ».",
 "Les enfants : plusieurs garçons et filles → ils.": "« Les enfants » : plusieurs garçons et filles, je dis « ils ».",
 "Ma sœur a un vélo → mes sœurs…": "Ma sœur a un vélo. Au pluriel : mes sœurs…",
 "Ma tante = médecin, avec le verbe être.": "Avec le verbe être, « médecin » dit qui est ma tante.",
 "Mon frère est grand → mes frères…": "Mon frère est grand. Au pluriel : mes frères…",
 "On remplace des personnes : on = nous, les gens.": "« On » remplace des personnes : « nous » ou « les gens ».",
 "Pense à conclure : -clure → -sion.": "Je pense au verbe « conclure » : -clure donne -sion.",
 "Pense à indiquer : -quer → -cation.": "Je pense au verbe « indiquer » : -quer donne -cation.",
 "Tu as vendu → fermé.": "« Tu as vendu » : je remplace « vendu » par « fermé ».",
 "Un déterminant devant : c’est un nom → -s.": "Il y a un déterminant devant : c’est un nom, donc -s.",
 "Une exception : discuter → discussion.": "Une exception : « discuter » donne « discussion ».",
 "as vient du verbe avoir : as → avais.": "« as » vient du verbe avoir : à l’imparfait, « avais ».",
 "sont vient du verbe être : sont → étaient.": "« sont » vient du verbe être : à l’imparfait, « étaient ».",
 "suis vient du verbe être : suis → étais.": "« suis » vient du verbe être : à l’imparfait, « étais ».",
 "il → est.": "Avec « il », j’écris « est ».",
 "ils → sont.": "Avec « ils », j’écris « sont ».",
 "ranger : 1er groupe → -é.": "« ranger » est du 1er groupe : le participe passé finit par -é.",
 "rangé : 1er groupe → ranger.": "« rangé » est du 1er groupe : l’infinitif est « ranger ».",
 "le vent → il.": "Je remplace « le vent » par « il ».",
 "les enfants → ils.": "Je remplace « les enfants » par « ils ».",
 "ma sœur → elle.": "Je remplace « ma sœur » par « elle ».",
 "l’ = ta robe : féminin singulier.": "« l’ » remplace « ta robe » : féminin singulier.",
 "mes amis : COD au pluriel → les.": "« mes amis » est un COD au pluriel : je dis « les ».",
 "« les » = ces fleurs, placé avant : féminin pluriel.": "« les » remplace « ces fleurs » et se place avant le verbe : féminin pluriel.",
 "À mon grand-père = à lui.": "« À mon grand-père » se remplace par « à lui ».",
 "à Paul → lui.": "« à Paul » se remplace par « lui ».",
 "à mes parents : COI au pluriel → leur.": "« à mes parents » est un COI au pluriel : je dis « leur ».",
 "à + le = au.": "« à » + « le » donne « au ».",
 "nous allons → nous allions.": "Je pars de « nous allons » pour écrire « nous allions ».",
 "nous prenons → il prenait.": "Je pars de « nous prenons » pour écrire « il prenait ».",
 "Ma cousine et moi = nous.": "Je remplace « Ma cousine et moi » par « nous ».",
 "ancien → ancienne : le n se double.": "Au féminin, « ancien » devient « ancienne » : le n se double.",
 "bon → bonne : le n se double.": "Au féminin, « bon » devient « bonne » : le n se double.",
 "gentil → gentille : la consonne se double.": "Au féminin, « gentil » devient « gentille » : la consonne se double.",
 "gros → grosse : deux s.": "Au féminin, « gros » devient « grosse » : deux s.",
 "long → longue.": "Au féminin, « long » devient « longue ».",
 "blanc → blanche.": "Au féminin, « blanc » devient « blanche ».",
 "frais → fraîche.": "Au féminin, « frais » devient « fraîche ».",
 "neuf → neuve.": "Au féminin, « neuf » devient « neuve ».",
 "vif → vive.": "Au féminin, « vif » devient « vive ».",
 "léger → légère.": "Au féminin, « léger » devient « légère ».",
 "épais → épaisse.": "Au féminin, « épais » devient « épaisse ».",
}

def reecrire(h):
    if h in AIDES_A_LA_MAIN: return AIDES_A_LA_MAIN[h]
    return regles(h)

RE_HINT = re.compile(r"""(["']?hint["']?\s*:\s*)(?:'((?:[^'\\]|\\.)*)'|"((?:[^"\\]|\\.)*)")""")
def transforme(s, liste=None, stat=None):
    def f(m):
        quote = "'" if m.group(2) is not None else '"'
        txt = m.group(2) if m.group(2) is not None else m.group(3)
        brut = txt.replace("\\'", "'").replace('\\"', '"')
        if not re.search(r"\s=\s|→|≠", brut): return m.group(0)
        n = reecrire(brut)
        if n is None:
            if liste is not None: liste.add(brut)
            return m.group(0)
        if stat is not None: stat["n"] += 1
        n = n.replace("\\", "\\\\")
        n = n.replace("'", "\\'") if quote == "'" else n.replace('"', '\\"')
        return m.group(1) + quote + n + quote
    return RE_HINT.sub(f, s)

# autres textes d'aide (légendes des écrans « Je regarde », étapes de méthode) : texte exact → phrase claire
TEXTES = {
 "Elles discutent → c’est le verbe.": "« Elles discutent » : « discutent » est le verbe.",
 "il a → ils ont": "Au pluriel, « il a » devient « ils ont ».",
 "il est → ils sont": "Au pluriel, « il est » devient « ils sont ».",
 "Le sujet → la personne.": "Le sujet, c’est la personne.",
 "Ce qu’on possède → avoir.": "Ce qu’on possède : le verbe avoir.",
 "Plusieurs mots : Tom et Léa = ils.": "Plusieurs mots : « Tom et Léa », je dis « ils ».",
 "Léa et moi = nous": "« Léa et moi » : je dis « nous ».",
 "Léa et Tom = ils": "« Léa et Tom » : je dis « ils ».",
 "Toi et Tom = vous": "« Toi et Tom » : je dis « vous ».",
 "Les filles = elles → -ent": "« Les filles » : je dis « elles », le verbe prend -ent.",
 "Léa : féminin → e.": "« Léa » est féminin : j’écris -e.",
 "Léa : féminin → e": "« Léa » est féminin : j’écris -e",
 "Pluriel → s.": "Au pluriel, j’écris -s.",
 "Féminin pluriel → es.": "Au féminin pluriel, j’écris -es.",
 "pluriel → s": "au pluriel, j’écris -s",
 "féminin pluriel → es": "au féminin pluriel, j’écris -es",
 "elles → -ent": "avec « elles », -ent",
 "tu → -s · nous → -ons · vous → -ez · ils → -ent": "avec « tu » -s · avec « nous » -ons · avec « vous » -ez · avec « ils » -ent",
 "Le déterminant m’aide : les, des, mes, ces → pluriel.": "Le déterminant m’aide : « les », « des », « mes », « ces » sont pluriels.",
 "2. « les » → pluriel : filles.": "2. « les » est pluriel : « filles ».",
 "3. Filles : féminin pluriel → petites.": "3. « Filles » est féminin pluriel : « petites ».",
 "4. J’écris la terminaison : ils → -ent.": "4. J’écris la terminaison : avec « ils », -ent.",
 "2. Je le remplace : ils → -ent.": "2. Je le remplace par « ils » : -ent.",
 "2. Le verbe : elles → sont.": "2. Le verbe : avec « elles », « sont ».",
 "3. Le participe passé : féminin pluriel → es.": "3. Le participe passé : au féminin pluriel, -es.",
 "1. Le nom noyau : maisons → féminin pluriel.": "1. Le nom noyau : « maisons » est féminin pluriel.",
 "Qui est-ce qui regarde ? Je → regarde, sans -nt.": "Qui est-ce qui regarde ? Avec « je » : « regarde », sans -nt.",
 "c’est = cela est.": "« c’est » veut dire « cela est ».",
}
RE_LIT = re.compile(r"""(?<![\w$])(['"])((?:(?!\1)[^\\\n]|\\.){4,160})\1""")
def transforme_textes(s, stat=None):
    def f(m):
        q = m.group(1); t = m.group(2).replace("\\'", "'").replace('\\"', '"')
        if t in TEXTES: n = TEXTES[t]
        elif re.search(r"\s=\s", t) and not re.search(r"[{};%*§]|=>", t):
            n = regles(t)
            if n is None or n == t: return m.group(0)
        else: return m.group(0)
        if stat is not None: stat["t"] = stat.get("t", 0) + 1
        n = n.replace("\\", "\\\\")
        n = n.replace("'", "\\'") if q == "'" else n.replace('"', '\\"')
        return q + n + q
    return RE_LIT.sub(f, s)

if __name__ == "__main__":
    s = P.read_text(encoding="utf-8"); liste = set(); stat = {"n": 0}
    t = transforme_textes(transforme(s, liste, stat), stat)
    if "--liste" not in sys.argv:
        P.write_text(t, encoding="utf-8")
    print(stat["n"], "aides (hint) et", stat.get("t", 0), "autres textes réécrits ;", len(liste), "restent à traiter")
    for x in sorted(liste): print(" -", x)
