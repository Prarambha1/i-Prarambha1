#FUNCTIONS = A block of code that performs a specific task. Place () after the function name to execute it.

def happy_birthday(name, age):
    print(f"Happy birthday to {name}!")
    print("Happy birthday to you!")
    print(f"You are {age} years old!")
    print("Happy birthday to you!")
    print()

happy_birthday("Bro", 20)
happy_birthday("Steve", 32)
happy_birthday("Joe", 34)

#EXERCISE 1
def display_invoice(username,amount, due_date):
    print(f"Hello {username}")
    print(f"Your bill is {amount} and is due on {due_date}")

display_invoice("Bro", 100, "01/01/2024")

