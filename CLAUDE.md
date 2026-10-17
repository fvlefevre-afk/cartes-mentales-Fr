# Leçons interactives de français — CM1

Site des leçons interactives (ceintures de français CM1) publié avec GitHub Pages.

## Règles de travail

- Toujours travailler directement sur la branche `main`.
- Ne jamais créer de branche ni de pull request : faire les commits sur `main` et les pousser directement.
- Répondre en français à l'enseignante, avec des mots simples (pas de jargon technique).

## Le site

- Tout le site tient dans `index.html` (images des cartes mentales intégrées en base64 dans l'objet `IMG`).
- Une leçon interactive = une entrée dans `TRACES` (avec `lesson:true`), une entrée dans `LESSONS`
  (sections avec `zone` en % sur la carte + écrans), des exercices en plus dans `PLUS`, et une carte dans `IMG`.
- Modèle pour une nouvelle leçon : G1, G2, G3 (carte mentale 1400×933 px, zones cliquables numérotées).
- Ouverture par période : `PERIODE_FICHIER` (en haut du fichier) et `PERIODE_CEINTURE`.
- PROVISOIRE : `TOUTES_LES_CARTES=true` ouvre toutes les leçons interactives à tout le monde, quelle que
  soit la période. Repasser à `false` pour remettre le blocage par période.
- Accès enseignant (provisoire) : l'adresse du site suivie de `?enseignant` ouvre toutes les périodes
  (variable `ENSEIGNANT` dans le bloc PÉRIODES), sans rien enregistrer ni changer pour les élèves.
- Pas de noms d'élèves dans le dépôt : il est public.
