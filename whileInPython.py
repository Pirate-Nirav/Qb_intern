'''
Python Loops
Python has two primitive loop commands
* while loop
* for loop
The while Loop
With the while loop we can execute a set of statements as long as a condition is true
'''

i = 1
while i <= 5:
    print(i)
# With the break statement I can stop the loop when the condition is true
    if i == 3:
        break
    i += 1

# the continue statement can stop the current iteration and continue with the next

i = 0
while i <= 5:
    i += 1
    if i == 3:
        continue
    print(i)


# the else statement
# with the else statement we can run a block of code once when the condition is no longer true

i = 1
while i <= 5:
    print(i)
    i += 1
else:
    print("i is no longer than 6 ")
