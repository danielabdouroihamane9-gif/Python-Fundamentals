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
        # If all checks pass, assign the attributes
        self.name = name        
        self.planet_type = planet_type
        self.star = star 

    def orbit(self):        # This method simulates the planet orbiting around its star
        return f"{self.name} is orbiting around {self.star}..."

    def __str__(self):       # This method defines how the planet is represented as a string
        return f"Planet: {self.name} | Type: {self.planet_type} | Star: {self.star}"

def main():     
    print("--- Welcome to the Cosmic Registry ---")
    planets = []        # This list will hold all the planet instances

    while True:     # This loop allows the user to continuously add planets until they choose to stop
        try:
            print("\nRegister a new planet:")
            name = input("Enter Name: ").strip()      # This prompts the user to enter the name and removes any extra whitespace
            p_type = input("Enter Type (e.g., Gas Giant): ").strip()    
            star = input("Enter Star Name: ").strip()

            # Create the instance(object) of the Planet class with the user input
            new_planet = Planet(name, p_type, star)
            planets.append(new_planet)      # Add the new planet to the list of planets
            
            print("\n Registration Successful!")
            print(new_planet)   
            print(new_planet.orbit())

        except (TypeError, ValueError) as e:
            #  This catches the errors you defined in your __init__
            print(f"\n Input Error: {e}")
            print("Please try again.")

        # Check if user wants to continue
        cont = input("\nAdd another planet? (y/n): ").lower()
        if cont != 'y':
            break

    print("\n--- Final Galactic Map ---")
    for p in planets:      # This loop prints out all the planets that were registered in the session
        print(p)

if __name__ == "__main__":      # This ensures that the main function runs only when this script is executed directly, not when imported as a module
    main()

  