"""
Nesting: This is an operation that allows you to create a tuple within another

SYNTAX: variablename = (a,b,c...)
where a,b,c... are tuples to be nested 
"""

#Example1: nest the tuples city and numbers below
city = "Abuja","Lagos","Uyo","calabar"
numbers = 1,2,3,4,5

nest = (city,numbers)
print(nest)
