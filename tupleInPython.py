'''
Tuple are used to store multiple items in a single variable
Tuple are one of the four built in datatypes in Python used to store collection of data , the other three are list, set, dictionary all with different quality and usage
The tuple is a collection which is ordered and unchangeable (immutable)
The tuples are written with the round brackets tuple()
The items are ordered , unchangeable and allow duplicates values
When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.
'''
thistuple = ("apple", "banana", "cherry", "orange")
print(thistuple)
# The check the length of the tuple use len() method
print(len(thistuple))
# To check the type use type() method
print(type(thistuple))

# Access the tuple
print(thistuple[1])
'''
Negative Indexing
Negative indexing means start from the end.
-1 refers to the last item, -2 refers to the second last item etc.'''

print(thistuple[-1])

'''
We can specifiy the range of the tuple using the slicing in the tuple by giving it starting and the ending value 
the return value will be a new tuple with the specified items
'''
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

# range of negative index

print(thistuple[-4:-1],"this is done with the negative index")

# Update the list
# For updating the tuple we have to convert the tuple into list then update it and then again we have to convert it to the tuple

thislist = list(thistuple)# converting tuple into list
thislist[1]="grape"
thistuple = tuple(thislist)# converting list into tuple
print(thistuple)

# Add tuple to a tuple
y = ("dragon",)
thistuple  += y
print(thistuple)

# Deleting the tuple completely with the del keyword

del y
#print(y)  this will give error 'NameError' because we have deleted the y

'''
Unpack the tuple    
When we create a tuple, we normally assign values to it. This is called "packing" a tuple
But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking"
Using Asterisk*
If the number of variables is less than the number of values, you can add an * to the variable name and the values will 
be assigned to the variable as a list
'''
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

# Using Asterisk
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)

'''
Loop through a tuple 
You can loop through the tuple items by using a for loop.
'''
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x)

for i in range(len(thistuple)):
    print(thistuple[i],"with range")