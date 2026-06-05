'''
A nested loop is a loop inside a loop
The "INNER LOOP" will be executed one time for each itearation of the "OUTER LOOP"
'''

food = ['rice','beans','soup']
fruits = ['orange','banana','apple']

for i in food:
    for j in fruits:
        print(i,j)