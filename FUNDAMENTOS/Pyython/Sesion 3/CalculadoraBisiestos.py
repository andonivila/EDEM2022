def bisiesto () :
    anio=int(input("Pon un año "))
    a=anio%4
    b=anio%100
    c=anio%400
    
    if a==0:
        print("Es un año bisiesto")
        exit()

    if b==0:
        if c==0:
            print("Es un año bisiesto")
            exit()
    else:
        print("No es un año bisiesto")
        
bisiesto ()
