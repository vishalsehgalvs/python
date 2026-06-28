# Python Tuples and Sets

> Source: https://unwiredlearning.com/blog/python

---

## Tuples

A **tuple** is like a list but **immutable** — once created, it cannot be changed.

> 🔁 **Analogy:** A tuple is like a sealed envelope with a date stamped on it. You can read what's inside, but you can't add, remove, or change the contents without unsealing (creating a new tuple).

```python
point = (3, 4)
colors = ("red", "green", "blue")
single = (42,)         # ⚠️ Note the trailing comma — required for single-element tuple!
empty = ()

# Tuple without parentheses (also works)
coords = 10, 20, 30    # (10, 20, 30)
```

> ⚠️ `(42)` is just `42` (an integer in parentheses). You need `(42,)` with a comma for a single-element tuple.

### Accessing tuple elements (same as list):
```python
t = ("apple", "banana", "cherry")

print(t[0])    # apple
print(t[-1])   # cherry
print(t[1:])   # ('banana', 'cherry')
```

### Tuple is immutable — cannot be changed:
```python
t = (1, 2, 3)
# t[0] = 99     # ❌ TypeError: 'tuple' object does not support item assignment
```

### Tuple methods (only 2!):
```python
t = (1, 2, 3, 2, 4, 2)

print(t.count(2))    # 3  — how many times 2 appears
print(t.index(3))    # 2  — index of first occurrence of 3
```

### Tuple unpacking:
```python
point = (10, 20)
x, y = point           # unpack into variables
print(x, y)            # 10 20

# Ignore some values with _
first, _, last = (1, 2, 3)
print(first, last)     # 1 3

# Unpack with *
a, *middle, z = (1, 2, 3, 4, 5)
print(a)       # 1
print(middle)  # [2, 3, 4]
print(z)       # 5
```

### When to use tuples vs lists:
| | Tuple | List |
|---|-------|------|
| Mutable? | ❌ No | ✅ Yes |
| Syntax | `(1, 2, 3)` | `[1, 2, 3]` |
| Use when | Data won't change | Data will change |
| Examples | `(x, y)` coordinates, RGB color, function return values | Shopping cart, student list |
| Performance | Slightly faster | Slightly slower |

---

## Sets

A **set** is an **unordered collection of unique values**. No duplicates allowed.

> 🔁 **Analogy:** A set is like a ballot box that rejects duplicate votes. You can put in names, but the box keeps only one of each name — no duplicates.

```python
fruits = {"apple", "banana", "cherry"}
numbers = {1, 2, 3, 4, 5}
empty_set = set()    # ⚠️ NOT {} — that creates an empty dict!
```

```python
# Duplicates are automatically removed
my_set = {1, 2, 2, 3, 3, 3}
print(my_set)   # {1, 2, 3}  ← only unique values

# Order is NOT guaranteed
s = {"banana", "apple", "cherry"}
print(s)   # could print in any order!
```

### Add and remove:
```python
fruits = {"apple", "banana"}

fruits.add("cherry")           # add one element
fruits.update(["mango", "grape"])  # add multiple

fruits.remove("banana")        # remove — raises KeyError if not found
fruits.discard("grape")        # remove — NO error if not found

popped = fruits.pop()          # removes and returns a random element
fruits.clear()                 # empties set
```

### Check membership:
```python
fruits = {"apple", "banana", "cherry"}
print("apple" in fruits)       # True
print("grape" in fruits)       # False
print("grape" not in fruits)   # True
```

### Set Operations (the real power of sets!):
```python
a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7}

# Union — all elements from both
print(a | b)          # {1, 2, 3, 4, 5, 6, 7}
print(a.union(b))     # same

# Intersection — only elements in BOTH
print(a & b)                   # {3, 4, 5}
print(a.intersection(b))       # same

# Difference — in a but NOT in b
print(a - b)                   # {1, 2}
print(a.difference(b))         # same

# Symmetric difference — in either but NOT both
print(a ^ b)                           # {1, 2, 6, 7}
print(a.symmetric_difference(b))       # same
```

```
a = {1, 2, 3, 4, 5}
b =          {3, 4, 5, 6, 7}

Union:          {1, 2, 3, 4, 5, 6, 7}
Intersection:         {3, 4, 5}
Difference (a-b): {1, 2}
Sym. diff:      {1, 2,       6, 7}
```

### Subset/superset checks:
```python
a = {1, 2, 3}
b = {1, 2, 3, 4, 5}

print(a.issubset(b))    # True  — a is contained in b
print(b.issuperset(a))  # True  — b contains a
print(a.isdisjoint({6, 7}))  # True — no elements in common
```

---

## `frozenset` — Immutable Set

```python
# frozenset is like a frozen (immutable) version of a set
immutable = frozenset(["apple", "banana", "cherry"])
# immutable.add("mango")  # ❌ AttributeError — can't modify!

# Useful as dictionary key (regular sets can't be dict keys)
```

---

## Remove Duplicates from a List Using Set

```python
names = ["Alice", "Bob", "Alice", "Carol", "Bob"]
unique_names = list(set(names))
print(unique_names)   # ['Alice', 'Bob', 'Carol'] (order may vary)
```

---

## Key Takeaways

- **Tuple**: ordered, immutable — use when data shouldn't change; `(1, 2, 3)`
- Single-element tuple needs a trailing comma: `(42,)` not `(42)`
- Tuple unpacking: `x, y = (10, 20)` — convenient multi-variable assignment
- **Set**: unordered, unique values — no duplicates; `{1, 2, 3}`
- `set()` for empty set (not `{}` — that's an empty dict!)
- `add()`, `remove()`, `discard()` — add/remove elements
- Set math: `|` union, `&` intersection, `-` difference, `^` symmetric difference
- Quick trick: `list(set(my_list))` removes all duplicates from a list
