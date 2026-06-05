# Write a program that calculate and displays the number of days, weeks and months you have left to live until 90 years old. Get the input from the user.

life_expectancy = int(input('How many Years do you want to live? '))
age = int(input('What is your current age: '))


years_left = life_expectancy - age;
days_left = years_left * 365
weeks_left = years_left * 52
months_left = years_left * 12

print(f"You have {days_left} days, {months_left} months and {weeks_left} weeks left, if you are to live for {life_expectancy} years ")


