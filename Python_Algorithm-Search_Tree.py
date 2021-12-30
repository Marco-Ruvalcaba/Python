def Linear( list, element ):
    for elem in list:
        if elem == element:
            return True
    return False

def Linear_Position( list, element ):
    for elem in list:
        if elem == element:
            return list.index(elem)
    return -1
