#16 COMPOUND INTEREST CALCULATOR:

principle = 0
rate = 0
time = 0
"""
while principle <= 0:
    principle = float(input("Enter the principle balance: "))
    if principle <= 0:
        print("principle balance can't be less than or equal to zero")
print(principle)

while rate <= 0:
    rate = float(input("Enter the interest rate: "))
    if rate <= 0:
        print("Interest rate can't be less than or equal to zero")
print(rate)

while time <= 0:
    time = int(input("Enter the time in year: "))
    if time <= 0:
        print("time can't be less than or equal to zero")
print(time)

print(f"Principle balance is {principle}")
print(f"Interest rate is {rate}")
print(f"Length of time is {time}")

total = principle * pow((1 + rate/100), time)
print(f"Balance after {time} year/s, is ${round(total, 2)}")
"""


while True:
    principle = float(input("Enter the principle balance: "))
    if principle < 0:
        print("principle balance can't be less than zero")
    else:
        break

while True:
    rate = float(input("Enter the interest rate: "))
    if rate < 0:
        print("Interest rate can't be less than zero")
    else:
        break

while True:
    time = int(input("Enter the time in year: "))
    if time < 0:
        print("time can't be less than zero")
    else:
        break

print(f"Principle balance is {principle}")
print(f"Interest rate is {rate}")
print(f"Length of time is {time}")

total = principle * pow((1 + rate/100), time)
print(f"Balance after {time} year/s, is ${round(total, 2)}")


