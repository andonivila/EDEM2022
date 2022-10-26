


dic=[]

print(f"Buenos dias, \n ¿Que operacion desea realizar? \n 1º Añadir un cliente (1) \n 2º Eliminar clientes por NIF (2) \n 3º Mostrar cliente por NIF (3) \n 4º Listar TODOS los clientes (4) \n 5º Mostrar UNICAMENTE los clientes preferentes (5) \n 6º Finalizar programa (6)")

eleccion=input('\n Indique un numero y pulse Enter   ')

q=0
a=1
i=0
z=0
repe='1'

while repe=='1':
    if eleccion =='1':
        nif_cliente=int(input('¿Cual es el DNI del cliente? '))
        nombre_cliente=input('¿Cual es el nombre del cliente? ')
        apellido_cliente=input('¿Cual es el apellido del cliente? ')
        telefono_cliente=input('¿Cual es el telefono del cliente? ')
        email_cliente=input('¿Cual es el email del cliente? ')
        preferente_cliente=input('¿Es el cliente preferente? ')
        dic.append({'DNI':nif_cliente, 'Nombre':nombre_cliente, 'Apellido':apellido_cliente, 'Telefono':telefono_cliente, 'Email':email_cliente, 'Preferente':preferente_cliente})
        repe=input("\n\n ¿Quiere realizar otra operacion? \nMarque 1 para SI \nMarque 0 para NO ")
        if repe=='1':
            eleccion=input('\n Indique un numero y pulse Enter   ')
        else:
            exit ()
            
    if eleccion=='2':
        bus_dni=int(input("Cual es el DNI "))
        print(next((x for x in dic if x['DNI'] == bus_dni), None))


    


