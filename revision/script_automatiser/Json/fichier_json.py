import json

"""personne = {
    "nom" : "Paul",
    "age" : 25,
    "amis" : ["Sophie", "Marie", "Jean"]
}

# Sérialiser DATA -> TXT "" (json) dumps
# Désérialiser TXT (json) -> DATA loads

personne_json = json.dumps(personne)
print("JSON: ", personne_json)

f = open("fichier_json.txt", "w")
f.write(personne_json)

f.close()"""


f = open("fichier_json.txt", "r")
donne_json = f.read()
personne = json.loads(donne_json)
f.close()