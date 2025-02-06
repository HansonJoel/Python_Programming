'''
Based on the temperature, suggest an appropriate outfit:

Below 50°F: Wear a jacket
50°F - 70°F: Wear a sweater
Above 70°F: Wear a t-shirt
Write a program that checks the temperature and prints the outfit suggestion.
'''
Temp = eval(input("Kindly enter your temperature in Farenheit: "))
if Temp >= 70:
    print("Wear a t-shirt")
elif Temp >=50 and Temp < 70:
    print("Wear a Sweater")
else:
    print("Wear a Jacket")