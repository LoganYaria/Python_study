# #Суммирование чисел sum([...] только с числами И С КОРТЕЖАМИ
# print(sum([1,2,3,4,5]))
# #Минимальное и максимальное значение в списке
# print(min([1,2,3,4,5]))
# print(max([1,2,3,4,5]))
#
# #Генератор списка
# numbers = (1,2,3,4,5)
# new_list = [number**2 for number in numbers]
# print(new_list)
#
#
food = ['rice','beans']
print(food)
food.append('broccoli')
print(food)
food.extend(['bread','pizza'])
print(food)
print(food[:2])
print(food[-1])
string='eggs,fuit,orangejuce'
breakfast=string.split(',')
print(breakfast)
print(len(breakfast))
lengths=[len(word) for word in breakfast]
print(lengths)
