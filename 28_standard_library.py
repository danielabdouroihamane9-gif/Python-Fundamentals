#28 LIBRARY = It is a pre-built collection of functions and data that are stored in a file and can be used by multiple programs.

"""   Some examples of popular modules in Python include:   """
#   - math: Provides mathematical functions such as trigonometric functions, logarithmic functions, and constants like pi.
#   - random: Provides functions for generating random numbers and performing random operations.
#   - datetime: Provides functions for working with dates and times.
#   - re: Provides functions for working with regular expressions.

#* To use a library in Python, you typically need to import it using the import statement. For example, to use the math library, you would write:
import math

#* Once you have imported a library, you can access its functions and data using the dot notation. For example, to use the sqrt function from the math library, you would write:
result = math.sqrt(16)
print(result)  # Output: 4.0

""" Other alternative ways to import a library include: """
#* 1. Importing modules with an alias:
import math as m
result = m.sqrt(16) # Output: 4.0

#* 2. Importing specific functions from a module:
from math import sqrt
result = sqrt(16) # Output: 4.0

#* 3. Importing all functions from a module (not recommended):
from math import *
result = pow(16, 2) # Output: 256.0

#* Constant from the math module:
pi_value = math.pi
print(pi_value)  # Output: 3.141592653589793

#* Class from the datetime module:
import datetime
birthday = datetime.date(2005, 04, 08)
print(birthday.day)  # Output: 8
print(birthday.month)  # Output: 4
print(birthday.year)  # Output: 2005


