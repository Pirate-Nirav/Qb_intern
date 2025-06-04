'''
Dictionary
Dictionaries are used to store data values in "key:value" pairs.
A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1969
}
print(thisdict)
print(thisdict["brand"])

'''
Ordered or Unordered?
When we say that dictionaries are ordered, it means that the items have a defined order, and that order will not change.
Unordered means that the items do not have a defined order, you cannot refer to an item by using an index.
Changeable
Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.
Duplicates Not Allowed
Dictionaries cannot have two items with the same key:
'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)

print(len(thisdict))

'''
Dictionary Items - Data Types
The values in dictionary items can be of any data type
'''
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
x = thisdict["brand"]
print(x)
print(thisdict)
print(type(thisdict))

# get keys , this key() method will return a list of all the keys in the dictionary
x = thisdict.keys()
print(x)
thisdict["color"] = "white"
print(thisdict)

#get values
# The values() method will return a list of all the values in the dictionary
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.values()
print(x) #before the change
car["year"] = 2020
print(x) #after the change

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.values()
print(x) #before the change
car["color"] = "red"
print(x) #after the change

'''
Get Items 
The items() method will return each item in a dictionary
'''
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.items()
print(x) #before the change
car["year"] = 2020
print(x) #after the change

if "model" in car:
    print("Yes, it is there ")

# change Values
# You can change the value of a specific item by referring to its key name:

thisdict["year"] = 1999
print(thisdict)

'''
Update dictionary 
The update() method will update the dictionary with the items from the given argument
The argument must be a dictionary, or an iterable object with key : value pairs 
'''
car.update({"year":2004})
print(car)

car["door"] = 5
print(car)

#Removing items
# There are several methods to remove items  from a dictionary
# pop() method removes the item with the specified key name

car.pop("model")
print(car)

# The popitem() method removes the last inserted item
thisdict = {
    "brand":"Toyota",
    "model":"Camery",
    "year": 2004
}
thisdict.popitem() # the year will be removed because it is inserted at last
print(thisdict)

# The del keywords removes the item with the specified key name
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)

# the clear () method will clear the dictionary after using the clear() method
thisdict.clear()
print(thisdict)

'''
Copy a Dictionaries 
You can copy a dictionary simply by typing dict1 = dict2, because : dict2 will be only reference to dict1 
'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1968
}
mydict = thisdict.copy()
print(mydict)

mydict = dict(thisdict)
print(mydict)

'''
Nested dictionary 
A dictionary can contain dictionaries this is called nested dictionary
'''

myfamily = {
    "child1":{
    "name" : "John",
    "age": 20
},
"child2":{
    "name" : "Abraham",
    "age" : 21
}
}
print(myfamily)
print(myfamily["child2"]["age"])

child3  = {
    "name" : "Joe",
    "age": 22
}
myfamily.update(child3)
print(myfamily)

'''
Methods in dictionaries
clear()	        Removes all the elements from the dictionary
copy()	        Returns a copy of the dictionary
fromkeys()	    Returns a dictionary with the specified keys and value
get()	        Returns the value of the specified key
items()	        Returns a list containing a tuple for each key value pair
keys()	        Returns a list containing the dictionary's keys
pop()	        Removes the element with the specified key
popitem()	    Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	    Updates the dictionary with the specified key-value pairs
values()	    Returns a list of all the values in the dictionary


'''