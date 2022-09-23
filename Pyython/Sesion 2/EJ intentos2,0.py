import random
numero_secreto=5
numero_intentos=5
puntuacion = 2 



usuario=str (input("Como te llamas? "))

print (f"Hola {usuario} tu puntuacion actual es de {puntuacion} ")
print (f"Las reglas son, tienes que adivinar el numero secreto \n 1º Tienes {numero_intentos} intentos \n 2º Si acierta en el primer intento: Se suman 5 puntos y el resultado se multiplican por 2 \n 3º Si acierta en el segundo intento: Se suman 5 puntos \n 4º Si acierta a la tercera: Se suma 2 puntos \n 5º Si falla todas las veces: Se resta 2 puntos    ")

numero_elegido = int(input("Escoge un numero: ")) 

while numero_elegido != numero_secreto and numero_intentos>1:
    if numero_elegido<numero_secreto:
        print ("El numero secreto es más grande")
        numero_intentos=numero_intentos-1 
        print (f"Te quedan {numero_intentos} intentos")
        numero_elegido = int(input("Escoge un numero: "))

    else:
        print ("El numero secreto es mas pequeño")
        numero_intentos=numero_intentos-1
        print (f"Te quedan {numero_intentos} intentos")
        numero_elegido = int(input("Escoge un numero: ")) 
if numero_elegido == numero_secreto & numero_intentos==5:
    print (f"Perfecto el numero era el {numero_secreto}")
    puntuacion=(puntuacion+5)*2
    print (f"Tu puntuacion es de {puntuacion}")

if numero_elegido == numero_secreto & numero_intentos==4:
    print (f"Perfecto el numero era el {numero_secreto}")
    puntuacion=puntuacion+5
    print (f"Tu puntuacion es de {puntuacion}")
    
    
