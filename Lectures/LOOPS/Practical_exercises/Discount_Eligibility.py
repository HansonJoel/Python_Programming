'''
A store offers a 10% discount if a customer’s purchase exceeds $100. Write a Python program that checks if a customer is eligible for the discount based on the total amount of their purchase.
'''
purchase = eval(input("What is your total purchase: "))
if purchase < 100:
    print("You are not eleigible for a discount")
else:
    discount = ((10/100) * purchase)
    bill = purchase - discount
    print("You are eligible for a 10% discount")
    print(f"Your discount is ${discount}. \nKindly pay ${bill}")
