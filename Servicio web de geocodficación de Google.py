import requests

address = input("Ingresar ubicación: ")

params = {'address':address}

response = requests.get("https://maps.googleapis.com/maps/api/geocode/json", params=params)

if response.status_code == 200:
	print(response.json())
	with open("Geocodificacion.json", "wb") as f:
		for x in response.iter_content():
			f.write(x)
		f.close()

# Visitanos en nuestra pagina: www.pythondiario.com