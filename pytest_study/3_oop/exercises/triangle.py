import math
class Triangle():
    _name = 'Triangle()'

    def __init__(self,side_1,side_2,side_3):

        if not isinstance(side_1, int) or not isinstance(side_2, int) or not isinstance(side_3, int):
            raise TypeError('sides should be int')

        if side_1 <= 0 or side_2 <= 0 or side_3 <= 0:
            raise ValueError('side should be positive')

        if side_1 > side_2+side_3:
            raise ValueError('side_1>side_2+side3 - wrong triangle!')
        elif side_2 > side_1+side_3:
            raise ValueError('side_2>side_1+side3 - wrong triangle!')
        elif side_3 > side_1+side_2:
            raise ValueError('side_2>side_1+side3 - wrong triangle!')

        self.side1 = side_1
        self.side2 = side_2
        self.side3 = side_3

    def get_name(self):
        return self._name

    def get_perimeter(self):
        return self.side1+self.side2+self.side3
    def get_perimeter_half(self):
        return self.get_perimeter()/2

    def get_area(self):
        return round(math.sqrt(self.get_perimeter_half() * (self.get_perimeter_half() - self.side1) * (
                    self.get_perimeter_half() - self.side2) * (self.get_perimeter_half() - self.side3)))

    def add_area(self,figure_name):
        if isinstance(figure_name,Triangle) or isinstance(figure_name,Circle) or isinstance(figure_name,Rectangle):
            return (self.get_area()+figure_name.get_area())
        else:
            raise ValueError(f'{figure_name} isn\'t a figure')

if __name__ =='__main__':
    pass
    # from rectangle import Rectangle
    # from circle import Circle
    # from square import Square
    # tryn_1 = Triangle(3,4,5)
    # tryn_2 = Square(5)
    #
    # print(tryn_1.get_area())
    # print(tryn_2.get_area())
    # print(tryn_1.add_area(tryn_2))