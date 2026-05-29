# 34 JSON FILE: It is stand as JavaScript Object Notation.
#              It is a lightweight data-interchange format that is easy for humans to read and write,
#              and easy for machines to parse and generate.
#              JSON is commonly used for dictionary or list data structures.

import json  # Importing the json module to work with JSON data

# 1. Prepare your data (a Python dictionary)
user_data = {
    "name": "Daniel",
    "age": 21,
    "is_student": True,
    "skills": ["Python", "Git", "SQL"],
    "gpa": 3.8,
}

# 2. Open a file in write mode ('w') and save the data
with open("user.json", "w") as file:
    # indent=4 makes the JSON file look neat and human-readable
    json.dump(
        user_data, file, indent=4
    )  # we use json.dump() to write the data to the file

print("✓ JSON file created and data written successfully!")

# 3. To read the data back from the JSON file, we can use json.load()
""" To load data back into Python, you use json.load()."""
# 1. Open the file in read mode ('r')
with open("user.json", "r") as file:
    # Load the JSON data back into a Python variable
    loaded_data = json.load(file)

# 2. Use it like a regular Python dictionary!
print("Data read from file:")
print(f"Name: {loaded_data['name']}")
print(f"Age: {loaded_data['age']}")
print(f"Skills: {', '.join(loaded_data['skills'])}")


