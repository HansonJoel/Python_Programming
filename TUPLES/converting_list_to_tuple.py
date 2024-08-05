"""
Converting List to Tuples
when you create a list and you realise you don't want this list to be altered throughout the program, you convert the list into a tuple. Remember, tuples are immutable.

SYNTAX: variablename = tuple(a)
where a is the list you want to convert to tuple

Example, we have a list called LST and want to convert it to tuple
"""

LST = [1,2,3,4]
tpl = tuple(LST) # This convert LST to tuple and saves in tpl
print(tpl)      # tpl now holds the values of lST as tuple
