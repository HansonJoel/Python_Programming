# How to create a set
# SYNTAX: variablename = set([a])
# where a is an argument. it can take only one argument

# Creating an empty set
empty_set = set()  # Note: {} creates an empty dictionary, not a set.
print(empty_set)  # Output: set()
print(type(empty_set))

# Creating a set from a list (duplicates are removed)
set_from_list = set([1, 2, 2, 3, 4])
print(set_from_list)  # Output: {1, 2, 3, 4}

# Creating a set using curly braces
my_set = {1, 2, 3, 4, 5}
print(my_set)  # Output: {1, 2, 3, 4, 5}
