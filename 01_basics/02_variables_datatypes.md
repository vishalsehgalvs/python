# Python Variables, Data Types & Keywords

> Source: https://unwiredlearning.com/blog/python

---

## Variables

A variable is a **named container** that stores a value in memory.

> 🔁 **Analogy:** A variable is like a sticky note with a label. You write "age = 30" on the note, stick it to a wall, and whenever you need the age, you look for the note labeled "age".

```python
x = 10          # integer variable
name = "John"   # string variable
pi = 3.14159    # float variable
is_active = True  # boolean variable
```

### Rules for variable names:
- Can contain letters, numbers, and underscores `_`
- **Must start** with a letter or underscore (not a number)
- Case-sensitive (`age` and `Age` are different!)
- Cannot use reserved words (`if`, `for`, `class`, etc.)

```python
my_variable = 10     # ✅ valid
userName = "Alice"   # ✅ valid
_list = [1, 2, 3]   # ✅ valid
2x = 5              # ❌ starts with number
my-var = 5          # ❌ hyphens not allowed
```

### Python is dynamically typed:
No need to declare the type — Python figures it out from the value:
```python
x = 10       # x is int
x = "hello"  # now x is a string — that's fine!
x = 3.14     # now x is float
```

---

## Data Types

```
Python Data Types
├── Numeric
│   ├── int     → 42, -3, 0
│   ├── float   → 3.14, -0.5
│   └── complex → 2+3j
│
├── Sequence
│   ├── str   → "Hello"
│   ├── list  → [1, 2, 3]
│   └── tuple → (1, 2, 3)
│
├── Mapping
│   └── dict  → {"key": "value"}
│
├── Set
│   ├── set       → {1, 2, 3}
│   └── frozenset → frozenset([1,2,3])
│
└── Boolean
    └── bool → True / False
```

```python
# Numeric
x = 42           # int
y = 3.14         # float
z = 2 + 3j       # complex

# String
name = "Alice"   # str

# List (mutable, ordered)
colors = ["red", "green", "blue"]

# Tuple (immutable, ordered)
point = (3, 4)

# Dictionary (key-value pairs)
person = {"name": "Emma", "age": 30}

# Set (unique values, unordered)
fruits = {"apple", "banana", "orange"}

# Boolean
is_active = True
```

### Check type with `type()`:
```python
x = 10
print(type(x))        # <class 'int'>

name = "Alice"
print(type(name))     # <class 'str'>

pi = 3.14
print(type(pi))       # <class 'float'>
```

---

## Type Conversion (Casting)

```python
# int to float
x = float(5)        # 5.0

# float to int (truncates decimal)
y = int(5.9)        # 5 (not 6!)

# int to string
s = str(42)         # "42"

# string to int
n = int("100")      # 100

# string to float
f = float("3.14")   # 3.14

# int to bool
b = bool(0)         # False
b = bool(1)         # True
b = bool(5)         # True (any non-zero = True)

# string to bool
b = bool("")        # False (empty string = False)
b = bool("hello")   # True  (non-empty = True)
```

> ⚠️ `int("hello")` will crash! You can only convert strings that actually contain a number.

---

## Literals

Literals are **fixed, raw values** you write directly in code:

```python
# Numeric literals
42           # integer literal
-3           # negative integer
3.14         # float literal
2 + 3j       # complex literal
0b1010       # binary literal (= 10)
0o12         # octal literal  (= 10)
0xA          # hex literal    (= 10)

# String literals
'Hello'      # single-quoted
"Hello"      # double-quoted
'''Hello
   World'''  # triple-quoted (multiline)

# Boolean literals
True
False

# Special literal
None         # represents "nothing" / null value
```

---

## Reserved Keywords

Python has **35 reserved words** you cannot use as variable names:

```
False    await    else     import   pass
None     break    except   in       raise
True     class    finally  is       return
and      continue for      lambda   try
as       def      from     nonlocal while
assert   del      global   not      with
async    elif     if       or       yield
```

```python
# Examples of how keywords work
if x > 0:        # if keyword
    pass         # pass keyword (do nothing)

for i in range(5):   # for, in keywords
    continue         # continue keyword

def greet():     # def keyword
    return "Hi"  # return keyword

class Dog:       # class keyword
    pass
```

---

## Naming Conventions (PEP 8)

| Style | Use for | Example |
|-------|---------|---------|
| `snake_case` | Variables, functions | `my_variable`, `get_name()` |
| `PascalCase` | Classes | `MyClass`, `BankAccount` |
| `SCREAMING_SNAKE` | Constants | `MAX_SIZE`, `PI` |
| `_single_underscore` | "Private" variables | `_internal_use` |
| `__double_underscore` | Name mangling | `__private_attr` |

```python
# ✅ Good naming
user_name = "Alice"          # snake_case for variables
MAX_RETRIES = 3              # UPPER_CASE for constants
class UserAccount:           # PascalCase for classes
    def get_balance(self):   # snake_case for methods
        pass

# ❌ Bad naming (works but ugly)
UserName = "Alice"     # looks like a class
MYFUNCTION = lambda: None  # constants style for function
```

---

## Multiple Assignment

```python
# Assign same value to multiple variables
x = y = z = 0
print(x, y, z)  # 0 0 0

# Assign different values in one line
a, b, c = 1, 2, 3
print(a, b, c)  # 1 2 3

# Swap values
a, b = b, a     # Python's clean swap!

# Unpack list
first, second, *rest = [10, 20, 30, 40, 50]
print(first)    # 10
print(second)   # 20
print(rest)     # [30, 40, 50]
```

---

## Key Takeaways

- Variables are created on assignment: `x = 5` — no type declaration needed
- Python is **dynamically typed** — a variable can hold any type, and types can change
- Check type with `type(value)`, convert with `int()`, `float()`, `str()`, `bool()`
- `None` represents "no value" — Python's equivalent of null
- Reserved keywords (`if`, `for`, `class`, etc.) cannot be used as variable names
- Use `snake_case` for variables/functions, `PascalCase` for classes, `UPPER_CASE` for constants
