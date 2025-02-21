class Vehicle:
    def general_usage(self):
        print("general usage: transportation")

class Car(Vehicle):
    def __init__(self):
        print("I am car")
        self.wheels=4 
        self.has_roof=True
    
    def specific_usage(self):
        print("specific usage: trip with family, go to office")

class Bike(Vehicle):
    def __init__(self):
        print("I'm Bike")
        self.wheels=2 
        self.has_roof=False 
    
    def specific_usage(self):
        print("specific usage: riding, racing.")

c=Car()
# c.general_usage()
# c.specific_usage()


b=Bike()
# b.general_usage()
# b.specific_usage() 

print(isinstance(c,Car)) # True 
print(isinstance(c,Bike)) # False 

print(issubclass(Car,Vehicle)) # True 
print(issubclass(Car,Bike)) # False