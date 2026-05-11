#34     Getters and Setters: Getters and setters are methods that allow you to access and modify private attributes of a class.
#       Getters are used to retrieve the value of a private attribute. 
#       Setters are used to set or update the value of a private attribute.
#       Properties connect getters and setters, and allow access to data.
#       They act like attributes but are actually methods that provide controlled access to private attributes.

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