import random

def coin_drop():
    """Just drop coin"""
    if random.randint(0,1) ==1:
        return ('eagle')
    else:
        return ('reshko')

full_circle=0
reshko=0
eagle=0

trying=''
throw = int(input('Enter number of throw: '))

for i in range(throw+1):
    circle = 0
    while ((reshko < 1)or(eagle < 1)):
        trying = coin_drop()
        if trying == 'eagle':
            eagle = eagle+1
        else:
            reshko = reshko+1
        circle = circle+1
    full_circle=full_circle+circle
    reshko=0
    eagle=0
print(full_circle/throw)




