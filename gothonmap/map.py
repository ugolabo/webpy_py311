#!/bin/python2
# -*- coding: utf-8 -*-

class Room(object):

    def __init__(self, name, namef, description, descriptionf, complement, complementf, choices=None, choicesf=None, imgone=None, imgtwo=None):
        self.name = name
        self.namef = namef		        
        self.description = description
        self.descriptionf = descriptionf
        self.complement = complement
        self.complementf = complementf   
        self.choices = choices
        self.choicesf = choicesf
        self.imgone = imgone
        self.imgtwo = imgtwo
        self.paths = {}

    def go(self, direction):
        return self.paths.get(direction, None)

    def add_paths(self, paths):
        self.paths.update(paths)

generic_death = Room("Death",
"Mort",
"You die.",
"Tu meurs.",
"THE END",
"FIN",
"",
"",
"/static/img/imgI.jpg",
"") # instance of Room

lower_deck_cursive = Room("Lower Deck Cursive",
"Coursive du pont inférieur",
"The Gothon pirates have boarded your ship. You are the last standing crew member. No surprise! While your comrades were fighting, you were... sleeping! Anyhow, this vessel must not fall into enemy's hands. You are now running down the lower deck cursive. A safe choice to avoid enemies. Ahead: the armory. As you emerge from the last hatch, one insectoid pirate jumps out, guarding the way to the armory. He's about to pull a weapon to blast you. What do you do?",
"Les pirates gothons ont abordé ton vaisseau. Tu es le seul survivant de l’équipage. Évidemment, alors que tes camarades combattaient, tu... dormais! Peu importe, ce vaisseau ne doit pas tomber aux mains de l’ennemi. Te voilà donc à la course dans la coursive du pont inférieur. Judicieux pour éviter les ennuis. Droit devant: l'arsenal. Alors que tu t’extrais de la dernière écoutille, un pirate insectoïde fait irruption. Il bloque l’entrée de l'arsenal. Il s’apprête à dégainer pour te griller. Que fais-tu?",
"",
"",
"[a] shoot! [b] dodge! [c] tell a joke",
"[a] tire! [b] esquive! [c] raconte une blague",
"/static/img/imgB.jpg",
"/static/img/iconB.png")

lower_deck_cursive_death_1 = Room("Epilogue",
"Épilogue",
"Quick on the draw, you yank out your blaster and fire it at the Gothon pirate. He leaps high in the air. Your laser misses him entirely. The pirate flies into an insane rage and blast you repeatedly in the face until you are dead. Then, the insectoid dissolves you with his saliva, and suck you up.",
"Rapide sur la gâchette, tu fais cracher ton laser en direction du pirate gothon. Ce dernier bondit dans les airs. Tu le rates. Fou de rage, le pirate bondit vers toi et te balance quelques décharges à la tête. Tu t’effondres. Puis, l’insectoïde te liquéfie avec sa salive, avant de t’aspirer.",
"THE END",
"FIN",
"",
"",
"/static/img/imgG.jpg",
"/static/img/iconD.png")

lower_deck_cursive_death_2 = Room("Epilogue",
"Épilogue",
"You dodge, weave, and slide as the pirate's blaster cranks a laser past your head. In the middle of your artful dodge, your foot slips. You bang your head on the wall, and pass out. You wake up shortly after, only to die as the insectoid dissolves you with his saliva, and suck you up.",
"Le pirate te balance des jets de laser; tu les esquives. Dans ce ballet improvisé, tu finis par glisser. Ta tête donne contre le mur. Tu t’assommes et t’écroules. Tu ne reprends connaissance que pour te rendre compte que l’insectoïde te liquéfie avec sa salive, avant de t’aspirer.",
"THE END",
"FIN",
"",
"",
"/static/img/imgG.jpg",
"/static/img/iconD.png")

