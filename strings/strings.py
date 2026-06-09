my_name = "Hill"
print("My name is: ", my_name)
print("Data type: ", type(my_name))
print(len(my_name))

course = "IT"
print("I'm persuing ", course)

# String methods- single line comment
""""
multple line comments
"""
print("any text")
country = "kenya"
print("My country is : ", country)

country_caps = country.upper()  # upper is the string method converts to upper case
print(country_caps)

# lower is the string method converts to lower case
country_lower = country_caps.lower()
print(country_lower)

# startswith
print(country_caps.startswith("K"))

# endswith
print(country_caps.endswith("Z"))

# replace method
print(country_caps.replace("KENYA", "TANZANIA"))

# strip method- used to clear whitespaces before and after a variable
dog = " Chiwawa "
print(dog)
print(dog.strip())

# rstrip - clears from the right side of the variable
print(dog.rstrip())

# lstrip - clear from the left side of the variable
print(dog.lstrip())
