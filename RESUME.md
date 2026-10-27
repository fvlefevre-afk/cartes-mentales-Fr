# Où en est-on ? (résumé pour reprendre dans un nouveau chat)

Dernière mise à jour : 23/10/2026. Lire aussi `CLAUDE.md` (règles du projet), `IDEES-EN-ATTENTE.md` (questions en attente)
et `outils/LISEZMOI.md` (mode d'emploi des outils).
Deux dépôts : celui-ci (`fvlefevre-afk/cartes-mentales-Fr`, branche `main`, site publié avec GitHub Pages) et le tableau de bord
(`fvlefevre-afk/ressources`, branche `branche-propre` **uniquement**). Le site de maths (`fvlefevre-afk/cartes-mentales-maths`) sert de modèle.
Répondre à l'enseignante en français, avec des mots simples. Dépôt public : jamais de noms d'élèves, jamais le mot de passe enseignant.

## L'essentiel
- **Site des leçons interactives de français**, trois classes : CE2 (27 leçons), CM1 (31), CM2 (33).
  Une leçon = une carte mentale cliquable + des écrans animés + des exercices « À toi ! ».
- **Ceintures** : G (grammaire), H (homophones, CM1 et CM2 seulement), C (conjugaison), V (vocabulaire), O (orthographe).
  Même code, même couleur, même notion dans les trois classes ; le CE2 en plus simple, le CM2 avec des écrans en plus.
  Exceptions : C6 et C7 (contenu différent au CE2 et au CM2, voir « En attente »), O7 (CE2 seulement).
- **Leçons CE2 et CM2 fabriquées à partir du CM1** : modifier une leçon CM1 change aussi ses versions CE2 et CM2.
- **Ouverture au fil de l'année** : chaque leçon s'ouvre à la date de sa ceinture (dates du tableau de bord) ; bouton 🔑 pour tout ouvrir.
- **Images** dans `images/` (cartes `G4.jpg`…, personnages) ; `index.html` ne garde que leur chemin (page de 0,4 Mo).

## Décisions de l'enseignante
- 20/10/2026 : ceintures de transfert H8 et C8 retirées ; leçons ouvertes au fur et à mesure, comme en maths.
- 23/10/2026 :
  - G4 : phrase « Mais où est donc Ornicar ? » retirée (elle montrait où / est à côté de ou / et).
  - G6 : compléments d'objet en indigo, compléments circonstanciels en marron (plus le vert de l'adjectif ni l'orange du déterminant).
  - G7 : écran « Avec avoir, c'est différent » gardé.
  - Orthographe : entraînement dans les 3 créneaux d'orthographe de la semaine (mardi, jeudi, vendredi) ;
    jeux Ortho Mémo et Les tournesols hors ceintures.
  - Cahier « Ceintures de conjugaison 2026 » : parties CE2 et CM2 à jour, « A REFAIRE » retiré du nom.
  - Images sorties de la page (dossier `images/`).

## Les fichiers
| Fichier ou dossier | Contenu |
|---|---|
| `index.html` | tout le site (leçons, écrans, exercices) |
| `images/` | cartes mentales et personnages |
| `outils/lecons/*.py` | une leçon CM1 par script ; `cm2_ajouts.py`, `ce2_ajouts.py` (versions CM2, CE2) ; `c6_c7_cm2.py`, `ce2_seulement.py` |
| `outils/inserer.py`, `outils/inserer_cm2.py` | mettent une leçon dans le site |
| `outils/tester.py` | teste les leçons (voir ci-dessous) |
| `outils/cahiers.py`, `outils/cahiers_donnees.py` | cahiers de progrès |
| `outils/dispositif2.md`, `outils/dispositifs_ce2/`, `outils/dispositifs_cm2/` | textes des dispositifs (orthographe, parties « En CE2 » et « En CM2 ») |
| (dépôt `ressources`) `Documents explicatifs des dispositifs ce2-cm1-cm2/` | les dispositifs de l'enseignante (référence ; dossier de ce dépôt retiré le 27/10/2026) |
| `Cahier de progrès cm1/`, `Cahier de progrès - CE2 - CM1 - CM2/` | cahiers de progrès |
| `programmes/` | programme du cycle 3, écarts CM1-CM2, vue des trois niveaux |

## Tester
- `python3 outils/tester.py tout` : toutes les leçons des trois classes (environ 10 min) ; `python3 outils/tester.py tout CE2` : une classe ;
  `python3 outils/tester.py G4 G4-CE2` : quelques leçons. Joue chaque animation et chaque exercice, vérifie les images ;
  la date est mise au 30 juin pour que toutes les leçons soient ouvertes. Résultat attendu : « TOUT EST BON ».
- Il faut Playwright pour Python, de la même version que le Chromium installé (dans les sessions Claude : `pip install playwright==1.63.0`).

## En attente (détail dans `IDEES-EN-ATTENTE.md`)
- Codes en double C6 / C7 : au CE2 ce sont les verbes irréguliers, au CM2 le plus-que-parfait et le passé simple.
- Un fichier de référence unique des ceintures (comme en maths). Vu le 23/10/2026 : dans le tableau de bord, les fiches de conjugaison
  CE2 et CM2 (`C_FICHES`, `17d-suivi-evaluations.js`) suivent encore l'ancienne numérotation.
