import pytest
from hamcrest import assert_that, calling, any_of, raises, equal_to, has_properties
from contextlib import suppress
import sys

sys.path.append('../..')
from circle import Circle
from triangle import Triangle
from rectangle import Rectangle
from square import Square

wrong_params_figures = [
    ([-3, -5, -4], 'input negative numbers'),
    ([0, 0, 0], 'input zero'),
    (['a', 'b', 'c'], 'symbol input'),
    ([0.3, 0.4, 0.5], 'float input')
]


@pytest.mark.parametrize('sides,missed_check', wrong_params_figures)
def test_wrong_input_triangle(sides, missed_check):
    with suppress(ValueError, TypeError):
        figure = Triangle(sides[0], sides[1], sides[2])
        raise AssertionError(f'Triangle was initialised with wrong_data:{missed_check}')


def test_wrong_input_triangle():
    with suppress(ValueError, TypeError):
        figure = Triangle(1, 2, 100)
        raise AssertionError(
            'Triangle was initialised with wrong_data: summ of to sides must be bigger than remaining side'
        )


@pytest.mark.parametrize('sides,missed_check', wrong_params_figures)
def test_wrong_input_square(sides, missed_check):
    with suppress(ValueError, TypeError):
        figure = Square(sides[0])
        raise AssertionError(f'Square was initialised with wrong_data: {missed_check}')


@pytest.mark.parametrize('sides, missed_check', wrong_params_figures)
def test_wrong_input_rectangle(sides, missed_check):
    with suppress(ValueError, TypeError):
        figure = Rectangle(sides[0], sides[1])
        raise AssertionError(f'Rectangle was initialised with wrong_data: {missed_check}')


@pytest.mark.parametrize('sides, missed_check', wrong_params_figures)
def test_wrong_input_circle(sides, missed_check):
    with suppress(ValueError, TypeError):
        figure = Circle(sides[0])
        raise AssertionError(f'Circle was initialised with wrong_data: {missed_check}')


elements_for_get_perimeter_or_area = [
    (Triangle(10, 15, 20), [45, 73]),
    (Square(5), [20, 25]),
    (Rectangle(5, 4), [18, 20]),
    (Circle(15), [94, 707])
]


@pytest.mark.parametrize('figure,value', elements_for_get_perimeter_or_area)
def test_method_perimeter(figure, value):
    default_figure = figure
    assert_that(
        default_figure.get_perimeter(), equal_to(value[0]),
        'Некорректный расчет периметра!'
    )


@pytest.mark.parametrize("figure,value", elements_for_get_perimeter_or_area)
def test_method_perimeter(figure, value):
    default_figure = figure
    assert_that(
        default_figure.get_area(), equal_to(value[1]),
        'Некорректный расчет периметра!'
    )


elements_for_add_area = [
    (Triangle(10, 15, 20), Square(5), 98),
    (Triangle(10, 15, 20), Rectangle(5, 4), 93),
    (Triangle(10, 15, 20), Circle(15), 780),
    (Square(5), Rectangle(5, 4), 45),
    (Square(5), Circle(15), 732),
    (Rectangle(5, 4), Circle(15), 727),
]


@pytest.mark.parametrize('cl_figure_1,cl_figure_2,value_add_area', elements_for_add_area)
def test_add_area(cl_figure_1, cl_figure_2, value_add_area):
    figure_1 = cl_figure_1
    figure_2 = cl_figure_2
    assert_that(
        figure_1.add_area(figure_2),
        equal_to(value_add_area),
        'Некорректный расчет периметра!'
    )

# @pytest.mark.parametrize('side_1,side_2,side_3,missed_check', wrong_params_for_triangle)
# def test_wrong_input_0_old(side_1, side_2, side_3, missed_check):
#     try:
#         a = Triangle(side_1, side_2, side_3)
#     except ValueError:
#         pass
#     except TypeError:
#         pass
#     else:
#         assert 1 == 0, f'We missed the check: {missed_check}'


# @pytest.mark.parametrize('side_1, side_2, side_3, missed_check', wrong_params_for_triangle)
# def test_wrong_input_1_by_hamcrest(side_1, side_2, side_3, missed_check):
#     assert_that(
#         calling(Triangle).with_args(side_1,side_2,side_3),
#         any_of(
#             raises(ValueError),
#             raises(TypeError),
#         ),
#         f'Triangle was initialised succsesfoly with wrong args: {missed_check}'
#         )
