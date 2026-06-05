# Syntax
# round(number, digits)

# Parameter
# number = the number you want to round
# digits (optional) → how many decimal places to round to

# Rounding to the Nearest Whole Number
x = 4.6
print(round(x))

print(round(4.2))


# 2. Rounding to Decimal Places
# You can specify how many decimal places you want.

pi = 3.14159
print(round(pi, 2))  # 2 means keep 2 digits after the decimal point.

print(round(5.6789, 1))
print(round(8.999, 2))

# For integers
print('round(674, 2): ',round(674,2))

print('round(674, 0): ',round(674,0))
print('round(674, -1): ',round(674,-1))
print('round(674, -2): ',round(674,-2))
print('round(674, -3): ',round(674,-3))
print('round(674, -4): ',round(674,-4))
print('round(674.1012, -2): ',round(674.1012,-2))




