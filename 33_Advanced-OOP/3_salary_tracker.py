class Employee:
    # class attribute to store base salaries for each level
    _base_salaries = {
        'trainee': 1000,
        'junior': 2000,
        'mid-level': 3000,
        'senior': 4000,
    }

    def __init__(self, name, level):
        # Validate that 'name' and 'level' are of type 'str' 
        if not isinstance(level, str):
            raise TypeError("'level' attribute must be of type 'str'.")
        # Validate that 'level' is one of the allowed values in the _base_salaries dictionary
        if level not in Employee._base_salaries:
            raise ValueError(f"Invalid value '{level}' for 'level' attribute.")
        
        self._name = name       
        self._level = level
        self._salary = Employee._base_salaries[level]   # Set the salary based on the level using the class attribute _base_salaries

    def __str__(self):      # String representation of the Employee object, showing the name and level.
        return f'{self.name}: {self.level}'

    def __repr__(self):     # Official string representation of the Employee object, showing the name and level in a format that can be used to recreate the object.
        return f"Employee('{self.name}', '{self.level}')"

    @property
    def name(self):     # Getter method for the 'name' attribute, allowing access to the private attribute _name.
        return self._name

    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str):
            raise TypeError("'name' must be a string.")
        self._name = new_name
        print(f"'name' updated to '{self.name}'.")

    @property
    def level(self):    # Getter method for the 'level' attribute, allowing access to the private attribute _level.
        return self._level

    @property
    def salary(self):   # Getter method for the 'salary' attribute, allowing access to the private attribute _salary.
        return self._salary


charlie_brown = Employee('Charlie Brown', 'trainee')
print(charlie_brown)
print(f'Base salary: ${charlie_brown.salary}')  # Output: Base salary: $1000