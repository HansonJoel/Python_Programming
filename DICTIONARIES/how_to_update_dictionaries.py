# How to update a dictionary

"""
d = {0:"welcome",1:"what is your name", "Name": "Sam"}
From the dictionary (d) above, we want to update the value of "name" by adding firstname and lastname
"""

d = {0:"welcome",1:"what is your name", "Name": "Sam"}
print(d)
d["Name"] = {"firstname":"Sam","Lastname":"Crew"}
print(d)

