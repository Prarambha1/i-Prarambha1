# logical operators = used on conditional statements
# and = checks two or more conditions if True
# or = checks if at least one condition is True
# not = True if condition is False, and vice versa

temp = 25
sunny = True

if temp > 0 or temp < 30:
    print("The weatehr is good!")
else:
    print("The weatehr is bad!")

if not sunny:
    print("It is cloudy outside")
else:
    print("It is sunny outside")