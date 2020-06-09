price_course = 1500
max_students = 35
publicity = 5000
hours = 45
lead_teacher_per_hour = 200 if max_students > 20 else 150
teacher_student = 100
siete_percentage = 0.30

result = (price_course * max_students) - publicity - ((lead_teacher_per_hour + teacher_student) * hours)

siete_cincuenta = result * siete_percentage
iimap = (result - siete_cincuenta) / 2
actosoft = (result - siete_cincuenta) / 2
print("Ganancia mia: ", (hours * lead_teacher_per_hour) + actosoft)
print('Cantidad de alumnos: ', max_students)
print('Porcentaje 750:', siete_percentage * 100, '%')
print("Utilidad: ", result)
print("750: ", siete_cincuenta)
print("IIMAP: ", iimap)
print("Actosoft: ", actosoft)