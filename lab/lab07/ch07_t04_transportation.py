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
