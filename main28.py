

# *args = allows you to pass multiple non-key arguments
# **kwargs = allows you to pass multiple keyword arguments
# unpacking operator
# 1. positional 2. default 3. keyword 4. arbitrary

def add(*nums):
    total = 0
    for num in nums:
        total += num
    return total

print(add(1, 2, 3, 4, 5))

def display_name(*args):
    for arg in args:
        print(arg, end=" ")
    print()

display_name("Dr.", "Spongebob", "Harold", "Squarepants", "III")

#exercisee
def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_address(street="123 Fake St.", city="Detroit", state="MI", zip="54321")


#exercisee222
def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()

    if "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    else:
        print(f"{kwargs.get('street')}")

    print(f"{kwargs.get('city')} {kwargs.get('state')}, {kwargs.get('zip')}")

shipping_label(
    "Dr.", "Spongebob", "Squarepants",
    street="123 Fake St.",
    pobox="1002",
    city="Detroit",
    state="MI",
    zip="54321"
)