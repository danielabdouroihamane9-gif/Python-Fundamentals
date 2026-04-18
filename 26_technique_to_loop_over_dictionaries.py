#26 TECHNIQUES TO LOOP OVER DICTIONARIES

products = {
    "Laptop": 999.99,
    "Mouse": 29.99,
    "Keyboard": 79.99
}

#* Looping over values:
for value in products.values():
    print(value) # Output: 999.99, 29.99, 79.99

#* Looping over keys:
for key in products:
    print(key) # Output: Laptop, Mouse, Keyboard

#* Looping over key-value pairs:
for key, value in products.items():
    print(f"{key}: {value}") # Output: Laptop: 999.99, Mouse: 29.99, Keyboard: 79.99

#* Offer 20% discount on all products and update the prices in the dictionary:
for product, price in products.items():
    products[product] = round(price * 0.8, 2) # Update the price with a 20% discount and round to 2 decimal places
print(products) # Output: {'Laptop': 799.99, 'Mouse': 23.99, 'Keyboard': 63.99} (since the prices have been updated with a 20% discount)

#* Using enumerate() to loop over the keys of the dictionary and get the index of each key:
for index, product in enumerate(products.keys()):
    print(f"{index}: {product}") # Output: 0: Laptop, 1: Mouse, 2: Keyboard (since the enumerate() function provides the index of each key in the dictionary)

#* Using enumerate() to loop over the values of the dictionary and get the index of each value:
for index, price in enumerate(products.values()):
    print(f"{index}: {price}") # Output: 0: 799.99, 1: 23.99, 2: 63.99 (since the enumerate() function provides the index of each value in the dictionary)  

#* Using enumerate() to loop over the key-value pairs of the dictionary and get the index of each pair:
for index, (product, price) in enumerate(products.items()):
    print(f"{index}: {product} - {price}") # Output: 0: Laptop - 799.99, 1: Mouse - 23.99, 2: Keyboard - 63.99

#* Customize the initial value of the index in the enumerate() function:
for index, (product, price) in enumerate(products.items(), start=1):
    print(f"{index}: {product} - {price}") # Output: 1: Laptop - 799.99, 2: Mouse - 23.99, 3: Keyboard - 63.99 (since the index starts from 1 instead of the default 0)