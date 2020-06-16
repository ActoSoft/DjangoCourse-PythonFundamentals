class Persona:

    def __init__(self, name, last_name, age, gender):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.gender = gender

    def get_full_name(self):
        return f'{self.name} {self.last_name}'

    def get_full_age(self):
        return f'{self.age} años'

    def set_name(self, name):
        self.name = name

class Alumno(Persona):

    def __init__(self, matricula, avg, *args):
        super(Alumno, self).__init__(*args)
        self.matricula = matricula
        self.avg = avg

    def get_student_info(self):
        return f'{self.get_full_name()} - Matrícula: {self.matricula}'

class Docente(Persona):

    def __init__(self, id, email, name, last_name, age, gender):
        super().__init__(name, last_name, age, gender)
        self.id = id
        self.email = email

    def get_teacher_info(self):
        return f'{self.get_full_name()} - Cédula: {self.id}'

alumno = Alumno(2016640182, 10, 'Martín', 'Melo Godínez', 23, 'M')
print(alumno.get_full_name())
print(alumno.get_student_info())

docente = Docente('DOC1234', 'docente@gmail.com', 'Juan', 'Olvera', 21, 'M')
print(docente.get_full_age())
print(docente.get_teacher_info())