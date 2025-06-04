'''
This the basic calculator which can perform the task like addition, subtraction, multiplication and division of two variables
In this program wee will use the function to do the task
'''
def add(a,b):
    print(a+b,"is the answer")
def sub(a,b):
    print(a-b,"is the answer")
def mul(a,b):
    print(a*b,"is the answer")
def div(a,b):
    print(a/b,"is the answer")
is_running  = True
while is_running:
    print(" 1)Addition \n 2)Subtraction \n 3)Multiplication \n 4)DIvision \n 5)Quit")
    num = int(input("Which operation would you like to perform ???"))
    if num == 5:
        is_running = False
        break
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    if num == 1:
        add(a,b)
    elif num == 2:
        sub(a,b)
    elif num == 3:
        mul(a,b)
    elif num == 4:
        div(a,b)
    else:
        print("Please enter a valid number")

    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))


