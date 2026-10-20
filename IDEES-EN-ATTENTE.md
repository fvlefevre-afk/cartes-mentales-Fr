# Idées en attente

Propositions faites pendant le travail, auxquelles il n'a pas encore été répondu.
Rayer ou supprimer une ligne une fois la décision prise.

## Leçons

- [ ] **G4 – « Mais où est donc Ornicar ? »** : la carte G4 cite cette phrase, qui contient les jumeaux *où* et *est*.
  La retirer pour appliquer la même prudence qu'en homophones ?
- [ ] **G6 – couleurs** : le complément d'objet est en vert et le complément circonstanciel en orange,
  les mêmes couleurs que l'adjectif et le déterminant en G3. Garder, ou choisir d'autres couleurs ?
- [ ] **G7 – écran « Avec avoir, c'est différent »** : ajouté pour éviter que les élèves accordent partout.
  Le garder, ou le réserver à C4 (passé composé avec avoir) ?

## Orthographe (Dispositif 2, nouvelle version à ceintures)

- [ ] **Créneau** : où placer les 30 min d'entraînement collectif et les fiches (par exemple à côté de la dictée) ?
- [ ] **Ceinture O7 (Marron)** : ajouter une ceinture de transfert en dictée, comme H8 et C8 ?
- [ ] **Jeux du pack sans ceinture** : noms en [e] / [té] (Ortho Mémo), mots en ac / af / ap (Les tournesols) :
  les laisser hors ceintures, ou en faire des ceintures ?
- [ ] **Cahier « conjugaison 2026 – A REFAIRE »** : la partie CM1 a été remise à jour (C1 à C5 et C8).
  Les parties CE2 et CM2 n'ont pas été touchées. Faut-il aussi les revoir ?

## Réglages du site

- [ ] **Blocage par période** : toutes les leçons sont ouvertes provisoirement (`TOUTES_LES_CARTES=true`).
  Quand faut-il remettre le blocage par période ?
- [ ] **Accès enseignant provisoire** (`?enseignant` à la fin de l'adresse) : le garder ou le retirer ?
- [ ] **Alléger la page** : ranger les images des cartes mentales dans un dossier `images/` au lieu de les
  intégrer dans `index.html` (page plus légère, cartes remplaçables à la main).

## GitHub et Claude

- [ ] **Inviter `gigi75lefevre-collab`** comme collaborateur du dépôt (Settings → Collaborators).
- [ ] **Supprimer l'ancien dépôt** resté sur le compte `gigi75lefevre-collab`, pour ne pas confondre les deux.
- [ ] **Autoriser le site education.gouv.fr** dans les réglages de Claude (rubrique Capacités), pour que Claude
  puisse télécharger lui-même les documents officiels.

## Faire comme sur le site de maths (proposition du 20/10/2026)

- [ ] **Ouverture au fur et à mesure** : chaque leçon s'ouvre à sa date (dates prévues + fichier `ouvertures.json` fabriqué
  par le tableau de bord), pastille « nouveau » 7 jours, page fermée « s'ouvrira le … », accès enseignant par bouton 🔑 et
  mot de passe. Remplacerait `TOUTES_LES_CARTES`, `PERIODE_FICHIER` et `?enseignant`.
- [ ] **Même bandeau que les maths** : Sommaire, ◀ ceinture ▶ (seulement les leçons ouvertes de la classe), CE2 / CM1 / CM2, 🖨.
- [ ] **Codes en double** : C6 et C7 n'ont pas le même sens au CE2 (verbes irréguliers) et au CM2 (plus-que-parfait,
  passé simple). En maths, un même code = une même compétence dans les trois classes. Renuméroter ?
- [ ] **Un fichier de référence unique des ceintures** (comme `architecture_ceintures.py` en maths) d'où sortent le site,
  les cahiers de progrès et le fichier « Langue - ceintures » du tableau de bord.
- [ ] **Test automatique de toutes les leçons** aux trois niveaux, et un fichier `RESUME.md` pour reprendre le travail.
