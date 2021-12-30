def particionado(lista):

    pivote = lista[0]
    menores = []
    mayores = []

    for i in range( 1, len(lista) ):
        if lista[i] < pivote:
            menores.append(lista[i])
        else:
            mayores.append(lista[i])

    return menores, pivote, mayores

def Quicksort( list ):
    if len( list ) < 2:
        return list

    minor, pivot, mayor = particionado(list)

    return Quicksort( minor ) + [pivot] + Quicksort( mayor )
