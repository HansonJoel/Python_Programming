'''
We can set a default parameter value to a function, so that if we call a function without argument, it uses the default parameter value that has been set
'''

def my_function(country = "Norway"):  # assigned a default value (norway) to the country parameter
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()                        # This will output the default parameter value  
my_function("Brazil")