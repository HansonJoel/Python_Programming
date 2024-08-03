mix = [1,6,'simplilearn', 'get', 'cerified']
letters = ['a','b','c','d','e','f','g','h']

"""Example 1: Extract the first 3 elements from the mix list"""
print(mix[:3]) 
# or
print(mix[0:3])


"""Example 2: Extract the element from "simplilearn" to the end of the mix list"""
print(mix[3:])

# Example 3: Extract "simplilearn" and "get" from the mix list
print (mix[2:4])

# Example 4: print mix list in reverse order
print(mix[::-1])


""" Example 5 : Extract every element from the letters list at interval of 2"""
print(letters[::2])


""" Example 6: Starting from "b", extract every element from the letters list at interval of 2"""
print (letters[1::2])
