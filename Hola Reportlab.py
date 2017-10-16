#Importamos los modulos necesarios
from reportlab.pdfgen import canvas

doc = canvas.Canvas("Hola Mundo.pdf")

#Escribimos una cadena de Texto dentro del documento
doc.drawString(100, 750, "Hola Mundo!!!")

#Guardamos el documento
doc.save()
