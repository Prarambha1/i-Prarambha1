capitals = {
    "USA": "Washington D.C.",
    "India": "New Delhi",
    "China": "Beijing",
    "Russia": "Moscow"
}

# print(dir(capitals))
# print(help(capitals))
# print(capitals.get("Japan"))

if capitals.get("Russia"):
    print("That capital exists")
else:
    print("That capital doesn't exist")


# Update/add/remove items in the dictionary
capitals.update({"Germany": "Berlin"})
capitals.update({"USA": "Detroit"})
capitals.pop("China")
capitals.popitem()
# capitals.clear()

# Get all keys
keys = capitals.keys()
print(keys)

for key in capitals.keys():
    print(key)

# Get all values
values = capitals.values()
print(values)

for value in capitals.values():
    print(value)

# Get all items
items = capitals.items()
for key, value in capitals.items():
    print(f"{key}: {value}")