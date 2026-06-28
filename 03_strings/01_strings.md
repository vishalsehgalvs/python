# Python Strings

> Source: https://unwiredlearning.com/blog/python

---

## What Is a String?

A string is a **sequence of characters** — text. Strings are immutable (you can't change individual characters in place).

> 🔁 **Analogy:** A string is like a necklace of beads. Each bead is a character. You can look at any bead by its position, take a slice of beads, or count them — but you can't swap one bead without making a new necklace.

```python
s1 = 'Hello'          # single quotes
s2 = "Hello"          # double quotes (same thing)
s3 = '''Hello
World'''              # triple quotes for multiline
s4 = """Another
multiline"""
```

---

## Comments and Docstrings

### Single-line comments
```python
# This is a comment
x = 10  # This is an inline comment
```

### Multi-line comments
```python
'''
This is a
multiline comment
(technically a string literal, but commonly used as comment)
'''
```

### Docstrings — document your code
```python
def add(a, b):
    """
    Adds two numbers and returns the result.

    Args:
        a (int or float): First number
        b (int or float): Second number

    Returns:
        int or float: Sum of a and b
    """
    return a + b

# Access docstring:
print(add.__doc__)
```

---

## Indexing and Slicing

```
String:   H  e  l  l  o
Index:    0  1  2  3  4     (positive indexing)
          -5 -4 -3 -2 -1    (negative indexing from end)
```

```python
s = "Hello"

# Indexing
print(s[0])    # H  (first)
print(s[4])    # o  (last)
print(s[-1])   # o  (last, using negative index)
print(s[-2])   # l  (second-to-last)

# Slicing: s[start:stop:step]
print(s[1:4])   # ell  (index 1, 2, 3 — stop is exclusive)
print(s[:3])    # Hel  (from start to index 2)
print(s[2:])    # llo  (from index 2 to end)
print(s[:])     # Hello (full copy)
print(s[::2])   # Hlo  (every 2nd character)
print(s[::-1])  # olleH (reverse string!)
```

---

## Common String Methods

### Case methods
```python
s = "Hello, World!"

print(s.lower())       # "hello, world!"
print(s.upper())       # "HELLO, WORLD!"
print(s.title())       # "Hello, World!"   (capitalizes first letter of each word)
print(s.capitalize())  # "Hello, world!"   (capitalizes only first letter)
print(s.swapcase())    # "hELLO, wORLD!"  (swaps cases)
```

### Strip (remove whitespace or characters)
```python
s = "  Hello, World!  "
print(s.strip())        # "Hello, World!"   (both ends)
print(s.lstrip())       # "Hello, World!  " (left only)
print(s.rstrip())       # "  Hello, World!" (right only)

# Remove specific characters
s = "***Hello***"
print(s.strip("*"))     # "Hello"
```

### Find and search
```python
s = "Hello, World!"

print(s.find("World"))    # 7  (first occurrence position)
print(s.find("Python"))   # -1 (not found → -1)
print(s.index("World"))   # 7  (like find, but raises ValueError if not found)
print(s.rfind("l"))       # 10 (search from right)

print(s.startswith("Hello"))  # True
print(s.endswith("Python"))   # False

print(s.count("l"))       # 3  (how many times "l" appears)
```

### Replace
```python
s = "Hello, World!"
print(s.replace("World", "Python"))   # "Hello, Python!"

# Replace max n occurrences
s = "aaa"
print(s.replace("a", "b", 2))   # "bba" (only first 2)
```

### Split and join
```python
# split — break string into list
s = "Hello, World!"
print(s.split())      # ['Hello,', 'World!']  (split on whitespace)
print(s.split(","))   # ['Hello', ' World!']  (split on comma)

csv = "Alice,Bob,Carol"
names = csv.split(",")   # ['Alice', 'Bob', 'Carol']

# join — combine list into string
words = ["Hello", "World"]
print(" ".join(words))     # "Hello World"
print("-".join(words))     # "Hello-World"
print("".join(words))      # "HelloWorld"
```

### Check content
```python
print("123".isdigit())     # True  — all digits?
print("abc".isalpha())     # True  — all letters?
print("abc123".isalnum())  # True  — all letters+digits?
print("  ".isspace())      # True  — all whitespace?
print("HELLO".isupper())   # True  — all uppercase?
print("hello".islower())   # True  — all lowercase?
print("Hello World".istitle())  # True — title case?
```

### Format
```python
template = "Hello, {name}! Welcome to {place}."
print(template.format(name="Alice", place="Wonderland"))
# Hello, Alice! Welcome to Wonderland.
```

---

## String Concatenation and Repetition

```python
s1 = "Hello"
s2 = " World"

# Concatenation with +
print(s1 + s2)          # "Hello World"

# Repetition with *
print("Ha" * 3)         # "HaHaHa"
print("-" * 20)         # "--------------------"

# += for appending
result = ""
result += "Hello"
result += " World"
print(result)           # "Hello World"
```

---

## String is Immutable!

```python
s = "Hello"
# s[0] = "J"   # ❌ TypeError: strings are immutable!

# To "change" a string, create a new one
s = "J" + s[1:]     # "Jello"
```

---

## Multiline Strings

```python
poem = """
Roses are red,
Violets are blue,
Python is awesome,
And so are you!
"""
print(poem)

# Or with \
long_line = "This is a very long line that " \
            "continues here."
```

---

## Raw Strings (for file paths, regex)

Prefix with `r` to treat backslashes as literal:

```python
path = r"C:\Users\alice\Desktop"   # backslashes NOT escaped
print(path)   # C:\Users\alice\Desktop

# Without r:
path = "C:\\Users\\alice\\Desktop"  # need double backslash
```

---

## Key Takeaways

- Strings are immutable — methods return NEW strings, they don't modify in place
- Indexing starts at 0; negative indexes count from the end (`-1` = last)
- Slicing: `s[start:stop:step]` — stop is exclusive; `s[::-1]` reverses a string
- `lower()`, `upper()`, `strip()`, `replace()`, `split()`, `join()` — most commonly used methods
- `find()` returns -1 if not found; `index()` raises `ValueError`
- Comments: `#` for single-line; `"""..."""` for docstrings
- Raw strings `r"path\here"` treat backslashes as literal — useful for Windows paths and regex