the_armory = Room("The Armory",
"L'Arsenal",
"Lucky for you they made you learn Gothon insults in the academy.  You tell the one Gothon joke you know. The Gothon stops, waits, then busts out laughing. While he's laughing, you shoot him square in the head, putting him down. You then jump through the armory door. It's dead quiet... You lock the door and run to the far side of the room. All the laser weapons are gone. You find the explosive container. There is a keypad lock on the box. You need a 3-digit code to get the bomb out. You can guess. Howerver, after five attempts, you know the lock will fuse forever. Enter three digits.",
"Tu trouves bien utile d’avoir mémorisé un peu de gothon à l’académie.  Tu racontes donc la seule blague dont tu te souviens. Le Gothon fige, réfléchit, puis éclate de rire. Alors qu’il s’esclaffe, tu lui balances un jet laser à la tête. Il s’écroule. Tu enjambes le corps et pénètres dans l'arsenal. Il règne un silence mortuaire... Tu verrouilles la porte et t’élances vers le fond de la pièce. Les armes laser ont été emportées. Tu retrouves le conteneur à explosifs. Pour l’ouvrir, tu dois entrer un code à trois chiffres sur le clavier. Tente de deviner. Par contre, après cinq tentatives, le verrou se soude à jamais. Entre trois chiffres.",
"",
"",
"[###]",
"[###]",
"/static/img/imgG.jpg",
"/static/img/iconA.png") # code: 132

the_armory_2 = Room("The Armory",
"L'Arsenal",
"Not working. Try again. Enter three digits.",
"Non. Essaie encore. Entre trois chiffres.",
"",
"",
"[###]",
"[###]",
"/static/img/imgJ.jpg",
"/static/img/iconA.png") # code: 132

the_armory_3 = Room("The Armory",
"L'Arsenal",
"Not working. Hurry up! You remember that all the combinations aboard begin with \'1\', plus two digits.",
"Raté. Dépêche-toi! Tu te rappelles que les combinaisons à bord débutent par \'1\', plus deux chiffres.",
"",
"",
"[1##]",
"[1##]",
"/static/img/imgJ.jpg",
"/static/img/iconA.png") # code: 132

the_armory_4 = Room("The Armory",
"L'Arsenal",
"Not working. Come on! Try again. The code begins with \'1\', plus two digits.",
"Raté. Aller! Essaie encore. Le code débute par \'1\', plus deux chiffres.",
"",
"",
"[1##]",
"[1##]",
"/static/img/imgJ.jpg",
"/static/img/iconA.png") # code: 132

the_armory_5 = Room("The Armory",
"L'Arsenal",
"Not working. Mmmmh... OK! OK! OK! You remember. These combinations are always made with digits \'1, 2, and 3\'! Hence, \'1\', plus two digits.",
"Raté. Mmmmh... OK! OK! OK! Ça revient. Les combinaisons ne comportent que les chiffres \'1, 2 et 3\'! Donc, \'1\', plus deux chiffres.",
"",
"",
"[1##]",
"[1##]",
"/static/img/imgJ.jpg",
"/static/img/iconA.png") # code: 132

the_armory_death = Room("Epilogue",
"Épilogue",
"The lock buzzes once more. Only this time, you hear a sickening melting sound. The mechanism is fused together. Without weapon: no hope. You decide to sit there. Time passes... and passes... Suddenly, you hear a muffled thud. Something hit the ship? Then, another thud? And, more thuds. This time, heavier and louder. The hull begins shaking and roaring. Soon, the temperature falls, air pressure drops, oxygen becomes scarcer... They let the ship strand on the asteroid belt!! You fall into a faint... to never wake up again.",
"Le verrou bourdonne une dernière fois et tu l’entends se souder. Le mécanisme a sauté. Sans arme, c’est l’impasse. Tu décides de t’assoir. Le temps passe... et passe... Soudain, tu entends un bruit sourd. Quelque chose a percuté le vaisseau? Puis, un autre bruit? Et encore. De plus en plus lourd et fréquent. La coque vrombit et grince. L’air se refroidit, la pression chute, l’oxygène se raréfie... Ils ont laissé le vaisseau s’échouer dans la ceinture d’astéroïdes!! Tu t’évanouis... pour ne jamais te réveiller.",
"THE END",
"FIN",
"",
"",
"/static/img/imgF.jpg",
"/static/img/iconF.png")

