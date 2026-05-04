fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

newlist_1 = [x for x in fruits if x != "apple"]
newlist_0 = [x.upper() for x in fruits]
newlist_4 = [x if x != "banana" else "orange" for x in fruits]

# function to create an iterable
newlist_2 = [x for x in range(10)]
newlist_3 = [x for x in range(10) if x % 3 == 0]

print(newlist)

print(newlist_1)
print(newlist_0)
print(newlist_2)
print(newlist_3)
print(newlist_4)