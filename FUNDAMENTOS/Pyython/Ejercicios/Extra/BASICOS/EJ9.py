anio=int(input("Pon un año "))

def bisiesto (a) :
     a=anio%4
     b=anio%100
     c=anio%400

     if a==0:
        if b==0:
            if c==0:
                print("Es un año bisiesto")
            else:
                print("No es un año bisiesto")
        
bisiesto (anio)
