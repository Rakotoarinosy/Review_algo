class Pizza:
    def __init__(self, nom, prix, ingredients):
        self.nom = nom
        self.prix = prix
        self.ingredients = ingredients
        
    def afficher(self):
        print(f"{self.nom}: {self.prix}$")
        print(f"{', '.join(self.ingredients)}")
        
pizza1= Pizza("4 fromages",8.5, ("brie", "emmental", "compte", "compté", "parnesan"))

pizza1.afficher()