cellphone = {
    'marca': 'Xiaomi',
    'RAM': 6,
    'almacenamiento': 64,
    'color': 'negro'
}

print(cellphone)
print('La marca es:', cellphone['marca'])
new_marca = input('Dame el nombre de la nueva marca: ')

# Actualizar un valor del diccionario
cellphone['marca'] = new_marca
print(cellphone)

# Agregar un nuevo elemento a un diccionario
so = input('Cuál es el sistema operativo?: ')
cellphone['so'] = so
print(cellphone)

# Eliminar un elemento de un diccionario
print('ELIMINANDO COLOR')
del cellphone['color']
print(cellphone)

# Iterando una diccionario
for clave, valor in cellphone.items():
    print(f'El clave es: {clave}, y su valor es {valor}')

# Iterando sólo las claves
for clave in cellphone.keys():
    print(f'La clave es: ', clave)

# Interar sólo los valores
for value in cellphone.values():
    print(f'El valor es: ', value)