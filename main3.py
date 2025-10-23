import math

# Built-in function "round" rounds numbers
x = 3.14
y = -4

# Round x to the nearest integer
rounded_x = round(x)
print(f"Rounded value of {x} is: {rounded_x}")

# Absolute value of y
result = abs(y)
print(f"Absolute value of {y} is: {result}")

# Power function: 2 raised to 3
power = pow(2, 3)
print(f"2 raised to the power 3 is: {power}")

# Maximum value between x and y
maximum = max(x, y)
print(f"Maximum value between {x} and {y} is: {maximum}")

# Minimum value between x and y
minimum = min(x, y)
print(f"Minimum value between {x} and {y} is: {minimum}")

print("-----------------------------------")
print()
print()
print("-----------------------------------")


# MATH MODULE
print("Math Module")
a = 9.1

# Mathematical constants
print(f"Value of pi: {math.pi}")
print(f"Value of e: {math.e}")

# Square root of a
square = math.sqrt(a)
print(f"Square root of {a} is: {square}")

# Ceiling value (round up)
ceil = math.ceil(a)
print(f"Ceiling value of {a} is: {ceil}")

# Floor value (round down)
floor = math.floor(a)
print(f"Floor value of {a} is: {floor}")

print("-----------------------------------")
print()
print()
print("-----------------------------------")

print("CIRCUMFERENCE CALCULATION")
print()
print()

radius = float(input("Enter the radius of the circle: "))

circumference = 2 * math.pi * radius

print(f"The circumference of a circle with radius {radius} is: {circumference}")
print("-----------------------------------")
print()
print()
print("-----------------------------------")

# AREA OF CIRCLE
print("AREA OF CIRCLE")
print()
print()

radius_area = float(input("Enter the radius of the circle: "))

area = math.pi * (radius_area ** 2)

print(f"The area of a circle with radius {radius_area} is: {area}")

print("-----------------------------------")
print()
print()
print("-----------------------------------")

#Hypotenuse calculation
print("HYPOTENUSE CALCULATION")
print()
print()

a = float(input("Enter side A: "))
b = float(input("Enter side B: "))

c = math.sqrt(pow(a, 2) + pow(b, 2))

print(f"Side C = {c}")

print("-----------------------------------")
print("END")