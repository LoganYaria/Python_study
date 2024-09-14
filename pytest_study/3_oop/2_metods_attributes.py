class Car():
    wheels = 4 #attribute   лучше создавать константу, которую не будешь менять

    def drive(self):# metod
        print('Car is drive!')
    def stop(self):
        print('Car is stop')

class Animal():
    legs = 4

    def eat(self):
        print('Animal is eat')
    def sleep(self):
        print('Animal is sleep')


nissan_qashkai = Car()
print(nissan_qashkai.wheels)