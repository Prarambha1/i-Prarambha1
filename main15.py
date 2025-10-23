#2D collections
fruits =  ["apple", "banana", "cherry"]
vegetables = ["carrot", "potato", "cucumber"]
meats = ["chicken", "beef", "pork"] 

groceries = [fruits, vegetables, meats]

for collection in groceries:
    for food in collection:
        print(food, end=" ")
    print()

#exercise:
num_pad = ((1, 2, 3),
           (4, 5, 6),
           (7, 8, 9),
           ("*", 0, "#"))

for row in num_pad:
    for num in row:
        print(num, end=" ")
    print()     