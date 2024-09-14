# Объявление

class Car:
    pass

class Animal(Car):
    pass

# Экземпляр класса

toyota_camry = Car()
lada = Car()
dog = Animal()

print('Is toyota car? ', isinstance(toyota_camry,Car)) # проверка принадлежности к классу объекта
