__author__ = "Luis Salcedo"

#Visita nuestro Blog http://www.pythondiario.com/

from googleapiclient.discovery import build
import pprint

api_key = "CLAVE_DE_API"

service = build('books', 'v1', developerKey=api_key)

request = service.volumes().list(source='public', q='python')

response = request.execute()
pprint.pprint(response)

print('\n Encontrado %d libros:' % len(response['items']))
for book in response.get('items', []):
  print('Titulo: %s'% (
    book['volumeInfo']['title']))
