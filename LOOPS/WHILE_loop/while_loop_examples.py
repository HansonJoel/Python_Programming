# Example1
""" 
write a program that ask the user to enter a multiple of 7 and the program keep running until a multiple of 7 is entered"""

var = int(input("Enter a multiple of 7: "))
while var%7 != 0:
	var = int(input("Enter a multiple of 7: "))
else:
	print("%d is a multiple of 7" %var)

# Example2
""" write a program that take input from a user and calculate temperature in fahrenheit. The user exit the program once -1000 is being inputted
"""
temp = 0
while temp != -1000:
	temp = eval(input("Enter a temperature (-1000 to quit): "))
	if temp != -1000:
		print('In Fahrenheit that is', 9/5*temp+32)
	else:
		print("Bye")

# Exercise 3
""" "print Hello world" 10 times """
i = 1
while i <= 10:
	print("Hello World")
	i+=1


# Exercise 4
i = 10
while i > 1:
	print("Learning Python")
	i-=1

# Exercise 5
""" Calculate the sum of the first 10 natural numbers"""
sum = 0
i = 1
while i <= 10:
	sum = sum + i
	i+=1
print(sum)

# Exercise 6
""" Print the sum of the even numbers between 1 and 10"""
i=1
sum = 0
while i <= 10:
	if i%2 ==0:
		sum = sum + i
	i+=1
print(sum)


# Exercise 7
""" This exercise receives input of numbers from the user, and reverses the given integer i.e if i input 5678 i should output 8765"""
n= int(input("Enter a range of numbers: "))
nr= 0
while n%10 != 0:
	c = n%10
	nr = nr *10 + c
	n = n//10
print(nr)

# Exercise 8
"""
How to calculate the length of a list using the while loop and not the len function"""
x = [1,2,3,"Python"]
length = 0
i=1
try:
	while x[i]:
		length = length + 1
		i+=1
except IndexError:
	print(length)
