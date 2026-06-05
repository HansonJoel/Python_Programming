# Type Casting

print('10'+'10')

print(int('10') + int('10'))

length = len('Jenny khatri')
print('Your name has '+ str(length) + ' characters')

# Exercise: write a program that accepts a 2 digit number from the user and print the sum of the 2 numbers

number = input('Kindly enter a 2 digit number: ')
first_number = int(number[0])
second_number = int(number[1])
sum = first_number + second_number
print('The sum of the numbers you entered is', sum)