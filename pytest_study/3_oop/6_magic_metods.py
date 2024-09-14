class Liverpool:
    def __init__(self, players):
        self.players = players

    def __repr__(self): #Очень хорошая практика для хорошего формата вывода
        return f'Liverpool: {self.players}'

    def __str__(self):
        return f'You\'ll never waalk alone!{self.players}'

    def __add__(self,other): # сложение
        if not isinstance(other, Liverpool):
            raise ValueError('Cant be summed')
        return self.players + other.players

    def __call__(self, *args): # порверка на callable
        return str(self) + ' got args ' + str(args)

    def __eq__ (self,other): # сравнение
        return self.players == other.players


liverpoolu18 = Liverpool(18)
liverpoolu20 = Liverpool(20)

l = [liverpoolu20,liverpoolu18,'pines']

print(callable(liverpoolu18))
