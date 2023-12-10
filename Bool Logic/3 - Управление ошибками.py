# ValueError
# происиходит при ошибке обработки типа данных объетка.

# TypeError
# происходит при операции с кривыми типами.

# NameError
# при обработке переменноей, имя которой не было определено.

# ZeroDivisionError
# косяки с нулем в делении

# OverflowError
# если результат операциислишком большой.


# #Ключевые слова try & except для перехвата ошибок
# try:
#     number = int(input('Print number: '))
# except ValueError:
#     print('That was not int')
#
# def devide(num1,num2):
#     try:
#         print(num1/num2)
#     except (TypeError,ZeroDivisionError):
#         print('somthing wrong is going on')
#
# print(devide(3,0))
# #OR
# def devide(num1,num2):
#     try:
#         print(num1/num2)
#     except TypeError:
#         print('You entered not int, mother fucker!')
#     except ZeroDivisionError:
#         print('Devide on null is wrong. you are stuped!')
#
# print(devide('3',0))

# #except бкз исключения (не рекомендуюется к использованию)
#
# try:
#     3/0
#     #Do some errors with high probably
# except:
#     print('Some Errror is hapend')

