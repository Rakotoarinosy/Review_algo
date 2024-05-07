#EXERCICE FONCTIONS
# Tables de multiplication

def tables_de_multiplication(n,min = 1,max = 10):
    if min > max:
        print("ERREUR : Le min est supérieur au max")
        return  
    for i in range(min, max+1):
        resultat = i*n
        print(f"{i}*{n} = {resultat}")
tables_de_multiplication(5)