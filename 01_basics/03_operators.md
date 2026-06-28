# Python Operators

> Source: https://unwiredlearning.com/blog/python

---

## Types of Operators

Python has 7 types of operators:
```
Arithmetic    → +  -  *  /  %  **  //
Relational    → ==  !=  >  <  >=  <=
Logical       → and  or  not
Assignment    → =  +=  -=  *=  /=  %=  **=  //=
Bitwise       → &  |  ^  ~  <<  >>
Membership    → in  not in
Identity      → is  is not
```

---

## 1. Arithmetic Operators

```python
x = 10
y = 3

print(x + y)   # 13  — addition
print(x - y)   # 7   — subtraction
print(x * y)   # 30  — multiplication
print(x / y)   # 3.3333... — division (always float!)
print(x % y)   # 1   — modulus (remainder)
print(x ** y)  # 1000 — exponentiation (10 to the power 3)
print(x // y)  # 3   — floor division (rounds DOWN)
```

> 💡 **Important:** `/` always returns a float in Python 3. `//` returns an integer (floor division).

```python
print(7 / 2)   # 3.5   ← float division
print(7 // 2)  # 3     ← floor division (drops decimal)
print(-7 // 2) # -4    ← floors toward negative infinity!
```

---

## 2. Relational (Comparison) Operators

Return `True` or `False`:

```python
x = 5
y = 3

print(x == y)   # False — equal to
print(x != y)   # True  — not equal to
print(x > y)    # True  — greater than
print(x < y)    # False — less than
print(x >= y)   # True  — greater than or equal to
print(x <= y)   # False — less than or equal to
```

---

## 3. Logical Operators

Combine multiple conditions:

```python
# and — True only if BOTH are True
print(True and False)    # False
print(True and True)     # True
print(5 > 3 and 2 < 4)  # True

# or — True if AT LEAST ONE is True
print(True or False)     # True
print(False or False)    # False
print(5 > 10 or 2 < 4)  # True

# not — flips True↔False
print(not True)          # False
print(not False)         # True
print(not (5 > 3))       # False
```

### Short-circuit evaluation:
```python
# "and" stops at first False
False and print("never runs")   # print never executes!

# "or" stops at first True
True or print("never runs")     # print never executes!
```

---

## 4. Assignment Operators

```python
x = 5       # assign

x += 3      # same as x = x + 3  → 8
x -= 3      # same as x = x - 3  → 5
x *= 3      # same as x = x * 3  → 15
x /= 3      # same as x = x / 3  → 5.0
x %= 3      # same as x = x % 3  → 2.0
x **= 3     # same as x = x ** 3 → 8.0
x //= 3     # same as x = x // 3 → 2.0
```

---

## 5. Bitwise Operators

Operate on **integers at the binary (bit) level**:

```python
# Binary: 5 = 0101, 3 = 0011

print(5 & 3)   # 1   — AND:  0101 & 0011 = 0001
print(5 | 3)   # 7   — OR:   0101 | 0011 = 0111
print(5 ^ 3)   # 6   — XOR:  0101 ^ 0011 = 0110
print(~5)      # -6  — NOT:  ~0101 = 1010 (two's complement)
print(5 << 2)  # 20  — left shift:  0101 << 2 = 10100
print(5 >> 2)  # 1   — right shift: 0101 >> 2 = 0001
```

---

## 6. Membership Operators

Check if a value **is inside** a sequence:

```python
fruits = ["apple", "banana", "orange"]

print("apple" in fruits)      # True
print("grape" in fruits)      # False
print("grape" not in fruits)  # True

# Works on strings, lists, tuples, sets, dicts
print("p" in "Python")        # True
print("z" not in "Python")    # True

# For dicts, checks KEYS
person = {"name": "Alice", "age": 30}
print("name" in person)       # True
print("Alice" in person)      # False (values, not keys)
```

---

## 7. Identity Operators

Compare **memory addresses** (are they the SAME object?), not values:

```python
a = [1, 2, 3]
b = a           # b points to the SAME list

print(a is b)       # True — same object in memory
print(a is not b)   # False

c = [1, 2, 3]       # c is a DIFFERENT list with same values
print(a is c)       # False — different objects!
print(a == c)       # True  — same values (== compares values)
```

```
a → [1, 2, 3]  ←── b points here too
                    (a is b → True)

c → [1, 2, 3]       (different location in memory)
                    (a is c → False, but a == c → True)
```

> 💡 Use `==` to compare **values**, use `is` to compare **identity** (same object). Never use `is` to compare integers or strings — use `==`.

---

## Operator Precedence (Order of Operations)

Higher rows are evaluated first (like PEMDAS in math):

```
1. ()                 — Parentheses (highest priority)
2. **                 — Exponentiation
3. ~, +, - (unary)   — Unary operators
4. *, /, //, %        — Multiplication, division
5. +, -               — Addition, subtraction
6. <<, >>             — Bitwise shifts
7. &                  — Bitwise AND
8. ^                  — Bitwise XOR
9. |                  — Bitwise OR
10. ==, !=, <, >, <=, >= — Comparison
11. not               — Logical NOT
12. and               — Logical AND
13. or                — Logical OR (lowest priority)
```

```python
# Examples
print(2 + 3 * 4)        # 14 (not 20) — * before +
print((2 + 3) * 4)      # 20 — parentheses override
print(2 ** 3 ** 2)      # 512 — ** is right-associative: 2**(3**2) = 2**9
print(not True or False) # False — not before or
```

---

## Key Takeaways

- `/` is always float division; use `//` for integer (floor) division
- `%` gives the remainder — useful for checking even/odd (`x % 2 == 0`)
- `**` is exponentiation: `2**10 = 1024`
- `and`, `or`, `not` work on any truthy/falsy values, not just booleans
- `in` / `not in` check membership in lists, strings, tuples, sets, dict keys
- `is` checks identity (same object in memory); `==` checks value equality — don't mix them up
- Use parentheses `()` to control evaluation order when in doubt
