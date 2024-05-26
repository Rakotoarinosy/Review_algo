# FICHIERS TEXTE : EXERCICE
# "Ecrire des nombres"

# nombres.txt

f = open("nombres.txt", "w")

for i in range (1,11):
    f.write(f"{i}\n")
    
f.close()