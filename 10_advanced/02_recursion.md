# Python Recursion

> Source: https://unwiredlearning.com/blog/python

---

## What Is Recursion?

Recursion is when a **function calls itself** to solve a smaller version of the same problem.

> 🔁 **Analogy:** Imagine you're in a line of people, and you want to know what position you're in. You ask the person in front of you. They ask the person in front of them. This continues until the first person (who knows they're #1) tells the next person, who adds 1 and tells the next... until the answer reaches you. That's recursion!

Every recursive function needs:
1. **Base case** — the stopping condition (no more recursion)
2. **Recursive case** — the function calling itself with a smaller problem

---

## Basic Structure

```python
def recursive_function(parameters):
    # Base case — STOP condition
    if base_condition:
        return base_value

    # Recursive case — call itself with smaller problem
    return recursive_function(smaller_parameters)
```

---

## Example 1: Factorial

`5! = 5 × 4 × 3 × 2 × 1 = 120`

```python
def factorial(n):
    # Base case
    if n == 0 or n == 1:
        return 1

    # Recursive case
    return n * factorial(n - 1)

print(factorial(5))   # 120
print(factorial(0))   # 1
```

How it works:
```
factorial(5)
  = 5 * factorial(4)
  = 5 * (4 * factorial(3))
  = 5 * (4 * (3 * factorial(2)))
  = 5 * (4 * (3 * (2 * factorial(1))))
  = 5 * (4 * (3 * (2 * 1)))    ← base case hit!
  = 5 * (4 * (3 * 2))
  = 5 * (4 * 6)
  = 5 * 24
  = 120
```

---

## Example 2: Fibonacci

`F(n) = F(n-1) + F(n-2)`, where `F(0)=0, F(1)=1`

```python
def fibonacci(n):
    # Base cases
    if n == 0:
        return 0
    if n == 1:
        return 1

    # Recursive case
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(0))   # 0
print(fibonacci(1))   # 1
print(fibonacci(5))   # 5
print(fibonacci(10))  # 55
```

---

## Example 3: Sum of a List

```python
def list_sum(numbers):
    # Base case — empty list
    if len(numbers) == 0:
        return 0

    # First element + sum of the rest
    return numbers[0] + list_sum(numbers[1:])

print(list_sum([1, 2, 3, 4, 5]))   # 15
```

---

## Example 4: Reverse a String

```python
def reverse_string(s):
    if len(s) <= 1:      # base case
        return s

    return reverse_string(s[1:]) + s[0]   # recursive case

print(reverse_string("hello"))   # "olleh"
```

---

## The Call Stack

Each recursive call is added to the call stack:

```
Call:  factorial(4)
       factorial(3)
       factorial(2)
       factorial(1)  ← hits base case, returns 1
Stack: [f(4), f(3), f(2), f(1)]

Return: f(1) = 1
        f(2) = 2 * 1 = 2
        f(3) = 3 * 2 = 6
        f(4) = 4 * 6 = 24
```

> ⚠️ **Recursion limit:** Python limits recursion to 1000 calls by default. Exceeding it causes `RecursionError: maximum recursion depth exceeded`.

```python
import sys
print(sys.getrecursionlimit())   # 1000

# Increase limit (use with caution!)
sys.setrecursionlimit(5000)
```

---

## Recursion vs Iteration

| | Recursion | Iteration (loops) |
|---|-----------|-------------------|
| Code style | Elegant, closer to math definition | More explicit |
| Performance | Slower (function call overhead, stack) | Faster |
| Memory | More (call stack) | Less |
| Risk | RecursionError if too deep | No depth limit |
| Best for | Trees, graphs, divide-and-conquer | Simple counting, loops |

```python
# Factorial: recursion
def factorial_recursive(n):
    return 1 if n <= 1 else n * factorial_recursive(n - 1)

# Factorial: iteration (usually better for production)
def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
```

---

## Fibonacci with Memoization (Optimization)

Naive Fibonacci recalculates the same values many times. **Memoization** caches results:

```python
from functools import lru_cache

@lru_cache(maxsize=None)   # cache all results
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(50))    # fast!  (without cache: extremely slow)
print(fibonacci(100))   # still fast
```

---

## Key Takeaways

- Recursion = a function that calls itself to solve smaller subproblems
- Every recursive function needs a **base case** (stops recursion) and a **recursive case**
- Without a base case (or a wrong one) → infinite recursion → `RecursionError`
- Python default recursion limit: 1000 calls
- Recursion is elegant for problems naturally defined recursively (trees, fractals, divide-and-conquer)
- For simple counting/looping tasks, iteration is faster and safer
- Use `@lru_cache` from `functools` to cache expensive recursive calls (memoization)
