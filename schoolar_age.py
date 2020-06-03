age = int(input('Dame la edad que tienes: '))

if age > 0:
    if age < 6:
        print('Kinder')
    elif age >= 6 and age < 12:
        print('Primaria')
    elif age >= 12 and age < 15:
        print('Secundaria')
    elif age >= 15 and age < 18:
        print('Preparatoria')
    elif age >= 18 and age < 23:
        print('Universidad')
    else:
        print('Profesionista')
else:
    print('Aun no naces')