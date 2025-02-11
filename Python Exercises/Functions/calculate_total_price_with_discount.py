'''
💡 Scenario: You are developing an online shopping platform. Create a function that calculates the total price after applying a discount of 10% for purchases greater than 500
'''

def calculate_total_price(price, discount_percentage=0):
    return price - ((discount_percentage/100)*price)
    

price = int(input("Kindly enter your Bill: "))

discount_percentage = 0
if price >= 500:
    discount_percentage = 10
    print("You have a 10% discount")
    
else:
    print("Sorry, you do not qualify for a discount")


Total_Bill = calculate_total_price(price, discount_percentage)
print(f"Your Total Bill is ${Total_Bill}")




    
