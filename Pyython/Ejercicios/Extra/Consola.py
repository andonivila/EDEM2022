''' 
EJERCICIO PARA CASA 

Una consola que pida

Nombre 
Email
Contraseña
Edad
y aceptar el entrar

(pensar que datos son cada elemento)

Con todos los elementos tiene que crear un usuario (diccionario)

y mostrar los datos por consola al finalizar

'''



print ("Hola usuario")



input("Pulsa enter para continuar...")

name = input ("¿Cual es tu nombre? ")
print (f"Perfecto {name} ayudame a responder a unas preguntas")

email=input ("Puedes decirme tu direccion de correo ")

print (f"Perfecto {name} entonces tu correo es {email} ¿no?")

input("Pulsa enter para confirmar...")

from ast import AugAssign
import getpass
from webbrowser import get



password = getpass.getpass ("Escribe tu contraseña ")
password_again = getpass.getpass ("Confirma tu contraseña ")

while password != password_again:
    print("Ups! Parece que algo ha salido mal,")
    password_again = getpass.getpass ("Vamos a probar otra vez ") 

print(f"Perfecto {name} parece que ha salido todo genial")

edad = input (f"¿Y {name} Cuanto años tienes? ")

print ("Perfecto!")

usuario = {'nombre':name, 'email':email, 'contraseña': password, 'edad':edad}

print("Vamos a revisar que todos los datos sean correctos,")
input ("Pulsa enter para continuar")

print ("Tu nombre de usuario es ... " , *usuario["nombre"])

print ("Tu direccion de correo electronico es ... ", usuario["email"])

print ("Tu contraseña es *********")

print ("Tu edad es ", usuario["edad"])

exit



