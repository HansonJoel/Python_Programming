# HOW TO DELETE ELEMENTS IN DICTIONARY
"""
There are 2 ways in deleting elements in dictionaries
1. del method 
2. .pop method
3. .popitem
"""


# del method
# SYNTAX: del variablename[a]
# where a is the key to be deleted
# Delete key(0) from the given element below


d = {0:"welcome",1:"what is your name", "Name": {"firstname":"Sam","Lastname":"Crew"}}

del d[0]
print(d) # this removes "welcome" from the dictionary


# d.pop method
# SYNTAX: variablename.pop(a)
# where a is the key to be deleted
# delete key(1) # This delete "what is your name" 

d.pop(1)
print(d)



# d.popitem
# SYNTAX: d.popitem()
"""with del and .pop method, we specify the element we want to delete but with the d.popitem(), we do not specify the element because it always delete the last element in the dictionary.see example below."""

d1 = {0:"welcome",1:"what is your name", "Name": {"firstname":"Sam","Lastname":"Crew"}}
d1.popitem()  # This deletes the last item "Name"
print(d1)

