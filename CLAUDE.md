# Leçons interactives de français — CM1

Site des leçons interactives (ceintures de français CM1) publié avec GitHub Pages.

## Règles de travail

- Toujours travailler directement sur la branche `main`.
- Ne jamais créer de branche ni de pull request : faire les commits sur `main` et les pousser directement.
- Répondre en français à l'enseignante, avec des mots simples (pas de jargon technique).
- Noter dans `IDEES-EN-ATTENTE.md` les propositions restées sans réponse, et retirer celles qui sont tranchées.

## Le site

- Tout le site tient dans `index.html` (images des cartes mentales intégrées en base64 dans l'objet `IMG`).
- Écrans animés : §…§ colore une terminaison en violet (conjugaison).
- Une leçon peut garder un champ `html` (ex. tableau des verbes de C1) : il s’affiche sous la carte et à l’impression.
- Une leçon interactive = une entrée dans `TRACES` (avec `lesson:true`), une entrée dans `LESSONS`
  (sections avec `zone` en % sur la carte + écrans), des exercices en plus dans `PLUS`, et une carte dans `IMG`.
- Modèle pour une nouvelle leçon : G1 à G7, H1 à H8, V1 à V6, C1 à C8, O1 à O6 (carte mentale 1400×933 px, zones cliquables numérotées).
- Les dispositifs de l’enseignante (dossier « Documents explicatifs des dispositifs ») font référence : les lire avant de créer une ceinture.
  Chaque document a une partie « En CM2 » à la fin (pas de document séparé pour le CM2) ; textes dans
  `outils/dispositifs_cm2/`, ajoutés avec `outils/ajout_docx.py`. Test CM2 : 3 items tronc commun + 3 items ajout CM2. Partie « En CE2 » aussi (`outils/dispositifs_ce2/`) ; test CE2 : 6 items CE2.
- Ouverture par période : `PERIODE_FICHIER` (en haut du fichier) et `PERIODE_CEINTURE`.
- PROVISOIRE : `TOUTES_LES_CARTES=true` ouvre toutes les leçons interactives à tout le monde, quelle que
  soit la période. Repasser à `false` pour remettre le blocage par période.
- Accès enseignant (provisoire) : l'adresse du site suivie de `?enseignant` ouvre toutes les périodes
  (variable `ENSEIGNANT` dans le bloc PÉRIODES), sans rien enregistrer ni changer pour les élèves.
- Sommaire par classe : boutons CE2 / CM1 / CM2 (adresse `#niveau=CE2`…). Une leçon sans champ `niveau`
  est rangée en CM1 ; pour une leçon d'une autre classe, ajouter `niveau:'CE2'` ou `niveau:'CM2'` dans `TRACES`.
- CM2 : mêmes numéros, mêmes couleurs, mêmes notions qu'en CM1 (choix de l'enseignante, octobre 2026).
  Une leçon CM2 (id `XX-CM2`, code affiché `XX`) = la leçon CM1 + les écrans de `CM2_PLUS` (étiquette « CM2 »,
  placés après le dernier écran de leur section) + un encadré « En CM2, j'apprends aussi » sous la carte.
  Fabriqués par `outils/lecons/cm2_ajouts.py`, mis dans le site par `outils/inserer_cm2.py`. Liste : `CM2_COPIE` ;
  l'étiquette « CM1 » de la carte est recouverte par « CM2 » (`CHIP_CM2`). C6 (plus-que-parfait, rouge) et
  C7 (passé simple, violette) n'existent qu'en CM2 (`outils/lecons/c6_c7_cm2.py`). Détail : `programmes/ecarts-CM1-CM2.md`.
- CE2 : mêmes numéros, mêmes couleurs, mêmes notions, en plus simple. Une leçon CE2 (id `XX-CE2`) = la leçon CM1
  sans les écrans listés dans `retirer`, + les écrans de `CE2_PLUS` (étiquette « CE2 ») + un encadré « Au CE2, je retiens » ;
  les zones de la carte sans écran sont masquées. Fabriqués par `outils/lecons/ce2_ajouts.py`, mis dans le site par
  `outils/inserer_cm2.py CE2`. Pas d'homophones au CE2. `retirer` : numéros d'écrans CM1 au 17/10/2026
  (`outils/lecons/titres_cm1_ref.json`) ou titres d'écrans ; le site compare les titres. Ceintures CE2 seulement : C6 et C7 (verbes irréguliers, sortis de C1-C5),
  O7 (sons « o », « é », « è » et accents) — `outils/lecons/ce2_seulement.py`. Vue d'ensemble : `programmes/ceintures-trois-niveaux.html`.
- Pas de noms d'élèves dans le dépôt : il est public.

## Outils

- Le dossier `outils/` contient les programmes qui fabriquent les cartes, les écrans, les exercices et les fiches
  du cahier de progrès. Mode d'emploi : `outils/LISEZMOI.md`.

## Homophones (Dispositif 1 bis — voir « Documents explicatifs des dispositifs »)

- Règle non négociable : jamais deux mots d'une même paire jumelle dans la même ceinture (H1 à H7).
  Le jumeau n'est jamais proposé comme choix ni comme réponse, et n'apparaît pas dans les phrases.
- Chaque mot s'ancre dans sa classe grammaticale et se prouve par une manipulation (« Je prouve »),
  jamais par un « truc » appris par cœur.
- Les paires ne se retrouvent qu'en H8 (transfert), une fois les deux côtés validés.
- Mots ajoutés en CM2 : qu'elle (H2), sans (H3), donc (H4), dont (H5), quel/quelle (H6), s'en (H7) ;
  leurs jumeaux restent dans une autre ceinture. Vérifier avec `outils/jumeaux.py`.
- Pas de ceintures d'homophones au CE2 (hors programme du cycle 2, décision d'octobre 2026) : elles commencent au CM1.

## Orthographe (Dispositif 2 — version à ceintures)

- Rubrique « Orthographe » du site : ceintures O1 à O6, avec test de validation comme les autres dispositifs.
- Code couleur : %…% surligne en jaune les lettres étudiées, |…| entoure la lettre qui décide (celle qui suit).
- Les exercices complètent le mot avec `fill:'hl'` (la lettre choisie apparaît surlignée, collée au mot).
- Pas de termes savants pour les élèves (« le son », « la lettre », « devant », « un mot de la même famille »).
- Cahier de progrès : `Cahier de progrès cm1/O - cahier de progrès.odt` (CM1 = parcours B dans les cahiers).
