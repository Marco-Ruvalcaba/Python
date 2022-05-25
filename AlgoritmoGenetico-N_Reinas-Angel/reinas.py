class Reinas:
    def __init__(self, n):
        self._n = n

    def Bitwise(self, genoma):
        NuDe = 0
        for i in range (self.tamano_gen):
            NuDe <<= 1
            NuDe |= genoma[i]
        return NuDe

    def f(self, cromosoma):
        f = 0
        nd = 0
        tamañoalelos = 4
        int = []

        # SE CONVIERTE A DECIMAL
        for i in range(len(cromosoma)):

            if nd >= genoma:
                return 0
            else:
                int[] = np.append(int[],[cromosoma])

        # SE VERIFICAN COLOSIONES EN Y
        for i in range(len(int):
            for j in range(tamañoalelos):
                if int[i] == int[j]:
                    return 0
                else:
                    f+=
        # SE VERIFICAN COLISIONES EN LAS DIAGONALES
