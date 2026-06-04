"""
TYPE HINTS AND MYPY: Type hints are a powerful feature in Python that allow you to specify the expected types of variables,
function parameters, and return values. They improve code readability and help catch errors early with tools like mypy.
"""

# SECTION 1 - BASIC TYPE HINTS
# ---------------------------
# Show how variables can be annotated with primitive types.

age: int = 25
name: str = "Alice"
height: float = 1.75
is_student: bool = True

print(age)
print(name)
print(height)
print(is_student)

# SECTION 2 - FUNCTION TYPE HINTS
# ------------------------------
# Annotate parameters and return values for functions.

def add_numbers(a: int, b: int) -> int:
    return a + b

result = add_numbers(10, 20)
print("Result:", result)

def greet(name: str) -> str:
    return f"Hello, {name}!"

print(greet("Daniel"))

# SECTION 3 - COMMON COLLECTION TYPES
# -----------------------------------
# Use generic collection syntax available in Python 3.9+.

numbers: list[int] = [1, 2, 3, 4, 5]
names: list[str] = ["Alice", "Bob", "Charlie"]
scores: dict[str, int] = {"Math": 90, "Science": 85}

print(numbers)
print(names)
print(scores)

def calculate_average(values: list[int]) -> float:
    return sum(values) / len(values)

average = calculate_average(numbers)
print("Average:", average)

# SECTION 4 - IMPORTING FROM TYPING
# --------------------------------
# Some type hints require typing imports for more advanced behavior.
from typing import Any, Dict, Optional, Tuple, Union, TypeAlias

"""
Optional, Union, Any, and TypeAlias are useful when a simple annotation
does not capture the full shape of the value.
"""

# SECTION 5 - OPTIONAL: A value that can be a specific type OR None
# ----------------------------------------------------------------

def get_nickname(user_id: int) -> Optional[str]:
    if user_id == 1:
        return "Dan"
    return None

nickname = get_nickname(1)
print("Nickname:", nickname)

nickname = get_nickname(999)
print("Nickname:", nickname)

# SECTION 6 - UNION: A value that can be one of multiple types
# -----------------------------------------------------------

def stringify(value: Union[int, float]) -> str:
    return str(value)

print(stringify(100))
print(stringify(3.14))

# SECTION 7 - ANY: Skip type checking for this value
# ------------------------------------------------

def process_unknown_data(data: Any) -> None:
    print("Received:", data)

process_unknown_data("hello")
process_unknown_data(123)
process_unknown_data([1, 2, 3])

# SECTION 8 - TUPLE: A fixed-size collection of values with specified types
# -----------------------------------------------------------------------

def get_coordinates() -> Tuple[float, float]:
    return (40.7128, -74.0060)

coordinates = get_coordinates()
print(coordinates)

# SECTION 9 - DICT: A collection of key-value pairs with specified types
# ---------------------------------------------------------------------

def get_student_scores() -> Dict[str, int]:
    return {"Alice": 95, "Bob": 88}

print(get_student_scores())

# SECTION 10 - TYPE ALIASES: Create custom type names for complex types
# --------------------------------------------------------------------

StudentScores: TypeAlias = dict[str, int]

def create_scoreboard() -> StudentScores:
    return {"Alice": 90, "Bob": 85, "Charlie": 95}

print(create_scoreboard())

# SECTION 11 - HOW MYPY WORKS
# --------------------------
# Mypy checks your type hints before running code.

print(
    """
To install mypy:

    pip install mypy

To check this file:

    mypy 38_type_hints_mypy.py

Mypy will analyze the type hints and report issues.
"""
)

# SECTION 12 - COMMON ERRORS MYPY CAN DETECT
# -----------------------------------------
# The following examples are commented out intentionally.

# age: int = "twenty-five"
# add_numbers("10", "20")
# def bad_function() -> int:
#     return "hello"
# numbers: list[int] = [1, 2, "three"]

# SECTION 13 - PRACTICAL EXAMPLE
# -----------------------------
# Use Optional return values and check for None before use.

def find_user_email(user_id: int) -> Optional[str]:
    users = {1: "alice@example.com", 2: "bob@example.com"}
    return users.get(user_id)

email = find_user_email(1)
if email is not None:
    print(email.upper())
else:
    print("No email found")

"""
Mypy encourages safer code by reminding us that values can be None.
Always check Optional values before treating them like a concrete type.
"""
