"""
Exercise 7: Shift elements

letters = ['a', 'b', 'c', 'd', 'e']
Write code to shift all elements one position to the right, with the last element wrapping around to the front. 
Result should be: ['e', 'a', 'b', 'c', 'd']. Do this without using collections.
deque – use list slicing and concatenation.
"""

letters = ['a', 'b', 'c', 'd', 'e']

letters = letters[-1:] + letters[:-1]

print(letters)