class ATM:
    # Class Variable
    counter = 1 
    
    def __init__(self):
        self.__balance = 0  # integer 
        self.__pin = ""  # String for pin
        self.sno = ATM.counter
        ATM.counter = ATM.counter+1
        print(id(self))

    def get_pin(self):
        return self.__pin
    
    def set_pin(self, new_pin):
        if type(new_pin)==str:
            self.__pin = new_pin
            print("Pin chnaged")
        else:
            return "Not Allowed"
    
    def menu(self):
        while True:  # loop to keep menu running until exit
            user_input = input("""1. Create Pin
2. Deposit
3. Withdraw
4. Check __balance
5. Exit
""")
            if user_input == "1":
                self.create_pin()
            elif user_input == "2":
                self.deposit()
            elif user_input == "3":
                self.withdraw()
            elif user_input == "4":
                self.check___balance()
            elif user_input == "5":  # exit option
                print(self.exit())
                break  # Exit the loop
            else:
                print("----------------------Invalid option-----------------------")

    def create_pin(self):
        self.pin = input("Enter the pin: ")  
        print("Pin set successfully")

    def deposit(self):
        temp = input("Enter the pin: ")
        if self.pin == temp:
            try:
                money = float(input("Enter the Amount: "))  #float
                if money > 0:  # Validate positive amount
                    self.__balance += money
                    print("Deposit successful")
                else:
                    print("--------------------------Invalid Pin--------------------------")
            except ValueError:
                print("Please enter a valid number")
        else:
            print("--------------------------Invalid Pin--------------------------")

    def withdraw(self):
        temp = input("Enter the pin: ")
        if self.pin == temp:
            try:
                amount = float(input("Enter the Amount: "))  # input here
                if amount <= 0:
                    print("--------------------------Invalid Pin--------------------------")
                elif self.__balance < amount:
                    print("Insufficient balance")
                else:
                    self.__balance -= amount
                    print("Withdrawal successful")
            except ValueError:
                print("Please enter a valid number")
        else:
            print("--------------------------Invalid Pin--------------------------")

    def check_balance(self):
        temp = input("Enter the pin: ")
        if self.pin == temp:
            print(f"Your balance is {self.__balance:.2f}rs")  #output
        else:
            print("--------------------------Invalid Pin--------------------------")

    def exit(self):
        return "Thank You"

        
    
    