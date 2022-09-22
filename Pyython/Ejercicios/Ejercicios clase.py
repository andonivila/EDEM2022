'''
Rango

'''

'''
miRango = range (0,10,2)

print(*miRango)

print (4%2)

'''

persona = {"gender":"female","name":"Zara","number":"3053","DNI":"4875663A"}

print(persona["DNI"])


print (f'El DNI DE {persona["name"]} ES {persona["DNI"]}')


'''
Con SET evitamos datos repetidos iterables
'''

misNumeros= [1,2,3,4,5,6,7,8,9,3,2,5,3]

misNumeros=set(misNumeros)

'''
Con * nos permite imprimir los elementos de una lista
eliminando los []
'''

print (*misNumeros)


mi_otro_set_de_datos= set (["a","a","a","b"])

print(*mi_otro_set_de_datos)

'''
Como ordenar listas
Invertir listas
'''

ListaNumeros = [16, 4, 9, 1, 3, 20, 8]

ListaNumeros.sort()

print (ListaNumeros)