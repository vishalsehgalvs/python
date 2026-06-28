# Python Logging and Datetime

> Source: https://unwiredlearning.com/blog/python

---

## Part 1: The `logging` Module

### Why Not Just Use `print()`?

| `print()` | `logging` |
|-----------|-----------|
| No severity levels | DEBUG, INFO, WARNING, ERROR, CRITICAL |
| Can't filter | Filter by level |
| No timestamps | Can include timestamps |
| No file output | Can write to files |
| Hard to disable | Easy to enable/disable |

> 🔁 **Analogy:** `print()` is like shouting everything to the room. `logging` is like a professional reporting system with labels — "this is urgent (ERROR)", "this is routine (INFO)", "this is for debugging (DEBUG)".

---

### Log Levels (in order of severity)

```
DEBUG    → detailed diagnostic info (lowest priority)
INFO     → general operation messages ("user logged in")
WARNING  → something unexpected but not critical (default threshold)
ERROR    → a serious problem; function failed
CRITICAL → very serious; program may not continue (highest priority)
```

```python
import logging

logging.debug("Debug message")       # not shown by default
logging.info("Info message")         # not shown by default
logging.warning("Warning message")   # shown (default level)
logging.error("Error message")       # shown
logging.critical("Critical message") # shown

# Output:
# WARNING:root:Warning message
# ERROR:root:Error message
# CRITICAL:root:Critical message
```

---

### Configuring `basicConfig`

```python
import logging

logging.basicConfig(
    level=logging.DEBUG,               # show all levels
    format="%(asctime)s - %(levelname)s - %(message)s",  # format
    datefmt="%Y-%m-%d %H:%M:%S"
)

logging.debug("This is a debug message")
logging.info("Application started")
logging.warning("Low disk space")
logging.error("Failed to connect to database")
logging.critical("System is down!")

# Output:
# 2024-01-15 10:30:00 - DEBUG - This is a debug message
# 2024-01-15 10:30:00 - INFO - Application started
# 2024-01-15 10:30:00 - WARNING - Low disk space
# 2024-01-15 10:30:00 - ERROR - Failed to connect to database
# 2024-01-15 10:30:00 - CRITICAL - System is down!
```

### Format variables:
| Variable | Description |
|----------|-------------|
| `%(asctime)s` | Timestamp |
| `%(levelname)s` | Level name (DEBUG, INFO, etc.) |
| `%(message)s` | The log message |
| `%(name)s` | Logger name |
| `%(filename)s` | Source file |
| `%(lineno)d` | Line number |

---

### Log to a File

```python
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("app.log"),   # write to file
        logging.StreamHandler()           # also print to console
    ]
)

logging.info("Application started")
logging.error("Something went wrong!")
```

---

### Named Loggers (Best Practice)

Use a named logger instead of the root logger — makes it easier to control per-module:

```python
import logging

# Create a logger with a name
logger = logging.getLogger("my_app")
logger.setLevel(logging.DEBUG)

# Create handlers
file_handler = logging.FileHandler("app.log")
console_handler = logging.StreamHandler()

# Set format
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add handlers to logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# Use the logger
logger.info("Starting application")
logger.debug("Loaded config: debug mode")
logger.error("Failed to read file")
```

---

## Part 2: The `datetime` Module

### Getting Current Date and Time

```python
from datetime import datetime, date, time, timedelta

# Current date and time
now = datetime.now()
print(now)           # 2024-01-15 10:30:45.123456
print(type(now))     # <class 'datetime.datetime'>

# Current date only
today = date.today()
print(today)         # 2024-01-15

# Create specific datetime
dt = datetime(2024, 6, 15, 14, 30, 0)   # year, month, day, hour, min, sec
print(dt)   # 2024-06-15 14:30:00
```

---

### Accessing Date Components