the_bridge = Room("The Bridge",
"Le pont",
"The container clicks open, the seal breaks, letting gas out. You find a dozen of time-bombs. You grab one. You run as quickly as you can to the starboard engine. Over there, you know the blast will trigger a chain reaction and destroy the ship. You burst onto the bridge with your bomb under your arm. You surprise three Gothon pirates. The three lezardoids haven't pulled their weapons out yet, as they see the active bomb under your arm. What do you do?",
"Le verrou se déclenche, le scellant se fend, le contenant se dépressurise. Tu prends une des douzaines de bombes à retardement. Tu te diriges à la hâte vers le réacteur du tribord. Une explosion y déclenchera une réaction en chaine et détruira le vaisseau. Tu émerges sur le pont du réacteur et tu surprends trois pirates gothons. Les trois lézaroïdes n’ont pas encore dégainé, mais ils fixent la bombe que tu portes. Que fais-tu?",
"",
"",
"[a] throw the bomb [b] slowly place the bomb",
"[a] lance la bombe [b] dépose la bombe",
"/static/img/imgK.jpg",
"/static/img/iconC.png")

the_bridge_death = Room("Epilogue",
"Épilogue",
"In a panic, you trigger off the timer, throw the bomb and make a leap for the door. Right as you drop it, a pirate shoots you in the back, killing you. As you die you see another pirate frantically trying to disarm the bomb. They got you, but they won't make it alive either.",
"En panique, tu déclenches la minuterie et tu balances la bombe. Alors que tu t’élances vers la porte, un pirate te tire mortellement dans le dos. Tu perds connaissance en voyant les pirates désespérément essayer de désarmer l’engin explosif. Ils t’ont eu, mais ils y passeront eux aussi.",
"THE END",
"FIN",
"",
"",
"/static/img/imgD.jpg",
"/static/img/iconE.png")

escape_pod = Room("Escape Pod",
"Navette de secours",
"You point your blaster at the bomb under your arm. The pirates put their hands up. You inch backward to the door and then carefully place the bomb on the floor, pointing your blaster at it. Then you set off the timer, jump back through the door, punch the close button and blast the lock. Now, you must reach the escape pods to get off this tin can. You get to the boarding bay. Suddenly, the ship rattles! The bomb just exploded. The reactor will melt down and the ship will soon be disintegrated! There are five pods, which one do you take? Enter a digit, from 1 to 5.",
"Tu pointes ton laser vers la bombe que tu tiens. Les pirates lèvent les bras. Tu recules vers la porte et tu poses délicatement la bombe au sol tout en la maintenant en joue. Puis, tu déclenches la minuterie, passes la porte, frappes le bouton de fermeture et fais sauter la console. Maintenant, tu dois gagner les navettes de secours pour t’éjecter du vaisseau. Tu atteins la zone d’embarquement. Soudain, le vaisseau tremble! La bombe vient d’exploser. Le réacteur va se fissurer et le vaisseau va bientôt se disloquer! Il y a cinq navettes, laquelle choisis-tu? Entre un chiffre, de 1 à 5.",
"",
"",
"[#]",
"[#]",
"/static/img/imgD.jpg",
"/static/img/iconC.png") # code: 2

escape_pod_2 = Room("Escape Pod",
"Navette de secours",
"As you are about to punch the keypad, a voice from within you murmurs: ’Be careful... the pods are trapped. Don't take odd numbers.’",
"Comme tu t’apprêtes à ouvrir le sas, une voix en toi te murmure: ’Attention... elles sont piégées. Ne prends pas les numéros impairs.’",
"",
"",
"[#]",
"[#]",
"/static/img/imgD.jpg",
"/static/img/iconC.png") # code: 2

