# Outils de fabrication des leçons

Ces petits programmes fabriquent les cartes mentales, les écrans animés, les exercices
et les fiches du cahier de progrès. Ils servent à reprendre le travail depuis n'importe quel compte.
Lire aussi `../CLAUDE.md` (règles du projet) et `../IDEES-EN-ATTENTE.md` (questions en attente).

Il faut Python 3 et Playwright avec Chromium (pour photographier les cartes et tester le site),
ainsi que LibreOffice (`soffice`) pour les PDF des cahiers.
Tout ce qui est fabriqué va dans `sortie/`, qui n'est pas enregistré dans le dépôt.

## Fabriquer ou modifier une leçon

1. Écrire ou modifier le script de la leçon dans `lecons/` (modèle récent : `lecons/o1_a_o6.py` ou `lecons/v6.py`).
   - `build(...)` (mapgen.py) dessine la carte mentale 1400×933 : 5 cadres, avec leurs positions `TL`, `TC`, `TR` et deux cadres en bas.
   - `E(...)` (lhelp.py) décrit un écran : section, picto, titre, avatar (`girl`/`boy`), bulle, étapes animées, exercice « À toi ! » et exercices en plus.
   - `Q(...)` est un exercice à choix (la bonne réponse est toujours la première ; le site mélange). `C`, `SV`, `S`, `V` sont des exercices où l'on clique sur des mots.
   - `save(...)` écrit `sortie/XX.json`.
2. Lancer le script : `python3 lecons/o1_a_o6.py` → `sortie/O1.json` et `sortie/O1_carte.jpeg`.
3. Regarder l'image de la carte dans `sortie/`.
4. La mettre dans le site : `python3 inserer.py O1` (remplace la leçon si elle existe déjà).
   Pour une nouvelle matière, ajouter aussi la famille dans `FAMILLES` et la période dans `PERIODE_CEINTURE` (dans `index.html`).
5. Tester : `python3 tester.py O1` joue toutes les animations et tous les exercices.
6. Homophones : `python3 jumeaux.py` vérifie qu'aucun jumeau interdit n'apparaît dans H2 à H7 (il lit `sortie/`, donc il faut avoir relancé les scripts h2 à h7).

Les leçons G1, G2, G3, H1, V1 et V2 ont été faites autrement, avant ces outils : elles se modifient directement dans `index.html`.

## Les leçons CM2

- Une leçon CM2 = la leçon CM1 + des écrans en plus. Ils sont écrits dans `lecons/cm2_ajouts.py`
  (un appel `lecon('G3', [points de l'encadré], E(...), ...)` par leçon ; la section `sec` doit exister dans la leçon CM1).
- `python3 lecons/cm2_ajouts.py` puis `python3 inserer_cm2.py` les met dans le site.
- C6 et C7 (CM2 seulement) : `python3 lecons/c6_c7_cm2.py` puis `python3 inserer.py C6-CM2 C7-CM2`.
- Tester : `python3 tester.py G3-CM2`.

## Les leçons CE2

- Une leçon CE2 = la leçon CM1 sans certains écrans (`retirer` : numéros des écrans CM1 au 17/10/2026, voir `lecons/titres_cm1_ref.json`,
  ou directement les titres des écrans ; le site compare les titres, donc ajouter un écran au CM1 ne décale rien) + des écrans CE2.
  Tout est dans `lecons/ce2_ajouts.py` (`lecon('G6', [encadré], [écrans retirés], E(...), titre='…')`).
- `python3 lecons/ce2_ajouts.py` puis `python3 inserer_cm2.py CE2`.
- C6, C7, O7 (CE2 seulement) : `python3 lecons/ce2_seulement.py` puis `python3 inserer.py C6-CE2 C7-CE2 O7-CE2`.
- Vue d'ensemble des trois niveaux : `python3 vue_trois_niveaux.py` refait `programmes/ceintures-trois-niveaux.html`.

## Les marques dans les étapes animées

`[sujet]` `(verbe)` `^déterminant^` `~adjectif~` `%surligné en jaune%` `#mot inconnu#` `|entouré|` `*apparition*`
`{barré animé}` `{{barré}}` `___` (trou) `/` (retour à la ligne) `§terminaison en violet§`.
Dans le texte d'un exercice, `[ ]`, `( )` et `< >` deviennent des mots à cliquer : éviter les parenthèses ailleurs.

## Les cahiers de progrès

- Les textes des ceintures sont dans `cahiers_donnees.py` (couleur, code, compétence).
- `python3 cahiers.py G H C V O` met à jour la partie CM1 (parcours B) des fiches de ces familles.
- `python3 cahiers.py 2026` met à jour le tableau CM1 des cahiers « 2026 » (grammaire, conjugaison).
- Puis refaire le PDF : `soffice --headless --convert-to pdf "Cahier de progrès cm1/O - cahier de progrès.odt"`.

## Les dispositifs

- `python3 ajout_docx.py "<dispositif>.docx" dispositifs_cm2/G.md` ajoute (ou remplace) la partie « En CM2 » à la fin d'un dispositif,
  avec les styles du document. Textes : `dispositifs_cm2/` et `dispositifs_ce2/` (G, H, C, V, S = Structure des ceintures, D5, D6, D7, D7a, D7b, EDL = vue d'ensemble).
- Les fiches du cahier de progrès : `python3 cahiers.py G H C V O 2026` remplit les parcours A (CE2), B (CM1) et C (CM2).

## Le dispositif 2 (orthographe)

`dispositif2.md` est le texte du dispositif. Pour refaire le .docx avec les styles de l'original :
dézipper l'ancien .docx dans un dossier, lancer `python3 md2docx.py dispositif2.md <dossier> <nouveau.docx>` (le programme refait lui-même le .docx).
