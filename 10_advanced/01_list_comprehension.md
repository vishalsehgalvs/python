# Python List Comprehension

> Source: https://unwiredlearning.com/blog/python

---

## What Is List Comprehension?

List comprehension is a **concise, readable way to create lists** from existing iterables.

> 🔁 **Analogy:** List comprehension is like a shopping filter. "Give me all items from the shelf that are on sale and cost less than $10" — instead of walking through every item manually and checking.

```python
# Traditional loop
squares = []
for x in range(1, 6):
    squares.append(x * x)
print(squares)   # [1, 4, 9, 16, 25]

# Same thing with list comprehension
squares = [x * x for x in range(1, 6)]
print(squares)   # [1, 4, 9, 16, 25]
```

---

## Basic Syntax

```
[expression  for  item  in  iterable]
     │               │         │
  what to        variable   what to
  produce         name      loop over
```

```python
numbers = [1, 2, 3, 4, 5]

doubles = [x * 2 for x in numbers]
# [2, 4, 6, 8, 10]

strings = [str(x) for x in numbers]
# ['1', '2', '3', '4', '5']

upper = [s.upper() for s in ["hello", "world"]]
# ['HELLO', 'WORLD']
```

---

## With Condition (Filtering)

```
[expression  for  item  in  iterable  if  condition]
```

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Only even numbers
evens = [x for x in numbers if x % 2 == 0]
# [2, 4, 6, 8, 10]

# Only odd and squared
odd_squares = [x**2 for x in numbers if x % 2 != 0]
# [1, 9, 25, 49, 81]

# Filter strings by length
words = ["apple", "cat", "banana", "go", "cherry"]
long_words = [w for w in words if len(w) > 4]
# ['apple', 'banana', 'cherry']
```

---

## If-Else in Expression

```python
# Ternary form: expression_if_true if condition else expression_if_false
numbers = [1, 2, 3, 4, 5, 6]

labels = ["even" if x % 2 == 0 else "odd" for x in numbers]
# ['odd', 'even', 'odd', 'even', 'odd', 'even']

# Absolute values
nums = [-3, -1, 0, 2, -5, 4]
absolute = [x if x >= 0 else -x for x in nums]
# [3, 1, 0, 2, 5, 4]
```

---

## Nested List Comprehension

Flatten a 2D list:
```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Traditional
flat = []
for row in matrix:
    for item in row:
        flat.append(item)

# With comprehension
flat = [item for row in matrix for item in row]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

Multiplication table:
```python
table = [[row * col for col in range(1, 4)] for row in range(1, 4)]
# [[1, 2, 3],
#  [2, 4, 6],
#  [3, 6, 9]]
```

---

## Dictionary Comprehension

```
{key_expr: value_expr  for  item  in  iterable}
```

```python
# Square of numbers as dict
squares = {x: x**2 for x in range(1, 6)}
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Invert a dictionary
original = {"a": 1, "b": 2, "c": 3}
inverted = {v: k for k, v in original.items()}
# {1: 'a', 2: 'b', 3: 'c'}

# Filter dict by value
prices = {"apple": 1.5, "banana": 0.5, "cherry": 2.0, "mango": 0.3}
expensive = {k: v for k, v in prices.items() if v > 0.8}
# {'apple': 1.5, 'cherry': 2.0}
```

---

## Set Comprehension

```
{expression  for  item  in  iterable}
```

```python
# Unique squares
numbers = [1, -1, 2, -2, 3, 3, 4]
unique_squares = {x**2 for x in numbers}
# {1, 4, 9, 16}   (unordered, unique values!)

# Unique first letters
words = ["apple", "banana", "apricot", "cherry", "blueberry"]
first_letters = {w[0] for w in words}
# {'a', 'b', 'c'}
```

---

## Generator Expression (Lazy Version)

Use `()` instead of `[]` for a **generator** — computes values on demand (memory-efficient):

```python
# List comprehension — creates entire list in memory
squares_list = [x**2 for x in range(1000000)]    # 8MB+

# Generator expression — lazy, one value at a time
squares_gen = (x**2 for x in range(1000000))     # almost no memory

# Consume with next() or loop
print(next(squares_gen))   # 0
print(next(squares_gen))   # 1
print(next(squares_gen))   # 4

# Or in a loop
total = sum(x**2 for x in range(100))   # generator directly in function call
```

---

## Comprehension Performance

List comprehensions are generally **faster than equivalent for loops**:

```python
import time

# Loop approach
start = time.time()
result = []
for x in range(1000000):
    result.append(x * 2)
print(f"Loop: {time.time() - start:.3f}s")

# Comprehension approach
start = time.time()
result = [x * 2 for x in range(1000000)]
print(f"Comprehension: {time.time() - start:.3f}s")

# Comprehension is typically 30-50% faster
```

---

## When NOT to Use Comprehensions

```python
# ✅ Good — simple, readable
evens = [x for x in range(20) if x % 2 == 0]

# ❌ Bad — too complex, hard to read
result = [f(x) for x in range(100) if g(x) > 0 if h(x) != 0 for y in nested if y < x]

# ✅ Better to use a loop when logic is complex
result = []
for x in range(100):
    if g(x) > 0 and h(x) != 0:
        for y in nested:
            if y < x:
                result.append(f(x))
```

> 💡 If your comprehension is hard to read in one line, use a regular loop instead. Readability beats cleverness.

---

## Key Takeaways

- `[expr for x in iterable]` — basic list comprehension
- `[expr for x in iterable if condition]` — with filtering
- `[a if cond else b for x in iterable]` — conditional expression
- `{k: v for k, v in items}` — dictionary comprehension
- `{expr for x in iterable}` — set comprehension
- `(expr for x in iterable)` — generator expression (lazy, memory-efficient)
- Use comprehensions for **simple** transformations/filters; use loops when logic is complex
- Comprehensions are generally faster than equivalent `for` + `append()` loops
