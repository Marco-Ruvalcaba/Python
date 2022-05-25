import reinas
import NR
#import queens

def main():

    n = 12       # n= Numero de reinas
    a = 30       # a= Numero de individuos
    b = 4        # c= Tamaño del gen
    c = b*n      # b= Numero de alelos
    d = 10000    # d= Generaciones
    e = 0.01     # e= Factor de mutacion

    nreinas = reinas.Reinas(n)
    ag = NR.AG(a, b, c, d, e, nreinas)
    ag.run()

if __name__ == '__main__':
    main()
