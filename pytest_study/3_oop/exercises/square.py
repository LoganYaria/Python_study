from rectangle import Rectangle
class Square(Rectangle):
    _name = 'Square'

    def __init__(self,side_1):
        super().__init__(side_1, side_2=side_1)

if __name__ == '__main__':  # при импортировании модуля в другой файл код ниже выполняться не будет
    sq = Square(3)
    print(sq.get_name(),sq.get_area(),sq.get_perimeter())