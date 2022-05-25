def biggest(list):
    acumulador = 0
    for element in list:
        if element > acumulador:
            acumulador = element
    return acumulador

list = [1,8,2,9,1,0,3,6,11,22,7,8,9,1,4,3,2,-11,12,99]
print(biggest(list))
