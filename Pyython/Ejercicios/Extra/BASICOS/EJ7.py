'''
Escribe un programa que contenga dos variables.
Una de ellas representa la contraseña de un usuario y la otra un texto introducido.
El programa debe poder mostrar por pantalla si las dos cadenas de texto son iguales 
sin tener en cuenta mayúsculas y minúsculas.

'''

con=str("conta")
usr=str(input("Escribe la contraseña "))

if con == usr:
    print("Son iguales")
else:
    print("No son iguales")