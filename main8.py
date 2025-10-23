#validate user input exercise
"""
1. username is no more than 12 characters
2. username cant conatin spaces
3. username can only contain letters
"""


# Username validation program
username = input("Enter your username: ")
if len(username) > 12:
    print("Your username can't be more than 12 characters.")
elif username.find(" ") != -1:
    print("Your username can't contain spaces.")
elif not username.isalpha():
    print("Your username can only contain letters.")
else:
    print(f"Welcome, {username}!")

print("-----------------------------------")
print()
print()
print("-----------------------------------")

#string indexing= accessing elements of a sequence using [] (indexing operator)
# [start : end : stop]

#exercise
credit_number = "1234-1234-456-7654"
print(credit_number[0])#indexing
print(credit_number[:4])#slicing
print(credit_number[5:9])#slicing
print(credit_number[5:])#slicing
print(credit_number[-1])#slicing
print(credit_number[::3])#step

print("-----------------------------------")
print()
print()
print("-----------------------------------")


#exercise
lasts_digits = credit_number[-4:]
print(f"XXXX-XXXX-XXXX-{lasts_digits}")

print("-----------------------------------")
print()
print()
print("-----------------------------------")


#reversing a string
credit_number = credit_number[::-1]
print(credit_number)


#email slicer
email = input("Enter your email: ")
if "@" in email:
    index = email.index("@")
    username = email[:index]
    domain = email[index+1:]
    print(f"Your username is {username} and domain is {domain}")
else:
    print("Invalid email format.")
