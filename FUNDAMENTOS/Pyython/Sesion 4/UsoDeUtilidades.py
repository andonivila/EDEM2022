from distutils.command.sdist import sdist
from turtle import pu
from Utilidades.Interacciones.cordialidad import saludar 
from Utilidades.Interacciones.cordialidad import despedida 
from Utilidades.Interacciones.kpis import puntuacion

#Estando en otro archivo podemos llamar a esta funcion con from cordialidad import saludar

desp=despedida('Anto')

print (desp)

print (f' Puntos obtenidos : {puntuacion (5)}')


