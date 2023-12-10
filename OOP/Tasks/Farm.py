class Flight:
    def __init__(self, captein_name, aircraft_type, flight_number, airp_dep, airp_dest, flight_time, route):
        self.captain_name = captein_name
        self.aircraft_type = aircraft_type
        self.flight_number = flight_number
        self.airp_dep = airp_dep
        self.airp_dest = airp_dest
        self.flight_time = flight_time
        self.route = route

    def __str__(self):
        return f'Hello, this is your captain speaking. My name is {self.captain_name}. Welcome a board of {self.aircraft_type}. Today we flying by flight {self.flight_number} from {self.airp_dep} to {self.airp_dest}. Flight time will be near {self.flight_time} hours'

    def feeding(self):
        if self.flight_time < 4:
            return ('You shoud take 1 lunches portions, and 2 tea portions for peron')
        elif self.flight_time < 8:
            return ('You shoud take 2 lunches portions, and 2 tea portions for peron')
        else:
            return ('You shoud take 2 lunches portions, and 3 tea portions for peron')

    def bad_weather(self,way_points):
        bad_weather_wp = []
        for point in way_points:
            if point in self.route:
                bad_weather_wp.append(point)
        if len(bad_weather_wp) == 0:
            return "All way is clear."
        else:
            return f'You should faster your pax on {(bad_weather_wp)} on rout.'

class TakeoffLanding(Flight):
    def __init__(self, captain_name, aircraft_type, flight_number, airp_dep, airp_dest, flight_time, route, weight):
        Flight.__init__(self,captain_name, aircraft_type, flight_number, airp_dep, airp_dest, flight_time, route)
        self.weight = weight

    def take_off(self,runways_for_take_off):
        suitable_runways=[]
        if self.weight > 70:
            for key in runways_for_take_off:
                if runways_for_take_off[key] >= 2000:
                    suitable_runways.append(key)
            if len(suitable_runways) == 0:
                return f'You can\'t take off with {self.weight} on board in {self.airp_dep}.'
            else:
                return f'You shoud choise {suitable_runways} for take off in {self.airp_dep}'
        else:
            return f'any of runways is suitable for {self.airp_dep}'

    def landing(self,runways_for_landing,landing_bad_weather_airports):
        is_weather_in_airport = super().bad_weather(landing_bad_weather_airports)
        if self.airp_dest in is_weather_in_airport:
            return 'You should fly to alternate airport.'
        else:
            suitable_runways = []
            if self.weight > 10:
                for key in runways_for_landing:
                    if runways_for_landing[key] >= 1500:
                        suitable_runways.append(key)
                if len(suitable_runways) == 0:
                    return f'You can\'t take off with {self.weight} on board in {self.airp_dest}.'
                else:
                    return f'You shoud choise {suitable_runways} for take off in {self.airp_dest}'
            else:
                return f'any of runways is suitable for {self.airp_dest}'






flight_001_take_off = TakeoffLanding('Boris Moiseev', 'Boeing 737', 'MU9889', 'St.Petersburg', 'VHHH', 12,['ULLI','way_point_1', 'way_point_2', 'way_point_3', 'way_point_3','VHHH'], 100)
#print(flight_001_take_off.landing({'RW28R':3000, 'RW28L':1500},['UUDD','UUHH','HGFA','VHHH']))

#flight_001 = Flight('Boris Moiseev', 'Boeing 737', 'MU9889', 'Moskow', 'Hong Kong', 12,['ULLI','way_point_1', 'way_point_2', 'way_point_3', 'way_point_3','VHHH'])

#rint(flight_001)
#print(flight_001.feeding())
#print(flight_001.bad_weather(['ULLI']))