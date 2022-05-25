import POO_Classes as CE
import DataStructures_Lists as DCT

import random
from random import shuffle

def main():
    L = []

    for i in range(0, 10):
        y = CE.Person( DCT.PersonNames[random.randint( 0, len(DCT.PersonNames)-1 ) ], DCT.PersonSurnames[random.randint( 0, len( DCT.PersonSurnames )-1 ) ], random.randint( 18, 75 ), "1." + str( random.randint( 50, 99 ) ), random.randint( 60, 99 ) )
        L.append(y)

    for i in L:
        i.ShowData()

main()
