class Airplane:
    # count = 1

    def __init__(self, ap_code, capacity):
        self.capacity = int(capacity)
        self.ap_code = ap_code
        self.number_vip_seat = int(0.1 * self.capacity)
        self.number_general_seat = self.capacity - self.number_vip_seat
        self.seats = {}
        self.reserved_seats = {}
        self.add_seat_general()
        self.add_seat_vip()

    def add_seat_general(self):
        for i in range(1, self.number_general_seat + 1):
            self.seats[f"gen-{i}"] = GeneralSeat(f"gen-{i}")
        # if Airplane.count <= self.number_general_seat:
        #     self.seats.append(VipSeat(Airplane.count))
        #     Airplane.count += 1

    def add_seat_vip(self):
        for i in range(self.number_general_seat + 1, self.capacity + 1):
            self.seats[f"vip-{i}"] = VipSeat(f"vip-{i}")

    def __repr__(self):
        return f"{self.seats}"

    def reserve_seat(self, type_seat):
        if type_seat == "vip":
            for key, val in self.seats.items():
                if isinstance(val, VipSeat):
                    self.reserved_seats[key] = val
                    self.seats.pop(key)
                    return val
            else:
                raise Exception("the capacity of vip seat is full")
        elif type_seat == "general":
            for key, val in self.seats.items():
                if isinstance(val, GeneralSeat):
                    self.reserved_seats[key] = val
                    self.seats.pop(key)
                    return val
            else:
                raise Exception("the capacity of general seat is full")


class Seat:
    price = 0

    def __init__(self, seat_number):
        self.seat_number = seat_number

    def __repr__(self):
        return f"{self.seat_number}"


class VipSeat(Seat):
    price = 1000


class GeneralSeat(Seat):
    price = 2000


def main():
    aiplane1 = Airplane("A1", 10)
    seat1 = aiplane1.reserve_seat("vip")
    seat2 = aiplane1.reserve_seat("general")
    seat3 = aiplane1.reserve_seat("vip")

    print(aiplane1)


# airplane1 = Airplane("123", 100)
# airplane1.add_seat()
# print(airplane1)


if __name__ == "__main__":
    main()
