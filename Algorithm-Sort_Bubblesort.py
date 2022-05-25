def Bubblesort( list ):
    for i in range( len(list) ):
        for j in range( i + 1, len(list) ):
            if list[i] > list[j]:
                aux = list[j]
                list[j] = list[i]
                list[i] = aux
    return list
