# Python Lists

> Source: https://unwiredlearning.com/blog/python

---

## What Is a List?

A **list** is an ordered, mutable collection of items. Items can be of any type, and you can change them after creation.

> 🔁 **Analogy:** A list is like a shopping cart. You add items, remove them, reorder them, and the cart keeps track of everything in order. You can have duplicate items too.

```python
numbers = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "cherry"]
mixed = [1, "hello", 3.14, True, None]   # any types!
nested = [[1, 2], [3, 4], [5, 6]]         # lists of lists
empty = []
```

---

## Indexing and Slicing

```
List:    apple   banana   cherry   mango   grape
Index:     0       1        2        3       4
           -5     -4       -3       -2      -1
```

```python
fruits = ["apple", "banana", "cherry", "mango", "grape"]

# Indexing
print(fruits[0])    # apple
print(fruits[2])    # cherry
print(fruits[-1])   # grape (last)
print(fruits[-2])   # mango

# Slicing: list[start:stop:step]
print(fruits[1:4])    # ['banana', 'cherry', 'mango']
print(fruits[:3])     # ['apple', 'banana', 'cherry']
print(fruits[2:])     # ['cherry', 'mango', 'grape']
print(fruits[::2])    # ['apple', 'cherry', 'grape'] (every 2nd)
print(fruits[::-1])   # reversed list!
```

---

## Modifying Lists

```python
fruits = ["apple", "banana", "cherry"]

# Change an element
fruits[1] = "blueberry"
print(fruits)   # ['apple', 'blueberry', 'cherry']

# Change a slice
fruits[0:2] = ["mango", "grape"]
print(fruits)   # ['mango', 'grape', 'cherry']
```

---

## Common List Methods

### Add elements

```python
numbers = [1, 2, 3]

numbers.append(4)              # add to END → [1, 2, 3, 4]
numbers.insert(1, 99)          # insert at index → [1, 99, 2, 3, 4]
numbers.extend([5, 6, 7])      # add multiple → [1, 99, 2, 3, 4, 5, 6, 7]
numbers += [8, 9]              # also extends → [1, 99, 2, 3, 4, 5, 6, 7, 8, 9]
```

### Remove elements

```python
numbers = [1, 2, 3, 2, 4]

numbers.remove(2)       # removes FIRST occurrence of 2 → [1, 3, 2, 4]
last = numbers.pop()    # removes & returns last element → returns 4
item = numbers.pop(1)   # removes & returns index 1 → returns 3

del numbers[0]          # delete by index
del numbers[1:3]        # delete a slice

numbers.clear()         # empties the list → []
```

### Search

```python
fruits = ["apple", "banana", "cherry", "apple"]

print(fruits.index("banana"))   # 1 (first occurrence index)
print(fruits.count("apple"))    # 2 (how many times)
print("cherry" in fruits)       # True
print("grape" in fruits)        # False
```

### Sort and reverse

```python
numbers = [3, 1, 4, 2, 5]

numbers.sort()                      # sorts in place: [1, 2, 3, 4, 5]
numbers.sort(reverse=True)          # descending: [5, 4, 3, 2, 1]
numbers.reverse()                   # reverses in place

# sorted() returns NEW list (doesn't modify original)
nums = [3, 1, 4, 2]
sorted_nums = sorted(nums)          # [1, 2, 3, 4]
print(nums)                         # [3, 1, 4, 2] ← unchanged!

# Sort strings
words = ["banana", "apple", "cherry"]
words.sort()                        # ['apple', 'banana', 'cherry']

# Custom sort key
words.sort(key=len)                 # sort by length
```

### Copy

```python
original = [1, 2, 3]

# Shallow copy (creates new list, same elements)
copy1 = original.copy()
copy2 = list(original)
copy3 = original[:]

# ⚠️ This is NOT a copy — same list!
same = original
same.append(4)
print(original)   # [1, 2, 3, 4] — original changed!
```

---

## Iterating Over Lists

```python
fruits = ["apple", "banana", "cherry"]

# Basic for loop
for fruit in fruits:
    print(fruit)

# With index using enumerate
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")
# 0: apple
# 1: banana
# 2: cherry

# While loop with index
i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1
```

---

## List Comprehension (Preview)

```python
# Create list from scratch
squares = [x**2 for x in range(1, 6)]
# [1, 4, 9, 16, 25]

# Filter items
evens = [x for x in range(10) if x % 2 == 0]
# [0, 2, 4, 6, 8]
```

---

## Useful Built-in Functions for Lists

```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6]

print(len(numbers))    # 8 — number of elements
print(sum(numbers))    # 31 — total
print(min(numbers))    # 1 — minimum
print(max(numbers))    # 9 — maximum
print(sorted(numbers)) # [1, 1, 2, 3, 4, 5, 6, 9] (new sorted list)

# Unpack list
a, b, c, *rest = [1, 2, 3, 4, 5]
print(a, b, c)  # 1 2 3
print(rest)     # [4, 5]
```

---

## Key Takeaways

- Lists are **ordered** and **mutable** — you can change, add, remove elements
- Indexing: `list[0]` for first, `list[-1]` for last
- Slicing: `list[start:stop:step]` — creates a new sublist
- `append()` adds to end; `insert(i, val)` adds at index; `extend()` adds multiple
- `remove(val)` removes first matching value; `pop(i)` removes and returns by index
- `sort()` modifies in-place; `sorted()` returns a new sorted list
- `len()`, `sum()`, `min()`, `max()` work on lists
- Use `list.copy()` or `list[:]` to make a real copy (not just another reference)
