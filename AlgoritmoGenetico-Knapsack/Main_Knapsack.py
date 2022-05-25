import Problema_Knapsack
import Algoritmo_Knapsack
#import queens

def main():

    #pesos = [22, 14, 16, 23, 12, 15, 22, 6, 19, 20, 40, 8, 16, 6, 15, 21, 16]
    #valores = [55, 34, 28, 30, 80, 3, 28, 24, 21, 43, 54, 12, 21, 11, 6, 21, 28]
    #valores = [1, 3, 5, 3, 1, 2, 8, 1, 6, 6, 4, 1, 2, 7, 2, 9, 1]
    valores = [5, 1, 2, 10, 6, 2, 13, 4, 6]
    #valores = [1, 1, 10, 11, 1, 1]

    a = 20              # a= Numero de individuos
    b = len(valores)    # b= Numero de alelos
    c = 1               # c= Tamaño del Gen
    d = 5000            # d= Generaciones
    e = 0.01            # e= Factor de mutacion
    f = 12

    for i in range(len(valores)):
        f += valores[i]

    #mochila = knapsack.Knapsack(pesos, valores, 215)
    mochila = Problema_Knapsack.Knapsack(valores, f, b)

    ag = Algoritmo_Knapsack.AG(a, b, c, d, e, mochila)
    ag.run()

if __name__ == '__main__':
    main()
