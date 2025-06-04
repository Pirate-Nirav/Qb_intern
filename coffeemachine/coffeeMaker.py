class CoffeeMaker:
    def __init__(self):
        self.resource = {
            "water": 300,
            "milk": 200,
            "coffee": 100
        }

    def report(self):
        # This will show the report of the resources like what is remaining in the machine
        print(f"Water: {self.resource['water']} ml")
        print(f"Milk: {self.resource['milk']} ml")
        print(f"Coffee: {self.resource['coffee']} g")

    def is_resource_ok(self, drink):
        # Return true if order can be made & return false if ingredients are insufficient
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resource[item]:
                print(f"Sorry, there is not enough {item}")
                can_make = False
        return can_make

    def make_coffee(self, order):
        # Deducts the required ingredients from the resource
        for item in order.ingredients:
            self.resource[item] -= order.ingredients[item]
        print(f"Here is your order: {order.name}")