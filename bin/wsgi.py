"""
Gestionnaire WSGI (Web Server Gateway Interface).

Ce fichier est le point d'entrée principal pour le déploiement de l'application
sur un serveur web compatible WSGI (comme Gunicorn ou uWSGI). Il initialise
l'environnement Python et expose l'objet `application` créé par web.py,
permettant au serveur de traiter les requêtes HTTP.
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys
import os


# Déterminer le répertoire du projet de manière dynamique.
# Ceci calcule le chemin du répertoire où se trouve ce fichier (wsgi_handler.py).
# L'ajouter à sys.path permet à Python de trouver des modules comme 'bin.app'.
# Obtenir le chemin absolu du répertoire de ce fichier
current_dir = os.path.dirname(os.path.abspath(__file__))
# Définir le chemin comme le répertoire actuel
path = current_dir

# Vérifier si le chemin du projet est déjà dans sys.path
if path not in sys.path:
    # Ajouter le chemin du projet à sys.path
    sys.path.append(path)

# Importer l'objet application depuis le module 'app' situé dans 'bin'
from bin.app import app

# Créer l'objet WSGI (Web Server Gateway Interface)
# L'objet 'application' est celui qui sera utilisé par le serveur web (comme Gunicorn ou Apache/mod_wsgi)
application = app.wsgifunc()
