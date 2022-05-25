# Primer ejercicio
Lista = [1,2,3,4,5,6, "Angel", 2,2,1, "Angel",3]

Lista = list( set(lista) )

print(Lista)

# Segundo ejercicio
Lista1 = [1,2,3,4,5,4,3,2,2,1,5]
Lista2 = [4,5,6,7,8,4,5,6,7,7,8]

a = set(Lista1)
b = set(Lista2)

union = list(a | b)
soloA = list(a - b)
soloB = list(b - a)
inter = list(a & b)

print("Union -> " union)
print("soloA -> " soloA)
print("soloB -> " soloB)
print("inter -> " inter)
