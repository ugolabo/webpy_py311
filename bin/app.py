"""
Moteur de Jeu Multilingue GothonWeb.

Ce module implémente le moteur de jeu web pour l'aventure "Starship Survivor"
en utilisant le framework web.py. Il gère :
1. La création et la persistance des sessions utilisateur via des fichiers JSON.
2. La gestion du changement de langue (Français et Anglais).
3. Le traitement des requêtes GET (affichage de la pièce) et POST (action utilisateur).
4. La navigation dans la carte du jeu (gothonmap.map).
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Définir la configuration de l'interpréteur Python et de l'encodage


import sys
import os
import json
import uuid

# --- Configuration et Initialisation ---

# Obtenir le chemin absolu du répertoire de app.py
current_dir = os.path.dirname(os.path.abspath(__file__))
# Déterminer le répertoire parent du projet (assumé)
project_root = os.path.dirname(current_dir)

# Vérifier et créer le répertoire 'sessions' s'il n'existe pas
sessions_dir = os.path.join(project_root, 'sessions')
if not os.path.exists(sessions_dir):
    # Créer le répertoire pour stocker les fichiers de sessions
    os.makedirs(sessions_dir)

# Ajouter le répertoire racine à sys.path pour pouvoir importer gothonmap
if project_root not in sys.path:
    sys.path.append(project_root)

# Importer le framework web et le fichier de la carte du jeu
import web
from gothonmap import map


# --- Fonctions d'Aide pour la Gestion des Sessions (Fichiers JSON) ---

def get_session_file_path(session_id):
    """Retourne le chemin complet vers le fichier de session JSON."""
    return os.path.join(sessions_dir, f"{session_id}.json")


def load_session_data(session_id):
    """
    Charge les données de session depuis un fichier JSON.

    Args:
        session_id (str): L'identifiant unique de la session.

    Returns:
        dict or None: Les données de session chargées ou None en cas d'échec/absence.
    """
    file_path = get_session_file_path(session_id)
    if os.path.exists(file_path):
        try:
            with open(file_path, 'r') as f:
                content = f.read()
                return json.loads(content) if content else None
        except json.JSONDecodeError as e:
            # En cas d'erreur de décodage, imprimer l'erreur et retourner None
            print(f"Erreur de décodage JSON pour la session {session_id}: {e}")
            return None
    return None


def save_session_data(session_id, data):
    """
    Sauvegarde les données de session dans un fichier JSON.

    Args:
        session_id (str): L'identifiant unique de la session.
        data (dict): Les données à sauvegarder.
    """
    file_path = get_session_file_path(session_id)
    with open(file_path, 'w') as f:
        json.dump(data, f)


def initialize_or_reset_session(lang):
    """
    Gère la création/réinitialisation d'une session.

    Crée une nouvelle session si l'ID n'existe pas ou si la langue change.
    Sinon, réinitialise simplement la pièce de la session existante à START.

    Args:
        lang (str): La langue de la session ('en' ou 'fr').

    Returns:
        str: L'ID de session.
    """
    start_room_tag = map.START.tag
    session_id = web.cookies().get('my_session_id')
    session_data = None

    if session_id:
        session_data = load_session_data(session_id)

    # Créer une nouvelle session si nécessaire
    if not session_id or not session_data or session_data.get("lang") != lang:
        session_id = str(uuid.uuid4())
        session_data = {"room": start_room_tag, "lang": lang}
        web.setcookie('my_session_id', session_id, expires = 3600)
    else:
        # Réinitialiser la pièce pour une nouvelle partie dans la même langue
        session_data["room"] = start_room_tag
        session_data["lang"] = lang

    save_session_data(session_id, session_data)
    return session_id


# --- Définition des URLs et de l'Application ---

urls = (
    "/", "Index",
    "/en", "IndexEn",
    "/fr", "IndexFr",
    "/game_en", "GameEngineEn",
    "/game_fr", "GameEngineFr"
)

app = web.application(urls, globals())


# --- Moteurs de Rendu des Templates ---

template_path = os.path.join(project_root, "templates")
render_en = web.template.render(template_path, base = "layout")
render_fr = web.template.render(template_path, base = "layout")


# --- Classes de Gestion des Index ---

class Index():
    """Gère la route racine '/' et redirige vers l'accueil en anglais par défaut."""
    def GET(self):
        """Redirige le chemin racine ('/') vers le point d'entrée anglais ('/en')."""
        raise web.seeother("/en")


