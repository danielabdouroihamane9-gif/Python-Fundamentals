#15 WHILE LOOP: Execute some code WHILE some conditions remain true

name = input("Enter your name: ")
while name == "":
    print("You didn't enter your name!")
    name = input("Enter your name: ")
print(f"Hello {name}!")

food = input("Enter your food? (q to quit): ")
while not food == "q":
    print(f"Your food is {food}")
    food = input("Enter another food? (q to quit): ")
print("bye!")

age = int(input("Enter your age: "))
while age < 0:
    print("Age can't be negative!")
    age = int(input("Enter your age: "))
print(f"You are {age} years old.")

num = int(input("Enter a number between 0 - 10: "))
while num < 0 or num > 10:
    print("You didn't enter the right number!")
    num = int(input("Enter a number between 0 - 10: "))
print(f"You choose {num}.")



