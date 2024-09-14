class Rectangle():
    _name = 'Rectangle'

    def __init__(self,side_1,side_2):

        if not isinstance(side_2, int) or not isinstance(side_2, int):
            raise TypeError('sides should be int')

        if side_2 <= 0 or side_1 <= 0:
            raise ValueError('side should be positive')

        self.side_2 = side_2
        self.side_1 = side_1

    def get_name(self):
        return self._name
    def get_area(self):
        return self.side_2*self.side_1
    def get_perimeter(self):
        return self.side_2 * 2 + self.side_1 * 2

if __name__ =='__main__': # при импортировании модуля в другой файл код ниже выполняться не будет

    req_1 = Rectangle(2,4)
    print(req_1.get_area())