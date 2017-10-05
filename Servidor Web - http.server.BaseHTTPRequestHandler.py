#Lo primero que hacemos es importar las librerias necesarias
from http.server import HTTPServer, BaseHTTPRequestHandler

"""
 Creamos una clase a la cual yo llamare "HttpHandler" que heredara 
 los metodos de la clase BaseHTTPRequestHandler.
"""
class HttpHandler(BaseHTTPRequestHandler):

	#Usaremos el metodo do_get, el cual es un metodo de BaseHTTPRquestsHandler.
	#Debemos recprdar que podemos hacer 2 tipos de peticiones, POST y GET
	#Usaremos GET

	def do_GET(self):
		#En este metodo definiremos las caractersticas de nuestro servidor HTTP.

		#Primero, enviamos una respuesta 200.
		#Eso lo logramos con el metodo send_response, psandole como argumento una respuesta
		self.send_response(200)

		#Luego, enviamos las cabezeras, yo enviare solo el tipo del contenido
		#Usamos el metodo send_header, pasandole como argumento la informacion deseada
		self.send_header('Content-type', 'text/HTML; charset=utf-8')
		#Con el metodo end_headers, terminamos de colocar las cabezeras del servidor
		self.end_headers()

		#Creamos una variable que contendra nuestro mensaje.
		#Fijense que estoy usando etiquetas HTML, ya que lo defini el los headers
		message = "<h1>Hola amigos de Mi Diario Python :D</h1>".encode()

		#Ahora, escribimos la respuesta en el cuerpo de la pagina
		self.wfile.write(message)

if __name__ == "__main__":
	server_address = ('', 8000)
	httpd = HTTPServer(server_address, HttpHandler)
	httpd.serve_forever()




