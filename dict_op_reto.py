# 1.- Vamos a recibir del teclado un país, y la cantidad de personas que viven ahí (en millones)
# 2.- El usuario podrá ingresar países hasta que ya no quiera.
# 3.- Construye un diccionario donde, cada país va a ser la clave, y la cantida de personas el valor.
# paises = {'USA': 50, 'Mexico': 30}
### Imprime todos los países dentro del diccionario, con la cantidad de habitantes
# Después, pide al usuario que ingrese el nombre de un país, para poder ver la cantidad de personas
# Accede al elemento del diccionario, que contiene ese dato

countries = {}
resp = 'S'
while resp == 'S':
    country = input('Dame el país: ')
    habitants = input('Dame la cantidad de habitantes (millones)')
    countries[country] = habitants
    resp = input('Desea ingresar otro país? (S/N): ')

for clave, valor in countries.items():
    print(f'País: {clave}, Cantidad de habitantes: {valor}')

country_to_see = input('Dame el país que deseas ver: ')
print(f'La cantidad de habitantes en {country_to_see} es: {countries[country_to_see]} millones de personas')