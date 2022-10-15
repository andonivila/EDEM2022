


def primos ():

    numero=int(input("Pon un numero "))
   
    print("El resto de /2")
    dos=numero%2
    print (dos)

    print("El resto de /3")
    tres =numero%3
    print (tres)

    print("El resto de /4")
    cuatro =numero%4
    print (cuatro)

    print("El resto de /5")
    cinco =numero%5
    print (cinco)

    print("El resto de /6")
    seis =numero%6
    print (seis)

    print("El resto de /7")
    siete=numero%7
    print(siete)

    print("El resto de /8")
    ocho=numero%8
    print(ocho)
    print("El resto de /9")
    nueve=numero%9
    print(nueve)


    if dos==0 or tres==0 or cuatro == 0 or cinco == 0 or seis == 0 or siete == 0 or ocho == 0 or nueve == 0 : 
        print ('El numero no es primo')
    else:
        print('El numero es primo')