"""
Définition de la carte du jeu et de la structure des pièces.

Ce module contient la classe Room, qui représente une pièce unique dans le jeu
d'aventure, ainsi que la définition concrète de toutes les pièces, leurs
descriptions multilingues et leurs règles de transition (chemins).
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Room():
    """
    Représente une pièce (salle) dans le jeu.

    Contient son état, sa description multilingue et les chemins
    possibles vers d'autres pièces.
    """

    def __init__(self, tag, name_en, name_fr, description_en, description_fr, complement_en, complement_fr,
                 choices_en = None, choices_fr = None, img_one = None, img_two = None):
        """
        Initialise un objet Room avec toutes ses propriétés.

        Args:
            tag (str): Le tag unique de la pièce (clé de référence).
            name_en (str): Le titre de la pièce en anglais.
            name_fr (str): Le titre de la pièce en français.
            description_en (str): La description principale en anglais.
            description_fr (str): La description principale en français.
            complement_en (str): Texte complémentaire/épilogue en anglais.
            complement_fr (str): Texte complémentaire/épilogue en français.
            choices_en (str, optional): Les options d'action en anglais.
            choices_fr (str, optional): Les options d'action en français.
            img_one (str, optional): Chemin vers la première image (principale).
            img_two (str, optional): Chemin vers la seconde image (icône/vignette).
        """
        # Définir le tag unique (utilisé comme clé de référence)
        self.tag = tag

        # --- ATTRIBUTS ANGLAIS ---
        self.name_en = name_en
        self.description_en = description_en
        self.complement_en = complement_en
        self.choices_en = choices_en

        # --- ATTRIBUTS FRANÇAIS ---
        self.name_fr = name_fr
        self.description_fr = description_fr
        self.complement_fr = complement_fr
        self.choices_fr = choices_fr

        # --- IMAGES ---
        self.img_one = img_one
        self.img_two = img_two

        # Initialiser le dictionnaire des chemins vers d'autres pièces
        self.paths = {}

    def go(self, direction):
        """
        Détermine la pièce suivante basée sur l'action donnée par l'utilisateur.

        Gère les correspondances exactes et le chemin de remplacement ('*').

        Args:
            direction (str): L'entrée de l'utilisateur.

        Returns:
            Room or None: L'objet Room suivant ou None si aucun chemin trouvé (sauf '*').
        """
        # Normaliser l'entrée (supprimer les espaces et convertir en minuscule)
        direction = direction.strip().lower()

        # Tenter d'obtenir une correspondance exacte (pour '132', 'a', 'b', etc.)
        next_room = self.paths.get(direction)

        # Vérifier si une correspondance exacte a été trouvée
        if next_room:
            # Si une correspondance exacte est trouvée, la retourner
            return next_room

        # Si aucune correspondance exacte n'est trouvée,
        # utiliser le chemin de remplacement '*' si il existe dans la pièce actuelle
        # (utilise '*' comme valeur par défaut si 'direction' n'existe pas).
        return self.paths.get("*")

    def add_paths(self, paths):
        """
        Ajoute ou met à jour les chemins (transitions) disponibles depuis cette pièce.

        Args:
            paths (dict): Dictionnaire des chemins {action: Room_objet}.
        """
        # Mettre à jour le dictionnaire des chemins avec les nouvelles routes
        self.paths.update(paths)


# --- Définition des pièces du jeu ---

# Définir la pièce de mort générique
generic_death = Room("generic_death",  # tag
                     "Death",  # name_en (titre)
                     "Mort",  # name_fr (titre)
                     "You die.",  # description_en
                     "Tu meurs.",  # description_fr
                     "THE END",  # complement_en
                     "FIN",  # complement_fr
                     "",  # choices_en
                     "",  # choices_fr
                     "/static/img/img_i.jpg",  # img_one
                     "/static/img/icon_d.png")  # img_two

# Définir la pièce de la coursive (Départ)
lower_deck_cursive = Room("lower_deck_cursive",
                          "Lower Deck Cursive",
                          "Coursive du pont inférieur",
                          "The Gothon pirates have boarded your ship. You are the last standing crew member. No surprise! While your comrades were fighting, you were... sleeping! Anyhow, this vessel must not fall into enemy's hands. You are now running down the lower deck cursive. A safe choice to avoid enemies. Ahead: the armory. As you emerge from the last hatch, one insectoid pirate jumps out, guarding the way to the armory. He's about to pull a weapon to blast you. What do you do?",
                          "Les pirates gothons ont abordé ton vaisseau. Tu es le seul survivant de l'équipage. Évidemment, alors que tes camarades combattaient, tu... dormais! Peu importe, ce vaisseau ne doit pas tomber aux mains de l'ennemi. Te voilà donc à la course dans la coursive du pont inférieur. Judicieux pour éviter les ennuis. Droit devant: l'arsenal. Alors que tu t'extrais de la dernière écoutille, un pirate insectoïde fait irruption. Il bloque l'entrée de l'arsenal. Il s'apprête à dégainer pour te griller. Que fais-tu ?",
                          "",
                          "",
                          "[a] shoot! [b] dodge! [c] tell a joke",
                          "[a] tire! [b] esquive! [c] raconte une blague",
                          "/static/img/img_b.jpg",
                          "/static/img/icon_a.png")

# Définir la première mort dans la coursive (échec du tir)
lower_deck_cursive_death_1 = Room("lower_deck_cursive_death_1",
                                  "Epilogue",
                                  "Épilogue",
                                  "Quick on the draw, you yank out your blaster and fire it at the Gothon pirate. He leaps high in the air. Your laser misses him entirely. The pirate flies into an insane rage and blast you repeatedly in the face until you are dead. Then, the insectoid dissolves you with his saliva and suck you up.",
                                  "Rapide sur la gâchette, tu fais cracher ton laser en direction du pirate gothon. Ce dernier bondit dans les airs. Tu le rates. Fou de rage, le pirate bondit vers toi et te balance quelques décharges à la tête. Tu t'effondres. Puis, l'insectoïde te liquéfie avec sa salive, avant de t'aspirer.",
                                  "THE END",
                                  "FIN",
                                  "",
                                  "",
                                  "/static/img/img_g.jpg",
                                  "/static/img/icon_f.png")

# Définir la deuxième mort dans la coursive (échec de l'esquive)
lower_deck_cursive_death_2 = Room("lower_deck_cursive_death_2",
                                  "Epilogue",
                                  "Épilogue",
                                  "You dodge, weave and slide as the pirate's blaster cranks a laser past your head. In the middle of your artful dodge, your foot slips. You bang your head on the wall and pass out. You wake up shortly after, only to die as the insectoid dissolves you with his saliva and suck you up.",
                                  "Le pirate te balance des jets de laser; tu les esquives. Dans ce ballet improvisé, tu finis par glisser. Ta tête donne contre le mur. Tu t'assommes et t'écroules. Tu ne reprends connaissance que pour te rendre compte que l'insectoïde te liquéfie avec sa salive, avant de t'aspirer.",
                                  "THE END",
                                  "FIN",
                                  "",
                                  "",
                                  "/static/img/img_g.jpg",
                                  "/static/img/icon_f.png")

# Définir la pièce de l'arsenal (Étape 1 du code)
the_armory = Room("the_armory",
                  "The Armory",
                  "L'Arsenal",
                  "Lucky for you they made you learn Gothon insults in the academy. You tell the one Gothon joke you know. The Gothon stops, waits, then busts out laughing. While he's laughing, you shoot him square in the head, putting him down. You then jump through the armory door. It's dead quiet... You lock the door and run to the far side of the room. All the laser weapons are gone. You find the explosive container. There is a keypad lock on the box. You need a 3-digit code to get the bomb out. You can guess. However, after five attempts, you know the lock will fuse forever. Enter three digits.",
                  "Tu trouves bien utile d'avoir mémorisé un peu de gothon à l'académie. Tu racontes donc la seule blague dont tu te souviens. Le Gothon fige, réfléchit, puis éclate de rire. Alors qu'il s'esclaffe, tu lui balances un jet laser à la tête. Il s'écroule. Tu enjambes le corps et pénètres dans l'arsenal. Il règne un silence mortuaire... Tu verrouilles la porte et t'élances vers le fond de la pièce. Les armes laser ont été emportées. Tu retrouves le conteneur à explosifs. Pour l'ouvrir, tu dois entrer un code à trois chiffres sur le clavier. Tente de deviner. Par contre, après cinq tentatives, le verrou se soude à jamais. Entre trois chiffres.",
                  "",
                  "",
                  "[###]",
                  "[###]",
                  "/static/img/img_g.jpg",
                  "/static/img/icon_b.png")  # code: 132

# Définir la pièce de l'arsenal (Étape 2 du code)
the_armory_2 = Room("the_armory_2",
                    "The Armory",
                    "L'Arsenal",
                    "Not working. Try again. Enter three digits.",
                    "Non. Essaie encore. Entre trois chiffres.",
                    "",
                    "",
                    "[###]",
                    "[###]",
                    "/static/img/img_j.jpg",
                    "/static/img/icon_one.png")  # code: 132

# Définir la pièce de l'arsenal (Étape 3 du code, Indice 1)
the_armory_3 = Room("the_armory_3",
                    "The Armory",
                    "L'Arsenal",
                    "Not working. Hurry up! You remember that all the combinations aboard begin with '1', plus two digits.",
                    "Raté. Dépêche-toi ! Tu te rappelles que les combinaisons à bord débutent par '1', plus deux chiffres.",
                    "",
                    "",
                    "[1##]",
                    "[1##]",
                    "/static/img/img_j.jpg",
                    "/static/img/icon_two.png")  # code: 132

# Définir la pièce de l'arsenal (Étape 4 du code, Indice 2)
the_armory_4 = Room("the_armory_4",
                    "The Armory",
                    "L'Arsenal",
                    "Not working. Come on! Try again. The code begins with '1', plus two digits.",
                    "Raté. Aller ! Essaie encore. Le code débute par '1', plus deux chiffres.",
                    "",
                    "",
                    "[1##]",
                    "[1##]",
                    "/static/img/img_j.jpg",
                    "/static/img/icon_three.png")  # code: 132

# Définir la pièce de l'arsenal (Étape 5 du code, Indice 3)
the_armory_5 = Room("the_armory_5",
                    "The Armory",
                    "L'Arsenal",
                    "Not working. Mmmmh... OK! OK! OK! You remember. These combinations are always made with digits '1, 2 and 3'! Hence, '1', plus two digits.",
                    "Raté. Mmmmh... OK ! OK ! OK ! Ça revient. Les combinaisons ne comportent que les chiffres '1, 2 et 3' ! Donc, '1', plus deux chiffres.",
                    "",
                    "",
                    "[1##]",
                    "[1##]",
                    "/static/img/img_j.jpg",
                    "/static/img/icon_four.png")  # code: 132

# Définir la pièce de mort de l'arsenal (après 5 échecs)
the_armory_death = Room("the_armory_death",
                        "Epilogue",
                        "Épilogue",
                        "The lock buzzes once more. Only this time, you hear a sickening melting sound. The mechanism is fused together. Without weapon: no hope. You decide to sit there. Time passes... and passes... Suddenly, you hear a muffled thud. Something hit the ship? Then, another thud? And, more thuds. This time, heavier and louder. The hull begins shaking and roaring. Soon, the temperature falls, air pressure drops, oxygen becomes scarcer... They let the ship strand on the asteroid belt!! You fall into a faint... to never wake up again.",
                        "Le verrou bourdonne une dernière fois et tu l'entends se souder. Le mécanisme a sauté. Sans arme, c'est l'impasse. Tu décides de t'asseoir. Le temps passe... et passe... Soudain, tu entends un bruit sourd. Quelque chose a percuté le vaisseau? Puis, un autre bruit ? Et encore. De plus en plus lourd et fréquent. La coque vrombit et grince. L'air se refroidit, la pression chute, l'oxygène se raréfie... Ils ont laissé le vaisseau s'échouer dans la ceinture d'astéroïdes ! Tu t'évanouis... pour ne jamais te réveiller.",
                        "THE END",
                        "FIN",
                        "",
                        "",
                        "/static/img/img_f.jpg",
                        "/static/img/icon_f.png")

# Définir la pièce du pont (après succès du code)
the_bridge = Room("the_bridge",
                  "The Bridge",
                  "Le pont",
                  "The container clicks open, the seal breaks, letting gas out. You find a dozen of time-bombs. You grab one. You run as quickly as you can to the starboard engine. Over there, you know the blast will trigger a chain reaction and destroy the ship. You burst onto the bridge with your bomb under your arm. You surprise three Gothon pirates. The three lezardoids haven't pulled their weapons out yet, as they see the active bomb under your arm. What do you do?",
                  "Le verrou se déclenche, le scellant fend, le contenant se dépressurise. Tu prends une des douzaines de bombes à retardement. Tu te diriges à la hâte vers le réacteur du tribord. Une explosion y déclenchera une réaction en chaine et détruira le vaisseau. Tu émerges sur le pont du réacteur et tu surprends trois pirates gothons. Les trois lézaroïdes n'ont pas encore dégainé, mais ils fixent la bombe que tu portes. Que fais-tu?",
                  "",
                  "",
                  "[a] throw the bomb [b] slowly place the bomb",
                  "[a] lance la bombe [b] dépose la bombe",
                  "/static/img/img_k.jpg",
                  "/static/img/icon_c.png")

# Définir la mort sur le pont (échec du placement de bombe)
the_bridge_death = Room("the_bridge_death",
                        "Epilogue",
                        "Épilogue",
                        "In a panic, you trigger off the timer, throw the bomb and make a leap for the door. Right as you drop it, a pirate shoots you in the back, killing you. As you die you see another pirate frantically trying to disarm the bomb. They got you, but they won't make it alive either.",
                        "En panique, tu déclenches la minuterie et tu balances la bombe. Alors que tu t'élances vers la porte, un pirate te tire mortellement dans le dos. Tu perds connaissance en voyant les pirates désespérément essayer de désarmer l'engin explosif. Ils t'ont eu, mais ils y passeront eux aussi.",
                        "THE END",
                        "FIN",
                        "",
                        "",
                        "/static/img/img_d.jpg",
                        "/static/img/icon_f.png")

# Définir la pièce de la navette de secours (Étape 1 du pod)
escape_pod = Room("escape_pod",
                  "Escape Pod",
                  "Navette de secours",
                  "You point your blaster at the bomb under your arm. The pirates put their hands up. You inch backward to the door and then carefully place the bomb on the floor, pointing your blaster at it. Then, you set off the timer, jump back through the door, punch the close button and blast the lock. Now, you must reach the escape pods to get off this tin can. You get to the boarding bay. Suddenly, the ship rattles! The bomb just exploded. The reactor will melt down and the ship will soon be disintegrated! There are five pods, which one do you take? Enter a digit, from 1 to 5.",
                  "Tu pointes ton laser vers la bombe que tu tiens. Les pirates lèvent les bras. Tu recules vers la porte et tu poses délicatement la bombe au sol tout en la maintenant en joue. Puis, tu déclenches la minuterie, passes la porte, tu frappes le bouton de fermeture et tu fais sauter la console. Maintenant, tu dois gagner les navettes de secours pour t'éjecter du vaisseau. Tu atteins la zone d'embarquement. Soudain, le vaisseau tremble ! La bombe vient d'exploser. Le réacteur va se fissurer et le vaisseau va bientôt se disloquer ! Il y a cinq navettes, laquelle choisis-tu? Entre un chiffre, de 1 à 5.",
                  "",
                  "",
                  "[#]",
                  "[#]",
                  "/static/img/img_d.jpg",
                  "/static/img/icon_e.png")  # code: 2

# Définir la pièce de la navette de secours (Étape 2 du pod, Indice 1)
escape_pod_2 = Room("escape_pod_2",
                    "Escape Pod",
                    "Navette de secours",
                    "As you are about to punch the keypad, a voice from within you murmurs: 'Be careful... the pods are trapped. Don't take odd numbers.'",
                    "Comme tu t'apprêtes à ouvrir le sas, une voix en toi te murmure : 'Attention... elles sont piégées. Ne prends pas les numéros impairs.'",
                    "",
                    "",
                    "[#]",
                    "[#]",
                    "/static/img/img_d.jpg",
                    "/static/img/icon_e.png")  # code: 2

# Définir la pièce de la navette de secours (Étape 3 du pod, Indice 2)
escape_pod_3 = Room("escape_pod_3",
                    "Escape Pod",
                    "Navette de secours",
                    "The voice goes again: 'Be careful...'",
                    "La voix te murmure encore : 'Attention...'",
                    "",
                    "",
                    "[#]",
                    "[#]",
                    "/static/img/img_d.jpg",
                    "/static/img/icon_e.png")  # code: 2

# Définir l'épilogue de la défaite
the_end_loser = Room("the_end_loser",
                     "Epilogue",
                     "Épilogue",
                     "You punch the keypad, the airlock opens, you jump into the pod. From the dark, you catch sight of a tiny red light floating towards you. This hiss? You are face to face with a combat drone. The last thing you notice is being disintegrated by a laser blast.",
                     "Tu frappes le bouton d'ouverture, le sas s'ouvre, tu bondis à l'intérieur. Dans l'obscurité, tu aperçois un voyant rouge flotter vers toi. Ce crépitement ? Tu fais face à un drone de combat. En moins de deux, tu es désintégré alors que le drone décharge son laser.",
                     "THE END",
                     "FIN",
                     "",
                     "",
                     "/static/img/img_c.jpg",
                     "/static/img/icon_g.png")

# Définir l'épilogue de la victoire
the_end_winner = Room("the_end_winner",
                      "Epilogue",
                      "Épilogue",
                      "You punch the keypad, the airlock opens, you jump into the pod and trigger the evasion procedure. The pod easily slides out into space, heading to the planet below. VICTORY! You look in the porthole and see your ship explode like a bright star, taking out the Gothon ship at the same time...",
                      "Tu frappes le bouton d'ouverture, le sas s'ouvre, tu bondis à l'intérieur, puis tu enclenches la procédure d'évacuation. La navette s'éjecte dans l'espace, puis ajuste sa trajectoire sur la planète. VICTOIRE! Tu regardes dans le hublot et tu assistes à l'explosion de ton vaisseau. L'onde de choc emporte aussi le vaisseau gothon...",
                      "THE END",
                      "FIN",
                      "",
                      "",
                      "/static/img/img_a.jpg",
                      "/static/img/icon_h.png")

# --- Définition des chemins (règles de transition) ---

# Séparateur visuel pour les chemins
###############################################################################

# Ajouter les chemins pour la coursive
lower_deck_cursive.add_paths({
    "a": lower_deck_cursive_death_1,
    "b": lower_deck_cursive_death_2,
    "c": the_armory
})  # Dictionnaire (k:v)

# Ajouter les chemins pour l'arsenal (Tentative 1)
the_armory.add_paths({
    "132": the_bridge,
    "a": the_armory_death,  # Transition de test (met fin à l'histoire)
    "*": the_armory_2  # Transition par défaut pour tout autre échec
})

# Ajouter les chemins pour l'arsenal (Tentative 2)
the_armory_2.add_paths({
    "132": the_bridge,
    "a": the_armory_death,  # Transition de test
    "*": the_armory_3  # Transition par défaut pour tout autre échec
})

# Ajouter les chemins pour l'arsenal (Tentative 3)
the_armory_3.add_paths({
    "132": the_bridge,
    "a": the_armory_death,  # Transition de test
    "*": the_armory_4  # Transition par défaut pour tout autre échec
})

# Ajouter les chemins pour l'arsenal (Tentative 4)
the_armory_4.add_paths({
    "132": the_bridge,
    "a": the_armory_death,  # Transition de test
    "*": the_armory_5  # Transition par défaut pour tout autre échec
})

# Ajouter les chemins pour l'arsenal (Tentative 5 - Dernière chance)
the_armory_5.add_paths({
    "132": the_bridge,
    "a": the_armory_death,  # Transition de test
    "*": the_armory_death  # Transition par défaut : mort après 5 échecs
})

# Ajouter les chemins pour le pont
the_bridge.add_paths({
    "a": the_bridge_death,
    "b": escape_pod
})

# Ajouter les chemins pour la navette de secours (Tentative 1)
escape_pod.add_paths({
    "2": the_end_winner,
    "1": escape_pod_2,
    "3": escape_pod_2,
    "4": escape_pod_2,
    "5": escape_pod_2
})

# Ajouter les chemins pour la navette de secours (Tentative 2)
escape_pod_2.add_paths({
    "2": the_end_winner,
    "1": escape_pod_3,
    "3": escape_pod_3,
    "4": escape_pod_3,
    "5": escape_pod_3
})

# Ajouter les chemins pour la navette de secours (Tentative 3 - Dernière chance)
escape_pod_3.add_paths({
    "2": the_end_winner,
    "1": the_end_loser,
    "3": the_end_loser,
    "4": the_end_loser,
    "5": the_end_loser
})


# Définir la pièce de départ du jeu (exportée)
START = lower_deck_cursive

