from multiprocessing.sharedctypes import Value
from turtle import st
import requests


def obtenerChiste ():
    
    # Definimos la URL a la que vamos a solicitar una respuesta y Realizamos la peticion GET 
    respuesta=requests.get('https://api.chucknorris.io/jokes/random')
    #Extraemos los datos en formato JSON
    datos=respuesta.json()
    #Obtenemos valor en la clave 'value' del JSON que nos interesa
    frase_chuck :str = datos ['value']
    return frase_chuck

