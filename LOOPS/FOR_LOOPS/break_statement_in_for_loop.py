'''
The break statement is used in the for loop to stop the loop before it loops through all the items
'''

# Exit the loop when i is 'cherry'
fruits = ['cherry','banana','cherry','orange']
for i in fruits:
    print(i)
    if i == 'cherry':
        break

'''
The first example above, is not satisfactory because if 'cherry' is the first item on the it will still output 'cherry' and we do not want to output cherry. so it is advicable we use the break statement before  we print
'''
                     # OR

#In this example, the break comes before the print
'''
fruits = ['apple','banana','cherry','orange']
for i in fruits:           
    if i == 'cherry':
        break
    print(i)

'''