from menu import Menu, MenuItem
from moneyMachine import MoneyMachine
from coffeeMaker import CoffeeMaker

money = 0
machine_open = True
coffee = CoffeeMaker()
ingredient = MenuItem
menu = Menu()
process = MoneyMachine()
menu.print_menu()
while machine_open:
    choice = input("What would you like to have?? ")

    if choice == "off":
        machine_open = False
    elif choice == "report":
        coffee.report()
        process.report()
    else:
        # Check if the choice is a valid numeric input (1, 2, or 3)
        if choice.isdigit():
            choice = int(choice)  # Convert input to integer
            drink = menu.find_drink(choice)

            if drink is None:
                print(f"Sorry, drink with ID {choice} is not available.")
            elif coffee.is_resource_ok(drink):
                if process.makePayment(drink.cost):
                    coffee.make_coffee(drink)
        else:
            print("Invalid input. Please enter a valid number (1, 2, or 3) or type 'off' to quit.")