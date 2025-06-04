class MenuItem:
    # Each menu item and its cost
    def __init__(self, idn, name, water, milk, coffee, cost):
        self.idn = idn
        self.name = name
        self.cost = cost
        self.ingredients = {
            'water': water,
            'milk': milk,
            'coffee': coffee
        }

class Menu:
    # Model the menu with drinks
    def __init__(self):
        self.menu = [
            MenuItem(idn=1, name='Latte', water=200, milk=150, coffee=24, cost=50),
            MenuItem(idn=2, name="Espresso", water=50, milk=0, coffee=18, cost=15),
            MenuItem(idn=3, name="Cappuccino", water=250, milk=50, coffee=24, cost=30)
        ]

    def print_menu(self):
        # Print the menu with prices
        print("MENU: Drink Name - Price (in ₹)")
        for item in self.menu:
            print(f"{item.idn}) {item.name}: ₹{item.cost}")


    def get_items(self):

        # This should return all the name available menu Item
        option = ""
        for item in self.menu:
            option += f"{item.name} /"
        return option

    def find_drink(self, order_id):
        """Searches the menu for a particular drink by name. Returns that item if it exists, otherwise returns None"""
        for item in self.menu:
            if item.idn == order_id:
                return item
        print("Sorry that item is not available.")
