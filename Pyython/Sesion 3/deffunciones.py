'''
from ctypes.wintypes import HLOCAL


def MiFuncionConParametros (a: str, b:str) ->None:
    print (f"{a}, {b}")

a="Hola"
b="Adios"

MiFuncionConParametros (a,b)
'''

from io import UnsupportedOperation


def MisElementos (*elementos):
    for elemento in elementos:
        print (f"Elemento: {elemento}")


MisElementos (1,2,3,4,5,6)


'''
Por consola solicitar al usuario un numero 
El programa debe de pedir numeros hasta que el usuario introduzca 
un año bisiesto 
'''