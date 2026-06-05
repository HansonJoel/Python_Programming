# How to access element in dictionaries
"""
d = {0:"welcome",1:"what is your name", "Name": {"firstname":"Sam","Lastname":"Crew"}}

The dictionary above contains 3 keys (0,1 and "name"). we want to retrive the value of the key "name"
"""

d = {0:"welcome",1:"what is your name", "Name": {"firstname":"Sam","Lastname":"Crew"}}
print(d["Name"])


# if we want to retrieve just first value of the key "Name"
print(d["Name"]["firstname"])


# USING THE GET METHOD
"""
The get method is another method which can be used for retrieving values in the dictionary

Syntax: variablename.get(a)
where a is key to the value you want to access
"""

# Retrive value of the key(1) in the given dictionary above
print(d.get(1))
