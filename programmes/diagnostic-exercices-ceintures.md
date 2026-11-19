# Diagnostic des exercices des ceintures de français (16/11/2026)

Mesure faite sur les exercices exportés pour le tableau de bord (103 leçons : chaque ceinture en CE2, CM1 et CM2). **Chiffres indicatifs** : l'export réunit
les exercices de plusieurs classes (environ 10 par écran) ; dans les cartes, chaque classe en montre moins (de l'ordre de 4 par écran pour les ceintures de grammaire).
La conformité au programme n'est pas mesurée automatiquement : elle demande une relecture ceinture par ceinture.

Repères de conformité (programme du cycle 3 du 17/04/2025, annexe du cycle 2, `ecarts-CM1-CM2.md`, cahiers de progrès) :
- G3 : repérer des groupes nominaux « dans une phrase simple » (Dét.+Nom, Dét.+Nom+Adj, Dét.+Adj.+Nom) ; complément du nom, épithète / attribut : CM2 seulement.
- Une phrase d'exercice de CE2 et CM1 : phrase simple, un seul verbe, sujet avant le verbe (sujet inversé = CM2), pas de proposition subordonnée (phrase complexe = CM2), pas de phrase sans verbe en CE2.
- Types de phrases au programme : déclaratives, interrogatives, impératives ; formes négative et exclamative : on peut varier la structure.
- **Jamais d'écriture fausse montrée** (décision du 15/11/2026) : les propositions d'un exercice sont de vraies formes ; une forme inventée devient un trou de quelques lettres.
  Contrôle : un dictionnaire français (`/usr/share/dict/french`) vérifie chaque mot proposé.

## Résultats (par ceinture)

Mesures : exercices identiques = part d'exercices en double dans la leçon (mêmes phrase, réponse et question) ; le « premier mot » n'est PAS un défaut pour des mots à compléter (« un / une ») ; « mince » = 3 exercices par écran.

| Ceinture | Constat | Priorité |
|---|---|---|
| O11 | **3 exercices par écran** (15 par leçon) ; aucun mot répété (le « 93 % même premier mot » des premières mesures était « un / une » : normal pour des mots à compléter ; erreur de lecture corrigée le 16/11/2026) | 1 |
| O2, O4, O6 | 13 à 17 % d'exercices identiques (recontrôlé le 16/11/2026) | 1 |
| O1 | 22 % d'exercices identiques (recontrôlé) ; O3 et O5 : à recontrôler | 2 |
| O7 à O12 | mince (15 à 21 exercices par leçon) | 1 |
| O1, O3, O4, O5, O6 | mêmes exercices en CE2, CM1 et CM2 : pas d'adaptation au niveau | 2 |
| C6, C7 (CE2) | mince (15 à 16 exercices par leçon) | 2 |
| H3, H5 | H3 : 45 % même premier mot ; H5 : 8 % de répétition | 3 |
| V5, V2, V4 | V5 : 50 % même premier mot ; V2 : 26 à 32 % | 3 |
| G1, G4, G5, G6, G7 | variété correcte (10 à 29 % même premier mot) ; conformité à relire | 4 |
| C1 à C5, V1, V3, V6 | peu de répétitions ; environ 4 exercices par écran dans les cartes | 4 |
| G2 | bien fourni ; un tiers des exercices sont des questions sans phrase (normal) | — |
| G3 | en cours : banque de phrases écrites et relues (`outils/lecons/g3_banque.py`) | en cours |

## Contrôle des formes inventées (16/11/2026)

Méthode : chaque mot proposé dans un exercice à choix est comparé à un dictionnaire français (`/usr/share/dict/french`). Les trous de lettres (`fill: circ`),
les prénoms et les mots de moins de 5 lettres sont écartés. Source : les exercices exportés (103 leçons, 6 822 exercices à choix). Un dictionnaire ne remplace pas une relecture :
les « inconnus » ci-dessous sont des formes inventées ou des morceaux de mots à examiner.

| Ceintures | Exercices touchés | Nature |
|---|---|---|
| C1, C2, C3, C4, C6, C7, C9 (conjugaison) — **corrigé le 16/11/2026** (`outils/formes_inventees.py`) | 134 (C1 42, C2 22, C6 20, C7 16, C3 14, C4 12, C9 8) | formes de verbes inventées : « prendent », « achettons », « oublirai », « faireras », « choisé », « allent », « faisez »… |
| G5 — **corrigé le 16/11/2026** | 16 | formes de verbes inventées : « finons », « choisisez », « finisent », « grandent » |
| G7 — **corrigé le 16/11/2026** | 33 | question « Quel GN est bien accordé ? » : choix parmi des groupes nominaux mal accordés |
| G3 (restes) — **corrigé le 16/11/2026** | 4 | un « grose » et 3 « Quel GN est bien accordé ? » dans le premier exercice de certains écrans (hors banque) |
| V5 et V3 — **corrigés le 16/11/2026** | 14 (+ V3) | mots inventés : « repossible », « recontent », « dépatient », « malagréable » |
| V2, V3, V4 | 111 (V3 84, V2 24, V4 3) | surtout des morceaux de mots (« onter », « nteur », « dinier ») : trous de lettres à confirmer |
| O10, O11, O12 | 57 | terminaisons à choisir (« ement / ément / emment », « ssion ») : trous de lettres, normal |
| O3, O5, O6, O7 à O9, C5, C8, G1, G2, G4, G6, H1 à H7, O1, O2, O4, V1, V6 | 0 | rien d'inventé (G2 : « a-t-il » est correct) |

Reste à examiner : V2, V3, V4 (morceaux de mots : sans doute des trous de lettres légitimes), O10 à O12 (terminaisons), G4 (« aujourd »).
Règle de remplacement : de vraies formes à choisir (« Les enfants ___ dehors. » : jouent / joue / jouez), ou un trou de quelques lettres (« Je pou___ai » : rr / r),
ou une question sur la règle avec la forme juste sous les yeux.

## Méthode retenue

Une banque de phrases écrites et relues, écran par écran et classe par classe, plutôt que des phrases fabriquées par programme (le sens n'est pas garanti).
Validation par l'enseignante écran par écran. Structures variées (pas toujours sujet, verbe, complément).

## Point du 19/11/2026 (ceintures O)

- **O7 (CE2), O8, O9, O10, O11, O12 : banques d'exercices écrites et intégrées** (`outils/lecons/o7_banque.py` … `o12_banque.py`, contrôles communs `banque_o.py` :
  mot recomposé cherché au dictionnaire, aucun exercice repris de la leçon, « À toi ! » compris, aucun signe phonétique). 9 à 15 exercices par écran au lieu de 3.
  Le dictionnaire ne suffit pas : « une ass___tte » donnait « assette » (mot du dictionnaire) au lieu d'« assiette » ; relire chaque mot recomposé (`python3 oN_banque.py`).
- **Doublons d'O1 à O6 : mesure à corriger.** Les « 13 à 22 % » additionnaient les trois classes. Or, quand une leçon a des séries par classe (`NIV_ATOI`), le CE2 voit
  l'« À toi ! » + les exercices en plus, le CM1 la série 2, le CM2 la série 3 (index.html, `startAtoi`) : un même exercice dans deux séries n'est jamais vu par le même élève.
  Recompté classe par classe : un seul cas, O1 au CE2 (« e___mener », « un ta___bour » aux écrans 2 et 6) → écran 6 « Attention ! » : « une bo___bonne », « néa___moins ».
- **O1, O3, O4, O5 « mêmes exercices en CE2, CM1 et CM2 » : réglé** (séries différentes par classe depuis cec952d).
- **Reste** : O1 à O6 n'ont que 3 ou 4 exercices par écran et par classe (O7 à O12 : 9 à 15).
