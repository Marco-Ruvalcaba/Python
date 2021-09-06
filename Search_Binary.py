def Binary( list, element ):
    left = 0
    right = len( list ) - 1
    while left <= right:
        half = int( ( right + left ) / 2 )
        if list[half] == element:
            return True
        elif list[half] < element:
            left = half + 1
        elif list[half] > element:
            right = half - 1
    return False

def Binary_Position( list, element ):
    left = 0
    right = len( list ) - 1
    while left <= right:
        half = int( ( right + left ) / 2 )
        if list[half] == element:
            return half
        elif list[half] < element:
            left = half + 1
        elif list[half] > element:
            right = half - 1
    return -1
