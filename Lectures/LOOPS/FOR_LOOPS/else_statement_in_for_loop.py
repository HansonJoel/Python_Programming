''''
The else statement specifies a block of code to be executed once a loop has executed successfully
'''

for i in range(6):
    print(i)
else:
    print("Finally finished")



# If you break the loop before the else statement, the else statement wont execute
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")