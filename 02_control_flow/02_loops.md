# Python Loops: for, while, break, continue, pass

> Source: https://unwiredlearning.com/blog/python

---

## Why Loops?

Loops let you run the same block of code multiple times without copy-pasting.

> 🔁 **Analogy:** A loop is like a stamp machine at the post office. Instead of manually stamping each envelope, you set up the machine and it stamps them all automatically.

---

## `for` Loop

Iterates over a **sequence** (list, string, tuple, range, etc.):

```python
fruits = ["apple", "banana", "orange"]

for fruit in fruits:
    print(fruit)
# Output:
# apple
# banana
# orange
```

```
for each item in the sequence:
    run the body
         │
         ▼
    (next item)
         │
         ▼
    (until no items left)
         │
         ▼
    loop ends
```

### `for` with `range()`:

```python
# range(stop) → 0 to stop-1
for i in range(5):
    print(i)
# Output: 0 1 2 3 4

# range(start, stop) → start to stop-1
for i in range(2, 7):
    print(i)
# Output: 2 3 4 5 6

# range(start, stop, step) → with step
for i in range(0, 10, 2):
    print(i)
# Output: 0 2 4 6 8

# Count down
for i in range(5, 0, -1):
    print(i)
# Output: 5 4 3 2 1
```

### `for` with `enumerate()` — index + value:
```python
fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
# 0: apple
# 1: banana
# 2: cherry
```

### `for` over a string:
```python
for char in "Hello":
    print(char)
# H e l l o  (each on new line)
```

---

## `while` Loop

Keeps running **while** a condition is `True`:

```python
counter = 0

while counter < 5:
    print(counter)
    counter += 1   # ← always update! or infinite loop

# Output: 0 1 2 3 4
```

```
condition True?
     │
    Yes ──► run body ──► go back to condition
     │
    No  ──► exit loop
```

### User input validation with `while`:
```python
number = int(input("Enter a number between 1 and 10: "))

while number < 1 or number > 10:
    print("Invalid! Try again.")
    number = int(input("Enter a number between 1 and 10: "))

print(f"Valid: {number}")
```

### Menu with `while`:
```python
choice = ""

while choice != "q":
    print("\n1. Say hello")
    print("2. Say bye")
    print("q. Quit")
    choice = input("Your choice: ")

    if choice == "1":
        print("Hello!")
    elif choice == "2":
        print("Goodbye!")
```

---

## `break` — Exit the Loop Early

Stops the loop immediately and jumps out:

```python
for i in range(10):
    if i == 5:
        break       # stop here
    print(i)
# Output: 0 1 2 3 4
```

### Practical: search in list
```python
numbers = [4, 7, 2, 9, 1, 5]
target = 9

for num in numbers:
    if num == target:
        print(f"Found {target}!")
        break       # no need to keep searching
```

---

## `continue` — Skip This Iteration

Skips the rest of the current iteration and moves to the next:

```python
for i in range(10):
    if i % 2 == 0:
        continue    # skip even numbers
    print(i)
# Output: 1 3 5 7 9
```

---

## `pass` — Do Nothing (Placeholder)

`pass` is a no-operation — does nothing. Used as a placeholder when you need a block but have no code yet:

```python
for i in range(10):
    if i % 2 == 0:
        pass        # even numbers: do nothing
    else:
        print(i)    # odd numbers: print
# Output: 1 3 5 7 9

# Common use: empty function/class body
class MyClass:
    pass   # will implement later

def my_function():
    pass   # will implement later
```

---

## `break` vs `continue` vs `pass`

```python
# break: exit loop entirely
for i in range(5):
    if i == 3: break
    print(i)
# 0 1 2

# continue: skip current iteration, keep looping
for i in range(5):
    if i == 3: continue
    print(i)
# 0 1 2 4

# pass: do nothing, continue normally
for i in range(5):
    if i == 3: pass
    print(i)
# 0 1 2 3 4   (pass has NO effect on flow)
```

---

## `for...else` and `while...else`

Python has a unique `else` for loops — runs when the loop **completes normally** (not broken out of):

```python
# for...else
for i in range(5):
    if i == 10:
        break
else:
    print("Loop completed without break!")  # ← this runs

# while...else
n = 0
while n < 3:
    n += 1
else:
    print("Done!")   # ← runs after loop
```

Useful for search patterns:
```python
numbers = [1, 2, 3, 4, 5]
target = 9

for num in numbers:
    if num == target:
        print(f"Found {target}")
        break
else:
    print(f"{target} not found")   # runs only if no break
# Output: 9 not found
```

---

## Nested Loops

A loop inside a loop — used for 2D data:

```python
for i in range(1, 4):
    for j in range(1, 4):
        print(i * j, end="\t")
    print()
# 1  2  3
# 2  4  6
# 3  6  9

# Triangle pattern
for i in range(1, 6):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()
# *
# * *
# * * *
# * * * *
# * * * * *
```

---

## Choosing the Right Loop

| Situation | Use |
|-----------|-----|
| Know how many times to repeat | `for` with `range()` |
| Iterate over items in a list/string | `for item in collection` |
| Repeat until condition changes | `while` |
| Run at least once | `while True` + `break` |

---

## Key Takeaways

- `for item in sequence:` — iterate over any iterable (list, string, tuple, range)
- `range(start, stop, step)` generates number sequences for `for` loops
- `while condition:` — repeats as long as condition is `True`; always update the condition variable!
- `break` exits the loop immediately
- `continue` skips the rest of the current iteration
- `pass` does nothing — used as a placeholder in empty blocks
- `for/while...else` block runs when loop ends naturally (no `break`)
- **Infinite loop** = `while True:` — must have a `break` condition inside!
