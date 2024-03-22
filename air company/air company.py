from samane.travel.travel import Travel
from samane.airplane.airplane import Airplane


class Airline:
    def __init__(self, name):
        self.name = name
        self.airplanes = []
        self.travels = []
        self.balance = 0

    def add_travel(self, index_of_plane, orgin, destination, move_time, end_time):
        self.travels.append(Travel(self.airplanes[index_of_plane], orgin, destination, move_time, end_time))

    def add_balance(self, price):
        self.balance += price

    def add_airplane(self, name_of_plane):
        for name in name_of_plane:
            self.airplanes.append(Airplane(name, 10))


air1 = Airline("A")
air1.add_airplane(["ssd", "aad", "bbc"])
air1.add_travel(1, "aaa", "bbb", "1234", "7890")
air1.add_travel(0, "caa", "dbb", "1534", "7690")
