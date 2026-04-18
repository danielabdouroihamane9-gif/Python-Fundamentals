"""
#5 ARITHMETIC & MATH:   ARITHMETIC OPERATORS, MATH FUNCTIONS AND EXERCISES.
'''ARITHMETIC OPERATORS:'''
friends = 5
friends += 3
print(friends)

friends = 5
friends -= 3
print(friends)

friends = 5
friends *= 3
print(friends)

friends = 5
friends **= 3
print(friends)

friends = 5
friends /= 3
print(friends)

friends = 5
reminder= friends % 3
print(reminder)
"""   """
''' MATH FUNCTIONS '''
x = 3.14
y = -8
z = 5
result = round(x) #arrondissement
print(result)

result = abs(y)   #absolute value
print(result)

result = pow(z, 2) #power
print(result)

result = max(x, y, z) #maximum
print(result)

result = min(x, y, z) #minimal
print(result)
"""   """
import math
x = 9
print(math.pi) #pi

print(math.e)            #exponentiel

result = math.sqrt(x)       #square root
print(result)

x = 9.1
result = math.ceil(x)       #adding up
print(result)

x = 9.5
result = math.floor(x)      #subtracting down
print(result)
"""
''' EXERCISES '''
''' EXP1: Calculate the Circonference of a circle; C = 2*pi*r '''
import math
radius = float(input("Enter the radius of a circle: "))
circumference = 2 * math.pi * radius
print(f"the circumference of the circle is {round(circumference, 2)}cm^2")

''' EXP2: Calculate the Area of a circle; A = pi * r^2'''
radius = float(input("Enter the radius of a circle: "))
area = math.pi * pow(radius,2)
print(f"the area of the circle is {round(area, 2)}cm^2")

''' EXP3: Calculate the Hypothenus of a triangle; C = sqrt(a^2 + b^2)'''
a = float(input("Enter the side of a: "))
b = float(input("Enter the side of b: "))
c = math.sqrt(pow(a,2)+ pow(b,2))
print(f"the hypothenus of the triangle is {c}cm ")



