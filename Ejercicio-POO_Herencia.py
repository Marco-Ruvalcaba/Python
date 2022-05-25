class Mascota():
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.vacunado = False
        self.adoptado = False
        self.comprado = False

    def __str__(self):
        return " Mascota \n Nombre: "+ self.nombre +"\n Edad:   "+ str(self.edad)

    def Caracteristicas(self):
        print("  ")
        print(" <- Mascota -> ")
        print(" Nombre:", self.nombre)
        print(" Edad:  ", self.edad)

class Gato(Mascota):
    def Maullido(self, sonido):
        self.maullido = sonido
        if(self.maullido):
            return "Tengo hambre"
        else:
            return "Alejate humano"

class Perro(Mascota):
    trucoAprendido = ""

    def Truco(self):
        self.trucoAprendido = "Dar la patita"

    def Caracteristicas(self):
        print(" <- Mascota -> ")
        print(" Nombre:", self.nombre)
        print(" Edad:  ", self.edad)
        print(" Truco: ", self.trucoAprendido)



Mi_Perro = Perro("Spanky", 8)

#Mi_Mascota.Truco()
Mi_Perro.Caracteristicas()

Mi_Gato = Gato("Touluse", 10)
Mi_Gato.Caracteristicas()
print( Mi_Gato.Maullido(True) )
