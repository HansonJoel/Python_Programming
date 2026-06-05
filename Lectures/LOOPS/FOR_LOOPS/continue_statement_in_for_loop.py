''''
The continue statement is used to stop the current iteration in the loop (jump an item) and continue with the next item
'''
# Do not print banana

Fruits = ['apple','banana','cherry','orange']
for i in Fruits:
    if i == 'banana':
        continue
    print(i)
