# El objetivo del programa es contar cuantas veces una palabra está presente en un texto
# 1.- Separa el texto, guardando cada palabra como un elemento de una lista
# 2.- Itera la lista y guarda cada palabra como un elemento de un diccionario, donde su valor
# va a ser la cantidad de veces que aparece esa palabra



texto = 'Este texto tiene algunas palabras Este es otro texto con algunas palabras diferentes'

# ¿Cómo verificar si ya existe una clave en un diccionario?

diccionario = {
    'tareas': 3,
    'participaciones': 2,
    'faltas': 1
}

print(diccionario)

if 'faltas' in diccionario:
    print("entro")
    diccionario['faltas'] += 1
else:
    print('No existe')

if 'calificaciones' in diccionario:
    print("entro")
else:
    diccionario['calificaciones'] = 1
print(diccionario)