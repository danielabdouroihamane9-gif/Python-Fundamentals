#31 CLASSES AND OBJECTS: They work hand in hand to organize and manage data.
#          Class: Is the template or blueprint of an Object
#          A class defines the properties (attributes) and behaviors (methods) that the objects created from the class will have.  
#          Object: is an instance of a class, and it can have its own unique values for the attributes defined in the class.
#          One class can create multiple objects, and each object can have different values for the attributes defined in the class.

from logging import config


from logging import config


class Dog:                          # Define a class named Dog
    def __init__(self, name, age):  # The __init__ method is a special method that is called when an object is created from the class. It initializes the attributes of the object.
        self.name = name            # Attribute: name, age.  (self is a reference to the current instance of the class, and it is used to access the attributes and methods of the class.)
        self.age = age

    def bark(self):                 # Method: bark.  (A function defined inside a class is called a method. It defines the behavior of the objects created from the class.)
        print(f"{self.name.upper()} says woof woof! I'm {self.age} years old!")

# Create an object of the Dog class
my_dog1 = Dog("Buddy", 3)  
my_dog2 = Dog("Max", 5)

# Call the bark method for each dog
my_dog1.bark()  # Output: BUDDY says woof woof! I'm 3 years old!
my_dog2.bark()  # Output: MAX says woof woof! I'm 5 years old!


# 1*    Attributes: are variables that belong to an Object, so they hold data. 
#   Two types of attributes: Instance attributes and Class attributes.
#   Instance attributes: are specific to each object and are defined in the __init__ method. They are accessed using the self keyword.
#   Class attributes: are shared among all instances of a class and are defined outside the __init__ method. They are accessed using the class name or an instance of the class.

class Dog:
    species = "French Bulldog" # Class attribute

    def __init__(self, name):
        self.name = name # Instance attribute

print(Dog.species) # French Bulldog

# Create two objects of the Dog class
dog1 = Dog("Jack")
print(dog1.name)    # Output: Jack
print(dog1.species) # Output: French Bulldog

dog2 = Dog("Tom")
print(dog2.name)    # Output: Tom
print(dog2.species) # Output: French Bulldog

# 2*    Methods: are functions defined inside a class that describe the behaviors of an object. They can manipulate the attributes of the object and perform actions.

class Car:
    def __init__(self, color, model):
        self.color = color  # Instance attribute
        self.model = model  # Instance attribute

    def describe(self):
        return f"This car is a {self.color} {self.model}"

car_1 = Car("red", "Toyota Corolla")
car_2 = Car("green", "Lamborghini Revuelto")

print(car_1.describe()) # This car is a red Toyota Corolla
print(car_2.describe()) # This car is a green Lamborghini Revuelto

# 3*    Special Methods: are predefined methods in Python that have special names and are used to perform specific operations.
#  In normally, Python data types already know how to perform operations like addition, subtraction, and string concatenation. 
#               However, when we create our own classes, Python doesn't know how to handle things automatically.
#               This is where special methods come in. They allow us to define how our objects should behave when we use certain operators on them.

""" Some common special methods include:
Arithmetic operations: In addition, __add__() is called, __sub__() for subtraction, __mul__() for multiplication, and __truediv__() for division.
String operations: __add__() is called for concatenation, __mul__() for repetition, __format__() for formatting, __str__() and __repr__() for text conversion.
Comparison operations: __eq__() is called for equality checks, __lt__() for less-than, __gt__() for greater-than.
Iteration operations: __iter__() is called to return an iterator and __next__() to fetch the next item. """

class Book:
   def __init__(self, title, pages):    # Instance attributes: title and pages
       self.title = title
       self.pages = pages

   def __len__(self):                   # special method __len__() is called when the built-in len() function is used on an object of the class. It should return the length of the object.
       return self.pages

   def __str__(self):           # special method __str__() is called when the built-in str() function is used on an object of the class. It should return a string representation of the object.    
       return f"'{self.title}' has {self.pages} pages"

   def __eq__(self, other):     # special method __eq__() is called when the equality operator (==) is used to compare two objects of the class. It should return True if the comparison is true and False otherwise.
       return self.pages == other.pages
  
