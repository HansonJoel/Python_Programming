# Numeric dataypes: Represent whole numbers, positive or negative without a decimal point
x = 10    # int
print(type(x))

y = 3.14
print(type(y))    # float

z = 2 + 3j
print(type(z))     # complex

# sequence type
name = "jenny"
print(type(name))     # string

fruits = ['apple','banana','orange']
print(type(fruits))    # list

# Mapping Type
student = {'name':'jenny', 'age':22, 'grade':'A'}
print(type(student))   # dictionary

# Set Types : An unordered collection of unique items, sets are mutable and do not allow duplicate values
unique_numbers ={1,2,3,4}
frozen_numbers = frozenset

# Boolean Types: Represent one of 2 values either true or false

