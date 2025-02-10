'''
Some functions can receive so many argument and you might not know the number the number of argument to be passed into it. 
If you do not know the number of Arguments that will be passed into your function, you will have to add a * before the parameter name in the function definition.
The function will receive the arguments as tuples, and can access the items accordingly:

Arbitrary Arguments are often shortened to *args in Python documentations
'''

def multiple_itemns(*args):    # You can use any name aside args
    print(args)
    print(type(args))    # This will display the data type of this function as tuple


names = input("Kindly enter your Full names: ")  # Requested the fullname from the user

multiple_itemns(names)  # Passed in the fullname into the function (multiple_items)


# Example 2 
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

