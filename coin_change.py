def coin_change(amount):
    coins = 0
    while amount > 0:
        if amount >= 10:
            coins += 1
            amount -= 10

        elif amount >= 5:
            coins += 1
            amount -= 5

        elif amount >= 2:
            coins += 1
            amount -= 2

        elif amount >= 1:
            coins += 1
            amount -= 1
        else :
            print("Enter ritght amount")

    return f"Total coins will be {coins}"

x = int(input("Enter the amount: "))
print(coin_change(x))
        
