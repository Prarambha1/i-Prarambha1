#Python calculator
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter an operator (+, -, *, /): ")

if operator == "+":
    print(f"{num1} + {num2} = {num1 + num2}")
elif operator == "-":
    print(f"{num1} - {num2} = {num1 - num2}")
elif operator == "*":
    print(f"{num1} * {num2} = {num1 * num2}")
elif operator == "/":
    if num2 != 0:
        print(f"{num1} / {num2} = {num1 / num2}")
    else:
        print("Error: Division by zero!")
else:
    print("Invalid operator!")
    

#weight conversion:
weight = float(input("Enter your weight: "))
unit = input("Kilogram or Pounds? (K or L): ").strip().lower()

if unit == "k":
    weight = weight * 2.205
    unit = "Lbs."
elif unit == "l":
    weight = weight * 2.205
    unit = "Kgs."
else:
    print(f"{unit} was not valid!")

print(f"Your weight is: {weight} {unit}")




# temperature conversion
unit = input("Is this temperature in Celsius or Fahrenheit (C/F)? ").strip().lower()
temp = float(input("Enter the temperature: "))

if unit == "c":
    fahrenheit = round((temp * 9/5) + 32, 1)
    print(f"{temp}°C is {fahrenheit}°F.")
elif unit == "f":
    celsius = round((temp - 32) * 5/9, 1)
    print(f"{temp}°F is {celsius}°C.")
else:
    print("Invalid temperature unit! Please enter 'C' for Celsius or 'F' for Fahrenheit.")


