lista_productos = []
lista_precios = []

qc=int(input("¿Quieres comprar, marca SI (1) o NO (2)? "))

while qc==1 :
    item = input('¿Que producto quieres compra? ')
    price = int (input('Cuanto cuesta? '))
    lista_productos.append(item)
    lista_precios.append(price)
    qc=int(input("¿Quieres comprar, marca SI (1) o NO (2)? "))

total_cuenta = sum(lista_precios)

print ('Tu lista de la compra es : \n') 
print (* lista_productos)
print ('\n')
print ('Todo ha costado: \n') 
print (f"{total_cuenta}€")