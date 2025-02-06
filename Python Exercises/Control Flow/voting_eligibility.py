'''
Write a program to check if a person is eligible to vote. A person must be at least 18 years old to vote. Ask the user for their age and print if they can vote or not.
'''

age = int(input("Kindly enter your age: "))
if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")