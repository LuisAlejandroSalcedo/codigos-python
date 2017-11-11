__author__ = "Luis Salcedo"

from PIL import Image, ImageDraw, ImageFont

img = Image.open("medusa.jpg")

draw = ImageDraw.Draw(img)

font = ImageFont.truetype("arial.ttf", 80)

draw.text((50, 50), "Hola, Mi Diario Python :D", 
	fill="white", font=font)

img.show()

# Vista nuestro blog: pythondiario.com