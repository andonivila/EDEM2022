clientes=[]


def addcliente () :
    nif=str(input('Escribe el DNI'))
    nombre=str(input('Escribe el nombre '))
    apellido=str(input('Escribe el apellido '))
    telefono = int(input('Escribe el telefono'))
    email=str(input('Escribe el email '))
    preferente=bool(input('Es preferente '))
    clientes.append({'DNI': nif, 'Nombre': nombre, 'Apellido' : apellido, 'Telefono': telefono, 'Email': email, 'Preferente': preferente })

addcliente ()
addcliente ()

clientes.pop(0)

print (clientes)
