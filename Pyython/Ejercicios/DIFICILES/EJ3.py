def impuestos ():
    tu_edad=int(input('¿Que edad tienes? '))
    if tu_edad > 15 and tu_edad < 71 :
        tu_ingreso=int(input('¿Que ingresos percibes al mes? '))
    else:
        print('No tienes que pagar impuestos')
        
    

    
    if tu_ingreso<800:
        print('No tienes que pagar impuestos')
        
    elif tu_ingreso==800 or tu_ingreso>800:
        deuda=tu_ingreso*0.10
        print(f'Tu salario bruto es de {tu_ingreso*12} \n tu aportacion en impuestos es de {deuda*12} \n tu salario neto es de {(tu_ingreso*12) - (deuda*12)}')

    elif tu_ingreso>800 and tu_ingreso<2000:
        deuda=tu_ingreso*0.30
        print(f'Tu salario bruto es de {tu_ingreso*12} \n tu aportacion en impuestos es de {deuda*12} \n tu salario neto es de {(tu_ingreso*12) - (deuda*12)}')

    elif tu_ingreso>2000:
        deuda=tu_ingreso*0.50
        print(f'Tu salario bruto es de {tu_ingreso*12} \n tu aportacion en impuestos es de {deuda*12} \n tu salario neto es de {(tu_ingreso*12) - (deuda*12)}')


decision=int(input('¿Quieres utilizar la calculadura de impuestos? \n SI (1) /// NO (0)\n'))

while decision==1:
    impuestos()
    decision=int(input('¿Quieres utilizar la calculadura de impuestos? \n SI (1) /// NO (0)\n'))
