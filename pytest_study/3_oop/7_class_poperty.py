class Plane:
    _flaps_status = 'Down' # неприватные для исп. внутри класса атрибуты
    __gear_status = 'Down' # приватные атрибуты

    def __init__(self, brand, type, count_engine):
        self.brand = brand
        self.type = type
        self.count_engine = count_engine

    @property # могу получить скрытые атрибуты изменить не позволит getter/setter/deletter
    def flaps(self):
        return self._flaps_status

    @flaps.setter
    def flaps(self, amount: str): #инициация и объявление amount
        if amount != 'Down':
            self._flaps_status = amount

    def get_flaps(self):
        return self._flaps_status

    def get_gear(self):
        return self.__gear_status

    def get_name(self):
        return self.brand

a320 = Plane('Airbus','jet',2)
a320.flaps = 'UP!'

print(a320.flaps)