""""
it stores multiple items in a single variable
Allows duplicates,indexed, ordered and unchangeable.
its created using ()
"""
fruits = ("apple", "banana", "cherry")
print("fruits: ", fruits)
print("datatype: ", type(fruits))

# getting length of a variable using len() function
print("length: ", len(fruits))

# converting list to tuple
fruits2 = ["mango", "orange"]
print("list of second fruits: ", fruits2)
print("datatype of list 2: ", type(fruits2))
fruits3 = tuple(fruits2)
print("fruits 3: ", fruits3)
print("fruits 3 datatype: ", type(fruits3))

# slicing a tuple
print(fruits[0:2])  # slices from position 0 but excludes position 2
fruits4 = list(fruits)
print("fruits 4: ", fruits4)

fruits4.append("cucumber")
print("fruit 4: ", fruits4)

# remove method- it removes the first occurance from a list
# remove cucumber from the list
# fruits4.remove("cucumber")
# print("fruits 4 removemed: ", fruits4)

# pop method- it removes specified item using its indexed
# if the index is not specify it removes the last item from the list
# print(fruits4.index("banana"))
# fruits4.pop(1)
# print("remaining fruits: ", fruits4)

# del()- deletes the list completely
# del fruits4
# print("fruits4 deleted: ", fruits4)

# clear method- it empties the list content and not the list itself
# fruits4.clear()
# print("empty list: ", fruits4)

# converting back list to tuple
fruits5 = tuple(fruits4)
print("fruits4 bact to tuple: ", fruits5)

"""
unpacking tuples- extract the values back to variable
numbers of variables must match the number of values in a tuple
if not you must use the asteric *
"""
(green, yellow, blue, pink) = fruits5
print("green: ", green)
print("yellow: ", yellow)
print("blue: ", blue)
print("pink: ", pink)

# unpack using asteric*
(red, *orange) = fruits5
print("red : ", red)
print("orange :", orange)
