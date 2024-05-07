def afficher_table(n, operateur_str, operation_cbk):
    for i in range(1,10):
        print(i, operateur_str,n, '=', operation_cbk(i,n))

#FONCTIONS LAMBDA

afficher_table(2,"*", lambda a, b : a*b)
print()
afficher_table(2,"+", lambda a, b : a+b)
print()
afficher_table(2,"^", lambda a, b : pow(a,b))
print()