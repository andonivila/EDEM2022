
'''
Nombre
Artista
Año
Precio
Género (solo pueden ser de los siguientes)
Pop 2
Electro
Reggaeton
Rock
Metal
Death Metal
Black Metal
'''

from pprint import pprint



Faith_in_the_future = {'Nombre':'Faith in the future', 'Artista':'Louis Tomlinson', 'Año' :'2022', 'Precio':'16.37','Genero':'Pop'}

Parklife ={'Nombre':'Parklife', 'Artista':'Blur', 'Año' :'1994', 'Precio':'7.99','Genero':'Pop'}

Random_access_memories = {'Nombre':'Random Access Memories', 'Artista':'Daft Punk', 'Año' :'2013', 'Precio':'11.99','Genero':'Electro'}

Kid_A= {'Nombre':'Kid A', 'Artista':'Radio Head', 'Año' :'2000', 'Precio':'','Genero':'Electro'}

Calle_13 = {'Nombre':'Calle 13', 'Artista':'Calle 13', 'Año' :'2005', 'Precio':'20','Genero':'Reggaeton'}

El_Abayarde = {'Nombre':'El Abayarde', 'Artista':'Tego Calderon', 'Año' :'2002', 'Precio':'23.50','Genero':'Reggaeton'}

Nevermind = {'Nombre':'Nevermind', 'Artista':'Nirvana', 'Año' :'1991', 'Precio':'9.99','Genero':'Rock'}

The_Dark_Side_of_the_Moon={'Nombre':'The Dark Side of the Moon', 'Artista':'Pink Floyd', 'Año' :'1973', 'Precio':'12.99','Genero':'Rock'}

Ride_the_Lightning = {'Nombre':'Ride the Lightning', 'Artista':'Metallica', 'Año' :'1984', 'Precio':'15.99','Genero':'Metal'}

The_Number_of_the_Beast = {'Nombre':'The number of the Beast', 'Artista':'Iron Maiden', 'Año' :'1982', 'Precio':'14.99','Genero':'Metal'}

Spiritual_Healing = {'Nombre':'Spiritual Healing', 'Artista':'Death ', 'Año' :'1990', 'Precio':'30','Genero':'Death Metal'}

Human = {'Nombre':'Human', 'Artista':'Death', 'Año' :'1991', 'Precio':'21','Genero':'Death Metal'}

Black_Metal={'Nombre':'Black Metal', 'Artista':'Venom', 'Año' :'1982', 'Precio':'7.99','Genero':'Black Metal'}

Dark_Medieval_Times={'Nombre':'Dark Medieval Times', 'Artista':'Satyricon ', 'Año' :'1993', 'Precio':'16','Genero':'Black Metal'}



input ("Bienvendio usuario, pulsa la tecla enter para acceder a nuestro catalogo  ")

print ("Hola! esta es la lista de discos disponibles :\n\n")

print ('Faith in the future of Louis Tomlinson  \n\nParklife of Blur \n\nRandom Access Memories of Daft Punk \n\nKid A of Radio Head \n\nCalle 13 of Calle 13 \n\nEl Abayarde of Tego Calderon \n\nNervermind of Nirvana \n\nThe Dark Side of the Moon of Pink Floyd \n\nRide The Lightning of Metallica \n\nThe number of the beast of Iron Maiden \n\nSpiritual Healing of Death \n\nHuman of Death \n\nBlack Metal of Venom \n\nDark Medieval Times of Satyricon\n\n')


numero = int (input("Selecciona del 1 al 14 disco que desea comprar  "))

if numero == 1 :
    pprint (Faith_in_the_future)
elif numero == 2 :
    print (Parklife)
elif numero == 3 :
    print (Random_access_memories)
    print ("descuento")
elif numero == 4 :
    print (Kid_A)
elif numero == 5 :
    print (Calle_13)
elif numero == 6 :
    print (El_Abayarde)
elif numero == 7  :
    print (Nevermind)
elif numero == 8 :
    print (The_Dark_Side_of_the_Moon)
elif numero == 9 :
    print (Ride_the_Lightning)
elif numero == 10 :
    print (The_Number_of_the_Beast)
elif numero == 11 :
    print (Spiritual_Healing)
elif numero == 12 :
    print (Human)
elif numero == 13 :
    print (Black_Metal)
elif numero == 14 :
    print (Dark_Medieval_Times)

