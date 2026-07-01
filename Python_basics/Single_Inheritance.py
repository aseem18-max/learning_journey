class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    def make_sound(self):
        print("Sound made by the animal")

class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species = "Dog")
        self.breed = breed
    def make_sound(self):
        print("Bark!")

class Cat(Animal):
    def __init__(self, name, species, color):
        Animal.__init__(self, name, species)
        self.color = color
        self.species = self.species
    def details(self):
        print(f"The color of the Cat is {self.color}")

d = Dog("Dog", "Dobberman")
d.make_sound()

a = Animal("Dog", "Dog")
a.make_sound()

c = Cat("Miouth", "cat", "white")
c.details()