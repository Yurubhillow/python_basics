""""
if statements in python are used to make decisions based on conditions.
The most common if statement is the simple if statement,
which executes a block of code if a specified condition is true.
The if statement can also be used in conjunction 
with the else and elif statements to create more complex
"""
a = 10
b = 20
if a >= b:
    print("a is greater than or equal to b")
else:
    print("a is less than b")

print("a is greater than b") if a > b else print(
    "a is less than or equal to b")

# elif statement- it is used to check multiple conditions
num1 = 10
num2 = 20
if num1 > num2:
    print("num1 is greater than num2")
elif num1 < num2:
    print("num1 is less than num2")
else:
    print("num1 is equal to num2")

# and operator- it is used to check if two conditions are true
num3 = 30
num4 = 40
if num3 > num4 and num3 < 50:
    print("num3 is greater than num4 and less than 50")
else:
    print("num3 is not greater than num4 or not less than 50")

# or operator- it is used to check if at least one condition is true
num5 = 50
num6 = 60
if num5 > num6 or num5 < 70:
    print("num5 is greater than num6 or less than 70")
else:
    print("num5 is not greater than num6 and not less than 70")
