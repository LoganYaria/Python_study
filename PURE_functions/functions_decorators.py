# Декораторы обертывают другую функцию и позволяют исполнять программный код до и после того,
# как обернутая функция выполнится
# Декоратор - это вызываемый объект, который на входе принимает один вызываемый объект, а на выходе возвращает другой

# Пример простого декоратора
def null_decorator(func):
    return func


# функция
def greet():
    return 'Hilou'


# Оборачивание функции использование декоратора null_decorator
greet = null_decorator(greet)
print(greet())


# Корректное использование декоратора ##################################################################################
@null_decorator
def bye():
    return 'good bye'


print(bye())


def uppercase(func):
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result

    return wrapper


@uppercase
def parrot():
    return 'chi'


# parrot = uppercase(parrot)

print(parrot)  # <function uppercase.<locals>.wrapper at 0x000001CC48FFF0D8>
print(parrot())  # CHI


# Многочисленные декораторы ############################################################################################

def strong(func):
    def wrapper():
        result = func()
        return f'<strong>{result}</strong>'

    return wrapper


def emphasis(func):
    def wrapper():
        return '<em>' + func() + '</em>'

    return wrapper


# Декораторы применяются снизу вверх
@strong
@emphasis
def little_funny_parrot():
    return 'Petya-Petr'


print(little_funny_parrot())  # <strong><em>Petya-Petr</em></strong>
