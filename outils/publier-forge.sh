#!/bin/bash
# Publie les cartes interactives de français sur La Forge : copie index.html, images/ et polices/ dans ../publication-francais (dépôt qui ne contient que le site) puis l'envoie.
# À lancer depuis n'importe où : bash outils/publier-forge.sh
set -e
ICI="$(cd "$(dirname "$0")/.." && pwd)"; PUB="$ICI/../publication-francais"
[ -d "$PUB/.git" ] || { echo "Dossier publication-francais introuvable à côté de ce dépôt."; exit 1; }
cd "$PUB" && git pull -q --rebase forge main      # reprend ouvertures.json s'il a été déposé sur La Forge
# ouvertures.json téléchargé depuis ⚙ Réglages (photo et nom de l'école, classes montrées) : le plus récent de « Téléchargements », s'il est plus récent que celui de La Forge
DL=$(ls -t "$HOME"/Téléchargements/ouvertures*.json "$HOME"/Downloads/ouvertures*.json 2>/dev/null | head -1)
if [ -n "$DL" ] && { [ ! -f "$PUB/ouvertures.json" ] || [ "$DL" -nt "$PUB/ouvertures.json" ]; } && python3 -c "import json,sys; j=json.load(open(sys.argv[1])); assert isinstance(j,dict) and 'classes' in j" "$DL" 2>/dev/null; then
  cp "$DL" "$PUB/ouvertures.json" && echo "ouvertures.json repris de : $DL (photo et nom de l'école, classes montrées)"
fi
cp "$ICI/index.html" "$PUB/index.html"
rm -rf $PUB/images && cp -r $ICI/images $PUB/images
rm -rf $PUB/polices && cp -r $ICI/polices $PUB/polices      # police Andika (10/11/2026) : sans ce dossier, les cartes s’affichent dans une autre police
cp "$ICI/.gitlab-ci.yml" "$PUB/.gitlab-ci.yml"           # la publication copie aussi polices/ dans la page en ligne
cd "$PUB" && git add -A
if git diff --cached --quiet; then echo "Rien à publier : le site en ligne est déjà à jour."; exit 0; fi
git commit -q -m "Mise à jour du site" && git push forge main && echo "Publié : le site se met à jour en 1 à 2 minutes."
