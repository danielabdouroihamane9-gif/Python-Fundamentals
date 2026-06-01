# Polymorphism: allows methods in different classes to share the same name but perform different tasks.
#               You call the same method name on different objects, and each responds in its own way.

""" "Example of Polymorphism: The speak method is defined in both the Cat and Bird classes,
but it behaves differently based on the object calling it."""


class Cat:  # Class 1
    def speak(self):  # Method with the same name in different classes
        return "A cat meow"


class Bird:  # Class 2
    def speak(self):  # Method with the same name in different classes
        return "A bird tweet"


class Monkey:  # Class 3
    def speak(self):  # Method with the same name in different classes
        return "A monkey ooh ooh aah aah ooh ooh aah aah"


def animal_sound(
    animal,
):  # Function that takes an object as an argument and calls the speak method
    print(animal.speak())


animal_sound(Cat())  # Output: A cat meow
animal_sound(Bird())  # Output: A bird tweet
animal_sound(Monkey())  # Output: A monkey ooh ooh aah aah ooh ooh aah aah
