"""
Python inheritance
Inheritance allow us to define a class that inherits all the methods and properties from another class.
Parent Class is the class being inherited from, also called base class
Child class is the class that inherits from the base class , also called as derived class.
"""
class Person:
    def __init__(self, fname, lname):
        self.fname  = fname
        self.lname = lname

    def myfunc(self):
        print(self.fname, self.lname)
'''
When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.

Note: The child's __init__() function overrides the inheritance of the parent's __init__() function.

To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:
'''
class child(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)

x = child("John", "Doe")
x.myfunc()

class Parent:
    def show(self):
        print("This is the parent class")

class Child(Parent):
    def show(self):
        super().show()
        print("This is the child class")

x = Child()
x.show()