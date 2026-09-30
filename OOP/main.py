from order import Menu, Order

RAW_MENU = {
    "Burgers": {"Cheeseburger": 89.00, "Beef Burger": 129.00, "Chicken Burger": 99.00},
    "Sides": {"French Fries": 49.00, "Onion Rings": 55.00},
    "Drinks": {"Soft Drink": 39.00, "Iced Tea": 45.00, "Bottled Water": 25.00},
}
STORE_NAME = "KHENJI FOOD RESTAURANT"

def ask_yes_no(prompt):
    while True:
        answer = input(prompt).strip().lower()
        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no"):
            return False
        print(" Invalid choices! Please enter 'y' or 'n'.")

def get_item_and_qty(menu):
    while True:
        raw = input("Item number: ").strip()
        if raw.isdigit() and int(raw) in menu.lookup:
            break
        print("  Invalid item number.")
    while True:
        raw_qty = input("Quantity: ").strip()
        if raw_qty.isdigit() and int(raw_qty) > 0:
            break
        print("  Invalid quantity.")
    return menu.get_item(int(raw)), int(raw_qty)

def main():
    menu = Menu(STORE_NAME, RAW_MENU)

    while True:
        menu.display()

        if not ask_yes_no("Order now? (y/n): "):
            print("Goodbye!")
            break

        is_senior = False
        order = Order(is_senior=is_senior)

        while True:
            menu_item, qty = get_item_and_qty(menu)
            order.add_item(menu_item, qty)
            if not ask_yes_no("Order another item? (y/n): "):
                break

        order.is_senior = ask_yes_no("Senior Citizen/PWD? (y/n): ")
        order.print_receipt(STORE_NAME)

        if not ask_yes_no("Would you like to order again? (y/n): "):
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()