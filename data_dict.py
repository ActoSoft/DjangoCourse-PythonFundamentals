name = input('Dame tu nombre: ')
last_name = input('Dame tus apellidos: ')
age = input('Dame tu edad: ')
email = input('Dame tu correo electrónico: ')

# Construyo el diccionario
person = {
    'nombre': name,
    'apellidos': last_name,
    'edad': age,
    'correo': email
}

print(f'Hola! Mi nombre es {person["nombre"]} {person["apellidos"]}, tengo {person["edad"]} años y mi correo es {person["correo"]}')

# person = []
# person.append(name)
# person.append(last_name)
# person.append(age)
# person.append(email)

# print(person)

# print(f'Hola! Mi nombre es {person[0]} {person[1]}, tengo {person[2]} años y mi correo es {person[3]}')