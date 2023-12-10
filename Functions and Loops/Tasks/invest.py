def invest(amount,persent,years):
    """Посчитает, насколько вы обаготитесь с опр суммой за опр количество лет"""
    for n in range(1,years+1):
        amount = amount + amount * (0.01 * persent)
        print(f'За {years} у вас накопится {amount:,.2f} денег.')


a=int(input('Введите сумму вклада: '))
p=int(input('Введите процент вклада: '))
y=int(input('Введите количество лет: '))
invest(a,p,y)
