# String Methods (.upper(), .lower(), .replace(), .strip())
# F-strings
# Operators
from base64 import encode
import random

print(random.randrange(1, 10))

x = 3j
y = 6.07

print(type(x))

l = int(y)

print(l)
print(type(x))

for x in 'banana':
    print(x)

m = 'mango'
print(len(m))

n = 'Life is full of surprises'


if 'surprises' in n:
    print('surprises is in n')
else:
    print('or is not in n')

g = 'finally, its over'
print(g[2:7])

print(g.replace('finally', 'at last'))
print(g.capitalize())
print(g.upper())
print(g.lower())
print(g.split())

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)
print(txt.encode('utf-8'))

print(10 > 9)
print(10 == 9)
print(10 < 9)

# Finding the position of a character or letter
# Searching for words in a sentence
# finding the length of a word
# Looping through a word
# Slicing a word
# All this together how to utilize these as a backend dev and a cloud engineer