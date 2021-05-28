#2. Utilizando la función get_all_sw_characters consuma los datos de todos los
#personajes de SW y resuelva lo siguiente:
#a. Listado ordenado de manera decreciente por nombre, mostrando nombre,
#altura y cantidad de peliculas
#b. Indicar los personajes que comienzan con la letra C y D, y los que terminan
#con s





import json
import requests

def consultar_personajes(url):
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        diccionario = json.loads(respuesta.text)       
        return diccionario
    else:
        print('nope')


urlbase = consultar_personajes('https://swapi.dev/api/people/')


sw_data = []

while(urlbase['next'] is not None):
    for doc in urlbase['results']:
        sw_data.append(doc)
    urlbase = consultar_personajes(urlbase['next'])


def nombre (item):    
    return (item['name'])

sw_data.sort(key=nombre)

for index, character in enumerate(sw_data):
        print(character['name'],'Peliculas :',character['films'],'Altura :',character['height'])
        



