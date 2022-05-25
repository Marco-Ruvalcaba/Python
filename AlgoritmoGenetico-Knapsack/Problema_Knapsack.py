class Knapsack:
    #def __init__(self, pesos, valores, capacidad):
    def __init__(self, valores, valorTotal, b):
        #self._pesos = pesos
        self._valores = valores
        self._valorTotal = valorTotal
        self._tope = b

    def f(self, cromosoma):
        f = 0
        for i in range(len(cromosoma)  ):
            if cromosoma[i] == 1:
                f += self._valores[i]
                
            if i < self._tope - 1:    # DONDE 5 ES EL ULTIMO ELEMENTO DEL INDIVIDUO
                if cromosoma[i] == 1 and cromosoma[i + 1] == 1:
                    f = 0
                    return f
                    
        return f
