#34     Getters and Setters: Getters and setters are methods that allow you to access and modify private attributes of a class.
#       Getters are used to retrieve the value of a private attribute. 
#       Setters are used to set or update the value of a private attribute.
#       Properties connect getters and setters, and allow access to data.
#       They act like attributes but are actually methods that provide controlled access to private attributes.
#       Deleters are used to delete an attribute from an instance of a class. They can be defined using the @<property_name>.deleter decorator.

#1* Create a getter by using the @property decorator. This allows you to access the method like an attribute.
class Circle:
    def __init__(self, radius):
        self._radius = radius  # Private attribute (conventionally indicated by a single underscore)

    @property
    def radius(self):       # Getter method for getting the radius
        return self._radius 

    @property
    def area(self):         # Getter method for calculating the area of the circle.
        return 3.14 * (self._radius ** 2)
radius = float(input("enter the radius of the circle: "))
my_circle = Circle(radius)  # Create an instance of the Circle class with the radius provided by the user.
print(f"The radius of the circle is: {my_circle.radius}")  # Access the radius using the getter method.
print(f"The area of the circle is: {my_circle.area}")      # Access the area using the getter method.

#2* Create a setter by using the @<property_name>.setter decorator. This allows you to set the value of the private attribute.
class Circle:
    def __init__(self, radius):
        self.radius = radius   # Calling the setter method to set the radius when initializing the object.

    @property
    def radius(self):       # A getter to get the radius of the circle.
        return self._radius

    @radius.setter
    def radius(self, value):  # Setter method for setting the radius
        if value <= 0:
            raise ValueError("Radius must be a positive number")
        self._radius = value

my_circle = Circle(5)  # Create an instance of the Circle class with an initial radius of 5.
print(f"Initial radius: {my_circle.radius}")  # Output: Initial radius: 5

radius = float(input("Enter a new radius for the circle: "))
my_circle.radius = radius  # Set a new radius using the setter method.
print(f"Updated radius: {my_circle.radius}")  # Output: Updated radius: <entered_value>

#3* Create a deleter by using the @<property_name>.deleter decorator. This allows you to delete the private attribute.
class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    # Getter
    @property
    def radius(self):
        return self._radius
    
    # Setter
    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("Radius must be a positive number")
        self._radius = value
    
    # Deleter
    @radius.deleter
    def radius(self):
        print("Deleting radius...")
        del self._radius  # Deletes the private attribute _radius

radius = float(input("Enter the radius of the circle: "))
my_circle = Circle(radius)  # Create an instance of the Circle class with the radius provided
print(f"Radius before deletion: {my_circle.radius}")  # Output: Radius before deletion: <entered_value>
del my_circle.radius  # Delete the radius using the deleter method.

try:
    print(my_circle.radius)  # Attempt to access the radius after deletion, which should raise an AttributeError.
except AttributeError as e:
    print(f"Error: {e}")  # Output: Error: 'Circle' object has no attribute '_radius' (or similar error message indicating the attribute is missing)
