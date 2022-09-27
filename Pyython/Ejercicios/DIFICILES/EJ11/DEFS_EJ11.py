from re import A


class Personal_Universitario():
    def __init__(self, personal):
        self.personal = personal

A1 = Personal_Universitario({'Id': 16, 'nombre': "jose", 'email': "jose@gmail.com"})

print(A1.personal)  # Devuelve {'Id': 16, 'nombre': 'jose', 'email': 'jose@gmail.com'}

print(A1.personal{'Id'})