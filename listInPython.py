# List items are ordered, changeable and allows duplicates in the list

# Ordered
# When we say that lists are ordered, it means that the items have a defined order, and that order will not change.
# If you add new items to a list, the new items will be placed at the end of the list.
'''
List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.

'''
list1 = ["apple", "banana", "pineapple"]
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

print(list1[::-1])
print(thislist[1:6])

# Checking if the item exists in the list1
if "apple" in list1:
    print("Yes, it is there")

# Changing the list items
thislist[1] = "dragonfruit"#['apple', 'dragonfruit', 'cherry', 'orange', 'kiwi', 'melon', 'mango']
print(thislist)

# Change a range of item value
thislist[1:3] = ["blackcurrant", "watermelon"]#['apple', 'blackcurrant', 'watermelon', 'orange', 'kiwi', 'melon', 'mango']
print(thislist)

'''
To insert a new list item, without replacing any of the existing value, we can use the insert() method to insert a new list item.
In this method we have user insert() with the index and the value
~Another one is append() in which we have to give the value and that item will be inserted at the last position of the list
~ Extend this method is written as extend(). one list is extended with the other list we can add multiple values or the list we wanted to extend in the first list 
'''
#Insert Items
thislist.insert(2, "Guava")#['apple', 'blackcurrant', 'Guava', 'watermelon', 'orange', 'kiwi', 'melon', 'mango']
print(thislist)

#Append Items
#To add an item to the end of the list, use the append() method:
list1.append("Grapes")# ['apple', 'banana', 'pineapple', 'Grapes']
print(list1)

# Extend method in the list:- To append element from another list
list1.extend(thislist)
print(list1)#['apple', 'banana', 'pineapple', 'Grapes', 'apple', 'blackcurrant', 'Guava', 'watermelon', 'orange', 'kiwi', 'melon', 'mango']

'''
Python remove list item
There are three methods to remove the item from the list which are remove(), pop(), and del keyword 
~ Remove method: The remove() method removes the specified item from the list, if there is any duplicate values then it will remove the first one  .
~ Pop method: The pop() method removes the specified item from the list if the index number is given else it will remove the last item from the list
~ Del method: The del keyword remove the entire list and also removes the specified index.
~ Clear method: The clear method clear the list without deleting the list
'''

#Remove method
thislist = ["apple", "banana", "banana","cherry"]
thislist.remove("banana")
print(thislist)

#Pop method with specified index
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

#Pop method with no index
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

#del method with specified index
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

#del method to remove entire list
thislist = ["apple", "banana", "cherry"]
del thislist

# clear() method
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

# Loop in the list
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

for i in range(len(thislist)):
  print(thislist[i])

thislist = ["apple1", "banana1", "cherry1"]
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i+1

[print(x) for x in thislist]


'''
List Comprehension
List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

Example:

Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.

Without list comprehension you will have to write a for statement with a conditional test inside:
1. List Comprehension Structure
A list comprehension has the following general syntax:
[expression for item in iterable if condition]
'''
fruits = ["apple", "banana", "cherry", "pineapple", "orange", "kiwi", "melon", "mango"]
new_fruits = []
for fruit in fruits:
    if 'a' in fruit:
        new_fruits.append(fruit)

print(new_fruits)

'''
The Syntax
newlist = [expression for item in iterable if condition == True]
The return value is a new list, leaving the old list unchanged.

Condition
The condition is like a filter that only accepts the items that evaluate to True.
Example
Only accept items that are not "apple":
'''
new_fruits = [x for x in fruits if x != 'apple']
print(new_fruits)
new_fruits = [x for x in range(10) if x < 5]
print(new_fruits)
new_fruits = [x.upper() for x in fruits]
print(new_fruits)
new_fruits = [x if x!= "banana" else "orange" for x in fruits]
print(new_fruits)

'''
Sort the list
Sort list AlphaNumerically 
The list have the sort() method that will sort the list alphanumerically, ascending by default. 
By default the sort() method is case sensitive, resulting all the capital letters are being sorted before lower case
The reverse() method will reverse the list without sorting it 
'''
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

# Sort descending the list:- listname.sort(reverse = True) is required to print it reverse
thislist = ["orange", "Mango", "kiwi", "Pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

'''
Copy a List
You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.

Use the copy() method
You can use the built-in List method copy() to copy a list.
'''

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist,"This is mylist")

# Another way to copy the list is the list() in built method
mylist = list(thislist)
print(mylist," in this i have used list() method")

# We can copy a list using slicing operator :
mylist = thislist[:]
print(mylist,"in this i have used slicing operator")

'''
Join Two Lists
There are several ways to join, or concatenate, two or more lists in Python.

One of the easiest ways are by using the + operator.\
'''
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

# Another way to join two lists is by appending all the items from list2 to list1 one by one

for x in list2:
    list1.append(x)

print(list1," this is list one ")

# Or we can use extend() method to join two list

list1.extend(list2)
print(list1, " this is done with extend() method")

'''
List Methods
Python has a set of built-in methods that you can use on lists.

    Method	    Description
    append()	Adds an element at the end of the list
    clear()	    Removes all the elements from the list
    copy()	    Returns a copy of the list
    count()	    Returns the number of elements with the specified value
    extend()	Add the elements of a list (or any iterable), to the end of the current list
    index()	    Returns the index of the first element with the specified value
    insert()	Adds an element at the specified position
    pop()	    Removes the element at the specified position
    remove()	Removes the item with the specified value
    reverse()	Reverses the order of the list
    sort()	    Sorts the list
'''