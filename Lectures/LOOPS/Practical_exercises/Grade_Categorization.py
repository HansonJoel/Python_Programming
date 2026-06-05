'''
Grade Categorization:
A school system assigns grades based on test scores:

90 and above: A
80-89: B
70-79: C
Below 70: F
Write a program that takes a test score as input and returns the corresponding grade.
'''

score = int(input("Kindly enter student score: "))
if score >= 90:
    print(f"Your score is {score}, you have an A")
elif score >=80 and score <= 89:
    print(f"Your score is {score}, You have a B")
elif score >=70 and score <= 79:
    print(f"Your score is {score}, You have a C")
else:
    print(f"Your score is {score}, You have an F")
    
