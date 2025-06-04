"""
There are mainly three types in the polymorphism that is :- Method overriding , method overloading , operator overloading  

# Here we are doing the method overriding in the below program as we know that the base class can use the parent class method, constructor and variable 
# As we can see that the B is the child class of the A class it can over ride the method with the same name so that's the reason the output is 
# "This is me class B"
class A:
    def show(self):
        print("This is me class A") 
    

class B(A):
    def show(self):
        print("This is me class B") 
    
obj = B()
obj.show()


# Using the super method to over the problem if you want to use the parent method instead of the child method 

class A:
    def show(self):
        print("This is me class A") 
    

class B(A):
    def show(self):
        super().show()
        print("This is me class B") 
    
obj = B()
obj.show()
'''
This is me class A
This is me class B
this is the outpt because the super will call the method of parent class  
'''

 # This is how the super method works inside the class
class Product:
    counter = 1
    def __init__(self,company,price,pid):
        self.company = company
        self.price = price 
        self.pid = Product.counter
        Product.counter += 1
         
    def show(self):
        print("This is me class A") 
    

class Phone(Product):
    def __init__(self,company, price, pid, ram, os):
        super().__init__(company, price, pid)
        self.ram = ram 
        self.os = os

    def bill(self):
        print(f" Product id is {self.pid}.Your Phone is of {self.company}. Price is {self.price}. Ram is {self.ram}. Os is {self.os}") 
    
obj = Phone("Samsung",20000,1,"8gb","Knox")
obj.bill()


class MyClass:
    def __init__(self, value):
        self.instance_variable = value

    @staticmethod
    def static_method(obj):
        if isinstance(obj, MyClass):
           print(f"Accessing instance variable from the static method: {obj.instance_variable}")
        else:
          print("Invalid object passed to static method")


# Creating an instance
my_object = MyClass(10)

# Calling the static method with an instance
MyClass.static_method(my_object)  # Output: Accessing instance variable: 10

# Calling the static method without an instance will fail
MyClass.static_method("Not an instance")  # Output: Invalid object passed to static method

from abc import ABC, abstractmethod

# Define an abstract class
class Animal(ABC):
    
    @abstractmethod
    def sound(self):
        pass  # This is an abstract method, no implementation here.

# Concrete subclass of Animal
class Dog(Animal):
    
    def sound(self):
        return "Dog Bark"  # Providing the implementation of the abstract method

# Create an instance of Dog
dog = Dog()
print(dog.sound())  # Output: Bark
"""

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

p1 = Point(1, 2)
p2 = Point(2, 3)
print(p1 + p2)  # Output: (3, 5)