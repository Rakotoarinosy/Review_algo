################# Tri à Bulles #################

def tri_a_bulles(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [64,90,34,25,12,22,11]
tri_a_bulles(arr)
print("Tri a bulle \n     Tableau trié: ")
print(arr)

################# Tri par sélection #################

def tri_par_selection(arr):
    n= len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            if arr[j] < arr[min_index]:
                min_index= j
                arr[i], arr[min_index] = arr[min_index], arr[i]
                
tri_par_selection(arr)
print("Tri par selection \n     Tableau trié: ")
print(arr)


################# Tri par insertion #################
def tri_par_insertion(arr):
    for i in range(1, len(arr)):
        cle = arr[i]
        j = i-1
        while j >= 0 and cle < arr[j]:
            arr[j+1] = arr[j]
            j-=1
            arr[j+1] = cle
tri_par_insertion(arr)
print("Tri par insertion \n     Tableau trié: ")

print(arr)


################# Tri rapide #################
def tri_rapide(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    elements_inf = [x for x in arr if x < pivot]
    elements_eq = [x for x in arr if x == pivot]
    elements_sup = [x for x in arr if x > pivot]
    return tri_rapide(elements_inf) + elements_eq + tri_rapide(elements_sup)

tri_rapide(arr)
print("Tri rapide \n    Tableau trié: ")

print(arr)