from scapy.all import *
import pyx

a = sniff(filter='tcp', count=1)
print(" \n\n ")
print("---- PRIMERA IMPRESION ----")
print("Paquete 1-")
hexdump(a[0])

print(" \n\n ")
print("---- SEGUNDA IMPRESION ----")
a[0].show()


b = raw( a[0] )

print("Cadena", b, "typo", type(b))
hexdumpList = []
indice = 0
for i in b:
    print("Byte", indice, "->", i, "HEX", hex(i))
    indice += 1
    hexdumpList.append( str( hex(i) ) )

for i in hexdumpList:
    print("Elemento de la lista ->", i)

print(" \n\n ")
print("---- EXPERIMENTO 1 ----")
print( len(a[0]) )
print("---- EXPERIMENTO 1 ----")

print(" \n\n ")
print("---- EXPERIMENTO 2----")
ls(a[0])
print("---- EXPERIMENTO 2 ----")




print(" \n\n ")
print("---- EXPERIMENTO 3 ----")
print( type( a[0] ) )
print("---- EXPERIMENTO 3 ----")
print( raw( IP() ) )
print("---- EXPERIMENTO 3 ----")
print( raw( TCP() ) )
print("---- EXPERIMENTO 3 ----")

print(" \n\n ")
print("---- EXPERIMENTO 4----")
for i in range(0, len(a[0]) ):
    print( type(i), "---->", a[0][i] )
    print(" \n ")
print("---- EXPERIMENTO 4 ----")

print(" \n\n ")
print("---- EXPERIMENTO 5----")
#print( a[0].sprintf(  ) )
#print( a[0].summary() )
print("---- EXPERIMENTO 5 ----")

#print(" \n\n ")
#print("---- CREACION DEL PDF ----")
#a[0].pdfdump("ejemplo.eps",layer_shift=1)




#
