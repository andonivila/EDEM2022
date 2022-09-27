from pprint import pprint


clientes=[]


def addcliente () :
    nif=str(input('Escribe el DNI'))
    nombre=str(input('Escribe el nombre '))
    apellido=str(input('Escribe el apellido '))
    telefono = int(input('Escribe el telefono'))
    email=str(input('Escribe el email '))
    preferente=bool(input('Es preferente '))
    clientes.append({'DNI': nif, 'Nombre': nombre, 'Apellido' : apellido, 'Telefono': telefono, 'Email': email, 'Preferente': preferente })



def delclie ():
    print (f"La lista de clientes es la siguiente \n")    
    i=len(clientes)
    if i==0:
        print ("El cliente 0 es ")
        print (clientes[0]('DNI'))
    elif i>0:
        print ("El cliente 0 es ")
        print (clientes[0])
        print ("El cliente 1 es ")
        print (clientes[1])

    elif i>1:
        print ("El cliente 0 es ")
        pprint (clientes[0]('DNI'))
        print ("El cliente 1 es ")
        print (clientes[1])
        print ("El cliente 2 es ")
        pprint (clientes[3])

    clientes.pop(int(input("Selecciona cliente a eliminar")))


addcliente ()
addcliente ()
delclie()

print (clientes)
