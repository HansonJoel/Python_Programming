"""
Remove: This method removes the first occurance of an element from a list

SYNTAX: listname.remove(a)
where a is the element to be removed
note: a can only accepy one argument.

Example: we want to remove "Hello there" from the list below
num = [1,2,3,4,5,"Hello there","get","certified","get","ahead"]
"""

num = [1,2,3,4,5,"Hello there","Hello there","get","certified","get","ahead"]
num.remove("Hello there")
print(num)


