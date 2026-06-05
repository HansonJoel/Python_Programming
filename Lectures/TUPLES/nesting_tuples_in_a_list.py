"""
Just like we can nest tuples with tuples, we can also nest tuples within a list. Now, tuples are immutable but list are mutable, so we can add as many tuples as we like inside of a list

SYNTAX: listname.append(a)
where 
listname is the list which the tuples will be added
a is the tuple to be added to the list
note: a takes only one argument
see examples, below
"""
LST = [(1,2,3),(4,5,6)] # here is a list with 2 tuples in it
print(LST)

# how to add tuples to the above list(LST)
LST.append("tuple inside list")
print(LST)
