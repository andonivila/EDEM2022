from pprint import pprint


titulo=str(input("Dime el titulo de la pelicula "))
director=str(input("Dime el director "))
year=str(input("¿En que año se rodo? "))
pais=str(input("¿Cual es el pais de origen? "))



pelicula = {'Titulo' : {titulo}, 'Director':{director}, 'Año':{year}, 'Pais':{pais}}

pprint (pelicula)