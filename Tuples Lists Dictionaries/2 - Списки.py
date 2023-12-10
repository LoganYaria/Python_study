#Создание списка
colors=['red','yellow','gray','black','green']
print(colors)

['one',2.0,3]

#string->list
print(list('Anastasiya'))
#tuple->list
print(list((1,2,3,4)))

eat='milk, breat, eggs'
eat_list=eat.split()
print(eat_list)
print(len(eat_list))

#Создание списка из строки
string='Nasya;Petya;Ysysa'
list_string=string.split('x')
print(list_string)

#Список имеет те же функции, что и кортежи

#Изменение ячейки списка при посощи срезов
colors = ['pipa','popa','lypa','zupa']
print(colors)
#colors[1] = 'tita'
#print(colors)
colors[1:3]=['toto','kotiktik','may','yuyuyuyuy']
print(colors)
print(len(colors))

#Методы изменения списка
#Вставка .insert(i,x)
colors = ['yellow','black','blue','red']
colors.insert(1,'gray')
colors.insert(100500,'ping')
colors.insert(-1,'brown')
print(colors)
#Удаление .pop(i)
color = colors.pop(2)
print(color)
print(colors)
#colors.pop(100500) не нада
colors.pop(-1)
print(colors)
colors.pop()#Удаляет крайнее значение
print(colors)
#Добавление в конец .append(x)
colors.append('violet')
print(colors)
#Добавление в конец несколько элементов .extend(iterable)
colors.extend(['white','soft-green'])
print(colors)
colors.extend(('white-grey','soft-green-gray'))
print(colors)
