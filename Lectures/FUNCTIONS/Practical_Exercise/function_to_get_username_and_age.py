# Example 1
"""Let's create a function that takes a user's name and age, and then prints a message."""
def greet_user(name, age):
    print(f"Hello {name}, you are {age} years old.")

# Getting input from the user
user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))

# Passing the input to the function
greet_user(user_name, user_age)
