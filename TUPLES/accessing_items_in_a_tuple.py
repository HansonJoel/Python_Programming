"""
How to access/extract a particular item and range of items in tuples
"""

# Example1: extract the item "Uyo" from the list
list = "Abuja","Lagos","Uyo","calabar", 1,2,3,4,5,"Niger"

print(list[2])

# Example2: extract the range of number 1-5 from the list
print(list[4:8])


# Example3: extract all the even numbers from the list below
numbers = 0,1,2,3,4,5,6,7,8,9,10
print(numbers[2::2])
