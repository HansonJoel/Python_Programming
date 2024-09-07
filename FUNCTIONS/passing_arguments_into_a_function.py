# Example1
def print_hello(n):
	print('Hello ' * n)
	
print_hello(3) # the value 3 is stored in the variable n
times = 2
print_hello(times)	

# Example 2 
# You can pass more than one argument into a function
def add_numbers(n1,n2):
	result = n1 + n2
	print = (" The sum is", result)
	
number1 = 5.4
number2 = 6.7

add_numbers(number1,number2)

# Example 3
"""Let's create a function that takes a user's name and age, and then prints a message."""
def greet_user(name, age):
    print(f"Hello {name}, you are {age} years old.")

# Getting input from the user
user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))

# Passing the input to the function
greet_user(user_name, user_age)


# Example 4
# if we want to print the sum of a list of input from the user
# we always define the function before you call
def add (numbers):
	total = 0
	for i in numbers:
		total = total + i
	print("The sum is", total)

values = (input("please enter a list of numbers separated by spaces: "))
number_list=list(map(int, values.split()))

add(number_list)
