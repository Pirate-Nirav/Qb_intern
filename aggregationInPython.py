"""
This type of relation is known as aggregation reltionship this have "has-a" relation between two class . One class make the other class do the things
and the object of other class is sent as the arguments while make the onject of the main class 
"""

class Customer:
    def __init__(self,name,age,add):
        self.name = name
        self.age = age
        self.add = add
        
    def showdetails(self):
        print(f"Hello {self.name} your age is {self.age}\nCity is {self.add.city} and state is {self.add.state}." )
        
    def edit_profile(self, new_name,new_city, new_pincode, new_state):
        self.name = new_name
        self.add.change_address(new_city,new_pincode,new_state)
        
        
class Address:
    def __init__(self, city, pincode, state ):
        self.city = city
        self.pincode =  pincode
        self.state = state
    
    def change_address(self, new_city,new_pincode,new_state ):
        self.city = new_city
        self.pincode =  new_pincode
        self.state = new_state
        
add =  Address("Karnavati",380051,"Gujarat")
cust =  Customer("Nirav", 20,add) # sending 'add' object as a argument
print("------------------------Before editing---------------------------")
cust.showdetails()
print("------------------------After editing-----------------------------")
cust.edit_profile("Thapa","Ahmedabad",380005,"Gujarat")
cust.showdetails()