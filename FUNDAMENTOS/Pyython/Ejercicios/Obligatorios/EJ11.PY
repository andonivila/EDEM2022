import time

dic=[]

print(f"\nBuenos dias, \n ¿Que operacion desea realizar? \n 1º Añadir un cliente (1) \n 2º Eliminar clientes por NIF (2) \n 3º Mostrar cliente por NIF (3) \n 4º Listar TODOS los clientes (4) \n 5º Mostrar UNICAMENTE los clientes preferentes (5) \n 6º Finalizar programa (6)")

eleccion=input('\n Indique un numero y pulse Enter   ')

q=0
a=1
i=0
z=0
repe='1'

while repe=='1':
    if eleccion =='1':
        nif_cliente=int(input('\n¿Cual es el DNI del cliente? '))
        nombre_cliente=input('¿Cual es el nombre del cliente? ')
        apellido_cliente=input('¿Cual es el apellido del cliente? ')
        telefono_cliente=input('¿Cual es el telefono del cliente? ')
        email_cliente=input('¿Cual es el email del cliente? ')
        preferente_cliente=int(input('¿Es el cliente preferente? --> Marque 1 para SI y 0 para NO <-- '))
        dic.append({'DNI':nif_cliente, 'Nombre':nombre_cliente, 'Apellido':apellido_cliente, 'Telefono':telefono_cliente, 'Email':email_cliente, 'Preferente':preferente_cliente})
        repe=input("\n\n ¿Quiere realizar otra operacion? \nMarque 1 para SI \nMarque 0 para NO \n ")
        if repe=='1':
            print("\n¿Que operacion desea realizar? \n 1º Añadir un cliente (1) \n 2º Eliminar clientes por NIF (2) \n 3º Mostrar cliente por NIF (3) \n 4º Listar TODOS los clientes (4) \n 5º Mostrar UNICAMENTE los clientes preferentes (5) \n 6º Finalizar programa (6)")
            eleccion=input('\n Indique un numero y pulse Enter   ')
        else:
            exit ()
            
    if eleccion=='2':
        bus_dni=int(input("Cual es el DNI "))
        donde_dni=(next((x for x in dic if x['DNI'] == bus_dni), None))
        dic.remove(donde_dni)
        repe=input("\n\n ¿Quiere realizar otra operacion? \nMarque 1 para SI \nMarque 0 para NO \n ")
        if repe=='1':
            print("\n¿Que operacion desea realizar? \n 1º Añadir un cliente (1) \n 2º Eliminar clientes por NIF (2) \n 3º Mostrar cliente por NIF (3) \n 4º Listar TODOS los clientes (4) \n 5º Mostrar UNICAMENTE los clientes preferentes (5) \n 6º Finalizar programa (6)")
            eleccion=input('\n Indique un numero y pulse Enter   ')
        else:
            exit ()
    
    if eleccion=='3':
        bus_dni=int(input("Cual es el DNI "))
        print(next((x for x in dic if x['DNI'] == bus_dni), None))
        repe=input("\n\n ¿Quiere realizar otra operacion? \nMarque 1 para SI \nMarque 0 para NO \n ")
        if repe=='1':
            print("\n¿Que operacion desea realizar? \n 1º Añadir un cliente (1) \n 2º Eliminar clientes por NIF (2) \n 3º Mostrar cliente por NIF (3) \n 4º Listar TODOS los clientes (4) \n 5º Mostrar UNICAMENTE los clientes preferentes (5) \n 6º Finalizar programa (6)")
            eleccion=input('\n Indique un numero y pulse Enter   ')
        else:
            exit ()

    if eleccion=='4':
        print(dic)
        repe=input("\n\n ¿Quiere realizar otra operacion? \nMarque 1 para SI \nMarque 0 para NO \n ")
        if repe=='1':
            print("\n¿Que operacion desea realizar? \n 1º Añadir un cliente (1) \n 2º Eliminar clientes por NIF (2) \n 3º Mostrar cliente por NIF (3) \n 4º Listar TODOS los clientes (4) \n 5º Mostrar UNICAMENTE los clientes preferentes (5) \n 6º Finalizar programa (6)")
            eleccion=input('\n Indique un numero y pulse Enter   ')
        else:
            exit ()

    if eleccion=='5':
        print(next((x for x in dic if x['Preferente'] == 1), None))
        repe=input("\n\n ¿Quiere realizar otra operacion? \nMarque 1 para SI \nMarque 0 para NO \n ")
        if repe=='1':
            print("\n¿Que operacion desea realizar? \n 1º Añadir un cliente (1) \n 2º Eliminar clientes por NIF (2) \n 3º Mostrar cliente por NIF (3) \n 4º Listar TODOS los clientes (4) \n 5º Mostrar UNICAMENTE los clientes preferentes (5) \n 6º Finalizar programa (6)")
            eleccion=input('\n Indique un numero y pulse Enter   ')
        else:
            exit ()
    
    if eleccion=='6':
        print('Finalizando programa....')
        time.sleep(2)
        exit () 

        

    


