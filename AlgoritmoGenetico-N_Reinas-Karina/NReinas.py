from math import sqrt
from math import ceil

class NReinas:
    def __init__(self, n):
        self._tamanio_matriz = n
        self._matriz = [[0 for i in range(n)] for i in range(n)]
        self._tamanio_gen = ceil(sqrt(n))
        #self._X = [i for i in range(n)]
        #self._Y = []
        
    def Bitwise_coordenadas(self, cromosoma):
        coor = []
        indice = 0
        for i in range(self._tamanio_matriz):
            bits = 0
            for j in range(self._tamanio_gen):
                bits <<= 1
                bits |= cromosoma[indice]
                indice += 1
            coor.append(bits)
        #self._Y = coor
        return [a for a in enumerate(coor)]    

    def Colisiones(self, coordenada):
        # Verticales
        j = coordenada[1]
        for i in range(self._tamanio_matriz):
            if i != coordenada[0] and self._matriz[i][j]:
                #print('CV')
                return True;
            
        # Horizonales
        i = coordenada[0]
        for j in range(self._tamanio_matriz):
            if j != coordenada[1] and self._matriz[i][j]:
                #print('CH')
                return True
        
        # Diagonal
        i = coordenada[0] + 1
        j = coordenada[1] - 1
        while i < self._tamanio_matriz and 0 <= j:
            if (self._matriz[i][j]):
                #print('CD')
                return True;
            i += 1
            j -= 1
        
        i = coordenada[0] - 1
        j = coordenada[1] + 1
        while 0 <= i and j < self._tamanio_matriz:
            if self._matriz[i][j]:
                #print('CD-')
                return True
            i -= 1
            j += 1
                
        # Diagonal invertida
        i = coordenada[0] - 1
        j = coordenada[1] - 1
        while 0 <= i and 0 <= j:
            if self._matriz[i][j]:
                return True
            i -= 1
            j -= 1
            
        i = coordenada[0] + 1
        j = coordenada[1] + 1
        while i < self._tamanio_matriz and j < self._tamanio_matriz:
            if self._matriz[i][j]:
                return True
            i += 1
            j += 1
            
        return False
    
    def DibujarReinas(self):
        for i in self._matriz:
            for j in i:
                if j == 1:
                    print('ℜ ', end = "")
                else:
                    print('• ', end = "")
            print()

    def f(self, cromosoma):
        f = 0
        coordenadas = self.Bitwise_coordenadas(cromosoma)
        for c in coordenadas:
            if self.Colisiones(c) == False:
                self._matriz[c[0]][c[1]] = 1
                f += 1
        return f

