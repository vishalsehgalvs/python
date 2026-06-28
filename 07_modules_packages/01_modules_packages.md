# Python Modules, Packages, and pip

> Source: https://unwiredlearning.com/blog/python

---

## What Is a Module?

A **module** is simply a `.py` file containing Python code (functions, classes, variables) that can be reused in other files.

> 🔁 **Analogy:** A module is like a toolbox. Instead of keeping all tools scattered around, you organize them into labeled boxes. Need a hammer? Open the "tools" box. Need math functions? Open the `math` module.

---

## Importing Modules

```python
# Import entire module
import math

print(math.pi)          # 3.14159...
print(math.sqrt(25))    # 5.0
print(math.ceil(4.2))   # 5
print(math.floor(4.9))  # 4
```

### `from` import — import specific things:
```python
from math import pi, sqrt, ceil

print(pi)        # 3.14159... (no "math." prefix!)
print(sqrt(16))  # 4.0
print(ceil(3.1)) # 4
```

### `as` — import with alias:
```python
import numpy as np           # common alias
import pandas as pd
from datetime import datetime as dt

# Now use the alias
arr = np.array([1, 2, 3])
today = dt.now()
```

### Import everything (avoid this!):
```python
from math import *    # imports ALL names from math

print(pi)         # works, but pollutes namespace!
print(sqrt(9))    # works
```

> ⚠️ `from module import *` is bad practice — can cause naming conflicts and makes code hard to read. Use specific imports instead.

---

## Commonly Used Standard Library Modules

```python
import math          # math functions (sqrt, log, pi, ceil, floor)
import random        # random numbers, shuffling
import os            # operating system (files, directories)
import sys           # Python interpreter settings
import datetime      # dates and times
import json          # JSON encode/decode
import re            # regular expressions
import time          # sleep, timing
import collections   # specialized data structures (Counter, deque)
import itertools     # iterators (chain, product, combinations)
import functools     # higher-order functions (reduce, lru_cache)
```

```python
import random
print(random.randint(1, 10))         # random int 1–10
print(random.choice(["a", "b"]))     # random element
nums = [1, 2, 3, 4, 5]
random.shuffle(nums)                  # shuffle in place
print(nums)

import os
print(os.getcwd())           # current working directory
print(os.listdir("."))       # files in current dir
os.mkdir("new_folder")       # create folder

import datetime
now = datetime.datetime.now()
print(now)                   # 2024-01-15 10:30:45.123456
```

---

## Creating Your Own Module

Create a file `greetings.py`:
```python
# greetings.py
def say_hello(name):
    return f"Hello, {name}!"

def say_goodbye(name):
    return f"Goodbye, {name}!"

DEFAULT_GREETING = "Hi"
```

Use it in another file in the same folder:
```python
# main.py
import greetings

print(greetings.say_hello("Alice"))     # Hello, Alice!
print(greetings.DEFAULT_GREETING)       # Hi

# Or import specific parts
from greetings import say_goodbye
print(say_goodbye("Bob"))               # Goodbye, Bob!
```

---

## `__name__ == "__main__"`

Every Python file has a `__name__` variable:
- When run directly: `__name__` is `"__main__"`
- When imported: `__name__` is the module's filename

```python
# calculator.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

# This block only runs when YOU run calculator.py directly
# It does NOT run when another file imports calculator
if __name__ == "__main__":
    print("Running calculator.py directly!")
    print(add(3, 5))      # 8
    print(subtract(10, 3)) # 7
```

```
Run "python calculator.py"     → prints output (name == "__main__")
Run "import calculator"        → no output, just loads functions
```

> 💡 This is a best practice — always put test/demo code inside `if __name__ == "__main__":` so your module can be safely imported by others.

---

## Packages

A **package** is a folder of modules (with an `__init__.py` file).

```
my_package/
│── __init__.py        ← makes this folder a package
│── module_a.py
│── module_b.py
└── sub_package/
    │── __init__.py
    └── module_c.py
```

```python
# Using a package
import my_package.module_a
from my_package import module_b
from my_package.sub_package import module_c
```

---

## pip — Python Package Manager

`pip` installs packages from [PyPI (Python Package Index)](https://pypi.org) — over 400,000 packages!

```bash
# Install a package
pip install requests
pip install numpy pandas matplotlib

# Install specific version
pip install requests==2.28.0

# Install from requirements file
pip install -r requirements.txt

# Upgrade a package
pip install --upgrade requests

# Uninstall
pip uninstall requests

# List installed packages
pip list

# Show info about a package
pip show requests

# Save current packages to file
pip freeze > requirements.txt
```

### `requirements.txt` example:
```
requests==2.28.0
numpy>=1.21.0
pandas
flask==2.2.0
```

---

## Virtual Environments

Always use a **virtual environment** to isolate project dependencies:

```bash
# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (Mac/Linux)
source venv/bin/activate

# Deactivate
deactivate
```

> 💡 Your shell shows `(venv)` when the virtual environment is active. Always activate before installing packages for a project!

---

## Key Takeaways

- `import module` — import whole module; access with `module.name`
- `from module import name` — import specific item directly
- `import module as alias` — use a shorter name
- Create your own modules just by making a `.py` file
- `if __name__ == "__main__":` — guards code that should only run when file is executed directly (not imported)
- Packages = folders with `__init__.py` — organize related modules
- `pip install package_name` — install from PyPI
- Always use virtual environments (`python -m venv venv`) to keep project dependencies isolated
