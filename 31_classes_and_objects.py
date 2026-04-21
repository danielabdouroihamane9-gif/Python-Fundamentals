#31 CLASSES AND OBJECTS: They work hand in hand to organize and manage data.
#           Class: Is the template or blueprint of an Object
#          Object: Is what is created using that blueprint.
#          They are fundamental concepts in OOP (Object-Oriented Programming) and are used to create reusable and modular code.
#          A class defines the properties (attributes) and behaviors (methods) that the objects created from the class will have.  
#          An object is an instance of a class, and it can have its own unique values for the attributes defined in the class.
#          One class can create multiple objects, and each object can have different values for the attributes defined in the class.

class Dog:                          # Define a class named Dog
    def __init__(self, name, age):  # The __init__ method is a special method that is called when an object is created from the class. It initializes the attributes of the object.
        self.name = name            # Atribute: name, age.  (self is a reference to the current instance of the class, and it is used to access the attributes and methods of the class.)
        self.age = age

    def bark(self):                 # Method: bark.  (A function defined inside a class is called a method. It defines the behavior of the objects created from the class.)
        print(f"{self.name.upper()} says woof woof! I'm {self.age} years old!")

# Create an object of the Dog class
my_dog1 = Dog("Buddy", 3)  
my_dog2 = Dog("Max", 5)

# Call the bark method for each dog
my_dog1.bark()  # Output: BUDDY says woof woof! I'm 3 years old!
my_dog2.bark()  # Output: MAX says woof woof! I'm 5 years old!
