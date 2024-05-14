class Person:
    def __init__(self, nom: str = "", age: int = 0):
        self.nom = nom # crée une variable d'instance : nom
        self.age = age
        if nom == "":
            self.demander_nom()
        print(f"Constructeur personne {self.nom}")
        
    def se_presenter(self):
        if self.age == 0:
            print(f"Bonjour, je m'appelle {self.nom}")
        else:
            print(f"Bonjour, je m'appelle {self.nom}, j'ai {self.age}")
            if self.est_majeur():
                print("Je suis majeur")
            else:
                print("Je suis mineur")
                
    def est_majeur(self):
        return self.age >= 18
    
    def demander_nom(self):
        self.nom = input("Entrez votre nom: ")

liste_personne = (Person("Jean",30),Person("Paul", 15),Person())
for personne in liste_personne:
    personne.se_presenter()

 
# personne1 = Person("Jean",30)
# personne2 = Person("Paul", 15)
# personne3 = Person()

# personne1.se_presenter()
# personne2.se_presenter()
# personne3.se_presenter()
