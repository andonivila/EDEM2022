'''
numero de la semana actual dentro del mes
dia dentro del año el 365 de 365 
dia del mes 
dia de la semana
'''


import datetime
from traceback import print_tb

#Fecha y Hora actual
print(f'Fecha y Hora actual: {datetime.datetime.now()}')
#Año actual
print(f'{datetime.datetime.today().strftime("%Y")}')
#Mes Escrito
print(f'{datetime.datetime.today().strftime("%B")}')
#Mes en numero
print(f'{datetime.datetime.today().strftime("%m")}')
#
print(f'{datetime.datetime.today().strftime("%W")}')
#
print(f'{datetime.datetime.today().strftime("%j")}')
#Dia en Numero
print(f'{datetime.datetime.today().strftime("%d")}')
#Dia escrito 
print(f'{datetime.datetime.today().strftime("%A")}')

