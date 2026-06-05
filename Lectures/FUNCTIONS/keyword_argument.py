'''
You can also send argument with the key=value syntax

Here, the 
'''
def multi_named_items(kwargs):
    print(kwargs)
    print(type(kwargs))

multi_named_items(fname = "Joel", lname= "Hanson")


# Example 2 
'''
If you do not know the number of keyword argumemt that will be passed into the function, add two asterisk: ** before the parameter name in the function
The function will receive the arguments as dictionary, and can access the items accordingly:
'''

def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

