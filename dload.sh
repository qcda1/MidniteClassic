#!/bin/bash

REPO="https://raw.githubusercontent.com/qcda1/MidniteClassic/refs/heads/main/"
FILES=("classic_modbusdecoder.py" "Payload.py")  # Liste des fichiers à télécharger

for file in "${FILES[@]}"; do
    if [ -f "$file" ]; then
        # Supprimer l'ancien backup s'il existe
        [ -f "$file.bak" ] && rm "$file.bak"
        
        # Renommer l'ancien fichier en .bak pour conserver la date/heure
        mv "$file" "$file.bak"
    fi
    
    echo "Downloading $file..."
    curl -o "$file" "$REPO/$file"
done

echo "Done !"

