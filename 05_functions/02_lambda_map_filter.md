# Python Lambda, map(), filter(), reduce()

> Source: https://unwiredlearning.com/blog/python

---

## Lambda Functions

A **lambda** is a small, anonymous (unnamed) function defined with the `lambda` keyword.

> 🔁 **Analogy:** A lambda is like a sticky note with a quick calculation on it. A regular function is like a formal recipe card with a name, instructions, and notes. Lambdas are for short, one-off use.

```python
# Regular function
def square(x):
    return x * x

# Equivalent lambda
square = lambda x: x * x

print(square(5))   # 25
```

### Lambda syntax:

```
lambda arguments: expression
         │              │
    comma-separated  single expression
    parameters       (auto-returned)
```

```python
# Single argument
double = lambda x: x * 2
print(double(5))   # 10

# Multiple arguments
add = lambda x, y: x + y
print(add(3, 4))   # 7

# With condition (ternary)
is_even = lambda x: True if x % 2 == 0 else False
print(is_even(4))   # True

# No arguments
greet = lambda: "Hello!"
print(greet())   # Hello!
```

### Where lambdas shine — as inline functions:

```python
# Sort a list of tuples by second element
pairs = [(1, 3), (2, 1), (4, 2)]
pairs.sort(key=lambda pair: pair[1])
print(pairs)   # [(2, 1), (4, 2), (1, 3)]

# Sort words by length
words = ["banana", "fig", "apple", "cherry"]
words.sort(key=lambda w: len(w))
print(words)   # ['fig', 'apple', 'banana', 'cherry']
```

---

## `map()` — Transform Every Element

Applies a function to **every element** in an iterable and returns a map object.

```
map(function, iterable)

[1, 2, 3, 4, 5]
     │ apply function to each
     ▼
[1, 4, 9, 16, 25]   (if function is x²)
```

```python
numbers = [1, 2, 3, 4, 5]

# Square each number
squared = map(lambda x: x * x, numbers)
print(list(squared))   # [1, 4, 9, 16, 25]

# Convert to list of strings
str_numbers = map(str, [1, 2, 3])
print(list(str_numbers))   # ['1', '2', '3']

# Convert a list of strings to uppercase
words = ["hello", "world", "python"]
upper = map(str.upper, words)
print(list(upper))   # ['HELLO', 'WORLD', 'PYTHON']

# Calculate lengths
words = ["apple", "banana", "cherry"]
lengths = list(map(lambda x: len(x), words))
print(lengths)   # [5, 6, 6]
```

> 💡 `map()` is lazy — it doesn't compute until you convert to `list()`.

---

## `filter()` — Keep Only Matching Elements

Keeps only the elements where the function returns `True`.

```
filter(function, iterable)

[1, 2, 3, 4, 5, 6, 7, 8, 9]
        │ keep only where function returns True
        ▼
[2, 4, 6, 8]   (if function checks even)
```

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Keep only even numbers
evens = filter(lambda x: x % 2 == 0, numbers)
print(list(evens))   # [2, 4, 6, 8]

# Remove empty strings
strings = ["apple", "", "banana", "", "cherry"]
non_empty = filter(lambda x: x != "", strings)
print(list(non_empty))   # ['apple', 'banana', 'cherry']

# Keep words longer than 3 chars
words = ["apple", "it", "banana", "car", "cherry"]
long_words = filter(lambda x: len(x) > 3, words)
print(list(long_words))   # ['apple', 'banana', 'cherry']

# Filter positive numbers
nums = [-3, -1, 0, 2, 5, -2, 7]
positives = list(filter(lambda x: x > 0, nums))
print(positives)   # [2, 5, 7]
```

---

## `reduce()` — Accumulate to Single Value

Applies a function **cumulatively** to reduce an iterable to a single value.

> **Must import** from `functools`!

```
from functools import reduce

reduce(function, iterable)

[1, 2, 3, 4, 5]
    │ apply function pairwise from left to right
    ▼
((((1+2)+3)+4)+5) = 15
```

```python
from functools import reduce

numbers = [1, 2, 3, 4, 5]

# Sum all numbers
total = reduce(lambda x, y: x + y, numbers)
print(total)   # 15

# Product of all numbers
product = reduce(lambda x, y: x * y, numbers)
print(product)   # 120

# Find maximum
nums = [34, 65, 12, 76, 25]
largest = reduce(lambda x, y: x if x > y else y, nums)
print(largest)   # 76

# Concatenate strings
words = ["Hello", " ", "World", "!"]
sentence = reduce(lambda x, y: x + y, words)
print(sentence)   # Hello World!

# With initial value (optional 3rd argument)
total = reduce(lambda x, y: x + y, [1, 2, 3], 10)
print(total)   # 16  (starts from 10, then adds 1+2+3)
```

---

## map vs filter vs reduce — Summary

```
map()     → transforms each element → returns same number of items
filter()  → keeps some elements     → returns ≤ original number
reduce()  → combines to one value   → returns single value

Input: [1, 2, 3, 4, 5]

map(x²)     → [1, 4, 9, 16, 25]    (5 items → 5 items)
filter(even) → [2, 4]               (5 items → 2 items)
reduce(+)    → 15                   (5 items → 1 item)
```

---

## List Comprehension vs map/filter

In modern Python, **list comprehensions** are often preferred over `map`/`filter` for readability:

```python
numbers = [1, 2, 3, 4, 5]

# map equivalent
squares_map = list(map(lambda x: x**2, numbers))
squares_comp = [x**2 for x in numbers]              # cleaner!

# filter equivalent
evens_filter = list(filter(lambda x: x%2==0, numbers))
evens_comp = [x for x in numbers if x % 2 == 0]    # cleaner!
```

---

## Key Takeaways

- `lambda x: expression` — anonymous one-line function, great for short inline use
- `map(func, iterable)` — apply function to every element; convert to `list()` to see results
- `filter(func, iterable)` — keep elements where function returns `True`; also lazy
- `reduce(func, iterable)` — collapse to single value; must `from functools import reduce`
- All three return lazy objects (not lists) — wrap in `list()` to get the result
- List comprehensions `[expr for x in iterable if condition]` are often cleaner than `map`/`filter`
