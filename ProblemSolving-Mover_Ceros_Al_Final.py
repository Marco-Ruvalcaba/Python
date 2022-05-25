def swap(a, b):
    temp = a
    a = b
    b = temp
    return a,b

def movezeros(list):
    ultimocero = 0
    for i in range(0, len(list)):
        if list[i] != 0:
            list[ultimocero], list[i] = swap(list[ultimocero], list[i])
            ultimocero += 1

    return list

list = [0, 0, 0, 22, 7, 8, 4]
print(movezeros(list))
