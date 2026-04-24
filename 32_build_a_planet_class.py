class Planet:
    def __init__(self, name, planet_type, star):
        if not isinstance(name, str):
            raise TypeError("name, planet type, and star must be strings")
        if not isinstance(planet_type, str):
            raise TypeError("name, planet type, and star must be strings")
        if not isinstance(star, str):
            raise TypeError("name, planet type, and star must be strings")
        if name == "":
            raise ValueError("name, planet_type, and star must be non-empty strings")
        if planet_type == "":
            raise ValueError("name, planet_type, and star must be non-empty strings")
        if star == "":
            raise ValueError("name, planet_type, and star must be non-empty strings")
        
        self.name = name
        self.planet_type = planet_type
        self.star = star     