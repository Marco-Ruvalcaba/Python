def Mergesort( list ):
    if len(list) > 1:
        mid = len(list)//2
        L = list[:mid]
        R = list[mid:]

        Mergesort(L)
        Mergesort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                list[k] = L[i]
                i += 1
            else:
                list[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            list[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            list[k] = R[j]
            j += 1
            k += 1
    return list
