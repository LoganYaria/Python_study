#Создание словаря
capitals = {
    'California': 'Sacramento',
    'New York': 'Albany',
    'Texas': 'Austin'
}
print(capitals)

#Создание словаря и последовательности кротежей
some_tuple=(
    ('California','Sacramento'),
    ('New York','Albany'),
    ('Texas','Austin')
)
capitals = dict(some_tuple)
print(capitals)

#Пустой словарь
{}
#or
dict()

#Обращение к словарю
print(capitals['New York'])

#Добавление и удаление значение в словари

capitals['Colorado'] = 'Denver'
print(capitals)

#Замена значения в словарях
capitals['Texas'] = 'Houston'
print(capitals)

#Удаление значения словарей
del capitals['Texas']
print(capitals)

#Проверка наличия ключа в словаре

print('Texas' in capitals)
print('Kansas' in capitals)
if 'Texas' in capitals:
    print('The capital of Texas is ', capitals['Texas'])

