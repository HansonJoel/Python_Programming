# Creating a function
"""
A function is a set of codes that perform some tasks. They
are also useful if you find yourself writing the same code at several different points in your program. You can put that code in a function and call the function whenever you want to execute that
code
note: Always define your function first before you make a call statement.
syntax : def function_name():
					statements
"""
# Example 1
def greeting():
	print("Good morning")
	
greeting()  # this is a call statement

# Example 2
def print_hello():
	print("Hello")
	
print_hello()

# Example 3
def draw_square():
	print('*' * 15)
	print('*', ' '*11, '*')
	print('*', ' '*11, '*')
	print('*' * 15)
	
draw_square()
