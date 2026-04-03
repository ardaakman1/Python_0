# OOP
class lamp:  # class is the blueprint for creating objects
    # __init__: The constructor. It runs automatically at the start
    # self: Refers to the specific object itself
    def __init__(self, colour):
        self.colour_of_light = colour  # stores the data
        self.condition = False  # stores the state (on/off)
    # Method: A function that defines an action
    def ac(self):
        self.condition = True  # change the state to on
        print(f"{self.colour_of_light} is turned on")

light = lamp("blue")  #creatinf an instance (real object from the class)
print(light.colour_of_light)
light.ac()  # calling a method an action