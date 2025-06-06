from random import randint, choice, shuffle

def generate_password():
    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '-', '_', '=', '+',  '|', ';', ':', "'", '"', ',', '.', '/', '?', '~', '`']

    password_list = [choice(alphabets) for _ in range(randint(8, 10))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]

    shuffle(password_list)
    password = "".join(password_list)

    print("Your generated password is:", password)

while True:
    user_input = input("Do you want to generate a password? (y/n): ").lower()
    
    if user_input == 'y':
        generate_password()
    elif user_input == 'n':
        print("Thanks for visiting!")
        break
    else:
        print("Wrong input, please enter 'y' or 'n'.")
