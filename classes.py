class Parent:
    def __init__(self,namee,age,salary):
        self.name = namee
        self._age = age
        self.__salary = salary

    def get_salary(self):
        print(self.__salary)

    def set_salary(self):
        s = input("salary:")
        self.__salary = s
        print(self.__salary)

obj = Parent("Nirav",10,0)
# print(obj.__salary)
print(obj.salary)
obj.get_salary()
obj.set_salary()
