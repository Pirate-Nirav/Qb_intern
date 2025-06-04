'''
Python Classes/Objects
Python is object oriented programming language with its properties and methods
A Class is like an object constructor, or a blueprint for creating objects
To create a class use keyword 'class'
Create an object named p1, and print the value of x
p1 = MyClass()
print(p1.x)
The __init__() function always executed when the class is initiated
Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created
'''

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

'''
The __str__() function controls what should be returned when the object is represented as a string 
'''
class Person1:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is ({self.age})years old"

p2 = Person1("John", 36)
print(p2)

'''
The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class
It doesn't have to be named self, we can call it when ever you like but it had to be first parameter of any function in the class
'''

class Person2:
    def __init__(thisisme, name, age):
        thisisme.name = name
        thisisme.age = age
    def myfunc(aaa):
        print("Hello my name is " + aaa.name)

pp = Person2("John", 36)
print(pp.myfunc())