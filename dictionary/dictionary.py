"""
This module contains the Dictionary class, 
which is used to represent a dictionary of words and their definitions. 
The Dictionary class provides methods for adding, removing, and looking up words in the dictionary.
The Dictionary class is implemented as a subclass of the built-in dict class,
and it provides additional functionality for working with words and definitions. 
The Dictionary class can be used to create a dictionary of words and their definitions, 
and it can be used to look up the definition of a word, add new words and definitions, 
and remove words from the dictionary."""

car_model = {
    "brand": "Toyota",
    "model": "Camry",
    "year": 2020
}
print("car model: ", car_model)
print("datatype: ", type(car_model))
print("length: ", len(car_model))

# keys method- it returns a list of all the keys in the dictionary
car_model_keys = car_model.keys()
print("car model keys: ", car_model_keys)

# values method- it returns a list of all the values in the dictionary
car_model_values = car_model.values()
print("car model values: ", car_model_values)

# items method- it returns a list of all the key-value pairs in the dictionary
car_model_items = car_model.items()
print("car model items: ", car_model_items)

# updating a dictionary- it adds a new key-value pair to the dictionary
car_model["year"] = 2026
print("car model after update: ", car_model)

# adding a new key-value pair to the dictionary
car_model["color"] = "red"
print("car model after adding color: ", car_model)
car_model.update({"price": 30000})
print("car model after adding price: ", car_model)

# converting dictionary to list
car2 = list(car_model)
print("car2: ", car2)
print("datatype: ", type(car2))

# clearing a dictionary- it removes all the key-value pairs from the dictionary
car_model.clear()
print("car model after clearing: ", car_model)

# deleting a dictionary- it removes the dictionary from memory
# del car_model
# print("car model deleted: ", car_model)

# in operator- it checks if a key is in the dictionary
fruit = {
    "name": "apple",
    "color": "red"
}
if "name" in fruit:
    print("Key 'name' is in the dictionary")
else:
    print("Key 'name' is not in the dictionary")
