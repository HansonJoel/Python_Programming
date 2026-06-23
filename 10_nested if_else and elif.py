# nested if_else statement

age = int(input(f' What is your age: '))
has_id = True

if age >= 18:
    if has_id:
        print('You can enter the Club')
    else:
        print(f"Kindly provide an ID")
else:
    print("You are too young to enter the Club")




# Nested if_elif_else Statement

height = int(input('Kindly enter your height in feets: '))

if height >=3:
    print('You can ride')
    age = int(input('What is your age: '))
    if age < 12:
        print ('Pay 150')
    elif age <= 18:
        print('Pay 250')
    else:
        print('Pay 500')
else:
    print('You can\'t ride')



