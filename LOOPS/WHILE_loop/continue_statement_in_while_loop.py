'''
Unlike the break statement, the continue statement is used to stop the current iteration(i.e jump an iteration) and continue with the next
'''

# continue to the next itearation if i is 3:
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue    # This will skip when i=3 and continue at 4
    print(i)

    # we did the incrementation before applying the continue statement to catch i=3