escape_pod_3 = Room("Escape Pod",
"Navette de secours",
"The voice goes again: ’Be careful...’",
"La voix te murmure encore: ’Attention...’",
"",
"",
"#",
"#",
"/static/img/imgD.jpg",
"/static/img/iconC.png") # code: 2

the_end_loser = Room("Epilogue",
"Épilogue",
"You punch the keypad, the airlock opens, you jump into the pod. From the dark, you catch sight of a tiny red light floating towards you. This hiss?  You are face to face with a combat drone. The last thing you notice is being disintegrated by a laser blast.",
"Tu frappes le bouton d’ouverture, le sas s’ouvre, tu bondis à l’intérieur. Dans l’obscurité, tu aperçois un voyant rouge flotter vers toi. Ce crépitement? Tu fais face à un drone de combat. En moins de deux, tu es désintégré alors que le drone décharge son laser.",
"THE END",
"FIN",
"",
"",
"/static/img/imgC.jpg",
"/static/img/iconG.png")

the_end_winner = Room("Epilogue",
"Épilogue",
"You punch the keypad, the airlock opens, you jump into the pod, and trigger the evasion procedure. The pod easily slides out into space, heading to the planet below. VICTORY! You look in the porthole and see your ship explode like a bright star, taking out the Gothon ship at the same time...",
"Tu frappes le bouton d’ouverture, le sas s’ouvre, tu bondis à l’intérieur, puis tu enclenches la procédure d’évacuation. La navette s’éjecte dans l’espace, puis ajuste sa trajectoire sur la planète. VICTOIRE! Tu regardes dans le hublot et tu assistes à l’explosion de ton vaisseau. L’onde de choc emporte aussi le vaisseau gothon...",
"THE END",
"FIN",
"",
"",
"/static/img/imgA.jpg",
"/static/img/iconH.png")

###############################################################################

lower_deck_cursive.add_paths({
    'a': lower_deck_cursive_death_1,
    'b': lower_deck_cursive_death_2,
    'c': the_armory
}) # dictionary (k:v)

the_armory.add_paths({
    '132': the_bridge,
    'a': the_armory_death, # pressing a with end the story; for testing
    '*': the_armory_2 # transition label
}) # dictionary (k:v)

the_armory_2.add_paths({
    '132': the_bridge,
    'a': the_armory_death, # pressing a ends the story; for testing
    '*': the_armory_3 # transition label
}) # dictionary (k:v)

the_armory_3.add_paths({
    '132': the_bridge,
    'a': the_armory_death, # pressing a ends the story; for testing
    '*': the_armory_4 # transition label
}) # dictionary (k:v)

the_armory_4.add_paths({
    '132': the_bridge,
    'a': the_armory_death, # pressing a ends the story; for testing
    '*': the_armory_5 # transition label
}) # dictionary (k:v)

the_armory_5.add_paths({
    '132': the_bridge,
    'a': the_armory_death, # pressing a ends the story; for testing
    '*': the_armory_death # transition label
}) # dictionary (k:v)

the_bridge.add_paths({
    'a': the_bridge_death,
    'b': escape_pod
})

escape_pod.add_paths({
    '2': the_end_winner,
    '1': escape_pod_2,
    '3': escape_pod_2,
    '4': escape_pod_2,
    '5': escape_pod_2
}) # dictionary (k:v)

escape_pod_2.add_paths({
    '2': the_end_winner,
    '1': escape_pod_3,
    '3': escape_pod_3,
    '4': escape_pod_3,
    '5': escape_pod_3
}) # dictionary (k:v)

escape_pod_3.add_paths({
    '2': the_end_winner,
    '1': the_end_loser,
    '3': the_end_loser,
    '4': the_end_loser,
    '5': the_end_loser
}) # dictionary (k:v)


START = lower_deck_cursive # variable
