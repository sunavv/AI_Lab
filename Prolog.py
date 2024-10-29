class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, "Dog")

buddy = Dog("Buddy")
print(buddy.name, buddy.species)


