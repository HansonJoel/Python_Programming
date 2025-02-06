'''
A shipping company charges different rates for packages:

Standard shipping: $5 for packages under 10 lbs,
$10 for packages 10-20 lbs,
$15 for packages over 20 lbs.
Write a program that takes the weight of a package as input and returns the shipping cost.
'''

weight = int(input("Kindly enter your weight in kg: "))

if weight <= 5:
    print(f"Your weight is {weight} \n Kindly pay $5")
elif weight >= 10 and weight <= 20:
    print(f"Your weight is {weight} \nKindly pay $10")
else:
    print(f"Your weight is {weight} \nKindly pay $15")