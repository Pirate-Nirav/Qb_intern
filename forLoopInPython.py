'''
Python in for loops
A for loop is used for iterating over a sequence( That is either a list ,tuple , dictionary , set oor string)
This is less like the for keywords in other programming languages, and work more like an iterator method as found in other object-oriented languages.
With for loop we can execute a set of statements once for each item in a list, tuple, set etc.
'''

fruits = ['apple', 'orange', 'strawberry']
for fruit in fruits:
    print(fruit)

# Looping through the string
n = "how are you?"
for x in n:
    print(x)

# The break statement

for x in fruits:
    print(x)
    if x == "orange":
        break
print("\n")
# The continue statement

for x in fruits:
    if x == "orange":
        continue
    print(x)

'''
The range() function 
To loop through a set of code a specified numbers of times, we can use range() function,
The range() function returns a sequence of number by default from 0 and increment by 1 (by default)
range(start, stop, step)    
'''

for x in range(0,33,3):
    print(x)



# Nested Loop

adj = [1,2,3]
fruits = ['apple', 'orange', 'strawberry']

for i in adj:
    for j in fruits:
        print(i,j)

# Pass statement
# for loops cannot be empty but if there is some condition or i want to leave it as it is then I can use pass statement

for x in adj:
    pass