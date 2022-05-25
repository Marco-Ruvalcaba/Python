import copy
import numpy as np
from math import ceil
from math import floor

class Individuo:
    def __init__(self, alelos, longitud_gen, cromosoma):
        self._alelos = alelos
        self._longitud_gen = longitud_gen
        self._cromosoma = cromosoma
        self._fitness = 0

class AG:
    def __init__(self, cantidad_individuos, alelos, tamano_gen, generaciones, p, problema):
        self._cantidad_individuos = cantidad_individuos
        self._alelos = alelos
        self._tamano_gen = tamano_gen
        self._generaciones = generaciones
        self._p = p
        self._problema = problema
        self._individuos = np.array([])
        self._generacion = 0

    def run(self):
        self.crearIndividuos()
        self._mejor_historico = self._individuos[0]
        self._generacion = 0
        while self._generacion < self._generaciones:
            self.evaluaIndividuos()
            hijos = np.array([])
            while len(hijos) < len(self._individuos):
                padre1 = self.ruleta()
                padre2 = self.ruleta()
                while padre1 == padre2:
                    padre2 = self.ruleta()
                h1, h2 = self.cruza(self._individuos[padre1], self._individuos[padre2])
                hijos = np.append(hijos, [h1])
                hijos = np.append(hijos, [h2])
            self.mutacion(hijos)
            self._individuos = np.copy(hijos)
            self._individuos[np.random.randint(len(self._individuos))] = copy.deepcopy(self._mejor_historico)
            if self._generacion % 100 == 0:
                print("G: ", self._generacion, '   M-H: ', self._mejor_historico._cromosoma, '   F: ', self._mejor_historico._fitness)
            self._generacion += 1

    def crearIndividuos(self):
        for i in range(self._cantidad_individuos):
            #cromosoma = np.random.randint(2, size = self._alelos) #Formara un numero aleatorio entre 0 y 2 (2) del tamaño de los alelos
            cromosoma = self.crearCromosoma()
            individuo = Individuo(self._alelos, self._tamano_gen, cromosoma)
            self._individuos = np.append(self._individuos, [individuo])
            
    def crearCromosoma(self):
        #Generar un nuevo cromosoma menor al numero de reinas-1 
        n = self._alelos / self._tamano_gen
        while True:
            cromosoma = np.random.randint(2, size = self._tamano_gen)
            if self.Bitwise(cromosoma) < n:
                break
        n = ceil(n)
        for i in range(n-1):
            #Generar un genoma de tamaño del gen y verificar si es menos al tamaño de la matriz
            while True:
                genoma = np.random.randint(2, size = self._tamano_gen)
                if self.Bitwise(genoma) < n:
                    break
            cromosoma = np.concatenate((cromosoma, genoma), axis = None) #Concatenar
        if self.verificarCruza(cromosoma):
            return cromosoma
        else:
            self.crearCromosoma()
            
            
    def Bitwise(self, genoma):
        numDec = 0
        for j in range(self._tamano_gen):
            numDec <<= 1
            numDec |= genoma[j]
        return numDec

    def evaluaIndividuos(self):
        for i in self._individuos:
            i._fitness = self._problema.f(i._cromosoma)
            if i._fitness > self._mejor_historico._fitness:
                self._mejor_historico = copy.deepcopy(i)

    def ruleta(self):
        f_sum = np.sum([i._fitness for i in self._individuos])
        if f_sum == 0:
            return np.random.randint(len(self._individuos))
        else:
            r = np.random.randint(f_sum + 1)
            k = 0
            F = self._individuos[k]._fitness
            while F < r:
                k += 1
                F += self._individuos[k]._fitness
            return k

    def cruza(self, i1, i2):
        h1 = copy.deepcopy(i1)
        h2 = copy.deepcopy(i2)

        s = self._alelos - 1
        punto_cruza = np.random.randint(s) + 1
        while True:
            for i in range(punto_cruza, self._alelos):
                h1._cromosoma[i], h2._cromosoma[i] = h2._cromosoma[i], h1._cromosoma[i]
            if self.verificarCruza(h1._cromosoma) and self.verificarCruza(h2._cromosoma):
                break
        return h1, h2
    
    def verificarCruza(self, cromosoma):
        n = ceil(self._alelos / self._tamano_gen)
        cruza = []
        indice = 0
        for i in range(n):
            bits = 0
            for j in range(self._tamano_gen):
                bits <<= 1
                bits |= cromosoma[indice]
                indice += 1
            cruza.append(bits)
        cruza = [a for a in enumerate(cruza)]
        for k in cruza:
            if k[1] >= n:
                return False
        return True
                        
    def mutacion(self, hijos):
        for h in hijos:
            for bit in range(len(h._cromosoma)):
                h2 = np.copy(h._cromosoma)
                if np.random.rand() < self._p:
                    h2[bit] = int(not h2[bit])
                    if self.validarPosicionMutacion(bit, h2):
                        h._cromosoma = np.copy(h2)
                    else:
                        h3 = np.copy(h._cromosoma)
                        h3[bit+1] = int(not h3[bit+1])
                        if self.validarPosicionMutacion(bit+1, h3):
                            h._cromosoma = np.copy(h3)    
                        """else:
                            h4 = np.copy(h._cromosoma)
                            h4[bit-1] = int(not h4[bit-1])
                            if self.validarPosicionMutacion(bit-1, h4):
                                h._cromosoma = np.copy(h4)"""
                        
                    
    def validarPosicionMutacion(self, bit, cromosoma):
        p = floor(bit / self._tamano_gen)
        n = ceil(self._alelos / self._tamano_gen)
        inicio = p * self._tamano_gen
        genoma2 = []
        genoma = np.array(genoma2, dtype=int)
        for i in range(inicio, inicio + self._tamano_gen):
            genoma = np.concatenate((genoma, cromosoma[i]), axis = None)
        bits = 0
        for j in range(self._tamano_gen):
            bits <<= 1
            bits |= genoma[j]
        dec = bits
        if dec >= n:
            return False
        else:
            return True
        
        