'''
Develop a number guessing game where the program selects a random
number, and the user tries to guess it within a limited number of attempts.

Let's break down into steps
Step1 : We will use the random number generator to get the number
Steps2 : Chances to guess the number will be limited like 5 or 7 , it will decrease every time they guess
Step3 : Using the condition to get the exact number
Step4 : If the user guesses the right number the game is over
'''

import random
a = random.randint(1,20)
# print(a)
is_true = True
count = 5
while is_true and count > 0:
    guess = int(input("Guess a number between 1 and 20: "))
    if guess == a:
        print("Hurrah , You have guessed correctly")
        is_true = False
        break
    elif guess > a:
        print("Guess higher")
        print(f"You have {count} tries left ")
        count -= 1
    elif guess < a:
        print("Guess lower")
        print(f"You have {count} tries left ")
        count -= 1
    else:
        print("Please try again, you lost one chance...")
        print(f"You have {count} tries left ")
        count -= 1