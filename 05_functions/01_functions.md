# Python Functions

> Source: https://unwiredlearning.com/blog/python

---

## What Is a Function?

A function is a **named, reusable block of code** that performs a specific task.

> 🔁 **Analogy:** A function is like a recipe. You write it once ("how to make pasta"), and anyone can follow it anytime. You don't rewrite the recipe each time you cook — you just say "make pasta."

**Why use functions?**
- **Reusability** — write once, use many times
- **Readability** — break code into named, understandable pieces
- **Maintainability** — fix a bug in one place, not everywhere

---

## Defining and Calling Functions

```python
# Define a function
def function_name(parameters):
    # function body
    return result    # optional

# Call a function
result = function_name(arguments)
```

```python
# Example: add two numbers
def add_numbers(a, b):
    result = a + b
    return result

# Call the function
sum = add_numbers(3, 5)
print(sum)   # 8
```

---

## Parameters vs Arguments

```
Parameters → placeholders in the function definition
Arguments  → actual values passed when calling

def add(a, b):    ← a and b are PARAMETERS
    return a + b

add(3, 5)         ← 3 and 5 are ARGUMENTS
```

---

## Return Values

```python
# Return a single value
def square(n):
    return n * n

result = square(5)
print(result)   # 25

# Return multiple values (as a tuple)
def min_max(numbers):
    return min(numbers), max(numbers)

low, high = min_max([3, 1, 4, 1, 5, 9])
print(low, high)   # 1 9

# No return = returns None
def greet(name):
    print(f"Hello, {name}!")   # just prints, doesn't return

val = greet("Alice")
print(val)   # None
```

---

## Default Parameters

Provide default values so callers can skip those arguments:

```python
def greet(name, message="Hello"):
    print(f"{message}, {name}!")

greet("Alice")              # Hello, Alice!
greet("Bob", "Hey")         # Hey, Bob!
greet("Carol", "Goodbye")   # Goodbye, Carol!
```

> ⚠️ Default parameters must come LAST:
```python
def f(a, b=5, c=10):  # ✅ OK
    pass

def f(a=5, b, c=10):  # ❌ SyntaxError: non-default argument follows default
    pass
```

---

## Types of Arguments

### Positional arguments:
Matched by **position** in order:
```python
def describe(name, age, city):
    print(f"{name}, {age}, from {city}")

describe("Alice", 30, "Seattle")   # Alice, 30, from Seattle
```

### Keyword arguments:
Matched by **name** — order doesn't matter:
```python
describe(age=30, city="Seattle", name="Alice")   # same result!
```

### Mix of both (positional must come first):
```python
describe("Alice", city="Seattle", age=30)   # ✅
# describe(city="Seattle", "Alice", 30)     # ❌ positional after keyword
```

---

## `*args` — Variable Positional Arguments

Accept **any number** of positional arguments:

```python
def add_all(*args):       # args is a TUPLE of all positional args
    total = 0
    for num in args:
        total += num
    return total

print(add_all(1, 2))        # 3
print(add_all(1, 2, 3, 4))  # 10
print(add_all())            # 0
```

---

## `**kwargs` — Variable Keyword Arguments

Accept **any number** of keyword arguments:

```python
def display_info(**kwargs):   # kwargs is a DICT of all keyword args
    for key, value in kwargs.items():
        print(f"{key}: {value}")

display_info(name="Alice", age=30, city="Seattle")
# name: Alice
# age: 30
# city: Seattle
```

---

## Combined: All Argument Types

```python
def sample_function(a, b, *args, **kwargs):
    print("a:", a)
    print("b:", b)
    print("args:", args)
    print("kwargs:", kwargs)

sample_function(1, 2, 3, 4, 5, key1="value1", key2="value2")
# a: 1
# b: 2
# args: (3, 4, 5)
# kwargs: {'key1': 'value1', 'key2': 'value2'}
```

**Order rule:** `def f(positional, *args, **kwargs)` — always this order.

---

## Local and Global Scope

```python
global_var = "I'm global"   # visible everywhere

def my_function():
    local_var = "I'm local"   # only inside this function
    print(global_var)          # ✅ can read global
    print(local_var)           # ✅ can read local

my_function()
print(global_var)   # ✅ works
# print(local_var)  # ❌ NameError: local_var not defined here
```

### Modifying a global variable inside a function:
```python
count = 0

def increment():
    global count   # ← tell Python we want the GLOBAL count
    count += 1

increment()
increment()
print(count)   # 2
```

> 💡 Avoid using `global` excessively — it makes code harder to reason about. Prefer passing values as arguments and returning them.

---

## Nested Functions

```python
def outer():
    x = 10

    def inner():
        print(x)    # can access outer's variable

    inner()

outer()   # prints 10
```

### `nonlocal` for modifying outer variable:
```python
def counter():
    count = 0

    def increment():
        nonlocal count   # modify the ENCLOSING function's variable
        count += 1
        return count

    return increment

c = counter()
print(c())   # 1
print(c())   # 2
print(c())   # 3
```

---

## Key Takeaways

- `def name(params):` defines a function; call it with `name(args)`
- `return` sends a value back; no `return` = returns `None`
- Default parameters: `def f(x, y=10):` — must be at the end
- Keyword arguments: `f(y=5, x=3)` — order doesn't matter when using names
- `*args` collects extra positional args as a tuple
- `**kwargs` collects extra keyword args as a dict
- Local variables: only exist inside the function they're defined in
- Use `global` to modify a global variable; use `nonlocal` for an enclosing function's variable