class IndexEn():
    """Initialise la session de jeu en anglais et redirige vers le moteur de jeu."""
    def GET(self):
        """Initialise la session de jeu en 'en', puis redirige vers /game_en."""
        initialize_or_reset_session(lang = "en")
        raise web.seeother("/game_en")


class IndexFr():
    """Initialise la session de jeu en français et redirige vers le moteur de jeu."""
    def GET(self):
        """Initialise la session de jeu en 'fr', puis redirige vers /game_fr."""
        initialize_or_reset_session(lang = "fr")
        raise web.seeother("/game_fr")


# --- Classe de Base pour le Moteur de Jeu (Logique Partagée) ---

class GameEngineBase():
    """
    Classe de base contenant la logique de jeu commune pour les deux langues (GET et POST).
    """
    # Attributs surchargés par les classes enfants (lang, render, next_url)
    lang = None
    render = None
    next_url = None

    def GET(self):
        """
        Affiche la pièce actuelle.

        Charge la session, vérifie la langue, récupère l'objet Room correspondant
        au tag de session, et utilise le moteur de rendu approprié. Redirige si
        la session est manquante ou invalide.
        """
        session_id = web.cookies().get('my_session_id')
        session_data = load_session_data(session_id)

        # Vérification et redirection si la session est invalide ou non conforme
        if (not session_id or not session_data or
            session_data.get("lang") != self.lang or not session_data.get("room")):
            raise web.seeother(f"/{self.lang}")

        # Charger l'objet Room réel
        current_room = getattr(map, session_data['room'])

        # Utiliser le moteur de rendu spécifique à la langue
        if self.lang == "en":
            return self.render.show_room_en(room = current_room, session = session_data)
        elif self.lang == "fr":
            return self.render.show_room_fr(room = current_room, session = session_data)

    def POST(self):
        """
        Traite l'action utilisateur.

        Récupère l'action de l'utilisateur, demande à la pièce actuelle de
        déterminer la pièce suivante, met à jour le tag 'room' dans la session
        si un mouvement a eu lieu, sauvegarde la session, et redirige vers
        la méthode GET (Pattern PRG).
        """
        form = web.input(action = None)
        session_id = web.cookies().get('my_session_id')
        session_data = load_session_data(session_id)

        # Vérification des données entrantes et de la session
        if (not session_data or not session_data.get('room') or not form.action or
            session_data.get('lang') != self.lang):
            # Redirection vers l'affichage de la pièce actuelle en cas d'erreur
            raise web.seeother(self.next_url)

        # Récupérer l'objet Room actuel
        current_room = getattr(map, session_data['room'])

        # Déterminer la pièce suivante
        next_room = current_room.go(form.action)

        if next_room:
            session_data['room'] = next_room.tag

        # Sauvegarder l'état (même si la pièce n'a pas changé)
        save_session_data(session_id, session_data)

        # Rediriger vers le GET pour l'affichage (Pattern PRG)
        raise web.seeother(self.next_url)


# --- Classes Spécifiques au Moteur de Jeu (Surcharge des Attributs) ---

class GameEngineEn(GameEngineBase):
    """Moteur de jeu pour la version anglaise."""
    lang = "en"
    render = render_en
    next_url = "/game_en"


class GameEngineFr(GameEngineBase):
    """Moteur de jeu pour la version française."""
    lang = "fr"
    render = render_fr
    next_url = "/game_fr"


# Bloc d'exécution principal
if __name__ == "__main__":
    web.config.debug = True
    app.run()
