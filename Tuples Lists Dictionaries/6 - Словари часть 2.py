#Создание словаря
capitals = {
    'California': 'Sacramento',
    'New York': 'Albany',
    'Texas': 'Austin'
}
# Перебор содержимого словаря
for key in capitals:
    print(key)#Вывод только ключа


for state in capitals:
    print(state, capitals[state])#Вывод только ключа

#Метод словаря .items()
print(capitals.items())

for state,capital in capitals.items():
    print(state,capital)
#Типы данных валидные для использовании в качестве ключей:
# int
# float
# string
# bool
# tuple

#Вложенные словари
states = {
    'California':
        {
            'capital': 'Sacremento',
            'flower': 'California pope'
        },
    'New York':
        {
            'capital': 'Albany',
            'flower': 'Rose'
        },
    'Texas':
            {
                'capital': 'Austin',
                'flower': 'Bluebonnet'
            }
}

#print(states)

print(states['New York'])
print(states['New York']['flower'])
