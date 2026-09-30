import datetime

class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Menu:
    def __init__(self, store_name, menu_data):
        self.store_name = store_name
        self.lookup = {}
        self._build_lookup(menu_data)

    def _build_lookup(self, menu_data):
        number = 1
        for category in menu_data:
            for item, price in menu_data[category].items():
                self.lookup[number] = MenuItem(item, price)
                number += 1

    def display(self, width=40):
        print("=" * width)
        print(self.store_name.center(width))
        print("=" * width)
        for number, item in self.lookup.items():
            print(f"{number:>2}. {item.name:<20} PHP {item.price:>6.2f}")
        print("=" * width)

    def get_item(self, number):
        return self.lookup.get(number)

class OrderItem:
    def __init__(self, menu_item, quantity):
        self.menu_item = menu_item
        self.quantity = quantity

    @property
    def total_price(self):
        return self.menu_item.price * self.quantity

class Order:
    BULK_QTY = 5
    BULK_RATE = 0.05
    SENIOR_RATE = 0.20

    def __init__(self, is_senior=False):
        self.items = []
        self.is_senior = is_senior

    def add_item(self, menu_item, quantity):
        self.items.append(OrderItem(menu_item, quantity))

    def compute_subtotal(self):
        return sum(item.total_price for item in self.items)

    def compute_total_quantity(self):
        return sum(item.quantity for item in self.items)

    def compute_discount(self):
        subtotal = self.compute_subtotal()
        total_qty = self.compute_total_quantity()

        if self.is_senior:
            return subtotal * self.SENIOR_RATE, "Senior/PWD Discount (20%)"
        elif total_qty >= self.BULK_QTY:
            return subtotal * self.BULK_RATE, "Discount (5%)"
        return 0.0, None

    def print_receipt(self, store_name, width=40):
        subtotal = self.compute_subtotal()
        discount, discount_label = self.compute_discount()
        total = subtotal - discount

        print("\n" + "=" * width)
        print(store_name.center(width))
        print(datetime.datetime.now().strftime("%b %d, %Y %I:%M %p").center(width))
        print("-" * width)
        for item in self.items:
            print(f"{item.menu_item.name:<16}{item.quantity:>3} x {item.menu_item.price:>6.2f} = {item.total_price:>7.2f}")
        print("-" * width)
        print(f"{'SUBTOTAL':<25}{subtotal:>15.2f}")
        if discount_label:
            print(f"{discount_label:<25}{-discount:>15.2f}")
        print(f"{'TOTAL':<25}{total:>15.2f}")
        print("=" * width)
        print("Thank you, come again!".center(width))
        print("=" * width + "\n")