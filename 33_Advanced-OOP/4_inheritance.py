# Inheritance: It allows a new class (called child or subclass) to inherit attributes and methods from an existing class (called parent or superclass).
#              This promotes code reusability and establishes a natural hierarchical relationship between classes.

"""Example of a single inheritance: The Dog class inherits from the Animal class, allowing it to use the sound method defined in the Animal class."""


class Animal:  # Parent class (superclass)
    def __init__(self, name):
        self.name = name

    def sound(self):
        return f"{self.name} makes a sound"


class Dog(Animal):  # Dog class inherits from Animal class
    bark = "woof! woof!! woof!!!"


jack = Dog("Jack")
print(jack.sound())  # Jack makes a sound
print(jack.bark)  # woof! woof!! woof!!!


# * Example of Inheritance with Method Overriding:
class Cat(Animal):
    def sound(self):
        return f"{self.name} says meow!"


whiskers = Cat("Whiskers")
print(whiskers.sound())  # Whiskers says meow!


# * Using the super() function to call the parent class's method:
class Bird(Animal):
    def __init__(self, name, species):
        super().__init__(name)  # Call the parent class's __init__ method
        self.species = species

    def sound(self):
        return f"{self.name} the {self.species} chirps!"  # Override the sound method


tweety = Bird("Tweety", "Canary")
print(tweety.sound())  # Tweety the Canary chirps!
