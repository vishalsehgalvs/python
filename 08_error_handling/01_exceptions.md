# Python Error Handling — Exceptions

> Source: https://unwiredlearning.com/blog/python

---

## What Is an Exception?

An **exception** is an error that occurs at runtime — it stops the program unless you handle it.

> 🔁 **Analogy:** An exception is like a car's check engine light. Something went wrong. You can ignore it (crash), handle it (pull over and fix it), or log it (take note and continue carefully).

```python
print(10 / 0)
# ZeroDivisionError: division by zero

print(int("hello"))
# ValueError: invalid literal for int() with base 10: 'hello'

name = "Alice"
print(name[100])
# IndexError: string index out of range
```

---

## `try / except`

Wrap risky code in `try`, handle errors in `except`:

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")

# Program continues after handling the exception
print("Program still running!")
```

```
       try block
          │
    ┌─────▼─────┐
    │  run code │
    └─────┬─────┘
          │
     error?  ──── No ──→  continue normally
       │
      Yes
       │
    ┌──▼──────────┐
    │ except block│
    └──┬──────────┘
       │
    continue program
```

---

## Catching Multiple Exceptions

```python
def safe_divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
        return None
    except TypeError:
        print("Error: Both arguments must be numbers")
        return None

print(safe_divide(10, 2))    # 5.0
print(safe_divide(10, 0))    # Error: Cannot divide by zero → None
print(safe_divide("a", 2))   # Error: Both arguments must be numbers → None
```

### Catch multiple in one `except`:

```python
try:
    x = int(input("Enter a number: "))
    result = 10 / x
except (ValueError, ZeroDivisionError) as e:
    print(f"Error: {e}")
```

### Catch any exception:

```python
try:
    risky_operation()
except Exception as e:
    print(f"Something went wrong: {e}")
```

---

## Common Built-in Exceptions

| Exception           | When it happens                       |
| ------------------- | ------------------------------------- |
| `ValueError`        | Wrong value type (e.g., `int("abc")`) |
| `TypeError`         | Wrong type (e.g., `"a" + 1`)          |
| `ZeroDivisionError` | Dividing by zero                      |
| `IndexError`        | List index out of range               |
| `KeyError`          | Dictionary key not found              |
| `AttributeError`    | Object has no such attribute          |
| `FileNotFoundError` | File doesn't exist                    |
| `ImportError`       | Module not found                      |
| `NameError`         | Variable not defined                  |
| `RecursionError`    | Too much recursion (infinite loop)    |
| `OverflowError`     | Number too large                      |

---

## `try / except / else / finally`

```python
try:
    # code that might fail
    num = int(input("Enter a number: "))
    result = 100 / num
except ValueError:
    print("That's not a valid number!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    # runs ONLY if NO exception occurred
    print(f"Result is: {result}")
finally:
    # ALWAYS runs — with or without exception
    print("Calculation attempt complete.")
```

```
try → succeeds? → else → finally
try → fails?    → except → finally
```

> 💡 `finally` is great for cleanup (close files, release connections) — it always runs.

---

## `raise` — Manually Raise Exceptions

```python
def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 150:
        raise ValueError("Age cannot exceed 150")
    return age

try:
    set_age(-5)
except ValueError as e:
    print(f"Invalid age: {e}")   # Invalid age: Age cannot be negative
```

### Re-raise an exception:

```python
def process():
    try:
        risky_code()
    except ValueError as e:
        print(f"Logged: {e}")
        raise   # re-raises the same exception
```

---

## Custom Exceptions

Create your own exceptions by inheriting from `Exception`:

```python
# Define custom exception
class InsufficientFundsError(Exception):
    def __init__(self, amount, balance):
        self.amount = amount
        self.balance = balance
        super().__init__(f"Cannot withdraw ${amount}, only ${balance} available")

class NegativeAmountError(Exception):
    pass

# Use it in a class
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount < 0:
            raise NegativeAmountError("Amount cannot be negative")
        if amount > self.balance:
            raise InsufficientFundsError(amount, self.balance)
        self.balance -= amount
        return self.balance

account = BankAccount(100)

try:
    account.withdraw(150)
except InsufficientFundsError as e:
    print(e)   # Cannot withdraw $150, only $100 available
except NegativeAmountError as e:
    print(e)
```

---

## Exception Hierarchy

```
BaseException
├── SystemExit
├── KeyboardInterrupt
└── Exception
    ├── ValueError
    ├── TypeError
    ├── ZeroDivisionError
    ├── IndexError
    ├── KeyError
    ├── AttributeError
    ├── FileNotFoundError
    ├── ImportError
    └── ... (and your custom exceptions)
```

Catching `Exception` catches all "normal" exceptions but not `SystemExit` or `KeyboardInterrupt` (which is usually desired).

---

## Best Practices

```python
# ✅ Catch specific exceptions
try:
    file = open("data.txt")
except FileNotFoundError:
    print("File not found")

# ❌ Too broad — hides bugs
try:
    something_complex()
except:          # catches EVERYTHING including Ctrl+C, SystemExit
    pass

# ✅ Log the error, don't just swallow it
import logging
try:
    risky()
except Exception as e:
    logging.error(f"Error in risky(): {e}")
    raise   # re-raise after logging

# ✅ Use finally for cleanup
try:
    f = open("file.txt")
    data = f.read()
except FileNotFoundError:
    print("File not found")
finally:
    if 'f' in locals():
        f.close()   # always close the file!
```

---

## Key Takeaways

- `try / except` handles errors gracefully without crashing the program
- Catch **specific** exceptions, not bare `except:` — it hides real bugs
- `else` block runs when `try` succeeds (no exception)
- `finally` block always runs — ideal for cleanup (closing files, releasing locks)
- `raise ExceptionType("message")` to manually trigger an exception
- Create custom exceptions by subclassing `Exception`
- Use `except ExceptionType as e:` to access the error message via `e`
