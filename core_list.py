"""
List Items
List items are ordered, changeable, and allow duplicate values.

List items are indexed, the first item has index [0], the second item has index [1] etc.

So it uses first come first serve and last in last out
and it also allow duplicates
"""

thisList = ['Apple', 'Banana', 'Cherry', 'Mango']

print(type(thisList))

myList = ['Apple', 4, True, False, 0, 6j, 'Banana', 'Mango']

myList[4] = 'Cherry'

print(len(myList))
print(myList)
print(myList[3:9])


if 'Cherry' in myList:
    print('Yes, Cherry is in the list(myList)')
elif 'Cherry'in thisList:
    print('Yes, Cherry is in the list(thisList)')
else:
    print('No, Cherry is not in the list');