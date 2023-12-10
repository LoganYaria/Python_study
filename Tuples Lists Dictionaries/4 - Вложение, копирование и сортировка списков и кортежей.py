#Вложенный список

# two_by_two=[[1,2],[3,4]]
# print(two_by_two[1][0])

# #Копирование списка
# import copy
# matrix_1 = [[1,2],[3,4]]
# #Некорректное копирование
# #matrix_2 = matrix_1
# #matrix_2[1][1]=0
# #print(matrix_1)
#
# matrix_2=copy.deepcopy(matrix_1)
# matrix_2[1][1]=0
# print(matrix_1,matrix_2)

#Сортировка списков .sort()
#Список строк сорртируется по алфавиту
colors=['red','blue','green']
colors.sort()
print(colors)
#Список чисел сорртируется по <
numbers=[100,100000,1]
numbers.sort()
print(numbers)
#Сортировка пользовательская

def get_second_element(item):
    """Возврат второго элемента кортежа"""
    return item[1]

items = [(5,6),(3,4),(1,2)]
items.sort(key=get_second_element)
print(items)