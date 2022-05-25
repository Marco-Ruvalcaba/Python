from scapy.all import *
import pyx

def Experimento():
    a = sniff(filter='tcp', count=1)

    print(" \n ")
    print("---- PRIMERA IMPRESION ----")
    hexdump(a[0])

    print(" \n\n ")
    print("---- SEGUNDA IMPRESION ----")
    a[0].show()


    b = raw( a[0] )

    #print("Cadena", b, "typo", type(b))
    hexdumpList = []
    indice = 0
    for i in b:
        indice += 1
        hexdumpList.append( str( hex(i) )[2:] )

    for i in hexdumpList:
        print("Elemento de la lista ->", i)

    print(" \n\n ")
    print("---- EXPERIMENTO 1 ----")
    print( len(a[0]) )
    print("---- EXPERIMENTO 1 ----")

    print(" \n\n ")
    print("---- CREACION DEL PDF ----")
    a[0].pdfdump("ejemplo.eps",layer_shift=1)
    

    return hexdumpList

list = Experimento()

print(list)







#
