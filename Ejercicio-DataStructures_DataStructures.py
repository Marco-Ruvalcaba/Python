# L I S T A S
# CREAR Lista
Lista = ["Lunes", "Martes", "Miercoles"]
# ACCEDER a elementos
print(Lista[0])  # Primer elemento
print(Lista[-1]) # Ultimo elemento
print(Lista[:3]) # Primer elemento al elemento indice 2
print(Lista[2:]) # Elemento indice 2 al Ultimo elemento

# AGREGAR Elementos a la Lista
Lista.append("Elemento")
Lista.insert(2, "Elemento")
Lista.extend(["Jueves", "Viernes"])

Lista2 = ["Sabado", "Domingo"]
Lista3 = Lista + Lista2

print("Elemento" in Lista)
print(Lista3.index("Domingo")) # Muestra el primer elemento que encuentra
print(Lista.count("Elemento")) # Muestra el conteo de los elementos coincidentes

#ELIMINAR elementos en la Lista
Lista.pop()           # Elimina el elemento en la ultima posicion
Lista.pop(2)          # Elimina el elemento en la posicion dada
Lista.remove("Lunes") # Elimina el elemento dado

#Limpiar la lista
Lista.clear()

#Invertir el orden de la Lista
Lista.reverse()

Lista = [1, 0, 2, 9, 3, 8, 4, 7, 5, 6]
Lista.sort()             # Ordenar la lista de menor a mayor - Ascendente
Lista.sort(reverse=True) # Ordenar la lista de menor a mayor - Descendente


# T U P L A S
# Las tuplas son INMUTABLES, no es posible agregar, modificar o eliminar elementos
# Las tuplas son mas RAPIDAS que las listas
# Las tuplas consumen menos memoria que las listas

#Crear Tupla
tupla = (1, 2, 3, 4, "Uno", "Dos", "Tres", "Cuatro", [4, 5, 6, 7] )

Lista = list(tupla)   # Convertir una tupla en una Lista
tupla = tuple(Lista3) # Convertir una tupla en una Lista


# C O N J U N T O S
# Los conjuntos no almacenan valores duplicados
# Los conjuntos no almacenan otras colecciones
# Los conjuntos no tienen un orden

# Crear Conjunto
conjunto = set()
conjunto = {}

# Agregar Elementos al conjuntos}
conjunto.add("Elemento")
conjunto.add(5)
conjunto.add('a')

# Eliminar elmentos de un conjunto
conjunto.discard("Elemento")

# Limpiar el conjunto
conjunto.clear()

# Buscar elemento en un conjunto
print( "Elemento" in conjunto )
print( "Elemento" not in conjunto )

#Operaciones matematicas con Conjuntos
a = {1, 2, 3}
b = {3, 4, 5}

c = a | c  # Union de Conjuntos
print(c)
c = a & c  # Interseccion de Conjuntos
print(c)
c = a - c  # Diferencia de Conjuntos
print(c)
c = a ^ c  # Diferencia simetrica
print(c)

a = {1, 2, 3}
b = {3, 4, 5}

c = {1, 2, 3, 4, 5}

print( a.issubset(c) )   # Subconjuntos
print( b.issubset(c) )   # Subconjuntos
print( c.issuperset(a) ) # Superconjuntos
print( a.isdisjoint(b) ) # Conjuntos disconexos

a = frozenset( {1, 2, 3}) #Hacer un conjunto INMUTABLES


# D I C C I O N A R I O S
#Crear Diccionario
diccionario = {}
diccionario = {"azul":"blue", "rojo":"red", "verde":"green"}
print(diccionario["azul"])

# Agregar Elementos a la Lista
diccionario["amarillo"] = "yellow"

# Modificar Elementos del Diccionario
diccionario["azul"] = "BLUE"

# Eliminar elementos en la Lista
del(diccionario["verde"])

#
equipo = { 10:"Paulo", 11:"Douglas", 7:"Cristiano", 17:"Mario"}

#Buscar en el diccionario
print( equipo[10] )
print( equipo.get( 19, "No existe la clave" ) )
print( 10 in equipo )

#Obtener las claves del diccionario
print( equipo.keys() )

#Obtener los valores del diccionario
print( equipo.values() )

print( len(equipo) )

#Limpiar la lista
equipo.clear()
