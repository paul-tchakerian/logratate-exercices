# logratate-exercices

Vous allez réaliser un script de backup de tous les fichiers du répertoire $HOME de
chacun des utilisateurs de votre système offrant ces différentes possibilités:
- Fichiers créés depuis moins de 7 jours
- Fichiers modifiés depuis plus de 7 jours
- Répertoires dont le contenu est > 10 Mo
- Répertoire et fichiers cachés
Les répertoires et fichiers collectés par votre script seront regroupés dans un .tar.gz
avec le nom de l’utilisateur, l’option choisie et la date et rangés dans le répertoire
/var/backup/. Les backups ne devront être rwx que par l’utilisateur concerné.

Par exemple:
-rw------- 1 john users 99 jun. 30 2023 /var/backup/john-fichiers-moins-7-jours-10-SEP-2023.tar.gz
