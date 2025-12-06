class Restaurant:
    def __init__(self):

        self.menu = {
            "Pizza": 250,
            "Burger": 120,
            "Pasta": 180,
            "Coffee": 80,
            "Sandwich": 100
        }

    def show_menu(self):
        print("---- MENU ----")
        for item, price in self.menu.items():
            print(f"{item}: ₹{price}")
        print()

    def print_bill(self, orders):
        total = 0
        print("\n---- BILL ----")
        for item in orders:
            if item in self.menu:
                price = self.menu[item]
                print(f"{item}: ₹{price}")
                total += price
            else:
                print(f"{item}: Not Available")
        print("----------------")
        print(f"Total Amount: ₹{total}")


restaurant = Restaurant()
restaurant.show_menu()

items = input("Enter items ordered (separated by commas): ").split(",")
items = [item.strip() for item in items]

restaurant.print_bill(items)
