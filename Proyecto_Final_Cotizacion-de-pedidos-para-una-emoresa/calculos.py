def calculate_subtotal(price, quantity):
    return price * quantity

def calculate_total_subtotal(subtotals):
    total = 0.0
    for sub in subtotals:
        total += sub
    return total

def get_discount_rate(client_type):
    discounts = {
        'A': 0.15,
        'B': 0.10,
        'C': 0.00
    }
    return discounts.get(client_type, 0.0)

def get_shipping_cost(zone):
    shipping_costs = {
        '1': 5.00,
        '2': 10.00,
        '3': 20.00
    }
    return shipping_costs.get(zone, 0.0)

def calculate_final_total(subtotal, discount_rate, shipping_cost):
    discount_amount = subtotal * discount_rate
    subtotal_with_discount = subtotal - discount_amount
    final_total = subtotal_with_discount + shipping_cost
    return discount_amount, final_total
