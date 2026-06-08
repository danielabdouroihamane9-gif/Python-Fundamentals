"""
DECORATORS: A decorator wraps a function/method to add behavior without changing the original code.
Syntax: @decorator_name
"""

# ============================================================================
# 1. @STATICMETHOD - Method that doesn't need 'self' or 'cls'
# ============================================================================
# Use: When a method is utility/helper code not tied to instance or class state
# Key: Doesn't receive self or cls, called on instance or class


class Math:
    @staticmethod
    def add(a, b):
        return a + b


print(Math.add(5, 3))  # Output: 8 (no instance needed)


# ============================================================================
# 2. @CLASSMETHOD - Method that receives 'cls' (the class itself)
# ============================================================================
# Use: When you need to access/modify class variables or create instances
# Key: First param is 'cls', called on class, works for inheritance


class Dog:
    species = "Canis familiaris"

    def __init__(self, name):
        self.name = name

    @classmethod
    def get_species(cls):
        return cls.species

    @classmethod
    def from_string(cls, dog_info):
        """Create instance from string - useful alternate constructor"""
        name = dog_info.split("-")[0]
        return cls(name)


print(Dog.get_species())  # Output: Canis familiaris
buddy = Dog.from_string("Buddy-Golden Retriever")
print(buddy.name)  # Output: Buddy


# ============================================================================
# 3. CUSTOM DECORATOR - Wrap a function to modify behavior
# ============================================================================
# How it works: Decorator takes a function → returns wrapper → wrapper replaces original


def simple_decorator(func):
    """Decorator that adds prefix/suffix to output"""

    def wrapper(*args, **kwargs):
        print("--- START ---")
        result = func(*args, **kwargs)
        print("--- END ---")
        return result

    return wrapper


@simple_decorator
def say_hello(name):
    print(f"Hello, {name}!")


say_hello("Alice")
# Output:
# --- START ---
# Hello, Alice!
# --- END ---


# Decorator with arguments
def repeat_decorator(times):
    """Decorator that runs function multiple times"""

    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)

        return wrapper

    return decorator


@repeat_decorator(times=3)
def cheer():
    print("Woohoo!")


cheer()
# Output: Woohoo! (printed 3 times)


# ============================================================================
# KEY DIFFERENCES AT A GLANCE
# ============================================================================
# @staticmethod  → Utility function, no access to instance/class
# @classmethod   → Access to class, useful for alternate constructors
# @custom        → Wrap functions to add pre/post behavior
