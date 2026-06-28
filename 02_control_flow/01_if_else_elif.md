# Python if / elif / else — Control Flow

> Source: https://unwiredlearning.com/blog/python

---

## What Is Control Flow?

Programs normally run line-by-line from top to bottom. **Control flow** lets you make decisions — run different code based on conditions.

> 🔁 **Analogy:** Control flow is like a GPS. Depending on road conditions (the condition), it says: "Turn left here" (if branch) OR "Turn right instead" (else branch).

---

## `if` Statement

Runs a block only if the condition is `True`:

```python
age = 18
if age >= 18:
    print("You are eligible to vote.")
# Output: You are eligible to vote.

# If condition is False, nothing happens
score = 40
if score >= 50:
    print("You passed.")
# (nothing printed — condition is False)
```

---

## `if / else` Statement

```
condition True?
     │
    Yes ──► run if block
     │
    No  ──► run else block
```

```python
age = 16
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
# Output: You are not eligible to vote.
```

---

## `if / elif / else` — Multiple Conditions

```
Check condition 1
     │
    True? ──► run block 1, skip rest
     │
    False ──► Check condition 2
                  │
                 True? ──► run block 2, skip rest
                  │
                 False ──► else block (catches everything)
```

```python
age = 18

if age < 13:
    print("You are a child.")
elif age >= 13 and age < 18:
    print("You are a teenager.")
else:
    print("You are an adult.")
# Output: You are an adult.
```

```python
score = 75

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Your grade is {grade}.")
# Output: Your grade is C.
```

---

## Indentation — Python's Code Blocks

In Python, **indentation defines what's inside a block**. Unlike C++ or JavaScript, there are no curly braces `{}` — only consistent spacing.

```python
# ✅ Correct indentation (4 spaces)
def greet(name):
    if name == "Alice":
        message = "Hello, Alice!"
    else:
        message = f"Hello, {name}!"
    print(message)    # this is inside greet() but NOT inside if/else

greet("Bob")

# ❌ Wrong — IndentationError
def greet(name):
if name == "Alice":   # ERROR! Expected indent after def
    message = "Hi"
```

> 💡 Use **4 spaces** per indentation level (PEP 8 standard). Mixing tabs and spaces causes errors!

---

## Nested `if` Statements

An `if` inside another `if`:

```python
age = 25
country = "USA"

if age >= 18:
    if country == "USA":
        print("You are eligible to vote in the USA.")
    elif country == "India":
        print("You are eligible to vote in India.")
    else:
        print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
```

```python
score = 75

if score >= 50:      # outer if
    if score >= 90:  # nested if
        grade = "A"
    elif score >= 70:
        grade = "B"
    else:
        grade = "C"
else:
    grade = "F"

print(f"Your grade is {grade}.")   # B
```

> 💡 Avoid excessive nesting — more than 2-3 levels of nesting makes code hard to read. Consider early returns or helper functions instead.

---

## Truthy and Falsy Values

In Python, `if` checks for **truthiness**, not just `True`/`False`:

```python
# These are FALSY (treated as False in if):
if 0:       pass   # False
if "":      pass   # empty string
if []:      pass   # empty list
if {}:      pass   # empty dict
if None:    pass   # None

# These are TRUTHY (treated as True):
if 1:       print("runs")    # non-zero number
if "hello": print("runs")   # non-empty string
if [1]:     print("runs")   # non-empty list
```

```python
name = ""
if name:
    print(f"Hello, {name}")
else:
    print("Name is empty!")
# Output: Name is empty!
```

---

## Common Conditions

```python
# Number ranges
if 1 <= x <= 10:            # pythonic range check
    print("between 1 and 10")

# String checks
if name.lower() == "alice": # case-insensitive
    pass

if name.startswith("A"):    # starts with
    pass

# None check
if value is None:           # use 'is' for None, not ==
    pass

if value is not None:
    pass

# List/collection empty check
if len(my_list) == 0:       # verbose way
    pass
if not my_list:             # pythonic way (falsy check)
    pass
```

---

## One-Line `if` (Ternary Expression)

```python
# Syntax: value_if_true if condition else value_if_false
age = 20
status = "adult" if age >= 18 else "minor"
print(status)  # adult

# Equivalent to:
if age >= 18:
    status = "adult"
else:
    status = "minor"
```

---

## Key Takeaways

- `if` runs a block only when condition is `True`
- `elif` checks another condition if the previous was `False`
- `else` catches everything that didn't match any condition
- Python uses **indentation** (4 spaces) to define code blocks — no curly braces
- Falsy values: `0`, `""`, `[]`, `{}`, `None`, `False` — all treated as `False` in conditions
- Avoid deep nesting — keep if/elif/else chains flat and readable
- One-line ternary: `x if condition else y`
