name = input('Dame tu nombre: ')
calif_1 = float(input('Dame tu calificación 1: '))
calif_2 = float(input('Dame tu calificación 2: '))
calif_3 = float(input('Dame tu calificación 3: '))

prom = (calif_1 + calif_2 + calif_3) / 3

if prom >= 7:
    print('Has aprobado el año!')
else:
    print('Tendrás que repetir el año ☹️')
