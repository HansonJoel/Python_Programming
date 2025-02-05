'''
To convert an integer e.g 12345 into a list of its individual digits, you can use the following methods:
List comparison method
map() method
'''

# List comparison method
numbers = 12345     # number to be converted to element of a list
string = str(numbers)   # first convert the numbers to string
num_list = [int(i) for i in string] 
# This iterates through the string "23456" treating each character ('2','3','4','5') as an individual element. int(i) convert each character(wich is a string) into an integer
print(num_list)


# map() method
number = 12345
num_list = list(map(int, str(number)))
#str(number) convert the integer to string
# map(int,str(number)) applies int() to each character
# list() convert the result into a list
print(num_list)

