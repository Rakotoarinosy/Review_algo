class Pizza:
    def __init__(self, nom, prix, ingredients, vegetarienne=False):
        self.nom = nom
        self.prix = prix
        self.ingredients = ingredients
        self.vegetarienne = vegetarienne
        
    def afficher(self):
        veg_str = ""
        if self.vegetarienne:
            veg_str = " - VEGETARIENNE"
        print(f"PIZZA {self.nom}: {self.prix}$ {veg_str}")
        print(f"{', '.join(self.ingredients)}")
        print()
        
class PizzaPersonnalisee(Pizza):
    PRIX_BASE = 7
    PRIX_PAR_INGREDIENT = 1.2
    DERNIER_NUMERO = 0
    
    def __init__(self):
        PizzaPersonnalisee.DERNIER_NUMERO += 1
        self.numero = PizzaPersonnalisee.DERNIER_NUMERO
        super().__init__(f"Personnalisée {self.numero}", 0, [])
        self.demander_ingedients_utilisateur()
        self.calculer_le_prix()
    
    def demander_ingedients_utilisateur(self):
        print()
        print(f"Ingredients pour la pizza personnalisée {self.numero}")
        while True:
            ingredient = input("Ajouter un ingrédient (ou ENTRER pour terminer) : ")
            if ingredient == "":
                 return
            self.ingredients.append(ingredient)
            print(f"Vous avez {len(self.ingredients)} ingrédient(s) : {', '.join(self.ingredients)}")
    
    def calculer_le_prix(self):
        self.prix = (self.PRIX_PAR_INGREDIENT*len(self.ingredients)) + self.PRIX_BASE

pizzas = (
    Pizza("4 fromages",8.5, ("brie", "emmental", "compte", "compté", "parnesan"),True),
    Pizza("Hawai", 9.5, ("tomate", "ananas", "oignons")),
    Pizza("4 saisons",11, ("oeuf", "emmental", "tomate", "jambon")),
    Pizza("Végétarienne", 7.8, ("champions", "tomate", "oignons", "poivrons"),True),
    PizzaPersonnalisee(),
    PizzaPersonnalisee()
)       

for i in pizzas:
    #if i.prix > 10:
    i.afficher()