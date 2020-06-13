class Person:
    def __init__(self, name, last_name, age, height, weight):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.height = height
        self.weight = weight

    def get_full_name(self):
        print(f'Nombre completo: {self.name} {self.last_name}')

    def calculate_imc(self):
        imc = (self.weight / self.height ** 2)
        print('Tu IMC es:', imc)

name = input('Dame tu nombre: ')
last_name = input('Dame tus apellidos: ')
age = input('Dame tu edad: ')
height = float(input('Dame tu altura: '))
weight = float(input('Dame tu peso: '))

person = Person(name, last_name, age, height, weight)

person.get_full_name()
person.calculate_imc()