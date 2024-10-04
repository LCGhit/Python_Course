"""Delivery fee calculate ."""


import datetime


def validateNum(start, end, message):
    """Validate number from range(start, end)."""
    flag = 'y'
    result = ''
    while (flag == 'y'):
        user_input = input(message)
        user_input = user_input.strip().lower()
        if (user_input.isdigit()):
            if (int(user_input) in range(start, end)):
                result = int(user_input)
                flag = 'n'
            else:
                print(f'Out of range. Insert a number from {start} to {end-1}')
        elif (user_input == ''):
            flag = 'n'
        else:
            print('Invalid input. Enter a number, please.')
    return result


def pickFromDict(some_dict, unit, scale, message):
    """Create menu to return a selected value."""
    for key, value in some_dict.items():
        print(list(some_dict).index(key)+1, key, str(value/scale)+unit)
    print('ENTER or 0 -> Finish')
    pick = validateNum(0, len(list(some_dict))+1, message)
    if (pick == ''):
        return 0
    return int(pick)


def createOrder():
    """Pick products from stock."""
    avail_products = {'item_01': 50, 'item_02': 200, 'item_03': 150,
                      'item_04': 300, 'item_05': 20, 'item_06': 500,
                      'item_07': 900, 'item_08': 1500}
    chosen_products = {}
    pick = pickFromDict(avail_products, '€', 100, 'Pick product => ')
    while (pick != 0):
        chosen_products[list(avail_products)[pick-1]] = \
            avail_products[list(avail_products)[pick-1]]
        pick = pickFromDict(avail_products, '€', 100, '\nPick product => ')
    return chosen_products


def orderTotal(order_dictionary):
    """Return total cost of cart."""
    total_cart_cost = 0
    for value in order_dictionary:
        total_cart_cost += order_dictionary[value]
    return total_cart_cost


def surchargeCalc(products_array):
    """Calculate surcharges from array of products."""
    num_items = len(products_array)
    cart_cost = orderTotal(products_array)

    cheap_cart_surcharge = 0
    if (cart_cost < 1000):
        cheap_cart_surcharge = 1000 - cart_cost

    excess_items_surcharge = 0
    if (num_items > 4):
        excess_items_surcharge = (50 * num_items-4)
    if (num_items > 12):
        excess_items_surcharge += 120

    delivery_range = {'City 1': 1000, 'City 2': 300, 'City 3': 2340,
                      'City 4': 4200, 'City 5': 1740}
    distance = pickFromDict(delivery_range, ' Km', 1000,
                            '\nWhere should we deliver your purchase? => ')
    distance = delivery_range[list(delivery_range)[int(distance)-1]]
    distance_surcharge = 200
    print('DISTANCE: ', distance)
    if ((distance - 1000) > 0):
        distance_surcharge += (((distance - 1000) // 500)*100) + 100

    rush_surcharge = 0
    current_time = str(datetime.datetime.now().time()).split(':')
    weekday = datetime.datetime.today().weekday()
    if (int(current_time[0]) in range(15, 20)) and (weekday == 4):
        rush_surcharge = (cheap_cart_surcharge + excess_items_surcharge
                          + distance_surcharge) * 0.2

    surcharges = {'Low cart value cost': cheap_cart_surcharge,
                  'Excess items cost': excess_items_surcharge,
                  'Distance cost': distance_surcharge,
                  'Rush cost': rush_surcharge}

    if (cart_cost >= 20000):
        for key, value in surcharges:
            surcharges[key] = 0

    return surcharges


def deliveryCostsTotal(surcharges_dict):
    """Calculate total delivery cost from surcharges array."""
    surcharge_total = 0
    for value in surcharges_dict:
        surcharge_total += surcharges_dict[value]

    if (surcharge_total > 1500):
        surcharge_total = 1500

    return surcharge_total


def mainFunc():
    """Create order and show all the added delivery costs."""
    order = createOrder()
    surcharges = surchargeCalc(order)
    total_delivery_cost = deliveryCostsTotal(surcharges)
    order_total = orderTotal(order)

    print('\nYOUR ORDER:')
    for key, value in order.items():
        print(f'{key} : {value/100}€')
    print(f'Cart total: {order_total/100:.2f}€')

    print('\nDELIVERY COSTS:')
    for key, value in surcharges.items():
        print(f'{key} : {value/100}€')
    print(f'Total delivery costs: {total_delivery_cost/100:.2f}€')

    print(f'\nYOUR PURCHASE TOTAL: \
    {(total_delivery_cost+order_total)/100:.2f}€')


if __name__ == '__main__':
    mainFunc()
