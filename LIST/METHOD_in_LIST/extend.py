"""
Extend: This method allows you add an entire list to another list
SYNTAX: listname.extend(a)
where a is the list to be added. 
note: you can only add one list into the parameter(a)
e.g we have an exiting list num = [1,2,3,4]
new list to be added stg = [5,"get","certified","get","ahead"]
"""

num = [1,2,3,4]
stg = [5,"get","certified","get","ahead"]
num.extend(stg)
print(num)
