#Importamos http.client para enviar peticones HTTP
import http.client as hc

#la libreria BeautifulSoup (bs4) nos permite parsear el contenido HTML
import bs4

#Creamos la conexión a "pythondiario.com"
conn = hc.HTTPConnection("www.pythondiario.com")
conn.request("GET", "/index.html") #Pedimos el archivo "index.html"
res = conn.getresponse() #Guardamos la respuesta en "res"

#parseamos la respuesta del servidor (cuerpo HTML)
sopa = bs4.BeautifulSoup(res.read(), "html.parser") 

"""
Creamos un archivo con extensión "txt" en el cual guadaremos 
los datos. Nos referiremos a este archivo como "scraping"
"""
with open("imagenes y links.txt", "w") as scraping:
	scraping.write("Links de la pagina: \n")

	#Con este for iteramos todas las etiquetas "a" que se encuentren
	for link in sopa.find_all("a"):
	#Con el metodo get decimos que solo queremos el valor del atributo
		scraping.write(str(link.get("href")) + "\n")

	scraping.write("\n Imagenes de la pagina: \n")
	
	#Iteramos todas las imagenes y obtenemos solo su atributo src
	for img in sopa.find_all('img'):
		scraping.write(str(img.get('src')) + "\n")

