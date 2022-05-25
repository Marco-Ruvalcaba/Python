import NReinas
import AGR

def main():
    
    nreinas = NReinas.NReinas(12)
    
    cant_individuos = 30
    tamanio_gen     = nreinas._tamanio_gen
    alelos          = nreinas._tamanio_matriz * tamanio_gen
    generaciones    = 3000
    p               = 0.023
        
    ag = AGR.AG(cant_individuos, alelos, tamanio_gen, generaciones, p, nreinas)
    ag.run()
    print('G: ', ag._generacion)
    print('   M-H: ', ag._mejor_historico._cromosoma, ag._mejor_historico._fitness)
    #print('   C->M-H: ', nreinas.Bitwise_coordenadas(ag._mejor_historico._cromosoma))
    nreinas.DibujarReinas()


if __name__ == '__main__':
    main()
