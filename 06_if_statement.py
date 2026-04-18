#6 IF: Do some code only IF some condition is True
#       Else do something else
age = int(input("Enter your age: "))
if age >= 120:
    print("you are too old to vote!")
elif age < 0:
    print("You are not born yet!")
elif age >= 18:
    print("You are eligible to vote!")
else:
    print("You are not eligible to vote!")

