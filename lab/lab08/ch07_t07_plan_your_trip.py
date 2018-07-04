def rental_car_cost(days):
    cost = 40 * days
    if days >= 7:
        cost -= 50
    elif days >= 3:
        cost -= 20
    return cost


def trip_cost(city, days):
    return rental_car_cost(days) + hotel_cost(days - 1) + plane_ride_cost(city)


def trip_cost(city, days, spending_money):
    return rental_car_cost(days) + hotel_cost(days - 1) + plane_ride_cost(city) + spending_money
