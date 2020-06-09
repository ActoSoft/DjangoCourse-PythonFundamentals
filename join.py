names = []
selection = "S"
while selection == "S":
    name = input('Ingresa un nombre: ')
    names.append(name)
    selection = input('Deseas ingresar otro nombre?: ')
print(','.join(names))