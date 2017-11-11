__author__ = "Luis Salcedo"

from PIL import Image, ImageDraw

img = Image.open("./medusa.jpg")

draw = ImageDraw.Draw(img)
draw.line((0, 0) + img.size, fill=128, width=100)
draw.line((0, img.size[1], img.size[0], 0), fill=128, width=100)

img.save("MedusaDraw.jpg")

# Vista nuestro blog: pythondiario.com