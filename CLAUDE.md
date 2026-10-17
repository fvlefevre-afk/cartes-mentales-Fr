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
- Ouverture par période : `PERIODE_FICHIER` (en haut du fichier) et `PERIODE_CEINTURE`.
- PROVISOIRE : `TOUTES_LES_CARTES=true` ouvre toutes les leçons interactives à tout le monde, quelle que
  soit la période. Repasser à `false` pour remettre le blocage par période.
- Accès enseignant (provisoire) : l'adresse du site suivie de `?enseignant` ouvre toutes les périodes
  (variable `ENSEIGNANT` dans le bloc PÉRIODES), sans rien enregistrer ni changer pour les élèves.
- Pas de noms d'élèves dans le dépôt : il est public.

## Homophones (Dispositif 1 bis — voir « Documents explicatifs des dispositifs »)

- Règle non négociable : jamais deux mots d'une même paire jumelle dans la même ceinture (H1 à H7).
  Le jumeau n'est jamais proposé comme choix ni comme réponse, et n'apparaît pas dans les phrases.
- Chaque mot s'ancre dans sa classe grammaticale et se prouve par une manipulation (« Je prouve »),
  jamais par un « truc » appris par cœur.
- Les paires ne se retrouvent qu'en H8 (transfert), une fois les deux côtés validés.

## Orthographe (Dispositif 2 — version à ceintures)

- Rubrique « Orthographe » du site : ceintures O1 à O6, avec test de validation comme les autres dispositifs.
- Code couleur : %…% surligne en jaune les lettres étudiées, |…| entoure la lettre qui décide (celle qui suit).
- Les exercices complètent le mot avec `fill:'hl'` (la lettre choisie apparaît surlignée, collée au mot).
- Pas de termes savants pour les élèves (« le son », « la lettre », « devant », « un mot de la même famille »).
- Cahier de progrès : `Cahier de progrès cm1/O - cahier de progrès.odt` (CM1 = parcours B dans les cahiers).
