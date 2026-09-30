from promo import get_discount_info


def compute_totals(orders, is_senior):
    subtotal = sum(qty * price for _, qty, price in orders)
    total_qty = sum(qty for _, qty, price in orders)

    discount, label = get_discount_info(subtotal, total_qty, is_senior)
    total = subtotal - discount
    return subtotal, discount, label, total