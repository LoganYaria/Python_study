my_first_tuple = (1,2,3)#Хапись кортежа при помощи литерала кортежа
my_second_tuple = (1,2.0,'three')#Разныет типы
#Пустой кортеж
empty_tuple=()
#Кортеж с одним элементом
tuple_of_one_element=(1,)

#Встроенная  функция tuple
string='строка'
string_tuple=tuple(string)# будет кортеж
#пустой кортеж
tuple=()
#Упаковка и распаковка кортежей
#Упаковка
coordinates = 2.23, 4.56
#Распкаовка
x, y = coordinates
print(x)

#Несколько присваиваний в одной строке
name,age,occupation='Petya',4,'parrot'
print(name,occupation)
# Проверка существования значения
Tuple='d',567,'Pecka','Kosk',777
print('Kosk' in Tuple)
print('777' in Tuple)
