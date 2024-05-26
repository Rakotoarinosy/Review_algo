# tri par sélection

l = [5, 8,10,2,1]
n = len(l)

for i in range(0, n):
    print("indice ",i)
    min_index = i
    for j in range(i+1,n):
        print("ji",j)
        if l[j]  < l[min_index]:
            min_index = j
            l[i], l[min_index] = l[min_index], l[i]

print("Tableau Trié : ", l)