#user input
name = input("Enter your name: ")
age = int(input("Enter your age: "))
age = age + 1
print(f"hello {name}")
print(f"You are {age} years old.")
print("---------------------------------------------")


#mad libs
adjective = input("Enter an adjective: ")
noun = input("Enter a noun: ")
adjective2 = input("Enter another adjective: ")
verb = input("Enter a verb: ")
adjective3 = input("Enter one more adjective:")

print(f"Today I went to a {adjective} zoo.")
print(f"In an exhibit, I saw a {noun}.")
print(f"The {noun} was {adjective2} and {verb}ing.")
print(f"I was {adjective3}.")
print("---------------------------------------------")


#area of a rectangle
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

area = length * width
print(f"The area of the rectangle is {area}.")
print("---------------------------------------------")


#shopping cart
item1_price = float(input("Enter the price of item 1: "))
item1_qty = int(input("Enter the quantity of item 1: "))

item2_price = float(input("Enter the price of item 2: "))
item2_qty = int(input("Enter the quantity of item 2: "))

total = (item1_price * item1_qty) + (item2_price * item2_qty)

print(f"The total cost of your shopping cart is {total}.")
print("---------------------------------------------")
