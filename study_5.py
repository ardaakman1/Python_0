# if you wish to define main nonetheless, you must very end of the code have 
# if __name__ == "__main__":
#     main()
def square(x):
    return x ** 2  # this is the exponentiation operator or x * x
# OOP
# properties + metods = class
# property is variable and metod is the special that can only be used with that variable 
class Student():
    def __init__(self, name, id):  # we should define this everytime when we are defining an object
        self.name = name
        self.id = id 
        # self is the jane itself
        
    def changeID(self, id):
        self.id = id
    
    def print(self):
        print(f"{self.name} - {self.id}")

jane = Student("jane", 10)
jane.print()
jane.changeID(11)
jane.print()