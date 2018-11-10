


------------------------------------------------------------------------------------
Bonjour Alain,

Pour démarrer le projet Django on installe d'abord Python

---sur Linux "sudo apt-get install python" #Vous aurez la version "2.7.x"

j'ai fait mon projet dessus puis on installe pip avec la commande "sudo easy_install pip"

---sur mac on part dans le site web de python on download python --v 2.7.x
pendant l'installation on coche la partie "pip" pour que ça l'installe avec si on a déjà fait cette étape on utilise "easy_install pip "
pour installer pip et aussi
si on a la partie environnement virtuelle on la coche aussi

on décompresse l'archive adixon.

Tu as un fichier SQL dans le dossier "DOC" du dossier source adixon on l'exécute avec phpMyAdmin dans la partie "import" il va te créer une base de données "adixon" et un utilisateur "ibrahima" avec le mot de passe "ibrahima" qui a access seulement à la base de données adixon.

On utilise la terminale pour activer l'environnement virtuelle du projet avec la commande sur la terminale "source django/bin/activate" pour le désactiver on écrit 'deactivate'

Et maintenant dans l'invite de commande tu écris "python manage.py runserver" et on écrit dans le navigateur "127.0.0.1:8000" et le projet django est lancer

NB: j'ai créé un environnement de développement avec virtualenv de python pour que tu n'ai peu d'installation à faire normalement.

Désoler du retard j'avais eu un petit souci avec mon trigger qui ne faisait pas ce que je voulais mais c'est réglé

-------------------------------------------------------------------------------------------
