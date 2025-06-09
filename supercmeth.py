class Parent:
    def show(self):
        print("This is parent")
class Parent2:
    def show(self):
        print("This is parent 2")

class child(Parent2,Parent):
    pass
        

chil = child()
chil.show()