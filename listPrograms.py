#Python program to interchange first and last elements in a list
list1 = [10,6,-8,-7,0,5,4,8,99,102,57,0,5,99]
'''
Interchanging first and last element in a list means [1,2,3,4,5,6] it will become [6,2,3,4,5,1]
so the first value will go to at the place of last item


print("Before swapping the first and last element",list1)
if len(list1) >= 2:
    list1[0], list1[-1] = list1[0], list1[-1]
elif len(list1) == 1:
    print("There is only one item ")
else:
    print("There is no item in the list ")
print("After swapping the first and last element",list1)


### Python program to swap two elements in a list
How can we do it?
First of all we have to take two number from the user
then find it index so that we can swap them

print(list1," this is the list before swapping the two elements")
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

if a in list1 and b in list1:
    i = list1.index(a)
    j = list1.index(b)
    list1[i], list1[j] = list1[j], list1[i]
    print("After swapping the first and last element",list1)
else:
    print("Element not in the list")

###Python | Reversing a List
list1.reverse()
print(list1)

#Another way is without using the method using for loop with the temp
a,b = 0 ,len(list1)-1
for i in range(len(list1)):
    list1[a],list1[b] = list1[b],list1[a]
    a += 1
    b -= 1
print("Reversed list is", list1)

# Using while loop

while a < len(list1):
    list1[a],list1[b] = list1[b],list1[a]
    a += 1
    b -= 1
print("After reversing list ",list1)

### Python program to find sum of elements in list	
First we can use the sum() method to get the total sum of the list
Another way is using for loop  

print(list1)
list2 = sum(list1)
print(list2)
# Let's do using the for loop
total  =0
for i in list1:
    total += i
print(f"The total sum of the list is {total} and the list is {list1}.")

### Python | Multiply all numbers in the list
First way is we can import the module name math and in that we can use prod() method to get the product of the list

import math
a = math.prod(list1)
print(a)

# Second way is using the loop

total = 1
for i in list1:
    total *= i
print(f"The product of the list is {total} and the list is {list1}.")
###Python program to find smallest number in a list  
Using the min() method we can get the smallest number from the list

a = min(list1)
print(a)

#Other method is from using sort method and using the index

list1.sort()
print(list1[0],"Using sort method and the index")

same like this  

# there is one another way which can be done with the nested for loop
def minimum(l):
    for i in range(len(list1)):
        for j in range(len(list1)):
            if list1[i] < list1[j]:
                list1[j], list1[j] = list1[j], list1[i]
    return list1[0]

print(minimum(list1))

 There will be two input given by the user
 Input :
 a = 50
 list = [20,30,50]

  The total of the list is 100 now have to make a list in which we will have the addition of list1 and the list[i] % of the a
  means the 20 % of 50 is 10 so we have to add the 10 + 20 = 30 so in the new list the output will be the 30 like this we will fetch the other value
 output : [30,45,75]


def custom(a, list):
    total = sum(list)
    list2=[]
    for i in range(len(list)):
        b = (list[i] / 100) * total
        b = b + (list[i] / 100) * a
        list2.append(b)
    print(list2)
list1 = [20,30,50]
print(custom(50, list1))



# Python program to find N largest element from a list
def n_largest(n : int, list1):
    list1.sort(reverse=True)
    return list1[:n]

print(list1)
n = int(input("Enter the number: "))
print("The", n, "largest elements are:", n_largest(n, list1))

# Python program to print even numbers in a list

def evenInList(list1):
    for i in range(len(list1)):
        if list1[i] % 2 == 0:
            print(list1[i])

print(evenInList(list1))

# Python program to print odd numbers in a List
def evenInOdd(list1):
    for i in range(len(list1)):
        if list1[i] % 2 == 1:
            print(list1[i])

print(evenInOdd(list1))


# Python program to print positive numbers in a list

def positiveNumberInList(list1):
    list1.sort()
    for i in range(len(list1)):
        if list1[i] >= 0:
            print(list1[i])

print(positiveNumberInList(list1))

# Python program to print negative numbers in a list
def positiveNumberInList(list1):
    list1.sort(reverse=True)
    for i in range(len(list1)):
        if list1[i] <= 0:
            print(list1[i])

print(positiveNumberInList(list1))

# Remove multiple elements from a list in Python

def removeMultiple(list1, *args):
    # Iterate over each element to remove
    for element in args:
        while element in list1:  # Continue removing while the element exists
            list1.remove(element)
    return list1
print(list1)
print("After removing the elements:")
print(removeMultiple(list1, 99, 0, 6))

# Python | Count occurrences of an element in a list

def occurances(n,list1):
    repeat = 0
    for item in list1:
        if item == n:
            repeat += 1
    return f"{n} occurs {repeat} times"

print(occurances(5,list1))

# Break a list into chunks of size N in Python

def chunk_list(lst, chunk_size):
    return [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]

print(list1)
print(chunk_list(list1,4))
'''