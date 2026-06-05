"""
An f-string (formatted string literal) is a way to insert variables or expressions directly into a string. It was introduced in Python 3.6 and is the most common way to format strings today.
"""
# syntax: f" {expressions}"



# insering values
name = 'Alice'
age = 30
print(f"Hello, my name is {name}, i am {30} years old")


# Evaluating Expressions
width = 5
height = 10
area = f"The area of a rectangle is {width * height} square meters"
print(area)


# formatted Numbers
price = 49.9876
print(f"Price: {price:.2f}")

# Calling function
name = 'John Doe'
print(f"My name is {name.upper()}")

