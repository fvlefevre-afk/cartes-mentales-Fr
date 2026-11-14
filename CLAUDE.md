# Leçons interactives de français — CM1

Site des leçons interactives (ceintures de français CM1) publié avec GitHub Pages.

## Règles de travail

- **Vocabulaire (10/11/2026, demande de l'enseignante)** : dire « les cartes interactives de français » (et « les cartes interactives de mathématiques »), jamais « le site ».
- **Publication** : les élèves ouvrent les cartes par une adresse de La Forge Éducation (forge.apps.education.fr), sur ordinateur, tablette et téléphone. Ce dépôt GitHub
  n'est pas l'adresse des élèves : `bash outils/publier-forge.sh` copie `index.html`, `images/`, `polices/` et `.gitlab-ci.yml` dans le dépôt voisin `publication-francais`
  et l'envoie sur La Forge. À lancer depuis un ordinateur où ce dépôt voisin existe (une session dans le nuage n'a pas accès à La Forge) : prévenir l'enseignante
  que les changements ne sont visibles des élèves qu'après cette publication.
- Toujours travailler directement sur la branche `main`.
- Ne jamais créer de branche ni de pull request : faire les commits sur `main` et les pousser directement.
- Répondre en français à l'enseignante, avec des mots simples (pas de jargon technique).
- Noter dans `IDEES-EN-ATTENTE.md` les propositions restées sans réponse, et retirer celles qui sont tranchées.

## Le site

- Le site tient dans `index.html` ; les images (cartes mentales `images/<id>.jpg`, personnages `images/fille*.jpg`, `images/garcon*.jpg`, `duo.jpg`)
  sont dans le dossier `images/` : l'objet `IMG` ne garde que leur chemin (page allégée de 11,7 Mo à 0,4 Mo, 23/10/2026).
  Une carte se remplace à la main en gardant le même nom de fichier (1400×933 px).
