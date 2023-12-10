#Обявление класса
class Dog:
    pass#штука используется для наметки шаблона, обычно означает, что позже мы займемся этим кодом.

#Добавление атрибутов классу
class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age

#Добавление своих атрибутов

class Dog:
    species='Canis familiaris' #Тоже атрибут класса
    def __init__(self, name, age):
         self.name = name
         self.age = age

#Создание экземпляра класса
class Dog:
    pass

a = Dog()
b = Dog()
print(a==b)#False

#Атрибуты класса экземпляра

class Dog:
    species = 'Canis familiaris'
    def __init__(self,name,age):
        self.name = name
        self.age = age

buddy = Dog('Buddy',4)
miles = Dog('Miles',9)

#Обращение к атрибутам экземпляра
print(buddy.name)
print(miles.age)

#Обращение к атрибутам класса
print(buddy.species)
print(miles.species)
#Значения атрибутов экземпляроов можно менять динамически
miles.age = 11
miles.species = 'Sobakus kusakus'
print(miles.name, miles.species, miles.age)

#Методы экземпляорв
class Dog:
    species = 'Canis familiaris'
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def description(self):
        return f'{self.name} is {self.age} years old.'

    def speak(self,sound):
        return f'{self.name} says {sound}.'

buddy = Dog('Buddy',7)
miles = Dog('Miles',9)

print(buddy.description(),miles.description())
print(buddy.speak("Gav, suka"),miles.speak('Mau, bleat\''))

#Описание класса __str__
class Dog:
    species = 'biter dog'
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
        return f'This is dog. It\'s name is {self.name}. It\'s {self.age} years old'

jack = Dog('Jack',15)
print(jack)