#22 FUNCTION = > A block of code that performs a specific task and can be reused throughout a program. 
#               Functions can take input parameters, perform operations, and return output values. 
#               They help to break down complex problems into smaller, manageable pieces and promote code reusability. 
#               In Python, functions are defined using the 'def' keyword followed by the function name and parentheses.

# Example of a simple function that takes two numbers as input and returns their sum:
def add_numbers(num1, num2):

    """This function takes two numbers as input and returns their sum."""

    result = int(num1) + int(num2)
    return result
""" Example usage of the function"""
sum_result = add_numbers(5, 10)
print("The sum of 5 and 10 is:", sum_result)

#1 Default argument: A default argument is a value that is assigned to a function parameter if no argument is provided when the function is called.
#                   Example of a function with a default argument:
def greet(name, greeting="Hello"):
    """This function takes a name and an optional greeting message."""
    return f"{greeting}, {name}!"
# Example usage of the function with and without the default argument
print(greet("Alice"))  # Uses the default greeting
print(greet("Bob", "Good morning"))  # Overrides the default greeting

#2 Keyword argument: A keyword argument is an argument that is passed to a function by explicitly specifying the parameter name and its corresponding value.
#                    Example of a function with keyword arguments:
def display_info(name, age):
    """This function takes a name and age as input and displays the information."""
    return f"Name: {name}, Age: {age}"
# Example usage of the function with keyword arguments:
print(display_info(name="Charlie", age=30))  # Using keyword arguments
print(display_info(age=25, name="Diana"))  # Using keyword arguments in a different order

#3 *args: The *args syntax allows a function to accept an arbitrary number of positional arguments.
#  **kwargs: The **kwargs syntax allows a function to accept an arbitrary number of keyword arguments.

#*            Example of a function that uses *args:
def sum_all(*args):
    """This function takes an arbitrary number of positional arguments and returns their sum."""
    return sum(args)
# Example usage of the function with *args:
print(sum_all(1, 2, 3))  # Output: 6   
print(sum_all(4, 5, 6, 7))  # Output: 22

#*            Example of a function that uses **kwargs:
def print_kwargs(**kwargs):
    """This function takes an arbitrary number of keyword arguments and prints them."""
    """for key in kwargs.keys():   # display the keys of the kwargs dictionary
        print(key) # Output: name, age, city"""
    """for value in kwargs.values(): # display the values of the kwargs dictionary
        print(value) # Output: Eve, 28, New York"""
    for key, value in kwargs.items(): # display the key-value pairs of the kwargs dictionary
            print(f"{key}: {value}") # Output: name: Eve, age: 28, city: New York

print_kwargs(name="Eve", age=28, city="New York")

#*             Example of a function that uses both *args and **kwargs:
def display_info(*args, **kwargs):
    """This function takes an arbitrary number of positional and keyword arguments and displays the information."""
    print("Positional arguments:")
    for arg in args:    # display the values of the args tuple
        print(arg)
    print("Keyword arguments:")
    for key, value in kwargs.items():   # display the key-value pairs of the kwargs dictionary
        print(f"{key}: {value}")
# Example usage of the function with both *args and **kwargs:
display_info(1, 2, 3, name="Frank", age=35) # Output: Positional arguments: 1, 2, 3; Keyword arguments: name: Frank, age: 35

#*             Example of a function using input() to get user input:
def get_user_info():
    """This function prompts the user for their name and age and returns the information."""
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    return f"Name: {name}, Age: {age}"
# Example usage of the function to get user input:
user_info = get_user_info()
print(user_info)

#*             Example of a function using input() as parameters:
def greet_user(name):
    """This function takes a name as input and returns a greeting message."""
    return f"Hello, {name}! Welcome to our program."
# Example usage of the function with input() as a parameter:
user_name = input("Enter your name: ")
greeting_message = greet_user(user_name)
print(greeting_message)


