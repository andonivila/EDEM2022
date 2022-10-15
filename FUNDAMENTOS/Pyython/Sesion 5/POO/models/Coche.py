class Coche () :
    # Atributos de clase
    marca :str 
    modelo :str 
    matricula :str 
    color :str  
    titular :str 
    velocidad :float = 0 
    def __init__(self, marca, modelo, matricula, color, titular) :
        self.marca = marca
        self.modelo = modelo
        self.matricula = matricula
        self.color = color
        self.titular = titular
    def arrancar (self):
        self.velocidad = 10
        print ('El coche ha arrancado')
    def frenar (self, presion : float):
        self.velocidad -= (presion -10)
        print (f"El coche ha frenado. Su velocidad ahora es de {self.velocidad}")





    