```python
from datetime import datetime

now = datetime.now()

print(now.year)         # 2024
print(now.month)        # 1
print(now.day)          # 15
print(now.hour)         # 10
print(now.minute)       # 30
print(now.second)       # 45
print(now.weekday())    # 0=Monday, 6=Sunday
```

---

### `strftime` — Format Datetime as String

"string format time" — converts datetime to a custom string:

```python
from datetime import datetime

now = datetime.now()

print(now.strftime("%Y-%m-%d"))           # 2024-01-15
print(now.strftime("%d/%m/%Y"))           # 15/01/2024
print(now.strftime("%B %d, %Y"))          # January 15, 2024
print(now.strftime("%H:%M:%S"))           # 10:30:45
print(now.strftime("%I:%M %p"))           # 10:30 AM
print(now.strftime("%A, %B %d, %Y"))      # Monday, January 15, 2024
```

### Common format codes:
| Code | Meaning | Example |
|------|---------|---------|
| `%Y` | 4-digit year | 2024 |
| `%m` | Month (01–12) | 01 |
| `%d` | Day (01–31) | 15 |
| `%H` | Hour 24h (00–23) | 14 |
| `%I` | Hour 12h (01–12) | 02 |
| `%M` | Minute (00–59) | 30 |
| `%S` | Second (00–59) | 45 |
| `%p` | AM/PM | PM |
| `%A` | Full weekday | Monday |
| `%B` | Full month name | January |
| `%a` | Abbreviated weekday | Mon |
| `%b` | Abbreviated month | Jan |

---

### `strptime` — Parse String to Datetime

"string parse time" — converts a string to datetime:

```python
from datetime import datetime

date_string = "2024-01-15"
dt = datetime.strptime(date_string, "%Y-%m-%d")
print(dt)         # 2024-01-15 00:00:00
print(type(dt))   # <class 'datetime.datetime'>

# Parse different formats
dt2 = datetime.strptime("January 15, 2024", "%B %d, %Y")
dt3 = datetime.strptime("15/01/2024 14:30", "%d/%m/%Y %H:%M")
```

---

### `timedelta` — Date Arithmetic

```python
from datetime import datetime, timedelta

now = datetime.now()

# Add/subtract time
tomorrow = now + timedelta(days=1)
yesterday = now - timedelta(days=1)
next_week = now + timedelta(weeks=1)
two_hours_later = now + timedelta(hours=2)

# Calculate difference between dates
start = datetime(2024, 1, 1)
end = datetime(2024, 12, 31)
diff = end - start
print(diff.days)   # 365

# Days until an event
event = datetime(2025, 7, 4)
today = datetime.now()
days_left = (event - today).days
print(f"{days_left} days until July 4th")
```

---

### `date` and `time` Objects

```python
from datetime import date, time

# Date only
d = date(2024, 6, 15)
print(d)           # 2024-06-15
print(d.year)      # 2024
print(d.isoformat())  # 2024-06-15 (ISO 8601 string)

# Time only
t = time(14, 30, 0)   # hour, minute, second
print(t)           # 14:30:00
print(t.hour)      # 14

# Combine date and time
from datetime import datetime
dt = datetime.combine(d, t)
print(dt)   # 2024-06-15 14:30:00
```

---

## Key Takeaways

**Logging:**
- Use `logging` instead of `print()` for production code
- Levels: `DEBUG < INFO < WARNING < ERROR < CRITICAL`
- `logging.basicConfig(level=..., format=..., handlers=[...])` to configure
- Use `logging.getLogger("name")` for module-specific loggers
- Log to files with `FileHandler`; console with `StreamHandler`

**Datetime:**
- `datetime.now()` — current date and time
- `date.today()` — current date only
- `strftime(format)` — datetime → string (format for display)
- `strptime(string, format)` — string → datetime (parse user input / files)
- `timedelta(days=n)` — add/subtract from dates
- Common codes: `%Y` year, `%m` month, `%d` day, `%H:%M:%S` time
