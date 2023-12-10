# #Работает и с символами
# print('a'<'b')

#Ключевое слово and

print(False and False)#False
print(2 > -2 and 10<1000)

#Ключевое слово or

print(False and False)#False
print(100 < 10 or 1 == 1)

#Ключевое слово not

print(not True == False)#True
#not имееет более низкий приоритет чем логические операнды, так что:
print(False == (not True))

#Иерархия операндов
#<>==
#not
#and
#or


#Ключевое слово if

if 2+2==4:
    print('2+2=4')

#Ключевое слово else

balls=40
if balls>=70:
    print('Вы сдали экз.')

else:
    print('Вы не сдали экз.')

#Ключевое слово elif

ball=85

if ball >= 90:
    print('Your mark is A!')
elif ball >=80:
    print('Your mark is 4!GJ')
elif ball >=70:
    print('Your mark is 3')
else:
    print('Loh, pidr.')
