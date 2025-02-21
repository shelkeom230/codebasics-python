class Animal:
    def sound(self):
        return "some generic sound"

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"

animals=[Dog(),Cat(),Animal()]

for animal in animals:
    print(animal.sound())
