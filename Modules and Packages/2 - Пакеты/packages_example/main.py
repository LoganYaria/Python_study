#main.py
#Класический вызов модулей из пакета mypackage
import mypackage.module1
import mypackage.module2
import mypackage.mysubpackage.module3

for every in mypackage.mysubpackage.module3.people:
    print (mypackage.module1.greet(every))

# print(mypackage.module1.greet('MiniPini'))
# print(mypackage.module2.depart('Kakashka'))

##Импорт сразу двух модулей из одного пакета
#main.py
# from mypackage import module1, module2
#
# print(module1.greet('Kot'))
# print(module2.depart('Popa'))

# #Импорт двух модулей из пакета под другими именами
# from mypackage import module1 as md1, module2 as md2
#
# print(md1.greet('MiniPini'))
# print(md2.depart('Kakashka'))

# #Импорт сразу функций из модулей пакта
# from mypackage.module1 import greet
# from mypackage.module2 import depart
#
# print(greet('MiniPini'))
# print(depart('Kakashka'))