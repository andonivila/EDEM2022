anio=int(input("Pon un año"))



def bisiesto (a: int) :
    a=a%4
    
    if a==0:
        a=a%100
    if a==0:
     a=a%400
    if a==0:
     print (f"Es un año bisiesto")
    else:
        print("No es un año bisiesto")

bisiesto (anio)
