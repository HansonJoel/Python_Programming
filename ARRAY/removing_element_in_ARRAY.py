# Removing element from an array
"""
You can remove  element your array using the remove function
syntax: variable_name.remove(a)
where a is the parameter to be remove it takes only one argument
"""
from array import *
arr = array ('i',[1,2,3,4])
print (arr)


arr.remove(2)  # remove element at index 2
print(arr)
