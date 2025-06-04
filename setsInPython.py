# Python Sets
'''
Set
Sets are use to store multiple items in  single variables
Sets is one of the four built-in datatype in Python used to store collection of data
The set is collection which is unordered, unchangeable and unindexed
Set items are unchangeable, but you can remove items and add new items.
Sets are written with curly brackets {}
'''

thisset = {"apple", "banana", "cherry", "orange"}
print(thisset)

#Sets are unordered, so you cannot be sure in which order the items will appear.
'''
Set Items
Set items are unordered, unchangeable, and do not allow duplicate values.
Unordered
Unordered means that the items in a set do not have a defined order.
Set items can appear in a different order every time you use them, and cannot be referred to by index or key.
Unchangeable
Set items are unchangeable, meaning that we cannot change the items after the set has been created.
In sets duplicates are not allowed , sets cannot have two items with same value 
'''

thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

# True and 1 are considered as same value in the sets
# False and 0 are considered as same value in the sets
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)

thisset = {"apple", "banana", "cherry", False, True, 0}
print(thisset)

print(len(thisset))
print(type(thisset))

#It is also possible to use the set() constructor to make a set.
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

# loop through in the set

for x in thisset:
    print(x,"using loop")   

'''
Add items in the sets
to add the items use add() method 
'''
thisset.add("orange")
print(thisset)

tropical = {"raspberrey", "grapes"}
thisset.update(tropical)

print(thisset)

# to remove the item in the set there is remove() method
# to remove the item in the  set there is discard() method
# there is clear() method to clear all the items of the set
# We can also use the pop() method but that will remove the random item from the set

thisset.discard("orange") # if there is no item in the set it will not raise an error
thisset.remove("raspberrey")# if there is no item in the set it will raise an error
print(thisset)

# loop items
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

'''
Join sets
The union() method and update() method are use to join all the items of the set 
The intersection() method keeps only the DUPLICATES
The difference() method keeps the items from the first set that are not in the other set(s).
The symmetric_difference() method keeps all items EXCEPT the duplicates.

You can use the | operator instead of the union() method, and you will get the same result.
'''
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

set3 = set1 | set2
print(set3)
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
myset =  set1.union(set2, set3, set4)
print(myset)

set1.update(set2)
print(set1)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2)
print(set3)


'''
Method	     Shortcut	Description
add()	 	            Adds an element to the set
clear()	 	            Removes all the elements from the set
copy()	 	            Returns a copy of the set
difference()	-	    Returns a set containing the difference between two or more sets
difference_update()	-=	Removes the items in this set that are also included in another, specified set
discard()	 	        Remove the specified item
intersection()	&	    Returns a set, that is the intersection of two other sets
intersection_update()	&=	Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	 	    Returns whether two sets have a intersection or not
issubset()      <=      Returns whether another set contains this set or not
            	<	Returns whether all items in this set is present in other, specified set(s)
issuperset()	>=	Returns whether this set contains another set or not
 	            >	Returns whether all items in other, specified set(s) is present in this set
pop()	 	            Removes an element from the set
remove()	 	        Removes the specified element
symmetric_difference()	^	Returns a set with the symmetric differences of two sets
symmetric_difference_update()	^=	Inserts the symmetric differences from this set and another
union()	|	            Return a set containing the union of sets
update()	|=	        Update the set with the union of this set and others

'''