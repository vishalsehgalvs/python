# Python Advanced OOP — Abstract Classes, Operator Overloading

> Source: https://unwiredlearning.com/blog/python

---

## Abstract Classes

An **abstract class** is a class that **cannot be instantiated** — it's a template that child classes must complete.

> 🔁 **Analogy:** An abstract class is like a job description that says "must be able to drive a vehicle." It doesn't matter if it's a car, truck, or bus — but you _must_ implement driving. You can't hire the job description itself; you hire someone who fills it.

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass    # child MUST implement this

    @abstractmethod
    def perimeter(self):
        pass

    def describe(self):   # can have concrete methods too
        print(f"Area: {self.area()}, Perimeter: {self.perimeter()}")

# shape = Shape()   # ❌ TypeError: Can't instantiate abstract class

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14159 * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

c = Circle(5)
c.describe()         # Area: 78.53975, Perimeter: 31.4159

r = Rectangle(4, 6)
r.describe()         # Area: 24, Perimeter: 20
```

---

## Operator Overloading

You can define what operators (`+`, `-`, `*`, `==`, `<`, etc.) do for your custom objects using **dunder (magic) methods**.

> 🔁 **Analogy:** Operator overloading is like teaching a calculator new rules. By default, `+` adds numbers. But for a `Vector` object, you can define `+` to mean "add corresponding components."

### Common dunder methods:

| Operator            | Method                     |
| ------------------- | -------------------------- |
| `+`                 | `__add__(self, other)`     |
| `-`                 | `__sub__(self, other)`     |
| `*`                 | `__mul__(self, other)`     |
| `/`                 | `__truediv__(self, other)` |
| `==`                | `__eq__(self, other)`      |
| `!=`                | `__ne__(self, other)`      |
| `<`                 | `__lt__(self, other)`      |
| `>`                 | `__gt__(self, other)`      |
| `<=`                | `__le__(self, other)`      |
| `>=`                | `__ge__(self, other)`      |
| `len()`             | `__len__(self)`            |
| `str()` / `print()` | `__str__(self)`            |
| `repr()`            | `__repr__(self)`           |
| `[]`                | `__getitem__(self, key)`   |

### Vector example:

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    def __repr__(self):
        return f"Vector({self.x!r}, {self.y!r})"

    def __len__(self):
        return 2   # always 2D

v1 = Vector(1, 2)
v2 = Vector(3, 4)

print(v1 + v2)    # Vector(4, 6)
print(v1 - v2)    # Vector(-2, -2)
print(v1 * 3)     # Vector(3, 6)
print(v1 == Vector(1, 2))   # True
print(len(v1))    # 2
```

### Book example:

```python
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __str__(self):
        return f'"{self.title}" ({self.pages} pages)'

    def __repr__(self):
        return f"Book('{self.title}', {self.pages})"

    def __lt__(self, other):
        return self.pages < other.pages

    def __add__(self, other):
        # Combine two books into a "collection"
        combined_pages = self.pages + other.pages
        combined_title = f"{self.title} + {other.title}"
        return Book(combined_title, combined_pages)

b1 = Book("Python Basics", 250)
b2 = Book("Advanced Python", 400)

print(b1)           # "Python Basics" (250 pages)
print(b1 < b2)      # True (250 < 400)

books = [b2, b1, Book("Regex Guide", 100)]
books.sort()        # uses __lt__ to sort by pages
for b in books:
    print(b)
# "Regex Guide" (100 pages)
# "Python Basics" (250 pages)
# "Advanced Python" (400 pages)
```

---

## `__str__` vs `__repr__`

```python
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    def __str__(self):
        # Human-readable (for print())
        return f"{self.celsius}°C"

    def __repr__(self):
        # Developer-readable (for debugging)
        return f"Temperature({self.celsius})"

t = Temperature(25)
print(t)          # 25°C               (uses __str__)
print(repr(t))    # Temperature(25)    (uses __repr__)

# In a list, __repr__ is used
temps = [Temperature(25), Temperature(100)]
print(temps)      # [Temperature(25), Temperature(100)]
```

---

## Static Methods and Class Methods

```python
class MathHelper:
    # Class attribute
    pi = 3.14159

    @staticmethod
    def add(a, b):
        """No self or cls — just a utility function."""
        return a + b

    @classmethod
    def circle_area(cls, radius):
        """cls refers to the class itself (not instance)."""
        return cls.pi * radius ** 2

print(MathHelper.add(3, 5))          # 8
print(MathHelper.circle_area(4))     # 50.26544

# Static methods don't need an instance
m = MathHelper()
print(m.add(1, 2))   # 3 (can also call on instance, but unusual)
```

|                           | `@staticmethod`   | `@classmethod`                    | Regular method    |
| ------------------------- | ----------------- | --------------------------------- | ----------------- |
| First arg                 | None              | `cls` (class)                     | `self` (instance) |
| Can access class attrs    | ❌                | ✅                                | ✅                |
| Can access instance attrs | ❌                | ❌                                | ✅                |
| Use case                  | Utility functions | Factory methods, alt constructors | Instance behavior |

---

## Polymorphism

Same method name, different behavior depending on the class:

```python
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class Duck(Animal):
    def speak(self):
        return "Quack!"

animals = [Dog(), Cat(), Duck(), Dog()]

# Same method, different output per class
for animal in animals:
    print(animal.speak())
# Woof!
# Meow!
# Quack!
# Woof!
```

---

## Key Takeaways

- `ABC` + `@abstractmethod` — define abstract classes; force child classes to implement certain methods
- Operator overloading: define `__add__`, `__eq__`, `__lt__`, etc. to make operators work with custom classes
- `__str__` = human-readable output for `print()`; `__repr__` = developer-readable for debugging
- `@staticmethod` — utility function in a class namespace; no `self` or `cls`
- `@classmethod` — receives the class itself as `cls`; useful for alternative constructors
- Polymorphism: different classes implement the same method name differently — enables flexible, interchangeable code
