# Abstraction is the process of hiding complex implementation details and showing only the
# essential features of an object.
# In Python, abstraction is often achieved by using abstract base classes (ABCs)
# and abstract methods. Abstract classes define required methods that concrete
# subclasses must implement.

"""Demonstrate abstraction in Python.

This example uses an abstract Shape class to define a clear interface for shapes.
Concrete shape classes like Rectangle implement the details of the interface.
"""

from abc import ABC, abstractmethod


class Shape(ABC):
    """Abstract base class for geometric shapes.

    The Shape class defines the interface that all shape subclasses must follow.
    It does not provide implementations for area() or perimeter().
    """

    @abstractmethod
    def area(self):
        """Return the shape's area.

        Concrete subclasses must override this method with their own implementation.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """Return the shape's perimeter.

        Concrete subclasses must override this method with their own implementation.
        """
        pass


class Rectangle(Shape):
    """Concrete class implementing a rectangle shape."""

    def __init__(self, width, height):
        # Store the rectangle dimensions.
        self.width = width
        self.height = height

    def area(self):
        """Calculate and return the rectangle's area."""
        return self.width * self.height

    def perimeter(self):
        """Calculate and return the rectangle's perimeter."""
        return 2 * (self.width + self.height)


def main():
    # Shape is an abstract class and cannot be instantiated directly.
    # The following line would raise a TypeError if uncommented:
    # shape = Shape()

    # Instead, instantiate a concrete shape class that implements all abstract methods.
    rect = Rectangle(5, 3)

    print("Rectangle example:")
    print(f"  Width: {rect.width}")
    print(f"  Height: {rect.height}")
    print(f"  Area: {rect.area()}")
    print(f"  Perimeter: {rect.perimeter()}")

    print("\nWhy abstraction matters:")
    print("  - The Shape class defines what methods a shape should have.")
    print("  - Rectangle provides the actual calculations for those methods.")
    print(
        "  - Users can rely on the shared Shape interface without knowing the details."
    )


if __name__ == "__main__":
    main()
