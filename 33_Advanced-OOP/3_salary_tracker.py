class Employee:
    # class attribute to store base salaries for each level
    _base_salaries = {
        'trainee': 1000,
        'junior': 2000,
        'mid-level': 3000,
        'senior': 4000,
    }

    def __init__(self, name, level): 
        self.name = name       
        self.level = level
        self._salary = Employee._base_salaries[level]   # Set the salary based on the level using the class attribute _base_salaries

    def __str__(self):      # String representation of the Employee object, showing the name and level.
        return f'{self.name}: {self.level}'

    def __repr__(self):     # Official string representation of the Employee object, showing the name and level in a format that can be used to recreate the object.
        return f"Employee('{self.name}', '{self.level}')"

    @property
    def name(self):     # Getter method for the 'name' attribute, allowing access to the private attribute _name.
        return self._name

    @name.setter        # Setter method for the 'name' attribute, allowing validation and updating of the private attribute _name.
    def name(self, new_name):
        if not isinstance(new_name, str):   # Validate that the new name is a string, and raise a TypeError if it is not.
            raise TypeError("'name' must be a string.")
        self._name = new_name       # Update the private attribute _name with the new name, and print a message indicating that the name has been updated.
        print(f"'name' updated to '{self.name}'.")

    @property
    def level(self):    # Getter method for the 'level' attribute, allowing access to the private attribute _level.
        return self._level

    @level.setter   # Setter method for the 'level' attribute, allowing validation and updating of the private attribute _level, as well as updating the salary based on the new level.
    def level(self, new_level):     
        if not isinstance(new_level, str):      # Validate that the new level is a string, and raise a TypeError if it is not.
            raise TypeError("'level' must be a string.")
        if new_level not in Employee._base_salaries:    # Validate that the new level is one of the valid levels defined in the class attribute _base_salaries, and raise a ValueError if it is not.
            raise ValueError(f"Invalid value '{new_level}' for 'level' attribute.")
        if hasattr(self, '_level') and new_level == self.level:     # Validate that the new level is not the same as the current level, and raise a ValueError if it is.
            raise ValueError(f"'{self.level}' is already the selected level.")
        if hasattr(self, '_level') and Employee._base_salaries[new_level] < Employee._base_salaries[self.level]:    # Validate that the new level is not lower than the current level and raise a ValueError if it is.
            raise ValueError("Cannot change to lower level.")
        
        self._salary = Employee._base_salaries[new_level]  # Update the salary based on the new level using the class attribute _base_salaries
        self._level = new_level # Update the private attribute _level with the new level.

    @property
    def salary(self):   # Getter method for the 'salary' attribute, allowing access to the private attribute _salary.
        return self._salary


charlie_brown = Employee('Charlie Brown', 'trainee')
print(charlie_brown)
print(f'Base salary: ${charlie_brown.salary}')  # Output: Base salary: $1000