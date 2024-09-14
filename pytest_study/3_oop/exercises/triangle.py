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


        self.side1 = side_1 and side_1 < side_2 + side_3
        self.side2 = side_2 and side_2 < side_1 + side_3
        self.side3 = side_3 and side_3 < side_1 + side_2

    def get_name(self):
        return self._name

    def get_perimetr(self):
        return self.side1+self.side2+self.side3
    def get_perimetr_half(self):
        return self.get_perimetr()

    def get_area(self):
        return round(math.sqrt(self.get_perimetr_half() * (self.get_perimetr_half() - self.side1) * (self.get_perimetr_half() - self.side2) * (self.get_perimetr_half() - self.side3)))
