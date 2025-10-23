#while loop = execute some code WHILE some condition remains true

#example 1
name = input("Enter your name: ")
while name == "":
    print("You didn't enter your name. Olease try again.")
    name = input("Enter your name: ")

print(f"Hello {name}")


#example 2
age = int(input("Enter your age: "))

while age<0:
    print("Age can't be negative")
    age = int(input("Enter your age: "))

print(f"You are {age} years old.")


#example 3
food = input("Enter a food you like (q to quit): ")

while not food == "q":
    print(f"You like {food}")
    food = input("Enter another food you like )q to quit): ")

print("bye!")

#example 4
num = int(input("Enter a number between 1 and 10: "))
while num < 1 or num > 10:
    print("{num} is not valid")
    num = int(input("Enter a number between 1 and 10: "))

print(f"Your number is {num}")


#python compound interest calculator
principal = 0
rate = 0
time = 0

while True:
    principal = float(input("Enter the principal amount: "))
    if principal <= 0:
        print("Principal can't be less than or equal to zero.")
    else:
        break

while True:
    rate = float(input("Enter the annual interest rate (in %): ")) / 100
    if rate <= 0:
        print("Rate can't be less than or equal to zero.")
    else:
        break

while True:
    time = int(input("Enter the number of years: "))
    if time <= 0:
        print("Time can't be less than or equal to zero.")
    else:
        break

total = principal * pow((1 + rate / 100), time)
print(f"Balance after {time} years: ${total:.2f}")