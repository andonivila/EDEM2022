tupla = (2, 4, 3, 5, 4, 6, 7, 8, 6, 1)

print("Encontrar los elementos de 3 a 5")
print (tupla.index (3), tupla.index (4), tupla.index (5) )

print("Encontrar los 6 primeros elementos")
print (tupla[0:6])

print("Muestra la tupla desde el 5 elemento hasta el final")
print (tupla[4:])

print("Muestra toda la tupla haciendo uso de [:]")
print (tupla[:])

print("Muestra todos los elementos desde la posición 2 a la 9 de dos en dos")
print (tupla[2:9:2])

print('Devuelve la tupla con un salto cada 4 elementos')
print (tupla[::4])

print('Usa un step negativo para mostrar la tupla desde la posición 9 a la 2')
print (tupla [-9:-2])


