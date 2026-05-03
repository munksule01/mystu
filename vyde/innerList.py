"""
Exercise 5: Inner list – average of sublists

matrix = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
For each inner list, calculate its average and store those averages in a new list averages. Print averages.

matrix = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
innerList = []
averages = []

for num in matrix:
    innerList.append(num)
    avg = sum(num) / len(num)
    averages.append(avg)

print(innerList)
print("Average list:", averages)
"""

matrix = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
averages = []

for row in matrix:
    avg = sum(row) / len(row)
    averages.append(avg)

print("Averages: ", averages)

# Short form

average_list = [sum(row) / len(row) for row in matrix]
print(average_list)

