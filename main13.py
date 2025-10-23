#collection  =  single "variable" used to store values
# list = [] ordered and changeable, Duplictes allowed
# tuple = () ordered and unchangeable, Duplictes allowed, faster than list
# set = {} unordered and unindexed, no Duplictes allowed


fruits = ["apple", "banana", "cherry"]
#print(dir(fruits))
#print(fruits[0::-1])
#print(len(fruits))
#print("apple" in fruits) #True
#for fruit in fruits:
    #print(fruits)
fruits.append("orange") #add to the end
fruits.insert(1, "blueberry") #add to specific index
fruits.remove("banana") #remove specific item
fruits.pop() #remove last item
fruits.sort() #sort the list
fruits.reverse() #reverse the list
fruits.clear() #clear the list
print(fruits)


#tuples
coordinates = (4, 5)
print(coordinates[0])
#coordinates[0] = 10 #error, tuples are unchangeable
print(coordinates)
#sets
my_set = {"apple", "banana", "cherry"}
my_set.add("orange") #add item
my_set.remove("banana") #remove item
my_set.clear() #clear the set
print(my_set)


#dictionaries
my_dict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
print(my_dict["name"])
my_dict["age"] = 31 #change value
my_dict["country"] = "USA" #add item
my_dict.pop("city") #remove item
my_dict.clear() #clear the dictionary
print(my_dict)
print(dir(my_dict))
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())
print(len(my_dict))
for key, value in my_dict.items():
    print(f"{key}: {value}")


