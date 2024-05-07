# Collections : (Tableaux : Array), Listes, Tuples...
# Tuple (): immutable -> Non modifiable
# Liste []: mutable -> modifiable : rajouter/supprimer des élémenrs ou les modifiers
# Plusieurs éléments

# ------------------------ TUPLES --------------------
#personnes = ("Mélanie", "Jean", "Martin", "Alice")
#print(personnes)
#print(personnes[-1]) # -1 pour le dernier element

#for i in range(0, len(personnes)):
#     print(personnes[i]) 

#for i in personnes:
#     print(i)
#     print(len(i))

# ------------------------- LISTES -------------------
#personnes = ["Mélanie", "Jean", "Martin", "Alice"]
#nouvelle_personne = "David"
#
## print(personnes)
#
#personnes.append(nouvelle_personne)
#del personnes[1]
#
## print(personnes)
#
#def afficher_personnes(c):
#    for i in c:
#        print(i)
#
#def modifier_valeur(a):
#    a[0] = 10
#    
#test = [1,2,3,4]
#print(test)
#modifier_valeur(test)
#print(test)

#afficher_personnes(personnes)

# ---------------------------- FONCTIONS ET TUPLES --------------------------

#def obtenir_informations():
#    return "Mélanie", 37, 1.60

#def afficher_informations(nom, age, taille):
#    print(f"Informations: Nom: {nom}, age: {age}, taille: {taille}") 

#infos = obtenir_informations()
#afficher_informations(*infos)

# print(infos)
# print(*infos)
# print("nom: " + infos[0])
# print("age: " + infos[0])
# print("taille: " + infos[0])

#nom, age, taille = obtenir_informations()
#afficher_informations(nom, age, taille)

# ---------------- SLICES ----------
personnes = ("Mélanie", "Jean", "Martin", "Alice", "Pierre", "Paul")

# [start:stop:step]

for i in personnes[-1:]:
    print(i)