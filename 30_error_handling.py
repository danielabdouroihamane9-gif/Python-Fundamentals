#30 ERROR HANDLING: Type error handling in python are: syntax error, name error, type error, index error, attribute error, value error.
""" 1. Syntax error: For example, if you forget to close a parenthesis or a quotation mark, you will get a syntax error.
    2. Name error: This occurs when you try to use a variable that hasn't been defined.
    3. Type error: This happens when an operation is performed on an object of an inappropriate type.
    4. Index error: This occurs when you try to access an index that is out of range for a sequence.
    5. Attribute error: This happens when you try to access an attribute that doesn't exist for an object.
    6. Value error: This occurs when a function receives an argument of correct type but inappropriate value."""

# Exception Handling: It's the process to catch and manage exceptions that may occur during the execution of your code.
#       Types of Exception Handling: try, except, raise, else, finally.
#       Try: The code that may raise an exception is placed inside the try block.
#       Except: The code to handle the exception is placed inside the except block.
#       Raise: The code to raise an exception is placed inside the raise statement.
#       Else: The code to execute if no exception occurs is placed inside the else block.
#       Finally: The code to execute regardless of whether an exception occurred is placed inside the finally block.

#   1_Example of Exception Handling:
try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 / num2
except ValueError:
    print("Please enter valid integers.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
else:
    print(f"The result of the division is: {result}")
finally:
    print("Execution completed.")

# Using as e: You can use the 'as' keyword to assign the exception to a variable (commonly 'e') and then print it.
#   2_Example of using e as an alias for the exception:
try:
    x = 1 / 0
except ZeroDivisionError as e:
    print(f'Error occurred: {e}')

#   3_Example of handling multiple exceptions in a single except block:
try:
    number = int(input('Enter a number: '))
    result = 10 / number
except (ValueError, ZeroDivisionError) as e:
    print(f'Error occurred: {e}')


# Raising Exceptions: You can raise exceptions in your code using the 'raise' keyword. This is useful when you want to signal that an error has occurred.
#   4_Example of raising an exception:
from ast import If
from genericpath import exists


def check_age(age):
    if age < 0:
        raise ValueError('Age cannot be negative')
    return age

try:
    check_age(-5)
except ValueError as e:
    print(f'Error: {e}') # Error: Age cannot be negative

#   5_Example of re-raising an exception: This is when you catch an exception but want to propagate it further up the call stack.
def process_data(data):
    try:
        result = int(data)
        return result * 2
    except ValueError:
        print('Logging: Invalid data received')
        raise  # Re-raises the same ValueError

try:
    process_data('abc')
except ValueError:
    print('Handled at higher level')

#   6_Example of using finally to ensure cleanup:
def process_data(data):
    try:
        print("1. Trying to convert data...")
        result = int(data)
    except ValueError:
        print("2. [Function] Error caught! Logging now...")
        raise  # This "launches" the error, but Python pauses it for 'finally'
    finally:
        print("3. [Function] I run no matter what. Cleaning up...")

try:
    process_data('abc')
except ValueError:
    print("4. [Main Program] I caught the error thrown by the function!")


# Exception classes: You can create your own custom exception classes by inheriting from the built-in Exception class.
#   7_Example of creating a custom exception class:
class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f'Insufficient funds: ${balance} available, ${amount} requested')

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount

try:
    new_balance = withdraw(100, 150)
except InsufficientFundsError as e:
    print(f'Transaction failed: {e}')


# Chaining exceptions: You can chain exceptions together using the 'from' keyword to indicate that one exception was caused by another.
#   8_Example of chaining exceptions:
def parse_config(filename):
    try:
        with open(filename, 'r') as file:
            data = file.read()
            return int(data)
    except FileNotFoundError:
        raise ValueError('Configuration file is missing') from None # This tells Python not to include the original FileNotFoundError in the traceback, making it cleaner for the user.
    except ValueError as e:
        raise ValueError('Invalid configuration format') from e # This indicates that the ValueError was caused by the original exception (e) and includes it in the traceback for debugging purposes.
try:
    config = parse_config('config.txt')     # If 'config.txt' does not exist, it will raise a ValueError with the message 'Configuration file is missing'. 
except ValueError as e:                     # If 'config.txt' exists but contains invalid data that cannot be converted to an integer, 
    print(f'Error: {e}')                    # it will raise a ValueError with the message 'Invalid configuration format' and include the original ValueError in the traceback.

# Assertions: You can use the 'assert' statement to check for conditions that should always be true in your code. If the condition is false, an AssertionError is raised.
#   9_Example of using assertions:
def calculate_square_root(number):
    assert number >= 0, 'Cannot calculate square root of negative number'
    return number ** 0.5

try:
    result = calculate_square_root(-4)
except AssertionError as e:             # variable e will contain the message 'Cannot calculate square root of negative number' which is printed to the console.
    print(f'Assertion failed: {e}')


"""
The raise statement is essential for creating robust applications where you need to enforce business rules, validate input, and provide meaningful error messages. 
By strategically using raise, you can make your code more predictable and easier to debug, while giving users clear feedback about what went wrong.
"""