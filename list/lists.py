''''
list are ordered, changeable, allow duplicates, are indexed and created using square brackets
'''
fruits = ["banana", "mango", "orange", "dragonfruit", "watermelon"]
print(f"list of fruits: {fruits}")
print(f"data type: {type(fruits)}")
print(f"the 4th fruit is : {fruits[3]}")

# slice
print(fruits[2:])
print(fruits[1:3])

# copy method - it copies all arrays from one variable to another variable
fruits2 = fruits.copy()
print(fruits2)
print(fruits)

# extend method- adds a specific value at the end of an array, must add a variable name
fruits3 = ["strawberry", "pears", "guava"]
fruits2.extend(fruits3)
print("fruits extended: ", fruits2)

# Append method- adds value at the end of a list
fruits2.append("cucumber")
print(fruits2)

# insert method - it takes the position then the item
fruits2.insert(2, "pears")
print(fruits2)

# index method - checks the position of an item
print(fruits2.index("orange"))

# count method- returs the occarence of an item
print(fruits2.count("pears"))
