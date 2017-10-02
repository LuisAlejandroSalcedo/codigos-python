import turtle

def dibujar_cuadrado():
  for x in range(0, 4):
	  turtle.forward(50)
	  turtle.left(90)
  
def mas_cuadrados():
  #Más cuadrados
  grados = 0
  turtle.speed(15)
  for x in range(1, 40):
	  for x in range(0, 4):
		  turtle.forward(50)
		  turtle.left(90)
	  turtle.left(grados + 10)