- Écrans animés : §…§ colore une terminaison en violet (conjugaison).
- **Lisibilité CM1 (10/11/2026, demande de l'enseignante)** : police Andika dans `polices/` (400, 400 italique, 700 ; licence `polices/OFL.txt`), plus de Google Fonts ;
  textes lus par l'élève à 16 px au moins (`--u` : 16 à 22 px ; bloc « Lisibilité CM1 » en fin de feuille de style) ; une leçon n'est jamais réduite sous 90 % (`MIN_LECON`), la page défile ;
  zones de la carte toujours visibles (pointillés, `.zone.fait` en vert, la prochaine `.zone.suivant` respire, immobile avec « réduire les animations ») ;
  rien n'est dit par la seule couleur : verbe souligné deux fois (sujet une fois), ✓ / ✗ devant les messages et les choix justes ou faux. Ne pas revenir en arrière sur ces points.
- G6 : compléments d’objet en indigo (#5e35b1), compléments circonstanciels en marron (#8d5524), sur la carte et dans les écrans
  (classe `lecon-G6`), pour ne pas reprendre le vert de l’adjectif ni l’orange du déterminant (choix de l’enseignante, 23/10/2026).
- Une leçon peut garder un champ `html` (ex. tableau des verbes de C1) : il s’affiche sous la carte et à l’impression.
- Une leçon interactive = une entrée dans `TRACES` (avec `lesson:true`), une entrée dans `LESSONS`
  (sections avec `zone` en % sur la carte + écrans), des exercices en plus dans `PLUS`, et une carte dans `IMG` (chemin vers `images/`).
- Modèle pour une nouvelle leçon : G1 à G7, H1 à H7, V1 à V6, C1 à C9, O1 à O7 (carte mentale 1400×933 px, zones cliquables numérotées).
- Les dispositifs de l’enseignante font référence : les lire avant de créer une ceinture. Depuis le 27/10/2026 ils sont dans le dépôt `ressources`
  (branche `branche-propre`) : « Documents explicatifs des dispositifs ce2-cm1-cm2 » (Structure des ceintures EDL, avec la page « Principes » ; dispositifs 5 à 7b ;
  un seul jeu pour la classe à trois niveaux et la classe de CM1 seul) et « Fichiers à déposer/Étude de la langue … » (dispositifs d’étude de la langue,
  plannings annuels). L’ancien dossier « Documents explicatifs des dispositifs » de ce dépôt est retiré ; les parties « En CM2 » / « En CE2 » ajoutées
  à ces anciens documents restent en texte dans `outils/dispositifs_cm2/` et `outils/dispositifs_ce2/` (`outils/ajout_docx.py`). Test CM2 : 3 items tronc commun + 3 items ajout CM2. Partie « En CE2 » aussi (`outils/dispositifs_ce2/`) ; test CE2 : 6 items CE2.
- **Ouverture des leçons au fur et à mesure (20/10/2026, comme le site de maths)** : une leçon s'ouvre à la date de sa ceinture
  pour sa classe et le reste ensuite. Dates prévues : `OUVERTURE_PREVUE` dans `index.html` = premier jour de la période de la ceinture
  (colonne « Période » du fichier « Langue - ceintures » du tableau de bord), calculé par `node outils/ouvertures_site.mjs ../ressources`
  (à relancer après tout changement de ce fichier). **Depuis le 10/11/2026 (demande de l'enseignante : plus de dépôt régulier), seules les dates prévues
  comptent** : `ouvertures.json` (sur La Forge) ne porte plus que le nom et la photo de l'école et les classes montrées (⚙ Réglages des cartes) ; ses dates éventuelles sont ignorées ;
  en cas d'écart avec la classe, la clé 🔑. Leçon fermée : « s'ouvrira le … » ;
  pastille « nouveau » pendant 7 jours. Plus de codes de période ni de `?enseignant`.
  Accès enseignant : bouton 🔑 du bandeau et mot de passe, le même que sur le site de maths (connu de l'enseignante, jamais écrit dans le dépôt ;
  empreinte `MDP_ENS`, à recalculer avec `empreinteEns("…")` sur les deux sites pour le changer) : tout s'ouvre jusqu'à la fermeture de l'onglet.
- Photo / nom de l’école (13/11/2026) : ils ne sont vus des élèves qu’une fois `ouvertures.json` publié ; `outils/publier-forge.sh` reprend tout seul le fichier téléchargé depuis ⚙ Réglages (le plus récent de ~/Téléchargements, s’il est plus récent que celui de La Forge) et la fenêtre Réglages avertit tant que le brouillon diffère du publié (`nonPublie`).
- Bandeau (comme le site de maths) : Sommaire et titre à gauche ; ◀ ceinture de la leçon ▶ au centre (sur le sommaire : nombre de leçons ouvertes) ;
  classe (CE2 / CM1 / CM2, `data-classe` : sur une leçon, ouvre la leçon du même code dans cette classe) et impression à droite.
  ◀ ▶ ne parcourent que les leçons ouvertes de la classe (`parcours()`). L'adresse `#G1` (lien du tableau de bord) ouvre la leçon G1 de la classe choisie ; `#G1&niveau=CE2` celle de cette classe ;
  une ceinture absente de la classe demandée ouvre la leçon d'une autre classe qui l'a (21/10/2026).
- Sommaire par classe : boutons CE2 / CM1 / CM2 (adresse `#niveau=CE2`…). Une leçon sans champ `niveau`
  est rangée en CM1 ; pour une leçon d'une autre classe, ajouter `niveau:'CE2'` ou `niveau:'CM2'` dans `TRACES`.
- Page d’une leçon (13/11/2026, demande de l’enseignante) : plus d’en-tête (ceinture + titre + « Clique sur une partie… »), redondant avec le titre du nuage ; le titre reste dans un `<h2 class="vh">` (lecteurs d’écran).
- Cartes de G2 (13/11/2026) : les trois (`G2`, `G2-CE2`, `G2-CM2`) sont fabriquées par `outils/lecons/g2_cartes.py` (même apparence ; dessins des enfants et pictos = images découpées de la carte CM1 d’origine, `outils/img/g2/*.png`, jamais redessinés). `python3 outils/lecons/g2_cartes.py`, puis copier `outils/sortie/G2*_carte.jpeg` dans `images/`. Couleurs soutenues comme G1 (`PALG`, option `pal` de `build`, classe `.box.tint`) ; seuls le sujet (bleu souligné) et le verbe (rouge) sont en couleur, titres et mots forts en noir (demande du 13/11/2026) ; note « À retenir » et duo d’enfants (repris de G1) retirés le 13/11/2026 (page surchargée) ; images `outils/img/g2/ampoule.png`, `duo.png` découpées de G1, `extra_html` de `build`) ; nuage central descendu (`cloud_dy=26`), numéros des zones à l’intérieur du cadre (CSS `.zone .num`, en haut à gauche). Cadres pleins = zones cliquables : option `ext` de `build` (mapgen.py : le haut du cadre monte de `ext` px, le titre est posé à l’intérieur, `hstyle=top:30px`), zones de G2 = cadres exacts.
- CM2 : mêmes numéros, mêmes couleurs, mêmes notions qu'en CM1 (choix de l'enseignante, octobre 2026).
  Une leçon CM2 (id `XX-CM2`, code affiché `XX`) = la leçon CM1 + les écrans de `CM2_PLUS` (étiquette « CM2 »,
  placés après le dernier écran de leur section) + un encadré « En CM2, j'apprends aussi » sous la carte.
  Fabriqués par `outils/lecons/cm2_ajouts.py`, mis dans le site par `outils/inserer_cm2.py`. Liste : `CM2_COPIE` ;
  l'étiquette « CM1 » de la carte est recouverte par « CM2 » (`CHIP_CM2`). C8 (plus-que-parfait, marron) et
  C9 (passé simple, noire ; un numéro de ceinture = une couleur quel que soit le niveau, 12/11/2026 : avant, rouge et violette comme C6 et C7) n'existent qu'en CM2 (`outils/lecons/c8_c9_cm2.py`, ids `C8-CM2`, `C9-CM2` ; anciens codes C6 et C7 jusqu'au 27/10/2026, numérotation du tableau de bord). Détail : `programmes/ecarts-CM1-CM2.md`.
- CE2 : mêmes numéros, mêmes couleurs, mêmes notions, en plus simple. Une leçon CE2 (id `XX-CE2`) = la leçon CM1
  sans les écrans listés dans `retirer`, + les écrans de `CE2_PLUS` (étiquette « CE2 ») + un encadré « Au CE2, je retiens » ;
  les zones de la carte sans écran sont masquées. Fabriqués par `outils/lecons/ce2_ajouts.py`, mis dans le site par
  `outils/inserer_cm2.py CE2`. Pas d'homophones au CE2. `retirer` : numéros d'écrans CM1 au 17/10/2026
  (`outils/lecons/titres_cm1_ref.json`) ou titres d'écrans ; le site compare les titres. Ceintures du CE2 : C6 et C7 (verbes irréguliers, sortis de C1-C5) ; au CM1 aussi (27/10/2026) : mêmes leçons, ids `C6` et `C7` (carte « … — CM1 »), fabriquées avec les
  leçons CE2 par `outils/lecons/ce2_seulement.py`. CE2 seulement : O7 (sons « o », « é », « è » et accents). Vue d'ensemble : `programmes/ceintures-trois-niveaux.html`.
- **Carte de rubrique (08/11/2026, demande de l'enseignante : navigation plus explicite dans chaque onglet)** : un clic sur une zone de la carte principale (la barre « 1 › 2 › … » sous la carte a été retirée le 13/11/2026 : elle ne servait à rien) ouvre d'abord une petite carte mentale de la rubrique (`renderSectionMap`, adresse `#t=G2/s:neg`) : au centre le nom de la rubrique,
  en liste (jamais en rond : décision du 09/11/2026), un bloc par écran avec « 👀 Je regarde » (écran) et « ✏️ À toi ! » (adresse `#t=G2/3?atoi` : ouvre l'écran avec l'exercice déjà lancé). Les écrans ont un lien
  vers leur rubrique (fil d'Ariane et bouton 🧭 dans la barre du bas) ; la carte de rubrique n’a plus que le bouton « Carte de la leçon » en haut à droite (09/11/2026). Pour toutes les leçons, sans fichier à fabriquer.
- **Exercices selon la classe (08/11/2026)** : G1 à G7, V1 à V6, H1 à H7, O1 à O6, C1 à C9 ont des phrases différentes en CE2 (exercices de base : `atoi` + `plus`), CM1 (`NIV_ATOI[id][2]`) et CM2 (`NIV_ATOI[id][3]`), sans bouton : le niveau suit la classe de la leçon (`niveauDe(t)`). Un écran sans `niv` garde les mêmes exercices pour tous. À étendre aux autres leçons si l'enseignante le demande.
- Carte de rubrique, présentation (09/11/2026) : bandeau d'accueil avec le personnage et des étoiles de progression (une par écran réussi), étapes en liste avec grosse pastille numérotée, gros bouton « Je regarde » et petit « À toi ! » ; l'étape à faire est mise en avant (`.suivant`), les étapes réussies en vert (`.fait`).
- **« À toi ! » (09/11/2026)** : moteur `startAtoi` dans `index.html`. Une série = les exercices de la classe (`atoi` + `plus` ou `NIV_ATOI`) + au plus deux exercices variés fabriqués automatiquement à partir d'eux :
  « remets les mots dans l'ordre » (type `o`, puces `.mot` avec `data-n` = place dans la phrase) et « dictée à trous » (type `s`, champ `#saisie` avec `data-attendu`). Un exercice raté revient plus loin (« à revoir »).
  Indice en deux temps (bouton 💡, puis réponse expliquée et mise en évidence `.montre` après deux erreurs). Personnage qui commente (`#fb`), étoile `.etoile-pop`, sons (WebAudio, préférence `atoi-son`), 🔊 Écouter (voix du navigateur), barre `#exProg`, bilan.
  `outils/tester.py` sait jouer ces types et tourne avec `reduced_motion` (sinon les boutons animés sont « instables » pour Playwright).
- Pas de noms d'élèves dans le dépôt : il est public.

## Outils

- Pour reprendre le travail : lire `RESUME.md` (où en est-on) puis `IDEES-EN-ATTENTE.md`.
- Avant chaque envoi qui touche aux leçons : `python3 outils/tester.py tout` doit répondre « TOUT EST BON ».
- Le dossier `outils/` contient les programmes qui fabriquent les cartes, les écrans, les exercices et les fiches
  du cahier de progrès. Mode d'emploi : `outils/LISEZMOI.md`.

## Homophones (Dispositif 1 bis — voir « Structure des ceintures EDL », page « Principes », dépôt `ressources`)

- Règle non négociable : jamais deux mots d'une même paire jumelle dans la même ceinture (H1 à H7).
  Le jumeau n'est jamais proposé comme choix ni comme réponse, et n'apparaît pas dans les phrases.
- Chaque mot s'ancre dans sa classe grammaticale et se prouve par une manipulation (« Je prouve »),
  jamais par un « truc » appris par cœur.
- Plus de ceinture de transfert H8 (ni de C8 en conjugaison), retirées le 20/10/2026, choix de l'enseignante :
  les paires ne se retrouvent dans aucune ceinture ; la révision se fait dans l'entraînement spiralé de chaque ceinture.
- Mots ajoutés en CM2 : qu'elle (H2), sans (H3), donc (H4), dont (H5), quel/quelle (H6), s'en (H7) ;
  leurs jumeaux restent dans une autre ceinture. Vérifier avec `outils/jumeaux.py`.
- Pas de ceintures d'homophones au CE2 (hors programme du cycle 2, décision d'octobre 2026) : elles commencent au CM1.

## Orthographe (Dispositif 2 — version à ceintures)

- Rubrique « Orthographe » du site : ceintures O1 à O6, avec test de validation comme les autres dispositifs.
- Code couleur : %…% surligne en jaune les lettres étudiées, |…| entoure la lettre qui décide (celle qui suit).
- Les exercices complètent le mot avec `fill:'hl'` (la lettre choisie apparaît surlignée, collée au mot).
- Pas de termes savants pour les élèves (« le son », « la lettre », « devant », « un mot de la même famille »).
- Cahier de progrès : `Cahier de progrès cm1/O - cahier de progrès.odt` (CM1 = parcours B dans les cahiers).
