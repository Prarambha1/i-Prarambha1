# For loops execute a block of code a fixed number of times.
# You can iterate over a range, string, sequence, etc.

# iterate forwards
for x in range(10):
    print(x)

# iterate backwards
for x in reversed(range(1, 11)):
    print(x)

print("HAPPY NEW YEAR!")

# step by 2
for x in range(0, 31, 2):
    print(x)

# iterate over a string
credit_card = "1234-5678-9234-3456"
for x in credit_card:
    print(x)

# continue example
for x in range(1, 21):
    if x == 13:
        continue
    print(x)

# in nested loops, outer loop runs; inner loop repeats each time
# nested loops example
for x in range(3):
    for y in range(1, 10):
        print(x, y)

# grid printer: rows × columns using a symbol
# nested loops with input for rows and columns
rows = int(input("Enter the # of rows: "))
columns = int(input("Enter the # of columns: "))
symbol = input("Enter a symbol to use: ")

for x in range(rows):
    for y in range(columns):
        print(symbol, end="")
    print()