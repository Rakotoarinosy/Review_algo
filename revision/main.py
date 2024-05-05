
def demander_age(nom):
    age_int = 0
    while age_int == 0:
        age_str = input(nom + " Quel est votre age ? ")
        try:
            age_int = int(age_str)
        except ValueError:
            print("ERREUR: Vous devez rentrer un nombre pour l'age")
    return age_int


def afficher_informations_personne(nom,age):
    print()
    print("Vous vous appelez " + nom + ", vous avez " + str(age) + " ans")
    print("L'an prochain vous aurez " + str(age+1) + " ans")
    if age > 60 :
        print("Vous êtes sénior") 
    elif age < 10:
        print("Vous êtes enfant")
    elif age == 17:
        print("Tout juste presque majeur")
    elif age == 18:
        print("Tout juste majeur : Félicitation")
    elif age >= 18:
        print("Vous êtes majeur")
    else:
        print("Vous êtes mineur")
    

def demander_nom():
    response_nom = input("Quel est votre nom ? ")
    while response_nom == "":
        response_nom = input("Veuillez entrez votre nom ? ")
    return response_nom

# demander l'age
#nom1 = demander_nom()
#nom2 = demander_nom()

#age1 = demander_age()
#age2 = demander_age()

#afficher_informations_personne(nom1,age1)
#afficher_informations_personne(nom2,age2)

for i in range(0,3):
    nom = "personne" + str(i+1)
    age = demander_age(nom) # type: ignore
    afficher_informations_personne(nom,age)