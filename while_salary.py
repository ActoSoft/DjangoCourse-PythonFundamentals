selection = 'Si'

while selection == 'Si':
    name = input('Dame tu nombre.: ')
    salary = float(input('Dame tu salario mensual: '))
    iva = salary * 0.16
    total = salary - iva
    print('El salario bruto de', name, 'es de:', total)
    selection = input('Deseas calcular otro salario (Si/No)')
print('Nos vemos!')