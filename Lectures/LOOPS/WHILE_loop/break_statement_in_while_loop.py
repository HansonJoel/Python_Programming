'''
The braek statement can be used in while loop to stop the loop even if the while condition is true. Example;
'''

i = 1
while i < 6:
    print(i, end=" ")
    if i == 4:
        break
    i += 1