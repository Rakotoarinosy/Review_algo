def element_dans_liste(element,liste):
    l_lower = [nom.lower() for nom in liste]
    return element.lower() in l_lower

noms = ["Jean", "Sophie", "Martin", "Christophe", "Zoe", "Martin"]

if element_dans_liste("jEan", noms):
    print("Element trouvé")
else:
    print("Element non trouvé")
