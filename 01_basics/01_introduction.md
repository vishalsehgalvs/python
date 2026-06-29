# Python Introduction, Setup & First Program

> Source: https://unwiredlearning.com/blog/python

---

## What Is Python?

Python is a **high-level, interpreted, general-purpose** programming language created by **Guido van Rossum** and first released in **1991**.

> 🔁 **Analogy:** If C++ is like driving a manual sports car — powerful but complex — Python is like a self-driving car. You can still go fast, but it handles all the gears for you so you can focus on where you're going.

**Key features:**

- **Readable syntax** — code looks almost like plain English
- **Dynamically typed** — no need to declare variable types
- **Cross-platform** — runs on Windows, Mac, Linux
- **Huge library** — built-in tools for almost everything
- **Massive ecosystem** — packages for web, data, AI, automation, and more
- **Interpreted** — runs line-by-line (no compilation step needed)

---

## What Python Is Used For

```
Python
  │
  ├── Web Development (Django, Flask, FastAPI)
  ├── Data Science & Analysis (Pandas, NumPy)
  ├── Machine Learning & AI (TensorFlow, scikit-learn)
  ├── Automation & Scripting (Selenium, PyAutoGUI)
  ├── API Development (REST APIs)
  ├── Desktop Apps (Tkinter, PyQt)
  └── DevOps & Cloud Tooling
```

---

## Installation

### Windows

1. Go to https://www.python.org/downloads/
2. Download the latest Python 3.x installer
3. ✅ **CHECK "Add Python to PATH"** during installation (important!)
4. Click "Install Now"
5. Verify: open Command Prompt → type `python --version`

### macOS

1. macOS comes with Python 2 (old/unsupported) — you need Python 3
2. Go to https://www.python.org/downloads/
3. Download the macOS installer and run it
4. Verify: open Terminal → type `python3 --version`

### Quick Verification

```bash
python --version      # Windows
python3 --version     # Mac/Linux
# Should show: Python 3.x.x
```

> 💡 You can also use an online Python REPL at https://replit.com or https://pythontutor.com — no installation needed!

---

## Writing Your First Python Program

### Method 1: Interactive Shell (REPL)

The **REPL** (Read-Eval-Print Loop) is a live interactive Python console:

```
Windows: Open CMD → type python → press Enter
Mac:     Open Terminal → type python3 → press Enter

>>> print("Hello, World!")
Hello, World!
>>> 2 + 3
5
>>> exit()    ← to quit
```

> 🔁 **Analogy:** The REPL is like a calculator — you type something, press Enter, and get the answer immediately. Great for testing small things.

### Method 2: Write a .py Script

```python
# hello.py

print("Hello, World!")
print("Welcome to Python!")
```

Run it:

```bash
python hello.py          # Windows
python3 hello.py         # Mac/Linux
```

Output:

```
Hello, World!
Welcome to Python!
```

---

## How Python Works

```
You write:          hello.py
                         │
                         ▼
                  Python Interpreter
                    (reads line by line)
                         │
                         ▼
                  Byte Code (.pyc)
                         │
                         ▼
               Python Virtual Machine (PVM)
                         │
                         ▼
                  Output on screen
```

Unlike C++, Python doesn't need a separate compile step — the interpreter handles everything when you run your script.

---

## Python vs JavaScript vs C++ Quick Compare

|             | Python                       | JavaScript             | C++                |
| ----------- | ---------------------------- | ---------------------- | ------------------ |
| Hello World | `print("Hello")`             | `console.log("Hello")` | `cout << "Hello";` |
| Variables   | `x = 5`                      | `let x = 5`            | `int x = 5;`       |
| Types       | Dynamic                      | Dynamic                | Static             |
| Semicolons  | ❌ No                        | ✅ (optional)          | ✅ Required        |
| Indentation | ✅ Required (defines blocks) | Style only             | Style only         |
| Speed       | Slower                       | Medium                 | Fastest            |

---

## Recommended Tools

| Tool                 | Use                | Where                 |
| -------------------- | ------------------ | --------------------- |
| **VS Code**          | Code editor        | code.visualstudio.com |
| **PyCharm**          | Python IDE         | jetbrains.com/pycharm |
| **Jupyter Notebook** | Data science       | jupyter.org           |
| **IDLE**             | Comes with Python  | Built-in              |
| **Replit**           | Online browser IDE | replit.com            |

---

## Key Takeaways

- Python is readable, beginner-friendly, and used everywhere — web, data, AI, automation
- Always install Python 3.x (not Python 2 — it's retired)
- ✅ Check "Add Python to PATH" on Windows during installation
- Run scripts with `python filename.py` (or `python3` on Mac)
- The REPL (`python` in terminal) lets you test code interactively
- No semicolons; indentation defines code blocks (use 4 spaces per level)
