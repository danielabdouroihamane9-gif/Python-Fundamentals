#11 CONDITIONAL EXPRESSION: A one line shortcut for the if else statement (ternary operator)
#                           Print or assign one or two values based on a condition
#                           X if condition else Y (formula)
num = 5
temp = 38
age = 52
a = 8
b = 5

print("Positive" if num > 0 else "Negative" )
print("It's sunny" if temp >= 35 else "It's cold")
print("Adult" if age>=18 else "Child")
max_num = a if a>b else b
print(max_num)
result = "Even" if num % 2 == 0 else "Odd"
print(result)
