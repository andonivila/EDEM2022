
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
from datetime import date 



Faith_in_the_future = {'Nombre':'Faith in the future', 'Artista':'Louis Tomlinson', 'Año' :'2022', 'Precio':'16.37','Genero':'Pop'}

Parklife ={'Nombre':'Parklife', 'Artista':'Blur', 'Año' :'1994', 'Precio':'7.99','Genero':'Pop'}

Random_access_memories = {'Nombre':'Random Access Memories', 'Artista':'Daft Punk', 'Año' :'2013', 'Precio':'12','Genero':'Electro'}

Kid_A = {'Nombre':'Kid A', 'Artista':'Radio Head', 'Año' :'2000', 'Precio':'20','Genero':'Electro'}

Calle_13 = {'Nombre':'Calle 13', 'Artista':'Calle 13', 'Año' :'2005', 'Precio':'20','Genero':'Reggaeton'}

El_Abayarde = {'Nombre':'El Abayarde', 'Artista':'Tego Calderon', 'Año' :'2002', 'Precio':'23.50','Genero':'Reggaeton'}

Nevermind = {'Nombre':'Nevermind', 'Artista':'Nirvana', 'Año' :'1991', 'Precio':'9.99','Genero':'Rock'}

The_Dark_Side_of_the_Moon={'Nombre':'The Dark Side of the Moon', 'Artista':'Pink Floyd', 'Año' :'1973', 'Precio':'12.99','Genero':'Rock'}

Ride_the_Lightning = {'Nombre':'Ride the Lightning', 'Artista':'Metallica', 'Año' :'1984', 'Precio':'15.99','Genero':'Metal'}

The_Number_of_the_Beast = {'Nombre':'The number of the Beast', 'Artista':'Iron Maiden', 'Año' :'1982', 'Precio':'14.99','Genero':'Metal'}

Spiritual_Healing = {'Nombre':'Spiritual Healing', 'Artista':'Death ', 'Año' :'1990', 'Precio':'30','Genero':'Death Metal'}

Human = {'Nombre':'Human', 'Artista':'Death', 'Año' :'1991', 'Precio':'21','Genero':'Death Metal'}

Black_Metal={'Nombre':'Black Metal', 'Artista':'Venom', 'Año' :'1982', 'Precio':'8','Genero':'Black Metal'}

Dark_Medieval_Times={'Nombre':'Dark Medieval Times', 'Artista':'Satyricon ', 'Año' :'1993', 'Precio':'16','Genero':'Black Metal'}



input ("Bienvendio usuario, pulsa la tecla enter para acceder a nuestro catalogo  ")

print ("Hola! esta es la lista de discos disponibles :\n\n")

print ('1º Faith in the future of Louis Tomlinson  \n\n2º Parklife of Blur \n\n3º Random Access Memories of Daft Punk \n\n4º Kid A of Radio Head \n\n5º Calle 13 of Calle 13 \n\n6º El Abayarde of Tego Calderon \n\n7º Nervermind of Nirvana \n\n8º The Dark Side of the Moon of Pink Floyd \n\n9º Ride The Lightning of Metallica \n\n10º The number of the beast of Iron Maiden \n\n11º Spiritual Healing of Death \n\n12º Human of Death \n\n13º Black Metal of Venom \n\n14º Dark Medieval Times of Satyricon\n\n')

numero = int (input("Selecciona del 1 al 14 disco que desea comprar  "))

if numero == 1 :
    pprint (Faith_in_the_future)
    seleccion=Faith_in_the_future
    nombre=Faith_in_the_future ['Nombre']
elif numero == 2 :
    pprint (Parklife)
    seleccion = Parklife
    nombre=Parklife['Nombre']
elif numero == 3 :
    pprint (Random_access_memories)
    print (f'\n\nEste genero tiene un 30% de descuento, el precio ahora es de 8,40€')
    Random_access_memories = {** Random_access_memories, 'Precio': '8.40'}
    seleccion = Random_access_memories
    nombre=Random_access_memories['Nombre']
elif numero == 4 :
    pprint (Kid_A)
    print (f'\n\nEste genero tiene un 30% de descuento, el precio ahora es de 14€')
    seleccion=(Kid_A)
    nombre=Kid_A['Nombre']
elif numero == 5 :
    pprint (Calle_13)
    seleccion=Calle_13
    nombre =Calle_13 ['Nombre']
elif numero == 6 :
    pprint (El_Abayarde)
    seleccion= El_Abayarde
    nombre = El_Abayarde ['Nombre']
elif numero == 7  :
    pprint (Nevermind)
    seleccion = Nevermind
    nombre = Nevermind ['Nombre']
elif numero == 8 :
    pprint (The_Dark_Side_of_the_Moon)
    seleccion =The_Dark_Side_of_the_Moon
    nombre= The_Dark_Side_of_the_Moon ['Nombre']
elif numero == 9 :
    pprint (Ride_the_Lightning)
    seleccion = Ride_the_Lightning
    nombre= Ride_the_Lightning['Nombre']
elif numero == 10 :
    pprint (The_Number_of_the_Beast)
    seleccion= The_Number_of_the_Beast
    nombre=The_Number_of_the_Beast ['Nombre']
elif numero == 11 :
    pprint (Spiritual_Healing)
    seleccion=Spiritual_Healing
    nombre = Spiritual_Healing ['Nombre']
elif numero == 12 :
    pprint (Human)
    seleccion=Human
    nombre=Human ['Nombre']
elif numero == 13 :
    pprint (Black_Metal)
    seleccion=Black_Metal
    nombre=Black_Metal['Nombre']
    print (f'\n\nEste genero tiene un 30% de descuento, el precio ahora es de 5.60')

elif numero == 14 :
    pprint (Dark_Medieval_Times)
    seleccion=Dark_Medieval_Times
    nombre=Dark_Medieval_Times['Nombre']
    Dark_Medieval_Times = {** Dark_Medieval_Times, 'Precio': '11,20€'}
    print (f'\n\nEste genero tiene un 30% de descuento, el precio ahora es de 11,20€')



nnumero=int(input(f'\n \n Ha escogido {nombre} pulsa la tecla 0 para generar el ticket '))

if nnumero == 0:
    print (f"\n\n Muchas gracias por tu compra\n\n") 
    hoy = date.today()
    print (f"Fecha de compra {hoy} ")
    
    print(r"""      
 ___________________________________________
|  _______________________________________  |
| / .-----------------------------------. \ |
| | | /\ :                        90 min| | |
| | |/--\:....................... NR [ ]| | |
| | `-----------------------------------' | |
| |      //-\\   |         |   //-\\      | |
| |     ||( )||  |_________|  ||( )||     | |
| |      \\-//   :....:....:   \\-//      | |
| |       _ _ ._  _ _ .__|_ _.._  _       | |
| |      (_(_)| |(_(/_|  |_(_||_)(/_      | |
| |                           |           | |
| `______ ____________________ ____ ______' |
|        /    []             []    \        |
|       /  ()              Anto ()  \       |
!______/_____________________________\______!  


""")


