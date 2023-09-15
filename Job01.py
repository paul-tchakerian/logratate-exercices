#!/bin/bash

# Répertoire de sauvegarde
backup_dir="/var/backup"

# Obtenez la date actuelle au format jour-mois-année
current_date=$(date +\%d-%b-\%Y)

# Parcourez tous les utilisateurs du système
for user in $(ls /home); do
    # Créez un répertoire de sauvegarde pour chaque utilisateur
    user_backup_dir="$backup/$user"
    mkdir -p "$user_backup"

    # Fichiers créés depuis moins de 7 jours
    find /home/$user -type f -ctime -7 -print0 | tar -czvf "$user_backup/$user-fichiers-moins-7-jours-$current_date.tar.gz" --null -T -

    # Fichiers modifiés depuis plus de 7 jours
    find /home/$user -type f -mtime +7 -print0 | tar -czvf "$user_backup/$user-fichiers-plus-7-jours-$current_date.tar.gz" --null -T -

    # Répertoires dont le contenu est > 10 Mo
    find /home/$user -type d -exec du -sm {} + | awk '$1 > 10' | cut -f2- | tar -czvf "$user_backup/$user-repertoires-plus-10Mo-$current_date.tar.gz" -T -

    # Répertoire et fichiers cachés
    tar -czvf "$user_backup/$user-fichiers-caches-$current_date.tar.gz" --exclude='*/*' /home/$user/.* 2>/dev/null
done


