import pytest
from hamcrest import assert_that, calling, any_of, raises,equal_to
from contextlib import suppress
import sys
sys.path.append('../..')
from circle import Circle
from triangle import Triangle
from rectangle import Rectangle
from square import Square

wrong_params = [
        (-3, -5, -4, 'input negative numbers'),
        (0, 0, 0, 'input zero'),
        (1, 2, 100, 'summ of to sides must be bigger than remaining side'),
        ('a', 'b', 'c', 'symbol input'),
        (0.3, 0.4, 0.5, 'float input')
    ]
@pytest.mark.parametrize('side_1,side_2,side_3,missed_check', wrong_params)
def test_wrong_input_0_mine(side_1, side_2, side_3, missed_check):
    try:
        a = Triangle(side_1, side_2, side_3)
    except ValueError:
        pass
    except TypeError:
        pass
    else:
        assert 1 == 0, f'We missed the check: {missed_check}'
@pytest.mark.parametrize('side_1,side_2,side_3,missed_check', wrong_params)
def test_wrong_input_1_Ilushke(side_1, side_2, side_3, missed_check):
    assert_that(
        calling (Triangle).with_args(side_1,side_2,side_3),
        any_of(
            raises(ValueError),
            raises(TypeError),
        ),
        f'Triangle was initialised succsesfoly with wrong args: {missed_check}'
        )
@pytest.mark.parametrize('side_1,side_2,side_3,missed_check', wrong_params)
def test_wrong_input_2_Ilushke_2(side_1,side_2,side_3,missed_check):
    with suppress(ValueError,TypeError):
        a = Triangle(side_1,side_2,side_3)
        raise AssertionError(f'Triangle was initialised with wrong_data:{missed_check}')

def test_method_perimeter():#default_triangle
    default_triangle = Triangle(10, 15, 20)
    answ = default_triangle.get_perimeter
    print(str(answ))
    # assert_that(
    #     str(answ), equal_to('45')
    # )



#45,72

# def test_triangle_perimetr():
#     a = Triangle(7,5,10)
#     assert (a.get_perimeter() == 22)
#
# def test_triangle_area():
#     a = Triangle(3,4,5)
#     print(a.get_area)
#     assert (a.get_area() == 6)


