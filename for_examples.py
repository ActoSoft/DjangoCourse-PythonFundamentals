# Reto 1 - Imprimir los 300 primeros números pares.
for i in range(2, 301, 2):
    print(i)

# Reto 2 - Imprime la tabla del 15. Muestra el resultado de los primeros 20 números.
# La impresión debe ser de la siguiente manera: 15 x 5 = 75.
for i in range(1, 21):
    print('15 x', i, '=', 15 * i)

# Reto 3 - Calcula la suma de los números impares ubicados entre el 50 y el 100.
acumulador_impares = 0 # Declado una variable en 0, para poder ir acumulando la suma.
for i in range(51, 100, 2):
    acumulador_impares += i
print('La suma de los números impares del 50 al 100 es:', acumulador_impares)

# Reto 4 - Calcula la suma de los números pares entre el 10 y el 100 (utilizar el módulo).
acumulador_pares = 0 # Declaro nuevamente una variable para ir acumulando las sumas.
for i in range(10, 101):
    if i % 2 == 0: # Con esta condición, nos aseguramos el que sea un número par.
        acumulador_pares += i
print('La suma de los números pares entre el 10 y el 100 es:', acumulador_pares)