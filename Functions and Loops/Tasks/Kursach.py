from random import randint
k=randint(1, 7)
for i in range(3):
    A=int(input ("Я задал тебе число. У тебя есть  три попытки. Попробуй угадать! :) Введи число от 1 до 7: "))
    if A<0 or A>7 or A==0:
        print ("Вы ввели недопустимое значение")
        break
    if A==k:
        print ("Вы угадали")
        break
    else:
        if i !=2:
            print ("Попробуй еще раз")
        if i == 2:
            print(f"Вы проиграли, верный ответ был: {k}")
            break

