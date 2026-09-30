BULK_QTY = 5
BULK_RATE = 0.05
SENIOR_RATE = 0.20

def get_discount_info(subtotal, total_qty, is_senior):
    if is_senior:
        return subtotal * SENIOR_RATE, "Senior/PWD Discount (20%)"
    elif total_qty >= BULK_QTY:
        return subtotal * BULK_RATE, "Discount (5%)"
    return 0.0, None