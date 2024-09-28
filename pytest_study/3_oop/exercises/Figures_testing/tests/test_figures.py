import pytest
import sys
sys.path.append('../..')
from circle import Circle
from triangle import Triangle
from rectangle import Rectangle
from square import Square

@pytest.mark.parametrize(
    'side_1,side_2,side_3,missed_check',
    [
        (-3, -5, -4, 'input negative numbers'),
        (0, 0, 0, 'input zero'),
        (1, 2, 100, 'summ of to sides must be bigger than remaining side'),
        ('a', 'b', 'c', 'symbol input'),
        (0.3, 0.4, 0.5, 'float input')
    ]
)
def test_wrong_input(side_1, side_2, side_3, missed_check):
    try:
        a = Triangle(side_1, side_2, side_3)
    except ValueError:
        pass
    except TypeError:
        pass
    else:
        assert 1 == 0, f'We missed the check: {missed_check}'

# def test_triangle_perimetr():
#     a = Triangle(7,5,10)
#     assert (a.get_perimeter() == 22)
#
# def test_triangle_area():
#     a = Triangle(3,4,5)
#     print(a.get_area)
#     assert (a.get_area() == 6)


