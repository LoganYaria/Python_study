class Circle():
    _name = 'Circle'
    pi = 3.14159
    def __init__(self,radius):
        if not isinstance(radius, int):
            raise TypeError('sides should be int')
        if radius <= 0:
            raise ValueError('side should be positive')

        self.radius = radius
    def get_name(self):
        return self._name
    def get_area(self):
        return round(self.pi * (self.radius**2))
    def get_perimeter(self):
        return round(2 * self.pi * self.radius)

    def add_area(self,figure_name):
        from rectangle import Rectangle
        from triangle import Triangle
        if isinstance(figure_name,Triangle) or isinstance(figure_name,Circle) or isinstance(figure_name,Rectangle):
            return (self.get_area()+figure_name.get_area())
        else:
            raise ValueError(f'{figure_name} isn\'t a figure')
if __name__ =='__main__': # при импортировании модуля в другой файл код ниже выполняться не будет
    cir_1 = Circle(0)

    print(cir_1.get_name(),cir_1.get_area(),cir_1.get_perimeter())



