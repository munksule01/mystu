"""
Exercise 4: Even and odd split

values = [23, 44, 57, 68, 91, 12, 33, 78]
Loop through and put even numbers into one list 
called evens and odd numbers into odds. Then print both lists.
"""

values = [23, 44, 57, 68, 91, 12, 33, 78]

evens = []
odds = []

for num in values:
    if num % 2 == 0:
        evens.append(num)
    else:
        odds.append(num)

print("Even Numbers: ", evens)
print("Odd Numbers: ", odds)