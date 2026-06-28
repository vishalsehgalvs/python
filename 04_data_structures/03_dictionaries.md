# Python Dictionaries

> Source: https://unwiredlearning.com/blog/python

---

## What Is a Dictionary?

A dictionary is an **unordered collection of key-value pairs**. Like a real dictionary — you look up a word (key) to get its definition (value).

> 🔁 **Analogy:** A dictionary is like a real-world phonebook. You look up a person's name (key) and find their phone number (value). Names must be unique — you can't have two entries for "Alice Smith".

```python
person = {"name": "Emma", "age": 30, "city": "Seattle"}
#          key      val     key  val    key      val
```

---

## Creating Dictionaries

```python
# Curly brace syntax
person = {"name": "Alice", "age": 30}

# dict() constructor
person = dict(name="Alice", age=30)

# From list of tuples
person = dict([("name", "Alice"), ("age", 30)])

# Empty dict
empty = {}
empty = dict()
```

---

## Accessing Values

```python
person = {"name": "Alice", "age": 30, "city": "NYC"}

# Square bracket — raises KeyError if key not found
print(person["name"])    # Alice
# print(person["phone"])  # ❌ KeyError!

# .get() — returns None (or default) if key not found (safe)
print(person.get("name"))         # Alice
print(person.get("phone"))        # None
print(person.get("phone", "N/A")) # N/A (custom default)
```

---

## Modifying Dictionaries

```python
person = {"name": "Alice", "age": 30}

# Add new key or update existing
person["city"] = "Seattle"     # adds new key "city"
person["age"] = 31             # updates existing "age"

# Update with multiple keys at once
person.update({"age": 32, "email": "alice@mail.com"})
print(person)
# {'name': 'Alice', 'age': 32, 'city': 'Seattle', 'email': 'alice@mail.com'}
```

---

## Removing Items

```python
person = {"name": "Alice", "age": 30, "city": "NYC"}

# pop() — removes and returns value
age = person.pop("age")     # returns 30, removes key "age"
print(age)                  # 30

# pop() with default (no KeyError if missing)
val = person.pop("phone", None)   # returns None if "phone" not found

# popitem() — removes and returns LAST inserted key-value pair
last = person.popitem()     # returns ('city', 'NYC')

# del — delete by key
del person["name"]

# clear() — empty the dict
person.clear()              # {}
```

---

## Iterating Over Dictionaries

```python
person = {"name": "Alice", "age": 30, "city": "Seattle"}

# Iterate over keys (default)
for key in person:
    print(key)
# name, age, city

# Iterate over values
for value in person.values():
    print(value)
# Alice, 30, Seattle

# Iterate over key-value pairs (most common!)
for key, value in person.items():
    print(f"{key}: {value}")
# name: Alice
# age: 30
# city: Seattle
```

---

## Dictionary Methods

```python
d = {"a": 1, "b": 2, "c": 3}

print(d.keys())     # dict_keys(['a', 'b', 'c'])
print(d.values())   # dict_values([1, 2, 3])
print(d.items())    # dict_items([('a', 1), ('b', 2), ('c', 3)])

# Check if key exists
print("a" in d)         # True
print("z" in d)         # False

# Get with default (never raises error)
print(d.get("a"))       # 1
print(d.get("z", 0))    # 0  ← default value

# Copy
d2 = d.copy()           # shallow copy

# Merge (Python 3.9+)
d1 = {"a": 1}
d2 = {"b": 2}
merged = d1 | d2        # {'a': 1, 'b': 2}
```

---

## Nested Dictionaries

```python
employees = {
    "Alice": {
        "age": 30,
        "dept": "Engineering",
        "salary": 90000
    },
    "Bob": {
        "age": 25,
        "dept": "Marketing",
        "salary": 70000
    }
}

# Access nested values
print(employees["Alice"]["dept"])    # Engineering
print(employees["Bob"]["salary"])    # 70000

# Modify nested value
employees["Alice"]["salary"] = 95000

# Iterate over nested dict
for name, info in employees.items():
    print(f"{name}: {info['dept']}")
```

---

## Dictionary Comprehension

```python
# Create dict from scratch
squares = {x: x**2 for x in range(1, 6)}
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Filter items
original = {"a": 1, "b": 2, "c": 3, "d": 4}
filtered = {k: v for k, v in original.items() if v > 2}
# {'c': 3, 'd': 4}

# Transform values
prices = {"apple": 1.5, "banana": 0.5, "cherry": 2.0}
discounted = {k: v * 0.9 for k, v in prices.items()}
# 10% discount on all items
```

---

## setdefault — Get or Initialize

```python
d = {"name": "Alice"}

# Gets existing value, or sets it if missing
d.setdefault("name", "Unknown")    # returns "Alice" (already exists)
d.setdefault("age", 0)             # sets age=0 (didn't exist), returns 0

print(d)   # {"name": "Alice", "age": 0}
```

---

## Real-World Example: Word Counter

```python
text = "the quick brown fox jumps over the lazy dog the fox"
words = text.split()

word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print(word_count)
# {'the': 3, 'quick': 1, 'brown': 1, 'fox': 2, ...}
```

---

## Key Takeaways

- Dictionaries store **key-value pairs** — keys must be unique and hashable (strings, numbers, tuples)
- Access: `d["key"]` (raises KeyError if missing) or `d.get("key", default)` (safe)
- Add/update: `d["key"] = value` or `d.update({...})`
- Delete: `d.pop("key")`, `del d["key"]`, `d.clear()`
- Iterate: `for k, v in d.items():` is the most common pattern
- Dictionary comprehension: `{k: v for k, v in ...}` — concise way to build dicts
- Python 3.7+ dicts maintain **insertion order**
- `in` checks keys only: `"key" in d` — not values
