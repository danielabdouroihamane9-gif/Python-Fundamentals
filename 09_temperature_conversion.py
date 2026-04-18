#9 TEMPERATURE CONVERSION
temp = float(input("Enter the temperature: "))
unit = input("Is this in celsius or fahrenheit? (C or F): ")
if unit == "C":
    temp = (temp * 1.8) + 32
    unit = "F."
    print(f"The temperature in fahrenheit is: {temp}°F")
elif unit == "F":
    temp = (temp - 32) / 1.8
    unit = "C."
    print(f"The temperature in celsius is: {temp}°C")
else:
    print(f"{unit} is not a valid unit!")