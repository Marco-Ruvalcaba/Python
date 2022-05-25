#TIPOS DE DATOS EN PYTHON
# TIPOS DE DATOS SIMPLES
# NUMERICOS
# * enteros (decimal, binario, octal, hexadecimal)
"Enteros: Este tipo de dato comprende el conjunto de los numeros enteros, pero en python el conjunto esta limitado por la capacidad de memoria disponible, no hay limite de representacion impuesto por el lenguaje"
"""
a = 2
b = 4
print( a + b ) <<< 6
print( a - b ) <<< -2
print( a * b ) <<< 8
print( b / a ) <<< 2
print( a % b ) <<< 2
"""
# * flotantes
"Flotantes: Este tipo de dato comprende el conjunto de los numeros flotantes, pero en python el conjunto esta limitado por la capacidad de memoria disponible, no hay limite de representacion impuesto por el lenguaje, se representan en el hardware del ordenador como fracciones de base 2"
"""
c = 2.2
d = 4.4
print( a + b ) <<< 6.6
print( a - b ) <<< -2.2
print( a * b ) <<< 9.68
print( b / a ) <<< 2
print( a % b ) <<< 2.2

"""
# * Complejos
"Complejos: Los numeros complejos tienen una parte real y otra imaginaria, y cada una de ellas se representa con un float"
"""
e = 2.2 + 3.3j
f = 4.4 + 3.3j
"""
# BOOLEANOS
# * bool(true, false)
"Bool: Esta clase solo se puede instanciar con dos valores/objetos: True y False"
"""
flag = True
flag = False
"""
# CADENAS DE TEXTO
# * string
"String: Un string es una secuencia inmutable de caracteres en formato Unicode"
"Ejemplo de un string"

# TIPOS DE DATOS COMPUESTOS
# SECUENCIAS
# * list
"List: Las listas son secuencias mutables de valores"
"""
lista = ['primero','segundo','tercero','cuarto','quinto']
print(factura[0]) <<< primero
print(factura[1]) <<< segundo
print(factura[2]) <<< tercero
print(factura[3]) <<< cuarto
print(factura[4]) <<< quinto

"Metodos"
lista.append("sexto")
lista.count("Sexto") <<< 1
lista.index("sexto") <<< 5
lista.insert(0, "cero") <<< ['cero', 'primero','segundo','tercero','cuarto','quinto', 'sexto']
lista.pop()             <<< ['cero', 'primero','segundo','tercero','cuarto','quinto']
lista.remove("cero")    <<< ['primero','segundo','tercero','cuarto','quinto']
lista.reverse()         <<< ['quinto', 'cuarto', 'tercero', 'segundo', 'primero']
lista.sort()            <<< ['cuarto', 'primero', 'quinto', 'segundo', 'tercero']
"""
# * tuple
"Tuple: Las tuplas son secuencuas inmutables de valores"
# * range
"Range: "

# MAPAS
# * dict
"Dict: Los diccionarios son tipos especiales de contenedores en los que se puede acceder a sus elementos a partir de una clave unica"

# CONJUNTOS
# * set
"Los conjuntos se utilizan para representar conjuntos unicos de elementos, es decir, en un conjunto no pueden existir dos objetos iguales"

# * Clases
"Python es un lenguaje orientado a objetos, de modo que tiene soporte de primer nivel para la creación de clases. No obstante, no es condición necesaria hacer uso de ellas para poder crear un programa"
"""
class NombreDeLaClase:
    def __init__(self, atributo1):
        self.atributo1 = atributo1
        self.atributo2 = "atributo2"

    def metodo1(self):
        print(Esto es un metodo)
        print("Esto es un atributo",{self.atributo1})
        print("Esto es otro atributo",{self.atributo2})
"""
# * Instancias
"""
instancia = NombreDeLaClase("atributo1")
instancia.metodo1()

instancia.atributo1 = "ejemplo-Atributo1"
instancia.atributo1 = "ejemplo-Atributo2"

instancia.metodo1()
"""

# * funciones
"Una función es un bloque de código con un nombre asociado, que recibe cero o más argumentos como entrada, sigue una secuencia de sentencias, las cuales ejecuta y devuelve un valor y/o realiza una tarea. La sentencia def es una definición de función usada para crear objetos funciones definidas por el usuario. Una definición de función es una sentencia ejecutable. La definición de función no ejecuta el cuerpo de la función; esto es ejecutado solamente cuando la función es llamada."
"""
def nombreDeLaFuncion(parametro1, parametro2):
    sentencia
    sentencia
    sentencia
    return valorDeRetorno
"""
# * Excepciones

# ESTRUCTURAS DE CONTROL - CICLOS
# ITERADORES
# * for
"Los ciclos for permiten ejecutar una o varias instrucciones de forma iterativa, una vez por cada elemento en la colección. Las colecciones pueden ser de varios tipos, el for puede recibir una colección predefinida o directamente de la salida de una función."
"""
for contador in range(1,10):
    print(contador)

numeros = [0, 1, 2, 3, 4, 5]
for numero in numeros:
    print(numero)
"""
# * for "each"
"""
frutas = {'Fresa':'roja', 'Limon':'verde', 'Papaya':'naranja', 'Manzana':'amarilla', 'Guayaba':'rosa'}
for nombre, color in frutas.items():
    print nombre, "es de color", color

for llave in frutas:
    print llave, 'es de color', frutas[llave]
"""
# * while
"El ciclo while permite ejecutar un bloque de instrucciones mientras se cumpla la condición dada. Primero comprueba que en efecto se cumple la condición dada y entonces, ejecuta el segmento de código correspondiente hasta que la condición no se cumpla."
"""
while numero <= 10:
    print numero
    numero += 1
"""

# ESTRUCTURAS DE CONTROL - CONDICIONALES
# * if
"La sentencia if EXPRESION, significa, Si se cumple la expresión condicional se ejecuta el bloque de sentencias seguidas"
# * if not
"La sentencia if not EXPRESION, significa que si se cumple la negacion de la expresion condicional se ejecuta el bloque de sentencias seguidas"
# * elif
"La sentencia elif EXPRESION, significa, De lo contrario Si se cumple la expresión condicional se ejecuta el bloque de sentencias seguidas"
# * else
"La sentencia else, significa, De lo contrario se cumple sin evaluar ninguna expresión condicional y ejecuta el bloque de sentencias seguidas."
"""
numero = 0
if numero > 0:
    print(positivo)
elif numero < 0:
    print(negativo)
else
    print(cero)
"""
# OPERADORES
# * is
"El operador is, significa, que prueba identidad: ambos lados de la expresión condicional debe ser el mismo objecto"
"""
print(1 is 1.)
<<< False
print(1 is 1)
<<< True
"""
# * in
"El operador in, significa, para cualquier colección del valor del lado derecho contenga el valor del lado izquierdo"
"""
b = [1, 2, 3]
print(2 in b)
<<< True
print(5 in b)
<<< False
"""
# * not in
"El operador not in, el contrario de operador in, devuelve True cuando un elemento no está en una secuencia."
"""
b = [1, 2, 3]
print(4 not in b)
<<< True
print(1 not in b)
<<< False
"""
