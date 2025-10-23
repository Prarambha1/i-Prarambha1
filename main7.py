
# Conditional Expressions Examples
num = 5
a = 6
b = 7
age = 13
temperature = 20
user_role = "admin"

# Print "Positive" if num > 0 else "Negative"
print("Positive" if num > 0 else "Negative")

# Assign "EVEN" if num % 2 == 0 else "ODD" to result and print it
result = "EVEN" if num % 2 == 0 else "ODD"
print(result)

# Compute max_num = a if a > b else b and print it
max_num = a if a > b else b
print(max_num)

# Compute min_num = a if a < b else b and print it
min_num = a if a < b else b
print(min_num)

# Compute status = "Adult" if age >= 18 else "Child" and print it
status = "Adult" if age >= 18 else "Child"
print(status)

# Compute weather = "HOT" if temperature > 20 else "COLD" and print it
weather = "HOT" if temperature > 20 else "COLD"
print(weather)

# Compute access_level = "Full Access" if user_role == "admin" else "Limited Access" and print it
access_level = "Full Access" if user_role == "admin" else "Limited Access"
print(access_level)