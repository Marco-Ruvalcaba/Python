def existeParASumar(list, resultado):
    inferior = 0
    superior = len(list)-1

    while inferior < superior:
        suma = list[inferior] + list[superior]
        if suma == resultado:
            return True
        if suma < resultado:
            inferior += 1
        else:
            superior -= 1

    return False

lista = [1,2,4,4]
resultado = 8

print(existeParASumar(lista, resultado))
