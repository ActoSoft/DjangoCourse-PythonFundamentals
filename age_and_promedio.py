age = int(input('Dame la edad que tienes: '))
promedio = float(input('Dame tu promedio: '))

if age > 0:
    if age < 6:
        print('Kinder')
        print('Tu no aplicas')
    elif age >= 6 and age < 12:
        print('Primaria')
        if promedio >= 9.5:
            print('Tienes un promedio aceptable para primaria')
        else:
            print('Tu promedio es deficiente en primaria')
    elif age >= 12 and age < 15:
        print('Secundaria')
        if promedio >= 9:
            print('Tienes un promedio aceptable para secundaria')
        else:
            print('Tu promedio es deficiente en secundaria')
    elif age >= 15 and age < 18:
        print('Preparatoria')
        if promedio >= 8.5:
            print('Tienes un promedio aceptable para prepa')
        else:
            print('Tu promedio es deficiente en prepa')
    elif age >= 18 and age < 23:
        print('Universidad')
        if promedio >= 8:
            print('Tienes un promedio aceptable para universidad')
        else:
            print('Tu promedio es deficiente en universidad')
    else:
        print('Profesionista')
        print('Tu y a no tienes promedio.')
else:
    print('Aun no naces')