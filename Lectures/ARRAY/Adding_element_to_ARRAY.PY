# How to add element to an array
"""
syntax: variable_name.append(a)
where a is the parameter to be added. it takes only one argument
"""

from array import *     # don't forget to always import array
arr = array ('i',[1,2,3,4])
print (arr)

arr.append(6)  # adding 6 to the array
print(arr)
