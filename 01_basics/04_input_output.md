# Python Input, Output & String Formatting

> Source: https://unwiredlearning.com/blog/python

---

## Output with `print()`

```python
print("Hello, World!")         # Hello, World!
print(42)                       # 42
print(3.14)                     # 3.14
print(True)                     # True

# Multiple values — separated by space by default
name = "Alice"
age = 30
print("Name:", name, "Age:", age)  # Name: Alice Age: 30
```

### `sep` and `end` parameters:

```python
# sep: change separator (default is space)
print("A", "B", "C")               # A B C
print("A", "B", "C", sep="-")      # A-B-C
print("A", "B", "C", sep="")       # ABC

# end: change what prints at the end (default is \n newline)
print("Hello", end=" ")
print("World")                      # Hello World  (on one line)

print("A", end="\n")
print("B")
# A
# B
```

---

## String Formatting — 3 Ways

### Method 1: Concatenation with `+`

```python
name = "Alice"
age = 30
print("Name: " + name + ", Age: " + str(age))  # must convert to str!
```

### Method 2: `.format()` method

```python
name = "Alice"
age = 30
print("Name: {}, Age: {}".format(name, age))           # positional
print("Name: {0}, Age: {1}".format(name, age))         # indexed
print("Name: {name}, Age: {age}".format(name=name, age=age))  # named
```

### Method 3: f-strings (Python 3.6+ — recommended ✅)

```python
name = "Alice"
age = 30
print(f"Name: {name}, Age: {age}")           # Name: Alice, Age: 30
print(f"Next year: {age + 1}")               # Next year: 31
print(f"Upper: {name.upper()}")              # Upper: ALICE
print(f"Pi: {3.14159:.2f}")                  # Pi: 3.14 (2 decimal places)
```

> 💡 f-strings are the cleanest and most modern way. Use them!

---

## Escape Characters

Special characters that go inside strings:

```python
print("Hello,\nWorld!")    # newline       → Hello,
                           #                 World!

print("Hello,\tWorld!")    # tab           → Hello,    World!

print("She said, \"Hi\"")  # double quote  → She said, "Hi"

print('It\'s fine')        # single quote  → It's fine

print("Backslash: \\")     # backslash     → Backslash: \

print("\r Overwritten")    # carriage return (go to line start)
```

| Escape | Meaning                              |
| ------ | ------------------------------------ |
| `\n`   | Newline                              |
| `\t`   | Horizontal tab                       |
| `\\`   | Literal backslash `\`                |
| `\'`   | Single quote in single-quoted string |
| `\"`   | Double quote in double-quoted string |
| `\r`   | Carriage return                      |
| `\a`   | ASCII bell (beep sound)              |
| `\b`   | Backspace                            |
| `\0`   | Null character                       |

---

## Input with `input()`

`input()` pauses the program and waits for the user to type something:

```python
name = input("Enter your name: ")
print("Hello, " + name + "!")

# Example run:
# Enter your name: Alice
# Hello, Alice!
```

> ⚠️ `input()` **always returns a string**! If you need a number, convert it:

```python
# This CRASHES with a TypeError:
age = input("Enter your age: ")
next_year = age + 1   # ❌ can't add int to str

# This WORKS:
age = int(input("Enter your age: "))   # convert to int!
next_year = age + 1
print(f"Next year you'll be {next_year}")

# For floats:
price = float(input("Enter price: "))
```

---

## Input Validation Example

```python
# Safe conversion with try/except
try:
    age = int(input("Enter your age: "))
    print(f"You are {age} years old.")
except ValueError:
    print("That's not a valid number!")
```

---

## Print Formatting with f-strings

```python
# Numbers
pi = 3.14159265
print(f"{pi:.2f}")      # 3.14    (2 decimal places)
print(f"{pi:.4f}")      # 3.1416  (4 decimal places)
print(f"{1000000:,}")   # 1,000,000 (thousands separator)
print(f"{0.5:.0%}")     # 50%     (percentage)

# Padding / alignment
name = "Alice"
print(f"{name:>10}")    # "     Alice" (right-align, 10 wide)
print(f"{name:<10}")    # "Alice     " (left-align, 10 wide)
print(f"{name:^10}")    # "  Alice   " (center, 10 wide)
print(f"{42:05d}")      # "00042"     (pad with zeros)
```

---

## Program Flow: Input → Process → Output

```
User types something
         │
         ▼
    input("Prompt: ")
         │
         ▼
    (always a string)
         │
         ▼
    Convert if needed
    int(), float()
         │
         ▼
    Process/Calculate
         │
         ▼
    print(result)
         │
         ▼
    User sees output
```

---

## Key Takeaways

- `print(value)` outputs to console; multiple values are space-separated by default
- `sep` changes the separator; `end` changes what comes at the end of the line
- `input("prompt")` reads user input — **always returns a string**
- Use `int()` or `float()` to convert input to numbers
- f-strings (`f"Hello {name}"`) are the best way to format output — readable and supports expressions
- Escape characters: `\n` for newline, `\t` for tab, `\\` for backslash, `\"` for double quote
