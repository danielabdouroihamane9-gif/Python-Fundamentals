"""
================================================================================
POLYMORPHISM - Concept Explanation:
================================================================================
Polymorphism allows methods in different classes to share the same name but
perform different tasks based on the object calling them. This enables you to
write code that works with objects of different types using the same interface.

Key Benefit: Write flexible and reusable code without needing to know the exact
type of the object at runtime.
================================================================================
"""


# ============================================================================
# Class 1: Cat - Defines a Cat animal with its own speak() behavior
# ============================================================================
class Cat:
    def speak(self):
        """
        Implements the speak() method for Cat class.
        When this method is called on a Cat object, it returns the sound a cat makes.
        """
        return "A cat meow"


# ============================================================================
# Class 2: Bird - Defines a Bird animal with its own speak() behavior
# ============================================================================
class Bird:
    def speak(self):
        """
        Implements the speak() method for Bird class.
        When this method is called on a Bird object, it returns the sound a bird makes.
        """
        return "A bird tweet"


# ============================================================================
# Class 3: Monkey - Defines a Monkey animal with its own speak() behavior
# ============================================================================
class Monkey:
    def speak(self):
        """
        Implements the speak() method for Monkey class.
        When this method is called on a Monkey object, it returns the sound a monkey makes.
        """
        return "A monkey ooh ooh aah aah ooh ooh aah aah"


# ============================================================================
# Polymorphic Function: Works with any object that has a speak() method
# ============================================================================
def animal_sound(animal):
    """
    This is a polymorphic function. It accepts ANY object as a parameter,
    as long as that object has a speak() method defined.

    Instead of writing separate functions for each animal (cat_sound(),
    bird_sound(), etc.), this single function works with all animals.

    The actual speak() method called depends on the type of object passed in.
    This is polymorphism in action!
    """
    print(animal.speak())


# ============================================================================
# DEMONSTRATION: Calling the polymorphic function with different objects
# ============================================================================

# Each call passes a different animal object to animal_sound()
# Even though we call the same function, different speak() methods execute
animal_sound(Cat())  # Calls Cat's speak() method → Output: A cat meow
animal_sound(Bird())  # Calls Bird's speak() method → Output: A bird tweet
animal_sound(
    Monkey()
)  # Calls Monkey's speak() method → Output: A monkey ooh ooh aah aah ooh ooh aah aah

# ============================================================================
# WHY IS THIS USEFUL?
# ============================================================================
# • You can easily add new animal classes without modifying animal_sound()
# • The function doesn't need to check what type of animal it is
# • If you have a list of different animals, you can call animal_sound()
#   on each one without needing separate logic for each animal type

# ============================================================================
# Example 2: Polymorphism with vehicle objects that share describe()
# ============================================================================
# The following classes both include a describe() method.
# The print_description() function can accept either object type and invoke
# the same method name, demonstrating polymorphic behavior.


class Car:
    def __init__(self, make, model):
        """Initialize a Car object with make and model."""
        self.make = make
        self.model = model

    def describe(self):
        """Return a descriptive string for this Car."""
        return f"This is a {self.make} {self.model} car."


class Bike:
    def __init__(self, make, model):
        """Initialize a Bike object with make and model."""
        self.make = make
        self.model = model

    def describe(self):
        """Return a descriptive string for this Bike."""
        return f"This is a {self.make} {self.model} bike."


def print_description(vehicle):
    """Print the result of calling describe() on the given vehicle."""
    print(vehicle.describe())


def main():
    """Run demonstration code when the module is executed directly."""
    # Demonstrate polymorphism with vehicle objects.
    car_example = Car("Toyota", "Camry")
    bike_example = Bike("Giant", "Escape")

    print_description(car_example)  # Output: This is a Toyota Camry car.
    print_description(bike_example)  # Output: This is a Giant Escape bike.


if __name__ == "__main__":
    main()
