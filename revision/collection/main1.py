# LISTES - EXERCICE : DEMANDER NOMS DE PERSONNES


# nom et l'age input

'''for i in range(3):
    nom = input("Nom de la personne : ")
    print("Le nom est :", nom)'''
    
# demander des mots de personnes
# boucle infinie, sort quand le nom est vide == "":
# seulement à la fin afficher tous les noms

noms = []

while True:
    nom = input("Entrez le nom : ")
    if nom == "":
        break
    noms.append(nom)

print()
print("Nom des personnes")
noms.sort() # ordre alphabetique
for nom in noms:
    print(" ",nom)
