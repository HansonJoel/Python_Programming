"""
Remember, tuples are immutable i.e we cannot add or remove elements to and from a tuple but we can modify the list within a tuple. This way, we can add and remove element to our list within tuples.
"""

#Example1: adding element to a list within tuple
tpl = (['a','b','c'],[1,2,3]) # tuple with 2 list items in it

tpl[0].append('d') 
print (tpl)

"""
tpl[0].append('d): tpl[0], accesses the first element [0] which is first index list in the tuple.
append('d'), adds d to the first list ['a','b','c']
"""


#Example2 : Removing element to a list within tuple          
tpl[0].remove('d')  # continuation from example1              
print (tpl)

"""                                                           tpl[0].remove('d'): tpl[0], accesses the first element [0] which is first index list in the tuple.
remove('d), removes 'd' to the first list ['a','b','c','d']
"""
