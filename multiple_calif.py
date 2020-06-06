selection = 'S'

name = input('Dame el nombre del alumno: ')
califs = []
while selection == 'S':
    calif = float(input('Dame la calificación: '))
    califs.append(calif)
    selection = input('Deseas agregar otra caliicación?: (S/N): ')
acum = 0
for calif in califs:
    acum += calif
mean = acum / len(califs)
print(f'El promedio del alumno {name} es: {mean}')