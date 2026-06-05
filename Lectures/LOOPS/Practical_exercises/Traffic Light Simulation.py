'''
Simulate a traffic light system. Depending on the color of the light (red, yellow, green), print the corresponding action:

Red: Stop
Yellow: Prepare to stop
Green: Go
Write a program that checks the light color and displays the appropriate action.
'''

Traffic_lights = ['red','yellow','green']
import random
sign = random.choice(Traffic_lights)
if sign == 'red':
    print("Light is RED → Stop")
elif sign == 'yellow':
    print("Light is YELLOW → Prepare to stop")
else:
    print("Light is GREEN → Go")