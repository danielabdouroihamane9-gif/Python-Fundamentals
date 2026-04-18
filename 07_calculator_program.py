#7 CALCULATOR PROGRAM
operator = input("Enter an operator (+ - * /): ")
num1 = float(input("Enter a 1st number: "))
num2 = float(input("Enter a 2nd number: "))
if operator == "+":
    result = num1 + num2
    print(round(result, 2))
elif operator == "-":
    result = num1 - num2
    print(round(result, 2))
elif operator == "*":
    result = num1 * num2
    print(round(result, 2))
elif operator == "/":
    result = num1 / num2
    print(round(result, 2))
else:
    print(f"{operator} is not a valid operator!")