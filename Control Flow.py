def ground_shipping(weight):
    flat_charge = 20.00
    if weight <= 2:
        return weight * 1.50 + flat_charge
    elif weight <= 6:
        return weight * 3.00 + flat_charge
    elif weight <= 10:
        return weight * 4.00 + flat_charge
    else:
        return weight * 4.75 + flat_charge


ground_shippingCost = ground_shipping(8.4)
print(ground_shippingCost)

premium_shipping = 125.00
print(premium_shipping)


def drone_shipping(weight):
    if weight <= 2:
        return weight * 4.50
    elif weight <= 6:
        return weight * 9.00
    elif weight <= 10:
        return weight * 12.00
    else:
        return weight * 14.25


drone_shippingCost = drone_shipping(1.5)
print(drone_shippingCost)


def cheapest_shipping(weight):
    Ground = ground_shipping(weight)
    Premium = premium_shipping
    Drone = drone_shipping(weight)
    if Ground < Premium and Drone:
        return "Use Ground shipping. It will cost you only  " + str(Ground)
    elif Premium < Ground and Drone:
        return "Use Premium shipping. It will cost you only  " + str(Premium)
    else:
        return "Use Drone shipping. It will cost you only  " + str(Drone)


print(cheapest_shipping(4.8))





















