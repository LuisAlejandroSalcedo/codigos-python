__author__ = "Luis Salcedo"

from matplotlib import pyplot

#Función Lineal.
def f(x):
    return 4*x-7

#En esta variable se genra una lista a partir de los valores -10 y 10.
#Todos estos valores seran los que tomara x.
x = range(-10, 10)

#Con el metodo plot especificamos que función graficaremos.
#El primer argumento es la variable con los valores de x.
#El segundo argumento le pasamos todos estos valares a la función con ayuda de un bucle.
pyplot.plot(x, [f(i) for i in x])

#Establecemos el color de los ejes.
pyplot.axhline(0, color="black")
pyplot.axvline(0, color="black")

#Especificamos los limites de los ejes.
pyplot.xlim(-11, 11)
pyplot.ylim(-11, 11)

#Guardamos el grafico en una imagen "png".
pyplot.savefig("función_lineal.png")

# Mostramos el grafico.
pyplot.show()

#Visita nuestro blog: http://www.pythondiario.com/