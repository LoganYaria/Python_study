#Умножение строк
string1="пи"
print(string1*3)

#Преобразование строк в числа
num1=int(input('Введи свою зарплату: '))
print(type(num1))
print(num1*555)
num2=input('Введи свою зарплату: ')
float_num2=float(num2)
print(float_num2)

#Преобразование чисел в строки
num1=1
num2=2
print("Два+один будет "+str(num1+num2))

#Упрощение вывода строк через форматирование
name='Анатолий'
arms=2
legs=3
print(f'Червяк {name} имеет {arms} руки и {legs} ноги! К слову, у него всего {arms+legs} конечностей!')

#Поиск подстроки в строке
string='I push my fingers in to my Eyes'
print(string.find('my'))#Находим только первое совпадение
print(string.replace('my','fucking'))
