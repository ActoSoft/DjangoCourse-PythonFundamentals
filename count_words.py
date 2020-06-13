# El objetivo del programa es contar cuantas veces una palabra está presente en un texto

texto = 'Este texto tiene algunas palabras Este es otro texto con algunas palabras diferentes'
words = texto.split(' ')
words_dict = {}
# for word in words:
#     if word in words_dict:
#         words_dict[word] += 1
#     else:
#         words_dict[word] = 1

# for word, counter in words_dict.items():
#     print('Palabra:', word, '===== No. de veces:', counter)
for word in words:
    words_dict[word] = words.count(word)

for word, counter in words_dict.items():
    print('Palabra:', word, '===== No. de veces:', counter)