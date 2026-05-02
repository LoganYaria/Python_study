# Пример передачи функции в функцию
def yell(text):
    return text.upper() + '!'

# message - функция более высокого порядка hight order function
# Функция message приниимает в себя функцию для декорирования текста + текст
def message(func, text):
    print(func(text))

some_text = 'some fucking stuped text'
# Передаем функцию yell в функцию message вместе с текстом
message(func=yell, text=some_text)  # SOME FUCKING STUPED TEXT!

# Встроенна функция map(func, iterr_obj)
# принимает объект-функцию, и итеррируемый объект. и применяет объект-функцию к каждой итерации
tuple_ = ('Hi', 'Hello', 'helicopter')
list_ = list(map(yell, tuple_))
print(list_)
print(map(yell, tuple_))

# Вложенные функции
def speak(text):
    def whisper(t):
        return t.lower() + '...'
    return whisper(text)

# За пределами внешней ф-ии нет внутренней ф-ии
# print(whisper('word'))  # NameError: name 'whisper' is not defined

# Возвращение внутренней ф-ии во внешнее пространство имен

def get_speak_func(volume):
    def whisper(t):
        return t.lower() + '...'

    def louder(t):
        return t.upper() + '!!!'

    if volume >= 0.5:
        return louder
    else:
        return whisper

var_ = get_speak_func(0.6)
var_('get thw fuck away for me')  # GET THW FUCK AWAY FOR ME!!!
var__ = get_speak_func(0.4)
var__('lets the bodies hits the floor')  # lets the bodies hits the floor...