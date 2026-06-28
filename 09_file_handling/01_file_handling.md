# Python File Handling

> Source: https://unwiredlearning.com/blog/python

---

## Why File Handling?

Programs often need to **read from** or **write to** files — config files, logs, CSV data, text reports, etc.

> 🔁 **Analogy:** Working with a file is like working with a physical document. You open it, do your work (read or write), then close it. If you forget to close it, it's like leaving a document spread open on your desk forever — other programs can't access it.

---

## Opening Files

```python
# Basic syntax
file = open("filename.txt", mode)

# ALWAYS close when done
file.close()
```

### File modes:
| Mode | Meaning |
|------|---------|
| `"r"` | Read (default). Error if file doesn't exist |
| `"w"` | Write. Creates file if not exist. **Overwrites** content |
| `"a"` | Append. Creates if not exist. Adds to end |
| `"x"` | Create. Error if file already exists |
| `"r+"` | Read + write |
| `"rb"` | Read binary (images, PDFs, etc.) |
| `"wb"` | Write binary |

---

## The `with` Statement — Context Manager (Recommended!)

The `with` statement automatically closes the file when the block exits — even if an error occurs:

```python
# ✅ Preferred — auto-closes file
with open("hello.txt", "w") as file:
    file.write("Hello, World!")
# file is automatically closed here

# ❌ Manual approach (easy to forget .close())
file = open("hello.txt", "w")
file.write("Hello, World!")
file.close()   # easy to forget, and won't run if exception occurs!
```

---

## Writing to Files

```python
# Write — creates file (or overwrites!)
with open("output.txt", "w") as file:
    file.write("First line\n")
    file.write("Second line\n")
    file.write("Third line\n")

# writelines — write a list of lines
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open("output.txt", "w") as file:
    file.writelines(lines)

# Append — add to existing file without overwriting
with open("output.txt", "a") as file:
    file.write("This line is added at the end\n")
```

---

## Reading from Files

```python
# read() — reads entire file as one string
with open("output.txt", "r") as file:
    content = file.read()
    print(content)

# readline() — reads ONE line at a time
with open("output.txt", "r") as file:
    first_line = file.readline()    # "First line\n"
    second_line = file.readline()   # "Second line\n"

# readlines() — reads all lines into a list
with open("output.txt", "r") as file:
    lines = file.readlines()
    # ["First line\n", "Second line\n", "Third line\n"]

# Iterate line by line (most memory efficient for large files)
with open("output.txt", "r") as file:
    for line in file:
        print(line.strip())   # strip() removes trailing \n
```

---

## File Operations with `os`

```python
import os

# Check if file exists
if os.path.exists("myfile.txt"):
    print("File exists!")

# Get file size
size = os.path.getsize("myfile.txt")

# Rename a file
os.rename("old_name.txt", "new_name.txt")

# Delete a file
os.remove("myfile.txt")

# Get current directory
print(os.getcwd())

# List files in directory
files = os.listdir(".")
```

---

## Working with CSV Files

```python
import csv

# Write CSV
data = [
    ["Name", "Age", "City"],
    ["Alice", 30, "New York"],
    ["Bob", 25, "Boston"],
    ["Carol", 35, "Chicago"]
]

with open("people.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

# Read CSV
with open("people.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)   # ['Name', 'Age', 'City'], ['Alice', '30', 'New York'], ...

# Read CSV as dictionary (header row = keys)
with open("people.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["Name"], row["Age"])   # Alice 30, Bob 25, ...
```

---

## Working with JSON Files

```python
import json

# Write JSON
data = {
    "name": "Alice",
    "age": 30,
    "hobbies": ["reading", "coding", "hiking"]
}

with open("data.json", "w") as file:
    json.dump(data, file, indent=4)   # indent for pretty-printing

# Read JSON
with open("data.json", "r") as file:
    loaded = json.load(file)

print(loaded["name"])     # Alice
print(loaded["hobbies"])  # ['reading', 'coding', 'hiking']
```

---

## Handling File Errors

```python
try:
    with open("nonexistent.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("Error: File not found!")
except PermissionError:
    print("Error: No permission to access this file!")
except IOError as e:
    print(f"I/O Error: {e}")
```

---

## Complete Example — Log File Writer

```python
import datetime
import os

def write_log(message, log_file="app.log"):
    """Append a timestamped message to a log file."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] {message}\n"

    with open(log_file, "a") as file:
        file.write(log_entry)

def read_log(log_file="app.log"):
    """Read and display all log entries."""
    if not os.path.exists(log_file):
        print("No log file found.")
        return

    with open(log_file, "r") as file:
        for line in file:
            print(line.strip())

# Usage
write_log("Application started")
write_log("User logged in: Alice")
write_log("Error: Database connection failed")

read_log()
# [2024-01-15 10:30:00] Application started
# [2024-01-15 10:30:01] User logged in: Alice
# [2024-01-15 10:30:02] Error: Database connection failed
```

---

## Key Takeaways

- `open(filename, mode)` opens a file; always close it with `file.close()` or use `with`
- **Always use `with open(...) as file:`** — it auto-closes and is exception-safe
- Modes: `"r"` read, `"w"` write (overwrites!), `"a"` append, `"x"` create new
- `file.read()` — entire file as string; `file.readlines()` — list of lines; `for line in file:` — line by line
- `file.write(string)` writes text; `file.writelines(list)` writes multiple lines
- Use `os.path.exists()` before reading to avoid `FileNotFoundError`
- `csv` module for CSV files; `json` module for JSON files — both work with `with open()`
