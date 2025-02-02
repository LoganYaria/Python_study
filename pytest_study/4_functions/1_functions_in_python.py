def function(arg):
    '''docstring'''
    {'key': 'value'}
    return 10 + arg


# f = function()
# print(function) # ссылка на функцию
# print('name: ', function.__name__)# имя
# print('code object: ', function.__code__)# code object
# print(type(function))# функция явл классом
# my_functions = ['a', 'b', 10, function] #хранение функций в структурах данных

fun = function # присвоили fun функцию
b = fun(5) # присвоили результат функции b
print(fun(5), b)