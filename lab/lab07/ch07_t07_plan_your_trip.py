# The following 3 lines of codes are for UnitTest and you don't need them for your real applications!
global hotel_cost
global plane_ride_cost
global rental_car_cost


def hotel_cost(nights: int) -> int:
    return 140 * nights


def plane_ride_cost(city: str) -> int:
    if city == "Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475


def rental_car_cost(days: int) -> int:
    cost = 40 * days
    if days >= 7:
        cost -= 50
    elif days >= 3:
        cost -= 20
    return cost


def trip_cost(city: str, days: int, spending_money: int = 0) -> int:
    return rental_car_cost(days) + hotel_cost(days - 1) + plane_ride_cost(city) + spending_money


if __name__ == '__main__':
    # Change below line
    print()
