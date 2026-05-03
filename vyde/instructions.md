🧠 General List Exercises

Exercise 1: Basic list operations

Start with numbers = [5, 12, 7, 3, 25, 18, 9]. Do the following without using built-in functions like min() or max() (write your own logic):

· Find and print the smallest number.
· Find and print the largest number.
· Print the sum of all numbers.

// Done

Exercise 2: Reverse without .reverse() or slicing

items = [10, 20, 30, 40, 50]
Create a new list that contains the same elements in reverse order (e.g., [50, 40, 30, 20, 10]) using a loop.

// Done

Exercise 3: Remove duplicates (general version)

data = [1, 2, 2, 3, 4, 4, 4, 5]
Write code to create a new list with each number appearing only once, preserving the original order (first occurrence stays). Do not use set() (but later try with set to see the difference).

// Done

Exercise 4: Even and odd split

values = [23, 44, 57, 68, 91, 12, 33, 78]
Loop through and put even numbers into one list called evens and odd numbers into odds. Then print both lists.

// Done

Exercise 5: Inner list – average of sublists

matrix = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
For each inner list, calculate its average and store those averages in a new list averages. Print averages.

Exercise 6: Palindrome checker in a list

words = ["radar", "hello", "level", "world", "racecar"]
Create a new list called palindromes containing only the words that read the same forwards and backwards. Hint: compare word to word[::-1].

Exercise 7: Shift elements

letters = ['a', 'b', 'c', 'd', 'e']
Write code to shift all elements one position to the right, with the last element wrapping around to the front. Result should be: ['e', 'a', 'b', 'c', 'd']. Do this without using collections.deque – use list slicing and concatenation.

Exercise 8: Find pairs that sum to target

nums = [2, 4, 3, 5, 7, 8, 1], target = 9
Print all unique pairs (order doesn't matter) from nums that add up to 9. Example output: (2,7), (4,5), (8,1). Avoid printing duplicate pairs like (2,7) and (7,2).

Exercise 9: Most frequent element

colors = ["red", "blue", "red", "green", "blue", "blue", "red", "red"]
Find which color appears most often. If there's a tie, pick any. Do this with a dictionary (count frequencies) then find max.

Exercise 10: Flatten a nested list

nested = [[1, 2], [3, 4, 5], [6], [7, 8, 9, 10]]
Write code to flatten into a single list: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]. Use a loop, then try with a list comprehension.

---

✅ Mini challenge after exercises

Write a single script that does all of the above one after another, with clear print statements saying which exercise is being shown. This will help you practice structuring code.

---

📚 General knowledge you're building

Exercise Skill
1 Manual min/max, accumulation
2 Loop-based reversal
3 Duplicate removal with order
4 Filtering with conditionals
5 Nested list iteration
6 String palindrome logic
7 List rotation
8 Nested loops or two-pointer thinking
9 Frequency counting with dict
10 Flattening (recursive thinking intro)

These are universal programming concepts – not tied to cloud, web, or data science. Master these, and you'll be comfortable with lists anywhere.

---

🔁 Next steps after lists

Once you're confident with these:

· Dictionaries – for counting, mapping, grouping
· Tuples & sets – when to use each
· List comprehensions – concise transformations
· Slicing tricks – advanced list manipulation