


numeroElegido=int(input("Elige un número: "))
numeroBuscado = 300
intentos = 3



while(numeroElegido != numeroBuscado):
    if(numeroElegido > numeroBuscado):
        numeroElegido = int(input("Has fallado, el número buscado es más pequeño: "))  
        print (intentos)
        intentos = intentos-1
       
    else:
        numeroElegido = int(input("Has fallado, el número buscado es más grande: "))



print(f"Has ganado, el número era {numeroBuscado}")



