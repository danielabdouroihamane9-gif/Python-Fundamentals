#17 FOR LOOPS: Execute a block of code a fixed number of times.
#             You can iterate over a range, string, sequence, etc.

for x in range(1, 11):
    if x == 5:
        break
    else:
        print(x)

for x in reversed(range(1, 11, 2)):
    print(x)
print("HAPPY BIRTHDAY!")

for x in range(1, 21):
    if x == 13:
        continue
    else:
        print(x)


credit_card = "14583207859"
for x in credit_card:
    print(x)

# Enumerate and Zip Functions and How do they work in Python?
#     The enumerate() function in Python is used to add a counter to an iterable and returns it as an enumerate object.
#     The zip() function in Python is used to combine two or more iterables (like lists, tuples, etc.) into a single iterable of tuples. 

#* Example of using the enumerate() function:
"""This function takes a list of items and prints each item along with its index"""               
items = ['apple', 'banana', 'cherry']
for index, item in enumerate(items, start=0):  # start=0 is the default value, it can be omitted
    print(f"Index: {index}, Item: {item}")  # Output: Index: 0, Item: apple
                                                               #              Index: 1, Item: banana
                                                               #              Index: 2, Item: cherry  
#* Example of using the zip() function:
"""This function takes two lists and combines them into a list of tuples using the zip() function"""
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35] 

for name, age in zip(names, ages):
    print(f"Name: {name}, Age: {age}")  # Output: Name: Alice, Age: 25
                                       	              #              Name: Bob, Age: 30
                                        	              #              Name: Charlie, Age: 35





