# calculate BMI
weight = float(input('Kindly enter your weight in kg: '))
height = float(input('Kindly enter your height in meters: '))

bmi = round(weight/height ** 2)
print(f'Your BMI is {bmi}')


if bmi <= 1.85:
    print("You are underweight")
elif bmi <=25:
    print("You have Normal Weight")
elif bmi < 30:
    print("You are overweight")
elif bmi < 35:
    print("You are Obese")
else:
    print("You are Clinically Obeses")


