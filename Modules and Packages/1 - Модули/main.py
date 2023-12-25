##main.py
##классический импорт:
# import adder
#
# value = adder.add(2,3)
# double_value = adder.double(value)
# #если хотим  использовать импортируемую функцию из импортируемоего модуля, надо прописать перед именем функции имя модуля
# print(value)
# print(double_value)

##import as <name>
##используется в основно если имя моддуля длинное, или есть конфликт в вызываемом модуле
# import adder as test
#
# value = test.add('floor','lava')
# print(value)

##from <module> import <name>
##используется в основном когда не теряется смысл от импорта например модуль datetime
# from adder import add,double
#
# value = add(55,45)
# print(value)
# double_value = double(value)
# print(double_value)


