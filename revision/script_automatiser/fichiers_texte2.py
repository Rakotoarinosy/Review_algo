#f = open("mon_fichier.txt", "r")
#texte = f.read()
#print(texte)

#for line in f:
#    print(line, end="")
#f.close()


import os.path

filename = os.path.join("rep","mon_fichier.txt")
print(filename)
if os.path.exists(filename):
    print("Le fichier existe")
    f = open(filename,"r")
    texte = f.read()
    print(texte)
    f.close()
else:
    print("Le fichier n'existe pas")
    
"""
try:
    f = open("mon_fichierdssss.txt", "r)
except FileNotFoundError:
    print("ERREUR : Le fichier n'a pas pu être ouverte car il n'a pas été trové")
else:
    texte = f.read()
    print(texte)
    f.close()
"""