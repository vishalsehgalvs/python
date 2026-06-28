# Python Regular Expressions (Regex)

> Source: https://unwiredlearning.com/blog/python

---

## What Are Regular Expressions?

A **regular expression** (regex) is a pattern used to search, match, and manipulate text.

> 🔁 **Analogy:** Regex is like a search filter. Just like `*.jpg` in a file explorer finds all JPEG files, a regex pattern finds text matching a specific structure — like "any email address" or "any phone number that starts with 555."

Python uses the built-in `re` module.

---

## Getting Started

```python
import re

text = "Hello, my phone number is 555-1234!"

# Search for pattern
match = re.search(r"\d{3}-\d{4}", text)   # find 3 digits - 4 digits
if match:
    print(match.group())   # 555-1234
```

---

## Common `re` Functions

| Function | Description |
|----------|-------------|
| `re.search(pattern, string)` | Finds **first** match anywhere in string; returns Match or None |
| `re.match(pattern, string)` | Matches only at the **beginning** of string |
| `re.findall(pattern, string)` | Returns **list of all** matches |
| `re.finditer(pattern, string)` | Returns **iterator** of Match objects for all matches |
| `re.sub(pattern, replace, string)` | **Replaces** all matches with replace string |
| `re.split(pattern, string)` | **Splits** string at each match |
| `re.fullmatch(pattern, string)` | Matches the **entire** string |

---

## Pattern Syntax

### Character basics:
| Pattern | Matches |
|---------|---------|
| `abc` | literal "abc" |
| `.` | any character except newline |
| `\d` | any digit `[0-9]` |
| `\D` | any non-digit |
| `\w` | word character `[a-zA-Z0-9_]` |
| `\W` | non-word character |
| `\s` | whitespace (space, tab, newline) |
| `\S` | non-whitespace |

### Anchors:
| Pattern | Matches |
|---------|---------|
| `^` | start of string |
| `$` | end of string |
| `\b` | word boundary |

### Quantifiers:
| Pattern | Means |
|---------|-------|
| `*` | 0 or more |
| `+` | 1 or more |
| `?` | 0 or 1 (optional) |
| `{n}` | exactly n times |
| `{n,m}` | between n and m times |
| `{n,}` | n or more times |

### Character classes:
| Pattern | Matches |
|---------|---------|
| `[abc]` | a, b, or c |
| `[a-z]` | any lowercase letter |
| `[A-Z]` | any uppercase letter |
| `[0-9]` | any digit |
| `[^abc]` | anything except a, b, c |

### Groups and alternation:
| Pattern | Means |
|---------|-------|
| `(abc)` | group — capture "abc" |
| `a\|b` | a or b |
| `(?:abc)` | non-capturing group |

---

## Examples

### Find email address:
```python
import re

text = "Contact us at support@example.com or sales@company.org"

# Simple email pattern
emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
print(emails)   # ['support@example.com', 'sales@company.org']
```

### Validate phone number:
```python
def is_valid_phone(phone):
    pattern = r"^\d{3}-\d{3}-\d{4}$"   # 123-456-7890
    return bool(re.fullmatch(pattern, phone))

print(is_valid_phone("123-456-7890"))   # True
print(is_valid_phone("1234567890"))     # False
print(is_valid_phone("123-45-6789"))    # False
```

### Find all numbers:
```python
text = "I have 3 cats, 2 dogs, and 10 fish."
numbers = re.findall(r"\d+", text)
print(numbers)   # ['3', '2', '10']
```

### Replace pattern:
```python
text = "My SSN is 123-45-6789 and my old SSN was 987-65-4321"

# Censor SSN numbers
censored = re.sub(r"\d{3}-\d{2}-\d{4}", "XXX-XX-XXXX", text)
print(censored)
# My SSN is XXX-XX-XXXX and my old SSN was XXX-XX-XXXX
```

### Split on multiple delimiters:
```python
text = "apple, banana; cherry: date"
fruits = re.split(r"[,;:]\s*", text)
print(fruits)   # ['apple', 'banana', 'cherry', 'date']
```

---

## Using Groups

Groups capture specific parts of a match:

```python
text = "John Smith: 555-1234, Jane Doe: 555-5678"

# Use groups to capture name and phone separately
pattern = r"(\w+ \w+): (\d{3}-\d{4})"
matches = re.finditer(pattern, text)

for match in matches:
    name = match.group(1)    # first group
    phone = match.group(2)   # second group
    print(f"Name: {name}, Phone: {phone}")

# Name: John Smith, Phone: 555-1234
# Name: Jane Doe, Phone: 555-5678
```

### Named groups:
```python
pattern = r"(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})"
match = re.search(pattern, "Date: 2024-01-15")

if match:
    print(match.group("year"))   # 2024
    print(match.group("month"))  # 01
    print(match.group("day"))    # 15
```

---

## Flags

```python
text = "Hello WORLD hello world"

# Case-insensitive
matches = re.findall(r"hello", text, re.IGNORECASE)
print(matches)   # ['Hello', 'hello']

# Multiline (^ and $ match each line)
text = "first line\nsecond line\nthird line"
matches = re.findall(r"^\w+", text, re.MULTILINE)
print(matches)   # ['first', 'second', 'third']
```

---

## Compiled Patterns (for Reuse)

If you use a pattern many times, compile it for better performance:

```python
import re

# Compile once
email_pattern = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")

# Use many times
texts = ["alice@example.com", "not-an-email", "bob@test.org"]
for text in texts:
    if email_pattern.search(text):
        print(f"Found email: {text}")
```

---

## Key Takeaways

- `import re` — Python's built-in regex module
- `re.search()` finds first match; `re.findall()` returns all matches as a list
- `re.sub()` replaces matches; `re.split()` splits on pattern
- `\d` = digit, `\w` = word char, `\s` = whitespace; capital versions = opposite
- `^` = start, `$` = end, `\b` = word boundary
- Quantifiers: `*` (0+), `+` (1+), `?` (0 or 1), `{n}` (exactly n), `{n,m}` (n to m)
- Use `r"..."` (raw strings) for patterns to avoid double-escaping backslashes
- Groups `(...)` capture parts of the match; access with `.group(1)`, `.group(2)`, etc.
- `re.compile(pattern)` for reusing patterns in performance-sensitive code
