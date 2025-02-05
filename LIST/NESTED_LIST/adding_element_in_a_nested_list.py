'''
You can use the standard method like append() and extend() to add element in a list
'''
numbers_list= [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
numbers_list.append([2])
numbers_list.append([2,3,4,5])
numbers_list.extend([2,3,4,5]) 


# Nesting a list inside another list
numbers_list[1].insert(1,['a','b','c'])

print(numbers_list)