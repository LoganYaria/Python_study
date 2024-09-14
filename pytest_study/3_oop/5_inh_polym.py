class Plane:
    _flaps_status = 'Down' # неприватные для исп. внутри класса атрибуты
    __gear_status = 'Down' # приватные атрибуты

    def __init__(self, brand, type, count_engine):
        self.brand = brand
        self.type = type
        self.count_engine = count_engine

    def get_flaps(self):
        return self._flaps_status

    def get_gear(self):
        return self.__gear_status

    def get_name(self):
        return self.brand

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
#Унаследуемся от класса Plane и переопределим его. расшираем функциональность, но не перопредеяем обратную совместимость
class Turboprop(Plane):
    def __init__(self, brand,count_engine):
        super().__init__(brand,'turboprop',count_engine) # Обращение к родителю БЕЗ SELF

class RussianPlane:
    # def get_name(self):# абстрактный метод: есть имя, нет реализации
    #     raise NotImplemented('This method is not implemented')
    def almost_ready(self):
        print(f'{self.brand} almost ready to fly. Just a few month/years, please')

#Множественная наследовательность
class RussianJet(RussianPlane,Plane):# главнее тот кто слева
    def __init__(self,brand,count_engine):
        super().__init__(brand,'jet',count_engine)

    def build_plane(self):
        if self.get_gear() == 'Down':
            print(f'We are on the ground, Lets build our {self.almost_ready()}') # метод almost_ready используется в
            # классе RussianPlane, который бегает за именем самолета в метод get_ma,e класса Plane. Это слишком глубоко
            # и питон хуй кладет на такие глубокие обращения

class Mixin: #
    pass


#
# tbm130 = Turboprop('TBM130',1)
# print (tbm130.type)
ms21 = RussianJet('MS21',2)
print(ms21.build_plane())

#https://younglinux.info/oopython/inheritance