# sets
"""
A set is an unordered collection of unique elements.
They are un ordered,unchangerable and unindexed.
no duplicates are allowed in a set.
its created using {}
"""

set1 = {"apple", "banana", "cherry"}
print("set1: ", set1)
print("datatype: ", type(set1))

set2 = {"mango", "orange", "banana"}
print("set2: ", set2)

# union method- it combines two sets and removes duplicates
set3 = set1.union(set2)
print("set3: ", set3)

set4 = set1 | set2
print("set4: ", set4)

# intersection method- it returns the common elements in both sets
set5 = set1.intersection(set2)
print("set5: ", set5)
set6 = set1 & set2
print("set6: ", set6)

# difference method- it returns the elements that are in set1 but not in set2
set7 = set1.difference(set2)
print("set7: ", set7)

set8 = set1 - set2
print("set8: ", set8)

# symmetric_difference method- it returns the elements that are in set1 or set2 but not in both
set9 = set1.symmetric_difference(set2)
print("set9: ", set9)

# copy method- it returns a copy of the set
set10 = set1.copy()
print("set10: ", set10)

# pop method- it removes a random item from the set
set1.pop()
print("set1 after pop: ", set1)

# remove method- it removes the specified item from the set
set1.remove("cherry")
print("set1 after remove: ", set1)
