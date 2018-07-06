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
