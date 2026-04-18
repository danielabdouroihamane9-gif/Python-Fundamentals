#4 USER INPUT: A function that prompts the user to enter data
#            Returns the entered data as a string.
'''
EXP1: Rectangle Area Calculator
'''
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the length of the rectangle: "))
area = length * width
print(f"The area of the rectangle is: {area}cm^2.")
'''
EXP2: Shopping Cart Program.  (knowing: Items, Price and quantity.)
'''
item = input("What do you want to purchase? ")
price = float(input("How much does it cost? "))
quantity = int(input("how many do you want it? "))
total = price * quantity
print(f"You bought {quantity} {item} for ${price} each ")
print(f"the total price is: ${total}")