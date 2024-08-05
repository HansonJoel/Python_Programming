"""
Just like we can add tuples to list, we can also remove tuples from list

SYNTAX: listname.remove(a)
where a is the tuple to be removed
a accepts only one argument
"""
# Remove tuple (4,5,6) from the list below
LST = [(1,2,3),(4,5,6),"tuple inside a list"]
LST.remove((4,5,6))      # removed (4,5,6) from the given list
print (LST)
