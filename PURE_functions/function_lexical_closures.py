# Функции - замыкания

def get_speak_func(text, volume):
    def whisper():
        return text.lower() + '...'
    def louder():
        return text.upper() + '...'
    if volume >= 0.5:
        return louder
    else:
        return  whisper

print(get_speak_func('loud_textik', 0.7))  # <function get_speak_func.<locals>.louder at 0x000002BF174BEC20>
print(get_speak_func('loud_textik', 0.7)())  # LOUD_TEXTIK...

# Еще пример ф-ии замыкания

def make_adder(n):
    def add(x):
        return x+n
    return add

# Мы конфигурируем make_adder давайе ей значение (3) и после чего оперируем с ней
plus_3 = make_adder(3)
print(plus_3(2))  # 5

plus_1_000_000 = make_adder(1_000_000)
print(plus_1_000_000(2))

print(make_adder(36)(33))
########################################################################################################################

# Объекты, ведущие себя как функции

class Adder:
    def __init__(self, n):
        self.n = n
    # Дандер __call__ позволяет вызвать экземпляр объекта  как функцию и исполнить метод __call__
    def __call__(self, x):
        return self.n + x

plus_100 = Adder(100)
print(plus_100(5)) # 105

