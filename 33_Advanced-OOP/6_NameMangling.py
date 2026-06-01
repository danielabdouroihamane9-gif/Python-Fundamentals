"""Name Mangling Example

This module demonstrates how Python implements "private" attributes
and methods using name mangling.

Usage:
- Define a class attribute or method with a double underscore prefix, e.g. __private_var.
- Python internally renames it to _ClassName__private_var.
- The attribute is still accessible, but the mangled name prevents accidental access.

When to use:
- Use name mangling when you want to make an attribute or method harder to override
  in subclasses or to avoid name clashes in a class hierarchy.
- Prefer a single underscore for "internal" attributes that are only a convention.
- Avoid using name mangling for public APIs or when external access should be easy.
"""


class Parent:
    """A simple parent class demonstrating name-mangled attributes."""

    def __init__(self):
        # Double underscore prefixes trigger Python name mangling.
        # The attribute is still accessible, but its name is changed internally.
        self.__private_var = "This is a private variable"

    def __private_method(self):
        """A private method defined with double underscore prefix."""
        return "This is a private method"

    def get_private_data(self):
        """Public method that returns the values of private members."""
        return self.__private_var, self.__private_method()


class Child(Parent):
    """A child class that inherits from Parent."""

    def access_parent_private_members(self):
        """Access parent private members using the mangled attribute names."""
        # Name mangling changes __private_var to _Parent__private_var
        # and __private_method to _Parent__private_method.
        return self._Parent__private_var, self._Parent__private_method()


def main():
    parent_instance = Parent()
    child_instance = Child()

    print("Using public Parent method:")
    print(parent_instance.get_private_data())
    print()

    print("Using Child to access mangled parent members:")
    print(child_instance.access_parent_private_members())
    print()

    print("Direct access to mangled names from outside the class:")
    print(parent_instance._Parent__private_var)
    print(parent_instance._Parent__private_method())
    print()

    print("Note:")
    print("- Double underscore names are not truly private in Python.")
    print("- They are renamed internally to avoid accidental access.")
    print("- Direct mangled access is possible, but not recommended.")


if __name__ == "__main__":
    main()
