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

""" Example of Multiple Inheritance: a class can inherit from more than one parent class. 
In this example, the FlyingFish class inherits from both Fish and Bird classes,
allowing it to have characteristics of both."""


class Fish:  # Parent class 1
    def swim(self):
        return "The fish is swimming"


class Bird:  # Parent class 2
    def fly(self):
        return "I can fly!"


class FlyingFish(Fish, Bird):  # Child class inheriting from both Fish and Bird
    def __init__(self, name):
        self.name = name

    def sound(self):
        return f"{self.name} says blub!"


nemo = FlyingFish("Nemo")
print(nemo.swim())  # The fish is swimming
print(nemo.fly())  # I can fly!
print(nemo.sound())  # Nemo says blub!
