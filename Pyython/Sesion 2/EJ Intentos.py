numero_elegido = int(input("Escoge un numero: ")) 
numero_secreto=300

numero_intentos=3



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


if numero_elegido == numero_secreto:
    print (f"Perfecto el numero era el {numero_secreto}")
    





