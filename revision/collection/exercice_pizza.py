def tri_personnalise(e):
    return e

def afficher(collection, n_premiers_elements=-1):
    #collection.sort(reverse=True)
    #c.sort(key=tri_personnalise)
    c = collection
    if n_premiers_elements != -1:
        c = collection[:n_premiers_elements]
        
    nb_pizzas = len(c)
    if nb_pizzas == 0:
        print("AUCUNE PIZZA")
        return
    
    print(f"----------- LISTE DES PIZZAS ({nb_pizzas}) ---------------")
    for pizza in c:
        print(pizza)
    print()
    print(f"La première pizza {c[0]}")
    print(f"La dernière pizza {c[-1]}")

pizzas = ("4 fromages", "végétarienne", "hawai", "calzone")
pizzas = list(pizzas)


def ajouter_pizza(collection):
    add_pizza = input("Pizza à ajouter: ")
    if add_pizza.lower() in collection:
        print("ERREUR : Cette pizza existe déjà")
    else:
        collection.append(add_pizza)

def pizza_existe(e, collection):
    for i in collection:
        if i == e:
            return True
    return False
    
ajouter_pizza(pizzas)
afficher(pizzas,2)