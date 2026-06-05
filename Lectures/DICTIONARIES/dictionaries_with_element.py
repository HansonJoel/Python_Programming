""" Dictionaries are made up of keys and values."""
# Example of dictionary with keys as integers

d2 = {1:"welcome", 2: "to", 3:"Python", 4:"Programming"}
print(d2)


# Example of dictionary with keys as strings
d3 = {"name":"Sam","Age":32, "Profession":"Surveyor"}
print(d3)



# Creating dictionary with element using the dict method
d4 = dict({1:"welcome", 2: "to", 3:"Python", 4:"Programming"})
print(d4)



"""
There is another method of creating dictionaries using the dict method by passing in keys and values as element of a list i.e as tuples within a list.
Here, we passing in a pair of element which are enclosed within the round brackets. Also you will see that the keys and values are not seperated by semicolon(:) but by commas(,)
"""

d5 = dict([(1,"welcome"),(2,"to"),(3,"Python"),(4,"tutorial")])
print(d5)

#
