"""
List Items
List items are ordered, changeable, and allow duplicate values.

List items are indexed, the first item has index [0], the second item has index [1] etc.

So it uses first come first serve and last in last out
and it also allow duplicates
"""

thisList = ['Apple', 'Banana', 'Cherry', 'Mango']

thisList[1:3] = ["watermelon"]

thisList.insert(2, 'Grapes')
print(thisList)
print(type(thisList))

myList = ['Apple', 4, True, False, 0, 6j, 'Banana', 'Mango']

myList[4] = 'Cherry'
myList.insert(3, 'Grapes')

print(len(myList))
print(myList)

myList[3:9] = ['Grapes', 'Pineapple', 'Watermelon', 'Strawberry', 'Blueberry', 'Raspberry']
print(myList[3:9])


if 'Cherry' in myList:
    print('Yes, Cherry is in the list(myList)')
elif 'Cherry'in thisList:
    print('Yes, Cherry is in the list(thisList)')
else:
    print('No, Cherry is not in the list');


theList = ['Apple', 'Banana', 'Cherry', 'Mango']
HeList = ['Pineapple', 'Strawberry', 'Blueberry', 'Raspberry']
thisTuple = ('Ama', 'Kofi', 'Kwame', 'Esi')

theList.append('Yellow Melon')
HeList.append('Dawadawa')


print(theList)
print(HeList)
print(thisTuple)

theList.extend(thisTuple)
print(theList)

HeList.extend(theList)
print(HeList)

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])