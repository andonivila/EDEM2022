from os import remove


dic = [{'Prueba':'1'},{'Prueba':22}]


bus_dni=int(input("Cual es el DNI "))
donde_dni=(next((x for x in dic if x['Prueba'] == bus_dni), None))

dic.remove(donde_dni)

print(dic)