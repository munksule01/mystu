"""
Exercise 1: Basic list operations

Start with numbers = [5, 12, 7, 3, 25, 18, 9]. 
Do the following without using built-in functions like min() or max() (write your own logic):

· Find and print the smallest number.
· Find and print the largest number.
· Print the sum of all numbers.

"""

min_maxList = [5, 12, 7, 3, 25, 18, 9]

# Find the smallest number
smallest = min_maxList[0]  # Start with the first element as the smallest
for num in min_maxList:
    if num < smallest:
        smallest = num

# Find the largest number
largest = min_maxList[0]  # Start with the first element as the largest
for num in min_maxList:
    if num > largest:
        largest = num

# Print the sum of all numbers
total = 0
for num in min_maxList:
    total += num

print(f"Smallest number: {smallest}")
print(f"Largest number: {largest}")
print(f"Sum of all numbers: {total}")
