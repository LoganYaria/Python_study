# Лямбда функции
# Лямбда функция одного выражения
# Лямбла функция сложения:::

add = lambda x, y: x + y
print(add(1,1))  # 2

# Функционально выражение
print(lambda x, y: x + y(2,2))  # <function <lambda> at 0x000002B3CFFCEB90>
print( (lambda x, y: x + y)(2,2))  # 4

# Самое частое  использование labda в сортировке с ключом по итерируемой структуре с не единственнм значением

list_ = [(1,'a'),(2,'d'),(3,'b'),(4,'c')]

print(sorted(list_, key=lambda x:x[1]))

list1_ = [{1:'a', 2:'b'}, {2: 'd', 1:'e'}, {3: 'b', 1:'f'}, {4: 'c', 1:'g'}]

list1_.sort(key=lambda x:x[1])
print(list1_)

print(sorted(range(-5,6), key=lambda x: x*x))

for i in range(-5,6):
    print(f'{i}:{i*i}')

# Плохие примеры использования lambda::::
# I
class Car:
    rev = lambda self: print('boom')
    crash = lambda self: print('babahHHH!')

my_car = Car()
print(my_car.crash())
# Пояснение:
# 1. Нарушение читаемости и стандартов
# 2. Проблемы с return значением
# 3. Отсутствие документации и аннотаций
# 4. Проблемы с дебаггингом
# 5. Сложности с наследованием и super()

# II

list_ = list(filter(lambda x: x % 2 ==0, range(16)))
print(list_)
# Пояснение
# 1. Cписковыми включениями читается проще
list_ = [x for x in range(16) if x % 2 ==0]
print(list_)
# 2. Не надо оборачивать в list()
# 3. Lambda добавляет лишнюю сложность