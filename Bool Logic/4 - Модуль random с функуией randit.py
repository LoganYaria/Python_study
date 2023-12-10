import random
# print(random.randint(1,3))



# #Проверка функции рандит
#
# def coin ():
#     """Подбрасывает монету!"""
#     return(random.randint(0,1))
# throw=int(input('Enter throw: '))
# eagle = 0
# reshko = 0
# for i in range(throw):
#     if coin() == 0:
#         reshko=reshko+1
#     else:
#         eagle=eagle+1
#
# print(f"""Вероятность выпадния орла после {throw:,} бросков составляет {eagle/throw:.2%}.
# В то же время вероятность выпадния решка после {throw:,} бросков составляет {reshko/throw:.2%}.""")

# #Функция random() возвращает десятичное силов в пределах [0.0:1.0)
#
# print(random.random())
def check_random ():#"""veroyatnost"""):
    if random.randint(0,1)==1:#"""<veroyatnost""":
        return 1
    else:
        return 0

counter = 0
for i in range(10000):
    counter = float(counter) + float(check_random())#0.7))

print(10_000/counter)