#25 DICTIONARIES = They are built-in data structures in Python that store key-value pairs. 
#                  They are mutable, unordered, and indexed by keys.
# GENERAL SYNTAX:   my_dict = {key1: value1, key2: value2, ...}

""" Example of a dictionary that stores information about a Margherita pizza recipe: """
pizza = {
    "name": "Margherita",
    "price": 8.99,
    "calories_per_slice": 250,
    "toppings": ["tomato sauce", "mozzarella", "basil"]
}

#* Another alternative way to create a dictionary using the dict() constructor:
pizza = dict([("name", "Margherita"), ("price", 8.99), ("calories_per_slice", 250), ("toppings", ["tomato sauce", "mozzarella", "basil"])])

#* Accessing values in a dictionary using keys:
print(pizza["name"])  # Output: Margherita
print(pizza["price"])  # Output: 8.99
print(pizza["calories_per_slice"])  # Output: 250
print(pizza["toppings"])  # Output: ['tomato sauce', 'mozzarella', 'basil']

#* To update a value in the dictionary, you can assign a new value to an existing key:
pizza["name"] = "Pepperoni"
print(pizza["name"])  # Output: Pepperoni

#* To add a new key-value pair to the dictionary, you can simply assign a value to a new key:
pizza["size"] = "Large"
print(pizza["size"])  # Output: Large

#* The .get() method can be used to access values in a dictionary without raising an error if the key does not exist:
pizza_name = pizza.get("name", "Unknown")
print(pizza_name)  # Output: Pepperoni

pizza_price = pizza.get("price", 0)
print(pizza_price)  # Output: 8.99

print(pizza.get("papa", "Default Value"))  # Output: Default Value (since "papa" key does not exist in the dictionary)

#* The .keys() method returns a view object that displays a list of all the keys in the dictionary:
print(pizza.keys())  # Output: dict_keys(['name', 'price', 'calories_per_slice', 'toppings', 'size'])

#* The .values() method returns a view object that displays a list of all the values in the dictionary:
print(pizza.values())  # Output: dict_values(['Pepperoni', 8.99, 250, ['tomato sauce', 'mozzarella', 'basil'], 'Large'])    

#* The .items() method returns a view object that displays a list of all the key-value pairs in the dictionary as tuples:
print(pizza.items())  # Output: dict_items([('name', 'Pepperoni'), ('price', 8.99), ('calories_per_slice', 250), ('toppings', ['tomato sauce', 'mozzarella', 'basil']), ('size', 'Large')]) 

#* The .pop() method removes a key-value pair from the dictionary and returns the value associated with the specified key:
pizza.pop("size", "Key not found") # Output: Large (since the "size" key exists in the dictionary and its value is returned before being removed)
print(pizza)  # Output: {'name': 'Pepperoni', 'price': 8.99, 'calories_per_slice': 250, 'toppings': ['tomato sauce', 'mozzarella', 'basil']} (since the "size" key-value pair has been removed)

#* The .clear() method removes all key-value pairs from the dictionary, leaving it empty:
pizza.clear()   # Output: {} (since all key-value pairs have been removed and the dictionary is now empty)

#* The .update() method updates the dictionary with key-value pairs from another dictionary or an iterable of key-value pairs:
new_info = {"name": "Veggie", "price": 9.99, "calories_per_slice": 200, "toppings": ["tomato sauce", "mozzarella", "bell peppers", "olives"]}
pizza.update(new_info)  # Output: {'name': 'Veggie', 'price': 9.99, 'calories_per_slice': 200, 'toppings': ['tomato sauce', 'mozzarella', 'bell peppers', 'olives']} 
#                                   (since the dictionary has been updated with the new key-value pairs from the new_info dictionary)

