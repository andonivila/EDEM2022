from cmath import pi

def area_triuangulo (a,b) :  
    area_t=(a*b)/2
    return print (f'El area de tu triangulo es {area_t}')

def area_circulo (a):
    area_c=(pi*(a**2))
    return print (f'El area de tu circulo es {area_c}')


area_triuangulo (5,2)
area_circulo(5)

