class Dog:
    species = 'Sobaka kusaka.'
    def __init__(self, name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name} is dog. It\'s {self.age} years old. It\'s {self.breed}.'
    def speak(self,sound):
        return f'{self.name} barks {sound}.'

#Создание  дочернего класса от  класса Dog()
class Duchshund(Dog):
    pass

class JackRusselTerrier(Dog):
    #Изменение метода родительского класса Dog()
    #def speak(self, sound = 'Arf'):
        #return f'{self.name} says {sound}.'
    #Добавление  своего аргумента к методу родительского класса, но обращение к нему как к функции
    def speak(self,sound="Arf"):
        return super().speak(sound)

class Bulldog(Dog):
    pass



buddy = Duchshund('Buddy',5)
jack = Bulldog('Jack',5)
miles = JackRusselTerrier('Miles',5)
jim = Bulldog('Jim',5)


#проверим, к какому классу принадлежит miles (да)
#print(type(miles))
#проверка, является ли miles объектом класса Dog (да)
#print(isinstance(miles, Dog))
#проверка, является ли miles объектом класса bulldog (да)
#print(isinstance(miles, Bulldog))

print(miles.speak())

#Перехватываем аргумент у метода
print(miles.speak('Naley vodochki, hozyain'))