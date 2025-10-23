#first program
print("Hello, World!")

#variables ---> a container for value (string, integer, float, boolean)

#strings
name = "John"
print(f"Hello {name}")
email = "bro1223@gmail.com"
print(f"Your email is {email}")

#integers
age = 25
print(f"You are {age} years old")

#float
price = 19.23
print(f"The price is {price}")

#Boolean
is_online = True

if is_online:
    print(f"You are online")
else:
    print("You are offline")

#Type casting --> converting one data type to another--> explicit and implicit
gpa = 3.9
student = True

print(type(name))
print(type(age))
print(type(email))
print(type(price))
print(type(student))

#explicit = 
age = float(age)
print(age)
print(type(age))

age = int(gpa)
print(gpa)
print(type(gpa))

student = str(student)
print(type(student))

age = bool(age)
print(age)


#implicit 
x = 10
y = 2.3

x = x/y
print(x)