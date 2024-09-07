# Return Statement
"""The return statement specifies what value or result should be sent back to the caller. Here, the call statement is replaced with the keyword "return". 
The returned value is not displayed except you choose to print out the value """


# Example 1 
"""
function to add two numbers, the return statement would send back the sum.,"""

def add(a, b):
    return a + b
result = add(3, 5)  # result will be 8


# Example 2
""" Return statement can also be used to exit a function"""
def check_even(num):
    if num % 2 == 0:
        return True
    return False
    
print(check_even(4))  # Output: True and the code is skipped

# Example 3
def greet(name):
	print("Hello ",name)
	return  # This code exit at this point and returns to call
	print("How do you do?")
	
greet("jack") # only the first print statement is executed
