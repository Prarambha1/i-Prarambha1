#if = do some code only IF the condition is True
#Else = do something else

age= int(input("Enter your age: "))

if age >= 100:
    print("You are too old to sign up!")
elif age >= 18:
    print("Your are now signed up!!")
elif age<0:
    print("You havent been born yet!") 
else:
    print("You must be 18+ to sign up!")


print("-----------------------------------")
print()
print()
print("-----------------------------------")


#ask user if they want soem food
response = input("Would you like some food (Y/H)?")

if response == "Y":
    print("Here is your food!")
elif response == "N":
    print("No food for you!")
else:
    print("Invalid response!")


print("-----------------------------------")
print()
print()
print("-----------------------------------")


#input name
name = input("Enter your name: ")

if name == "":
    print("You did not type in your name!")
else:
    print(f"Hello, {name}! Welcome!")


print("-----------------------------------")
print()
print()
print("-----------------------------------")


#boolean
for_sale = True
if for_sale:
    print("This item is for sale!")
else:
    print("This item is not for sale!")


print("-----------------------------------")
print()
print()
print("-----------------------------------")

