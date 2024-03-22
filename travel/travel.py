from ..airplane.airplane import Airplane


class Travel:
    def __init__(self, plane, orgin, destination, move_time, end_time):
        self.passenger = []
        self.orgin = orgin
        self.destination = destination
        self.move_time = move_time
        self.end_time = end_time
        self.ap =plane
        self.name = orgin[:3] + destination[:3]

    def add_passenger(self, passenger):
        self.passenger.append(passenger)


def main():
    trv1 = Travel("abcd", "efgh", "12345", "123456", aiplane1)


if __name__ == "__main__":
    main()
