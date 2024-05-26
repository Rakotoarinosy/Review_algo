# Inserer une chaine (Reverse)
# 
# "Bonjour toto"
# "otot ruojnoB"
# 
# Boucle
# Slice

def reverse_string1(str):
    r = ""
    for e in str:
        r = e + r
    return r

def reverse_string2(str):
    return s[::-1]

s = "Bonjour toto"

print(reverse_string2(s))
