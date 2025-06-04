class MoneyMachine:

    CURRENCY = "₹"

    coin_values = {
        "five" : 5.0,
        "tens" : 10.0,
        "twenty" : 20.0,
        "fifty" : 50.0
    }

    def __init__(self):
        self.profit = 0
        self.received_money = 0

    def report(self):
        # this will show the profit of the coffee machine
        print(f"Your profit is {self.CURRENCY} {self.profit}")

    def processmoney(self):
        # Returns tota calculated from the money inserted
        print("Insert the money : ")
        for coin in self.coin_values:
            self.received_money +=  int(input(f"How many {coin}? : ")) * self.coin_values[coin]
        return self.received_money

    def makePayment(self, cost):
        """Return true if the  payment is accepted or False otherwise """
        self.processmoney()
        if self.received_money >= cost:
            change  =round(self.received_money - cost, 2)
            print(f"Your change is {self.CURRENCY}{change}")
            self.profit += change
            self.received_money = 0
            return True
        else:
            print("Sorry, you don't have enough money")
            self.received_money = 0
            return False

