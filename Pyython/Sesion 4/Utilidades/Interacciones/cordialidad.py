# C:\Users\Usuario\Documents\GitHub\EDEM2022\Pyython\Sesion 4\Utilidades\Interacciones\cordialidad.py
#cordialidad.py
def saludar (nombre:str):
    print(f'Hola {nombre}')

#Estando en otro archivo podemos llamar a esta funcion con from cordialidad import saludar

def despedida (nombre:str)-> str:
    return (f'Hasta luego {nombre}')

    