'''
Python Match
The match statement is used to perform different actions based on different conditions
The Python Match Statement:
Instead of writing many if...else statements, I can use match statement
The match statement selects one of many code block to be executed

match expression:
    case x:
        code block
    case y:
        code block
    case _:     Use this character _ as the last case value if you want a code block to be executed when other do not matches
        code block

from traceback import print_exc


if_true = True
while if_true:
    day = int(input("Enter the day of the week: "))
    match day:
        case 0:
            if_true = False
        case 1:
            print("Monday")
        case 2:
            print("Tuesday")
        case 3:
            print("Wednesday")
        case 4:
            print("Thursday")
        case 5:
            print("Friday")
        case 6:
            print("Saturday")
        case 7:
            print("Sunday")
        case _:
            print("Enter a valid input")
    print("ENTER 0 TO EXIT")

if if_true == False:
    print("Exiting...")
    '''

day = 4
match day:
  case 1 | 2 | 3 | 4 | 5:
    print("Today is a weekday")
  case 6 | 7:
    print("I love weekends!")

month = 5
day = 4
match day:
  case 1 | 2 | 3 | 4 | 5 if month == 4:
    print("A weekday in April")
  case 1 | 2 | 3 | 4 | 5 if month == 5:
    print("A weekday in May")
  case _:
    print("No match")
