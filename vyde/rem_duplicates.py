"""
Exercise 3: Remove duplicates (general version)

data = [1, 2, 2, 3, 4, 4, 4, 5]
Write code to create a new list with each number appearing only once, 
preserving the original order (first occurrence stays). Do not use set() 
(but later try with set to see the difference).
"""

data = [1, 2, 2, 3, 4, 4, 4, 5]

unique_data = []

for item in data:
    if item not in unique_data:
        unique_data.append(item)
print("This is with for loops ", unique_data)

while data:
    item = data.pop(0)
    if item not in unique_data:
        unique_data.append(item)
print("This is with While loop ", unique_data)