# SHOPPING CART PROGRAM

foods = []
prices = []
total = 0

while True:
    food = input("Enter a food name to buy (q to quit): ")	#ask user input
    if food.lower() == "q":				#break if input = q
        break
    else:
        price = float(input(f"Enter the price of {food}: $"))	#price user input 
        foods.append(food)				#adding food into the collection of foods
        prices.append(price)				#adding price into the collection of prices

print("\n----- YOUR CARTS -----\n")

for food in foods:
    print(food, end=", ")				#printing all food
print()
for price in prices:
    total = total + price
print(f"The total price is ${total}")			#printing the total price
print()
print("Thanks for shopping with us")



