#!/bin/bash
# Publie le site sur La Forge : copie index.html et images/ dans ../publication-francais (dépôt qui ne contient que le site) puis l'envoie.
# À lancer depuis n'importe où : bash outils/publier-forge.sh
set -e
ICI="$(cd "$(dirname "$0")/.." && pwd)"; PUB="$ICI/../publication-francais"
[ -d "$PUB/.git" ] || { echo "Dossier publication-francais introuvable à côté de ce dépôt."; exit 1; }
cd "$PUB" && git pull -q --rebase forge main      # reprend ouvertures.json s'il a été déposé sur La Forge
cp "$ICI/index.html" "$PUB/index.html"
rm -rf $PUB/images && cp -r $ICI/images $PUB/images
cd "$PUB" && git add -A
if git diff --cached --quiet; then echo "Rien à publier : le site en ligne est déjà à jour."; exit 0; fi
git commit -q -m "Mise à jour du site" && git push forge main && echo "Publié : le site se met à jour en 1 à 2 minutes."
