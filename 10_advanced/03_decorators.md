# Python Decorators

> Source: https://unwiredlearning.com/blog/python

---

## What Is a Decorator?

A **decorator** is a function that **wraps another function** to add behavior before or after it runs — without modifying the original function.

> 🔁 **Analogy:** A decorator is like adding a security guard outside a store. When a customer (function call) arrives, the guard checks ID first (added behavior), lets them in (original function runs), then says goodbye (after behavior). The store itself didn't change.

---

## Functions Are First-Class Objects

In Python, functions can be passed as arguments and returned from other functions:

```python
def greet(name):
    return f"Hello, {name}!"

# Assign function to variable
say_hello = greet
print(say_hello("Alice"))   # Hello, Alice!

# Pass function as argument
def apply(func, value):
    return func(value)

result = apply(greet, "Bob")
print(result)   # Hello, Bob!

# Return function from function
def make_multiplier(n):
    def multiply(x):
        return x * n
    return multiply   # returns the inner function!

double = make_multiplier(2)
triple = make_multiplier(3)
print(double(5))   # 10
print(triple(5))   # 15
```

---

## Creating a Decorator

A decorator wraps a function by:
1. Taking the original function as an argument
2. Defining a wrapper function inside
3. Returning the wrapper

```python
def my_decorator(func):
    def wrapper():
        print("Before function runs")   # added behavior
        func()                          # original function
        print("After function runs")    # added behavior
    return wrapper

def say_hello():
    print("Hello!")

# Manually decorate
say_hello = my_decorator(say_hello)
say_hello()
# Before function runs
# Hello!
# After function runs
```

---

## Using `@` Syntax (Sugar)

The `@decorator` syntax is shorthand for `function = decorator(function)`:

```python
def my_decorator(func):
    def wrapper():
        print("Before function runs")
        func()
        print("After function runs")
    return wrapper

@my_decorator        # ← same as: say_hello = my_decorator(say_hello)
def say_hello():
    print("Hello!")

say_hello()
# Before function runs
# Hello!
# After function runs
```

---

## Decorator with Arguments

Use `*args, **kwargs` to make decorators work with any function signature:

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):       # accept any arguments
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)  # pass arguments to original
        print(f"Finished {func.__name__}")
        return result                   # return original result
    return wrapper

@my_decorator
def add(a, b):
    return a + b

@my_decorator
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

result = add(3, 5)   # Calling add → 8 → Finished add
print(result)        # 8

greet("Alice", greeting="Hey")   # Calling greet → Hey, Alice! → Finished greet
```

---

## Real-World Decorator Examples

### Timing decorator:
```python
import time
import functools

def timer(func):
    @functools.wraps(func)   # preserve original function name/docstring
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)
    return "done"

slow_function()
# slow_function took 1.0012 seconds
```

### Logging decorator:
```python
import functools

def log_calls(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"LOG: Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"LOG: {func.__name__} returned {result}")
        return result
    return wrapper

@log_calls
def multiply(x, y):
    return x * y

multiply(3, 4)
# LOG: Calling multiply with args=(3, 4), kwargs={}
# LOG: multiply returned 12
```

### Caching decorator (manual):
```python
def memoize(func):
    cache = {}
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper

@memoize
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(50))   # fast!
```

---

## Decorators with Parameters

A decorator factory — a function that *returns* a decorator:

```python
def repeat(n):          # outer: takes parameter
    def decorator(func):    # middle: the actual decorator
        def wrapper(*args, **kwargs):  # inner: replaces the function
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)   # call repeat(3) which returns the decorator
def say_hello():
    print("Hello!")

say_hello()
# Hello!
# Hello!
# Hello!
```

---

## Stacking Decorators

Multiple decorators stack from bottom to top:

```python
@timer
@log_calls
def my_function():
    pass

# Equivalent to:
# my_function = timer(log_calls(my_function))
# log_calls runs first (closest to function), then timer wraps that
```

---

## `functools.wraps`

Without `@functools.wraps`, the decorated function loses its name and docstring:

```python
import functools

def my_decorator(func):
    @functools.wraps(func)   # ← preserve metadata
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def greet(name):
    """Greets a person by name."""
    return f"Hello, {name}!"

print(greet.__name__)    # greet (not "wrapper")
print(greet.__doc__)     # Greets a person by name.
```

---

## Key Takeaways

- A decorator is a function that takes a function and returns an enhanced version
- `@decorator` syntax = `func = decorator(func)` — syntactic sugar
- Always use `*args, **kwargs` in wrappers to support any function signature
- Always use `@functools.wraps(func)` to preserve the original function's metadata
- Common uses: timing, logging, caching, authentication, validation
- Decorators with parameters need 3 levels: outer (params) → decorator → wrapper
- Stacking: `@a @b def f():` applies `b` first, then `a`
