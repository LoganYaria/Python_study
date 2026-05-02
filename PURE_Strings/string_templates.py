# При пользовательском вводе и последующей подстановке в переменные необходимо использовать шаблонные строки

from string import Template

errno = 50159747054
name = 'Bob'

# Template - Класс для работы со строками, поддерживающий подстановку с помощью символа $.
t = Template('Эй, $name!')

t_subs = t.substitute(name=name)
h_subs = t.substitute(name='Gan LUI G')
# .substitute - метод для замены шаблонга после символа $ на необходимую подстроку и возврат строки
print(t_subs)
print(h_subs)

# Пример с несколькими переменными:
full_message = Template('Hi, $name! This is your fucking $errno!')
print(full_message.substitute(name=name,errno=hex(errno)))

# Пример воровства, если использовать простоый формат
SECRET = 'this is the war!'
class Error:
    def __init__(self):
        pass

err = Error
# Злоумышленник через __globals__ пытается добраться до нашей переменной
user_input = '{error.__init__.__globals__[SECRET]}'
print(user_input.format(error=err))

# Через шаблоны
correct_user_input = '${error.__init__.__globals__[SECRET]}'
#  ValueError: Invalid placeholder in string: line 1, col 1
print(Template(correct_user_input).substitute(err = Error))

