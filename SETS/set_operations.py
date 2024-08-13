# SET OPERATIONS

set1 = {1, 2, 3}
set2 = {3, 4, 5}

"""
Union operation:
This combines all the element in all the set together
SYNTAX: sex1.union(set2) or variablename= set1|set2
""" 
union_set = set1 | set2  
un=set1.union(set2)

print(union_set)
print(un)

"""
intersection operation:
This finds the common element between the two sets
SYNTAX: set1.intersection(set2) or variablename = set1 & set2
"""
intersect = set1.intersection(set2)
print(intersect)


"""
Difference operation: 
This finds element that are in the first set but not in th second set
SYNTAX: set1.difference(set2) or variablename = set1 - set2
"""
difference = set1- set2
print(difference)

"""
Symmetrical differences:
Finds elements that are in the first set but not in the second.
SYNTAX: symmetric_difference_set = set1 ^ set2  or 
set1.symmetric_difference(set2)
"""
symmetric_difference = set1^set2
print(symmetric_difference)



# OTHER SET OPERATIONS
# issubset(): Checks if one set is a subset of another.
set3 = {1, 2}
print(set3.issubset(set1)) 

# issuperset(): Checks if one set is a superset of another.
print(set1.issuperset(set3))  

# clear(): Removes all elements from the set.
set1.clear()
print(set1)  # it becomes an empty sett
"""
Union operation:
This combines all the element in all the set together
SYNTAX: sex1.union(set2) or variablename= set1|set2
""" 
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1 | set2  
un=set1.union(set2)

print(union_set)
print(un)

"""
intersection operation:
This finds the common element between the two sets
SYNTAX: set1.intersection(set2) or variablename = set1 & set2
"""
intersect = set1.intersection(set2)
print(intersect)


"""
Difference operation: 
This finds element that are in the first set but not in th second set
SYNTAX: set1.difference(set2) or variablename = set1 - set2
"""
difference = set1- set2
print(difference)

"""
Symmetrical differences:
Finds elements that are in the first set but not in the second.
SYNTAX: symmetric_difference_set = set1 ^ set2  or 
set1.symmetric_difference(set2)
"""
symmetric_difference = set1^set2
print(symmetric_difference)



# OTHER SET OPERATIONS
# issubset(): Checks if one set is a subset of another.
set3 = {1, 2}
print(set3.issubset(set1)) 

# issuperset(): Checks if one set is a superset of another.
print(set1.issuperset(set3))  

# clear(): Removes all elements from the set.
set1.clear()
print(set1)  # it becomes an empty set
