""" You can replace multiple items in a list all at once""" 

players = [29,58,68,71,87,120]

""" i want to substitute the first 3 numbers in the players list (29,58,68) with 1,2,3"""


players [:4] = [1,2,3,4]
print (players)

# Description of what the following code does
"""
This takes the items from index 0 to 3 in the players list
and substitutes it with 1234.
"""


""" 
you can also remove the items. in this example, the first 2 index will be replaced with empty bracket []
"""
players [:2]= []
print(players)


"""
You can also delete the players list making it an empty list
"""
players [:] = []
print(players)
