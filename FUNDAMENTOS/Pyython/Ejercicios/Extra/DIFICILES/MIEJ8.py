
def MiFactorizacion ():
    elec=int(input("Elige un numero: "))
    elec=elec+1

    a=list(range(1,elec))
    largo=len(a)
    i=-2
    mul1=a[largo-1]
    mul2=a[largo-2]
    resul=mul1*mul2

    while i>-largo :
        
        i=i-1
        mul2=a[largo+i]
        resul=resul*mul2
    
    elec=elec-1
    print (f'El factorial del numero {elec} es {resul}')

MiFactorizacion ()