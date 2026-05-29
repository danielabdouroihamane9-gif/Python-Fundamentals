import json

# Let's practice reading and writing JSON files!


def write_json_example(filename):
    """How to write a Python dictionary to a JSON file."""
    print("--- 1. WRITING DATA TO JSON ---")

    # This is our Python dictionary (with nested lists and dictionary)
    student_profile = {
        "name": "Daniel",
        "major": "Computer Science",
        "current_semester": 4,
        "is_enrolled": True,
        "favorite_courses": [
            "Programming 1",
            "Database Systems",
            "Software Engineering",
        ],
        "grades": {"Python": "A", "Calculus": "B+", "Data Structures": "A-"},
    }

    print(f"Original Python data type: {type(student_profile)}")

    # 'w' mode means write. It creates the file if it doesn't exist, or overwrites if it does.
    with open(filename, "w") as file:
        # json.dump takes (data, file_object, formatting_options)
        json.dump(student_profile, file, indent=4)

    print(f"✓ Success: Saved student profile into '{filename}'\n")


def read_json_example(filename):
    """How to read data from a JSON file back into Python."""
    print("--- 2. READING DATA FROM JSON ---")

    # 'r' mode means read.
    with open(filename, "r") as file:
        # json.load takes (file_object) and returns a Python dictionary or list
        loaded_data = json.load(file)

    print(f"Loaded data type: {type(loaded_data)}")
    print(f"Student Name: {loaded_data['name']}")
    print(f"Major: {loaded_data['major']}")
    print(f"First Favorite Course: {loaded_data['favorite_courses'][0]}")
    print(f"Grade in Python: {loaded_data['grades']['Python']}\n")


def string_conversion_example():
    """How to convert directly between JSON strings and Python dictionaries (dumpS & loadS)."""
    print("--- 3. STRING TO DICT & DICT TO STRING (dumps / loads) ---")

    car_dict = {"brand": "Tesla", "model": "Model 3", "year": 2023, "electric": True}

    # 1. Convert Python dictionary to JSON String (dumps -> dump string)
    car_json_string = json.dumps(car_dict, indent=2)
    print("This is a raw string, NOT a dictionary anymore:")
    print(car_json_string)
    print(f"Type: {type(car_json_string)}\n")

    # 2. Convert JSON String back to Python Dictionary (loads -> load string)
    car_dict_again = json.loads(car_json_string)
    print("This is back to being a Python dictionary:")
    print(car_dict_again)
    print(f"Type: {type(car_dict_again)}")
    print(f"Car Brand: {car_dict_again['brand']}\n")


if __name__ == "__main__":
    json_filename = "student_data.json"

    # Step 1: Write data to the file
    write_json_example(json_filename)

    # Step 2: Read data back from the file
    read_json_example(json_filename)

    # Step 3: Bonus - Learn about json.dumps() and json.loads()
    string_conversion_example()
