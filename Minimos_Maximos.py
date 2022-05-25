import numpy as np
import matplolib.pyplot as plt

# UN DICCIONARIO PARA CREAR UNA FUENTE
titulo = {
'family' : 'serif',
'size' : 32,
'color' : '#55ffaa',
}

# GENERA UNA LINEA DESDE -2.5 HASTA 2.5 CON 32 PUNTOS
x = np.Linspace(-2.5, 2.5, 32)
y = 2*x**3 - 6*x + 4 

xp = [1,-1]
yp = [0, 8]

# ETIQUETAS
labels = ['Minimo', 'Maximo']

# PLOTEA (GENERA) LA GRAFICA
plt.plot(x,y,'b')
# PLOTEA UN * ROJO 
plt.plot(xp,yp, '*r')

#PLOTEA LOS LABELS
for t in zip(xp,yp, labels):
	plt.text(*t)

# ETIQUETAS
plt.xlabel('X')
plt.ylabel('Y')

# TITULO PARA LA GRAFICA
plt.title('2x^3 - 6x + 4')
# TITULO CON FUENTE 
plt.title('2x^3 - 6x + 4', fontdict = titulo)

plt.show()