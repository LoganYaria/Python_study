import time
class Plane:
    flaps_status = 'Down'
    gear_status = 'Down'

    def __init__(self, brand, type, count_engine):
        self.brand = brand
        self.type = type
        self.count_engine = count_engine

    def flaps_up(self):
        self.flaps_status = 'Up'
        print(f'Speed checked,flaps of {self.type} {self.brand} is up')

    def flaps_down(self):
        self.flaps_status = 'Down'
        print(f'Speed checked, flaps of {self.type} {self.brand} is down')

    def take_off(self):
        self.gear_status = 'Up'
        print(f'Positive rate, gear of {self.brand} is up!')

    def leand(self):
        self.gear_status = 'Down'
        print(f'Gear of {self.brand} is down!')

    def flying(self):
        if self.gear_status == 'Down':
            self.take_off()
        if self.flaps_status == 'Down':
            self.flaps_up()
        print(f'The {self.brand} is flying! The flaps is {self.flaps_status} and gear is {self.gear_status}')

    def approaching(self):
        if self.flaps_status == 'Up':
            self.flaps_down()
        if self.gear_status == 'Up':
            self.leand()
        print(
            f'The flaps is {self.flaps_status} and gear is {self.gear_status}. '
            f'Leanding checklist compete {self.brand} is ready for land'
              )


Boeing_737 = Plane('Boeing 737','jet',2)

Boeing_737.flying()
time.sleep(2)
Boeing_737.approaching()