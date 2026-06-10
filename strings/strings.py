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

# example
my_name2 = "Henry Ford"
print("My name is : ", my_name2)  # My name is: Henry Ford

# how to slice from the start to the end
print(my_name2[2:])  # nry Ford 2:- fom second position upto the end
print(my_name2[3])
print(my_name2[:2])  # prints only the first two characters
# slices from the starting position 2 but not including the last position 6
print(my_name2[2:6])
cat_name = "characterdevelopment"
print(cat_name[2:7])

# split -returns a list
fruits = "apple,banana,mango"
print(fruits.split(","))

# formatting a string
number = "1000000000"
# convert to int first
formatted = "{:,}".format(int(number))
print(formatted)

num1 = 100000
# use comma as a separator
formatted_number = f"{num1:,}"
print("Comma separated number: ", formatted_number)  # 100,000

num2 = "1000000000"
formatted_num2 = "{:,}".format(int(num2))
print(f"number formated is : {formatted_num2}")
