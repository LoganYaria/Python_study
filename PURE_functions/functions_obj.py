
def yell(text):
    return text.upper() + '!'

print(yell('hi'))

# Можно присваивать функции переменным
bark = yell
print(bark('Hav'))

del yell
# print(yell('Nyaf'))  # name 'yell' is not defined
# но даже после удаления функции мамки, функция доча будет работать
print(bark('Nyaf'))
print(bark.__name__) #  yell

# Функции можно хранить в структурах данных
funcs = [bark, str.lower, str.capitalize]
for f in funcs:
    print( f('Hi, bitches'))
