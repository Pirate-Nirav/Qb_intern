'''
class Customer:
    
    def __init__(self,name,gender):
        self.name = name
        self.gender = gender
    
def greet(customer):
    if customer.gender == "Male":
        print("Hello", customer.name,"sir")
    else:
        print("Hello", customer.name, "madam")
cust = Customer("Nirav", "Male")

greet(cust)

class Customer:
    def __init__(self,name):
        self.name = name
        
def greet(customer):
    print(id(customer))
    customer.name = "Nirav"
    print(customer.name)
    
cust = Customer("Thapa")
print(id(cust))

greet(cust)
print(cust.name)
'''

class Customer:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def intro(self):
        print(f"Hello {self.name}, your age is {self.age}")
        
c1 = Customer("Nirav", 19)
c2 = Customer("Hello", 18)
c3 = Customer("Thapa", 20)
list=[c1,c2,c3]
for i in list:
    print(i.name,i.age)