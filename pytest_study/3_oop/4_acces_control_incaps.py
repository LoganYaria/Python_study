class Plane:
    _flaps_status = 'Down' # неприватные для исп. внутри класса атрибуты
    __gear_status = 'Down' # приватные атрибуты

    def __init__(self, brand, type, count_engine):
        self.brand = brand
        self.type = type
        self.count_engine = count_engine

    def flaps_up(self):
        self._flaps_status = 'Up'
        print(f'Speed checked,flaps of {self.type} {self.brand} is up')

    def flaps_down(self):
        self._flaps_status = 'Down'
        print(f'Speed checked, flaps of {self.type} {self.brand} is down')

    def take_off(self):
        self.__gear_status = 'Up'
        print(f'Positive rate, gear of {self.brand} is up!')

    def leand(self):
        self.__gear_status = 'Down'
        print(f'Gear of {self.brand} is down!')

    def __approaching(self): #ghbdfnysq метод
        if self._flaps_status == 'Up':
            self.flaps_down()
        if self.__gear_status == 'Up':
            self.leand()
        print(
            f'The flaps is {self._flaps_status} and gear is {self.__gear_status}. '
            f'Leanding checklist compete {self.brand} is ready for land'
              )


if __name__ =='__main__': # при импортировании модуля в другой файл код ниже выполняться не будет

    Boeing_737 = Plane('Boeing 737','jet',2)

    print(Boeing_737._Plane__gear_status) # обраащение к приватному атрибуту