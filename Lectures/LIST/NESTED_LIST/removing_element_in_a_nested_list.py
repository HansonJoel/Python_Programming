numbers_list= [
    [1,2,3],
    [4,[20,-10,15],-5,6],     
    [7,8,9]
]

numbers_list[1].remove(-5) # This will remove -5 from the list
print(numbers_list)

numbers_list[1][1].remove(-10)
print(numbers_list)  # This will remove -10 from the nested list


