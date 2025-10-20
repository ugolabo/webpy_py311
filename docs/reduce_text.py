#!/usr/bin/env python3
# -*- coding: utf-8 -*-


try:
    helloFile = open("new2.txt", "r", encoding="utf-8")  # Ajouter explicitement de l'encodage
    helloContent = helloFile.read()
except FileNotFoundError:
    print("Erreur: Le fichier 'new2.txt' n'a pas été trouvé.")
    sys.exit(1)  # Quitter le script avec un code d'erreur
finally:
    helloFile.close()  # S'assurer que le fichier est fermé même en cas d'erreur

line = helloContent.strip()
print(line)
print("=" * 25)

start = 0
w = 50

# Longueur en caractères
line_length = len(line)

# Boucle dans une longue ligne utilisant une longueur désirée
while line_length - start >= w:
    print(line[start:start + w])
    start += w
print(line[start:])
