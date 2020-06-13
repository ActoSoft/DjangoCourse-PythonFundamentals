class Person:
    def __init__(self, matricula, name, last_name, avg, age, schoolar_age):
        self.matricula = matricula
        self.name = name
        self.last_name = last_name
        self.avg = avg
        self.age = age
        self.schoolar_age = schoolar_age

    def get_avg(self):
        return self.avg

    def set_avg(self, new_avg):
        self.avg = new_avg

    def get_start_year(self):
        start_year = 2020 - self.schoolar_age
        print(f'Ingresó a estudiar en el año: {start_year}')

    def get_start_age(self):
        start_age = self.age - self.schoolar_age
        print(f'Empezó a estudiar a los {start_age} años')

    def get_info(self):
        print(f'Nombre: {self.name} {self.last_name}. Matrícula: {self.matricula}. Promedio: {self.avg}')

person = Person('2016640182', 'Martín', 'Melo Godínez', 9.7, 23, 5)
person.get_start_year()
person.get_start_age()
person.get_info()
person.set_avg(9.2)
person_avg = person.get_avg()
print(person_avg)