#### Подчеркивания и их вариативность###########################################
# _var    #  неприватный атрибут для использования внутри класса               #
# class_  #  Если имя переменной занято, можно использовать '_' в конце имени  #
# __var   #  Приватный атрибут класса не наследуется                           #
# _       #  Принятый признак бесполезной переменной                           #
# __var__ #  Прямой признак магического метода                                 #
################################################################################


# _var##################################################################################################################
class Test:
    def __init__(self):
        self.foo = 11
        self._bar = 23

t = Test()
print(t.foo)
# Неприватный атрибут сработает т.к. внутриклассным он является только на договорной основе
print(t._bar)

from def_module import *

print(external_func())
# При подстановочном импорте внутренние методы/функции/атрибуты не работают
# print(_internal_func())

t2=Test2()
print(t2.kut)
# Но при этом, При подстановочном импорте, если в импортируемом классе есть внутриклассный атрибут
# Им можно оперировать.
print(t2._word_2)

# Обратим внимание, как работает _var для подстановочного импорта

from all_list_module import *
print(all_list_func_ext())

# Работа внетренней функции!!!
print(_all_list_func_int())

t3 = AllListTest3()
print(t3.kut)
# Работа внетреннего метода
print(t3._word_2)

# Нет работы с классом, имя которого не попало в список __all__
#t4 = AllListTest4

########################################################################################################################

# __var#################################################################################################################

class Test:
    def __init__(self):
        self.foo = 11
        self._bar = 23
        self.__baz = 24

# встроенная функция dir({obj}) - выводит все атрибуты объекта

t = Test()

print(f'Атрибуты класса : {dir(Test)}')
print(f'Атрибуты класса : {dir(Test())}')
print(f'Атрибуты экземпляра : {dir(t)}')  # _Test__baz - искажение имени атрибута
# print(t.__baz) AttributeError
print(t._Test__baz)

class ExtendedTest(Test):
    def __init__(self):
        super().__init__()
        self.foo = 'переопределено'
        self._bar = 'переопределено'
        self.__baz = 'переопределено'

t2 = ExtendedTest()
# print(t2.__baz) AttributeError
print(dir(t2)) # ... , _ExtendedTest__baz', '_Test__baz',...
print(t2._Test__baz) # 24
print(t2._ExtendedTest__baz) # переопределено

# Варианты возврата атрибутов с искажениями:
class ManglingTest:
    def __init__(self):
        self.__mangled = 'Hi!'

    def get_mangled(self):
        return self.__mangled

    # Искажение распространяется и на методы
    def __insert_method(self):
        return 42

    def call_insert_method(self):
        return self.__insert_method()

t3 = ManglingTest()
print(dir(t3)) # ..., _ManglingTest__mangled, '_ManglingTest__insert_method',....
print(t3.get_mangled())  # Hi!
# print(t3.__insert_method)  # AttributeError
print(t3.call_insert_method()) #42

# искажение и глобальные переменные
_MangledGlobal__mangled = 23

class MangledGlobal:
    def test(self):
        return __mangled  # при вызове этой переменной питон из-за __ автоматом расширит имя переменной
    # до _MangledGlobal и таким образом залетит в глобальную переменную _MangledGlobal__mangled

print(MangledGlobal().test()) # 23

# __var__###############################################################################################################
#  __var__ таким образом помечаются магические методы в классах питона

# _ ####################################################################################################################
#  _ таким именем можно назвать любую переменную, значение которой нам не пригодится в процессе.

simple_tuple = (1, 2, 3)
# необходим только первый элемент:
important_var, _, _ = simple_tuple
print(important_var, _,) # 1 3
# необходим только 3-й элемент
_,_, important_var = simple_tuple
print(important_var, _,) # 3 2
