lstdict = []

a=input("Nombre ")

b=int(input('dime DNI '))

lstdict.append({'Esto':a ,'DNI':b})


z=int(input("XXX "))

print(next((x for x in lstdict if x["DNI"] == z), None))


