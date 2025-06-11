from cowmoo import cow,monkey,wolf
user_input = int(input("What is the time?? Write in 24 hr:"))
if user_input > 0 and user_input <=12:
    print(cow)
elif user_input > 12 and user_input<=18:
    print(monkey)
elif user_input > 18 and user_input<=24:
    print(wolf)
else:
    print("Enter correct number..... between 1-24")