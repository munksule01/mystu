"""
Exercise 2: Reverse without .reverse() or slicing

items = [10, 20, 30, 40, 50]
Create a new list that contains the same elements in reverse order (e.g., [50, 40, 30, 20, 10]) using a loop.

NB: 
for i in range(len(items)):
    print(items[0:i])
"""

items = [10, 20, 30, 40, 50]

i = len(items) - 1
reverse_items = []
while i >= 0:
    reverse_items.append(items[i])
    i -= 1

print(reverse_items)

i = -1
reverse_items = []
for i in range(len(items)):
    reverse_items.append(items[len(items) - 1 - i])

print("This is with for loops ", reverse_items)