'''
Instead of passing the output on the conosole or terminal, you can decide to return the value to the function using the return value
'''
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))


# Example 2
def sum(num1=0,num2=0):
    return (num1 + num2)    # this will return the result to the function


total = sum(2,3)
print(total)