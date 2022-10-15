from cmath import pi

def volumen_cilindro ():
    a=int(input('Cual es el radio del cilindro '))
    h=int(input('Cual es la altura del cilindro '))
    area_c=(pi*(a**2))
    v_c=h*area_c 
    return print (f'El volumen de tu cilindro es {v_c}')


volumen_cilindro ()