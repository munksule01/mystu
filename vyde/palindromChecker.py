"""
Exercise 6: Palindrome checker in a list

words = ["radar", "hello", "level", "world", "racecar"]
Create a new list called palindromes containing only the words that read the same forwards and backwards. 
Hint: compare word to word[::-1].
"""

words = ["radar", "hello", "level", "world", "racecar"]

palindrome = []

for word in words:
    if word == word[::-1]:
        palindrome.append(word)
print(palindrome)
