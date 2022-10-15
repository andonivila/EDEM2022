import requests
import json
import time
import pandas as pd

resp = requests.get('https://thesimpsonsquoteapi.glitch.me/quotes')

frase=resp.json()[0]['quote']
personaje=resp.json()[0]['character']

Lisa='Lisa Simpson'
Homer='Homer Simpson'

print (frase)
print (personaje)



