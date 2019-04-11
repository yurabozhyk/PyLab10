class Voucher:
    voucher_amount = 0

    def __init__(self, country="Spain", duration_in_days=14, price=1000,
                    transport_type="Bus", passengers_quantity=2, hotel_stars=5):
        self.country = country
        self.duration_in_days = duration_in_days
        self.price = price
        self.transport_type = transport_type
        self.passengers_quantity = passengers_quantity
        self.hotel_stars = hotel_stars
        Voucher.voucher_amount += 1

    @staticmethod
    def get_static_field():
        return Voucher.voucher_amount

    def __del__(self):
        print(self.country + " deleted")

    def __str__(self):
        return str(self.__dict__)

def main():
    bus_voucher = Voucher()
    plane_voucher = Voucher("USA", 90, 10000, "Plane")
    car_voucher = Voucher("Sweden", 30, 2000, "Car", 4, 4)

    print(bus_voucher)
    print(plane_voucher)
    print(car_voucher)
    print(Voucher.voucher_amount)

if __name__ == '__main__':
    main()
