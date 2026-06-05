"""
insert: This method allows you place an element into a specific location in between a list

SYNTAX: listname.insert(a,b)
where a is the index position to be inserted
where b is the element/parameter to be inserted
note: insert method allows only one index and one parameter

Example, we have a list
num = [1,2,3,4,"get","certified","get","ahead"] and we want to insert the word "Hello" at index 4, we use the insert method
"""
num = [1,2,3,4,"get","certified","get","ahead"]
# SYNTAX: listname.insert(a,b)
num.insert(4,"Hello")
print(num)


