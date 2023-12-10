#Преобразование строки
string='Добрый Вечер, Я Диспетчер'
print(string.lower())
print('Добрый Вечер, Я Диспетчер'.lower())
print(string.upper())
print('Добрый Вечер, Я Диспетчер'.upper())

#Удаление пропусков строки
string='   Добрый Вечер, Я Диспетчер  '
print(string)
print(string.rstrip())
print(string.lstrip())
print(string.strip())

#Проверка наличия символов в начале или в конце строки
string="Stringa! "
print(string.startswith('Str'))
print(string.endswith('ga! '))


#Пользовательский ввод
response=input('Введите текст: ')
print('Вы ввели: '+response)