book1 = Book("Built Wealth Like a Boss", 420)       # Create an object of the Book class with the title "Built Wealth Like a Boss" and 420 pages
book2 = Book("Be Your Own Start", 420)      # Create another object of the Book class with the title "Be Your Own Start" and 420 pages

print(len(book1)) # Output: 420
print(len(book2)) # Output: 420
print(str(book1)) # Output: 'Built Wealth Like a Boss' has 420 pages
print(str(book2)) # Output: 'Be Your Own Start' has 420 pages
print(book1 == book2) # Output: True

# Shopping Cart Example:
""" 
Add items to the cart                                       # Using normal methods
Remove items from the cart                                  # Using normal methods
Get the number of items in the cart                         # Using __len__() special method
Check what items are in the cart                            # Using __iter__() special methods
Check if a specific item is in the cart                     # Using __contains__() special method
Return or display an item at a specific index in the cart   # Using __getitem__() special method
"""
class cart:
    def __init__(self):
        self.items = [] # Instance attribute: items, which is a list that will hold the items in the cart.

    def add_item(self, item): # Method to add an item to the cart
        self.items.append(item)

    def remove_item(self, item): # Method to remove an item from the cart
        if item in self.items:
            self.items.remove(item)
        else:
            print(f"{item} is not in the cart.")
    
    def list_items(self): # Method to list all items in the cart
        return self.items
    
    def __len__(self): # Special method to get the number of items in the cart
        return len(self.items)

    def __getitem__(self, index): # Speecial method to return an item at a specific index in the cart
        return self.items[index]
    
    def __contains__(self, item): # Special method to check if a specific item is in the cart
        return item in self.items
    
    def __iter__(self): # Special method to allow iteration over the items in the cart
        return iter(self.items)
    

my_cart = cart() # Create an object of the cart class
my_cart.add_item("Laptop") # Add items to the cart
my_cart.add_item("Phone") # Add another item to the cart
my_cart.add_item("wireless mouse") # Add another item to the cart
my_cart.add_item("Headphones") # Add another item to the cart

for item in my_cart: # Check what items are in the cart using iteration
    print(item, end=", ") # Output: Laptop, Phone, wireless mouse, Headphones,

print(len(my_cart)) # Get the number of items in the cart using __len__() special method. Output: 4
print(my_cart[1]) # Return or display an item at a specific index in the cart using __getitem__() special method. Output: Phone

print("Laptop" in my_cart) # Check if a specific item is in the cart using __contains__() special method. Output: True
print("Tablet" in my_cart) # Check if a specific item is in the cart using __contains__() special method. Output: False

my_cart.remove_item("Phone") # Remove an item from the cart

print(my_cart.list_items()) # List all items in the cart using list_items() method. Output: ['Laptop', 'wireless mouse', 'Headphones']

my_cart.remove_item("Tablet") # Try to remove an item that is not in the cart. Output: Tablet is not in the cart.


# 4* Handling Attributes Dynamically: Allowing you to access, modify, or delete attributes using getattr(), setattr(), hasattr() and delattr() functions.
#1   getattr(object, name, default): is used to retrieve the value of an attribute from an object. It takes three arguments: object, (string)attribute_name and a default value to return if the attribute does not exist.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person1 = Person("Alice", 30)

attr_name = input("Enter the attribute name to retrieve: ")
print(getattr(person1, attr_name, "Attribute not found"))   # If the user enters "name", output: Alice. If the user enters "age", output: 30. If the user enters an attribute that does not exist, output: Attribute not found.

#2   setattr(object, name, value): is used to set the value of an attribute on an object. It takes three arguments: object, (string)attribute_name and the value to set for the attribute.
class Configuration:
    pass
# Data loaded at runtime (e.g., from a config or env file)
settings_data = {
    "server_url": "https://api.example.com",
    "timeout_sec": 30,
    "max_retries": 3
} 
config_obj = Configuration() # Create an object of the Configuration class

# Dynamically set attributes using dictionary keys and values
for attr_name, attr_value in settings_data.items():
    setattr(config_obj, attr_name, attr_value)
# Now config_obj has attributes server_url, timeout_sec, and max_retries with the corresponding values from settings_data
print(config_obj.server_url) # Output: https://api.example.com  
print(config_obj.timeout_sec) # Output: 30
