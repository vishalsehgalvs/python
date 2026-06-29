# Python Programming Notes

> Source: https://unwiredlearning.com/blog/python

---

## What Is This?

A complete set of Python notes written in plain English — no jargon, real examples, ASCII diagrams, and analogies throughout. Covers everything from "Hello World" to OOP, decorators, and regex.

---

## Folder Structure

```
python/
├── README.md                         ← You are here
│
├── 01_basics/
│   ├── 01_introduction.md            ← What is Python, setup, first program
│   ├── 02_variables_datatypes.md     ← Variables, data types, literals, keywords
│   ├── 03_operators.md               ← All operator types
│   └── 04_input_output.md            ← input(), print(), f-strings
│
├── 02_control_flow/
│   ├── 01_if_else_elif.md            ← Conditionals, indentation, nested if
│   └── 02_loops.md                   ← for, while, break, continue, pass
│
├── 03_strings/
│   └── 01_strings.md                 ← Comments, string methods, escape chars
│
├── 04_data_structures/
│   ├── 01_lists.md                   ← Lists, indexing, slicing, methods
│   ├── 02_tuples_sets.md             ← Tuples, sets, frozensets
│   └── 03_dictionaries.md            ← Dicts, methods, iteration
│
├── 05_functions/
│   ├── 01_functions.md               ← Defining, calling, parameters, return
│   ├── 02_args_kwargs_scope.md       ← *args, **kwargs, local/global scope
│   └── 03_lambda_map_filter.md       ← Lambda, map, filter, reduce
│
├── 06_oop/
│   ├── 01_classes_objects.md         ← Classes, objects, __init__, self
│   ├── 02_inheritance.md             ← Inheritance, super(), multiple inheritance
│   └── 03_advanced_oop.md            ← Encapsulation, abstract classes, operator overloading
│
├── 07_modules_packages/
│   └── 01_modules_packages.md        ← import, from, pip, PyPI, __name__
│
├── 08_error_handling/
│   └── 01_exceptions.md              ← try/except/else/finally, custom exceptions
│
├── 09_file_handling/
│   └── 01_file_handling.md           ← open, read, write, context manager
│
└── 10_advanced/
    ├── 01_list_comprehension.md      ← List comprehension, generator expressions
    ├── 02_recursion.md               ← Recursion, base case, examples
    ├── 03_decorators.md              ← Decorators, @syntax, decorator factories
    ├── 04_regex.md                   ← Regular expressions, re module
    └── 05_logging_datetime.md        ← logging module, datetime module
```

---

## Quick Python Cheat Sheet

```python
# Variables
name = "Alice"
age = 30
pi = 3.14
is_active = True

# f-string output
print(f"{name} is {age} years old")

# List
fruits = ["apple", "banana", "cherry"]
fruits.append("mango")

# Dict
person = {"name": "Bob", "age": 25}
print(person["name"])

# Function
def greet(name):
    return f"Hello, {name}!"

# Class
class Dog:
    def __init__(self, name):
        self.name = name
    def bark(self):
        print(f"{self.name} says Woof!")

# List comprehension
squares = [x**2 for x in range(10)]

# Lambda
double = lambda x: x * 2
```

---

## Python vs Other Languages

| Feature        | Python              | JavaScript           | C++            |
| -------------- | ------------------- | -------------------- | -------------- |
| Typing         | Dynamic             | Dynamic              | Static         |
| Syntax         | Indentation         | `{}` braces          | `{}` braces    |
| Compilation    | Interpreted         | Interpreted/JIT      | Compiled       |
| Speed          | Slower              | Medium               | Fastest        |
| Use cases      | Data, AI, scripting | Web frontend/backend | Systems, games |
| Learning curve | Easiest             | Medium               | Hard           |

---

## How to Run Python

```bash
# Run a script
python hello.py          # Windows
python3 hello.py         # Mac/Linux

# Interactive shell (REPL)
python                   # Windows
python3                  # Mac/Linux
>>> print("Hello")       # type code directly
>>> exit()               # quit

# Check version
python --version
```

---

## Key Takeaways

- Python is beginner-friendly — indentation replaces braces, syntax reads like English
- Used for web dev, data science, AI/ML, automation, and scripting
- Dynamic typing — no need to declare variable types
- Everything is an object in Python
- Large standard library + massive ecosystem of packages (pip/PyPI)
