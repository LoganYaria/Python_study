from helpers import strings
from helpers import math

a = int(input('Enter length: '))
b = int(input('Enter width: '))
area_of_a_b = math.area(a,b)
print(strings.shout (f'the area of a {a}-by-{b} rectangle is {area_of_a_b}'))

