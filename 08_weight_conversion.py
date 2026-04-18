#8 WEIGHT CONVERSION
weight = float(input("Enter your weight: "))
unit = input("kilograms or pounds? (K or L): ")
if unit == "K":
    weight = weight * 2.205
    unit = "Lbs."
    print(f"Your weight is: {weight} {unit}")
elif unit == "L":
    weight = weight / 2.205
    unit = "Kgs."
    print(f"Your weight is: {weight} {unit}")
else:
    print(f"{unit} is invalid unit, retry!")