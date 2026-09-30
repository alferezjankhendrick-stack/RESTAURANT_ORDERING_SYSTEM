from menu import MENU, build_item_lookup, display_menu
from yes_no import ask_yes_no
from order import take_orders
from order_type import ask_customer_type
from calculate import compute_totals
from receipt import print_receipt

def main():
    lookup = build_item_lookup(MENU)

    while True:
        display_menu(lookup)

        if not ask_yes_no("Order now? (y/n): "):
            print("Goodbye!")
            break

        orders = take_orders(lookup, ask_yes_no)
        is_senior = ask_customer_type(ask_yes_no)
        subtotal, discount, label, total = compute_totals(orders, is_senior)
        print_receipt(orders, subtotal, discount, label, total)

        if not ask_yes_no("Would you like to order again? (y/n): "):
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()