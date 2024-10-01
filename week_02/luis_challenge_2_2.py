"""Delivery fee calculate ."""

#  Delivery depends on (BUT NEVER EXCEEDS 15€):
#  1) CART VALUE,
#  1.1) if (cart value < 10): surcharge = 10 - cart value
#  1.2) if (cart value >= 200): total_fee = 0

#  2) ITEMS IN CART,
#  2.1) 0.5*items_in_excess_of_four
#  2.2) +1.2 if (len(items)>12)

#  4) DELIVERY DISTANCE
#  4.1) 2+(additional_distance/500)

#  3) TIME OF THE ORDER
#  3.1) if current_time in range(15, 17): total_fee = total_fee*1.2

#  5.1) if (total_fee > 15): total_fee = 15
#  5.2) if (cart_value >= 200): total_fee = 0
