
def chaine_contient_chiffre(chaine):
    return any([c.isdigit() for c in chaine])

nom = input("Quel est le nom ? ")
if nom == "":
    print("Le nom est vide")
elif chaine_contient_chiffre(nom):
    print("Ce nom est invalide, il ne doit pas contenir de chiffres")
else:
    print("Bonjour " + nom)