# Python Classes and Objects (OOP)

> Source: https://unwiredlearning.com/blog/python

---

## What Is OOP?

**Object-Oriented Programming** organizes code around **objects** — things that have data (attributes) and behavior (methods).

> 🔁 **Analogy:** A class is a blueprint. A dog blueprint says "dogs have a name, breed, and can bark." An object is an actual dog built from that blueprint — "Buddy, Golden Retriever."

The four pillars:
- **Encapsulation** — bundle data + methods; hide internals
- **Inheritance** — new class inherits from existing class
- **Polymorphism** — same method name, different behavior per class
- **Abstraction** — hide complexity, show simple interface

---

## Defining a Class

```python
class Dog:
    def __init__(self, name, breed):   # constructor
        self.name = name               # instance attribute
        self.breed = breed

    def bark(self):
        print("Woof! Woof!")

    def describe(self):
        print(f"{self.name} is a {self.breed}")
```

---

## Creating Objects (Instances)

```python
# Create objects from the class
dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Max", "German Shepherd")

# Access attributes with dot notation
print(dog1.name)    # Buddy
print(dog2.breed)   # German Shepherd

# Call methods
dog1.bark()        # Woof! Woof!
dog2.describe()    # Max is a German Shepherd
```

---

## `__init__()` and `self`

### `__init__()` — the constructor

`__init__` runs **automatically** when a new object is created. It sets up initial state.

```python
class Person:
    def __init__(self, name, age):
        self.name = name    # sets instance attribute
        self.age = age

p = Person("Alice", 30)   # __init__ called automatically
print(p.name)   # Alice
```

### `self` — reference to the current object

`self` is the first parameter in every instance method. It refers to the object calling the method.

```python
class Dog:
    def __init__(self, name, breed):
        self.name = name       # self.name = THIS dog's name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says Woof!")   # uses THIS dog's name

dog1 = Dog("Buddy", "Labrador")
dog2 = Dog("Rex", "German Shepherd")

dog1.bark()   # Buddy says Woof!
dog2.bark()   # Rex says Woof!
# self = dog1 in the first call, self = dog2 in the second
```

> You don't pass `self` when calling — Python does it automatically!

---

## Instance Attributes vs Class Attributes

```python
class Dog:
    # Class attribute — shared by ALL instances
    species = "Canis familiaris"

    def __init__(self, name, breed):
        # Instance attributes — unique per object
        self.name = name
        self.breed = breed

dog1 = Dog("Buddy", "Labrador")
dog2 = Dog("Max", "Poodle")

print(dog1.species)   # Canis familiaris (class attribute)
print(dog2.species)   # Canis familiaris (same for all)

print(dog1.name)   # Buddy (instance attribute — unique)
print(dog2.name)   # Max   (different for each dog)

# Change class attribute
Dog.species = "Wolf"
print(dog1.species)   # Wolf (affects all instances!)
```

---

## Multiple Constructors with `@classmethod`

Python doesn't support multiple `__init__`, but you can use class methods:

```python
class Dog:
    def __init__(self, name=None, breed=None):
        self.name = name
        self.breed = breed

    @classmethod
    def with_name(cls, name):
        return cls(name=name)          # alternative constructor

    @classmethod
    def with_breed(cls, breed):
        return cls(breed=breed)

    def __str__(self):
        return f"Dog(name={self.name}, breed={self.breed})"

# Use default constructor
dog1 = Dog()                           # Dog(name=None, breed=None)
dog2 = Dog("Buddy", "Golden Retriever") # Dog(name=Buddy, breed=Golden Retriever)
dog3 = Dog.with_name("Max")             # Dog(name=Max, breed=None)
dog4 = Dog.with_breed("Labrador")       # Dog(name=None, breed=Labrador)
print(dog3)
```

---

## Encapsulation — Public vs Private

Python doesn't enforce strict private/public, but uses naming conventions:

```python
class BankAccount:
    def __init__(self, account_number, balance=0):
        self._account_number = account_number  # _ = "private" (convention)
        self._balance = balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited ${amount}. Balance: ${self._balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"Withdrew ${amount}. Balance: ${self._balance}")
        else:
            print("Invalid or insufficient funds.")

    def get_balance(self):
        return self._balance   # controlled access (getter)

account = BankAccount("12345678")
account.deposit(100)    # Deposited $100. Balance: $100
account.withdraw(50)    # Withdrew $50. Balance: $50
print(account.get_balance())   # 50
# account._balance = 99999   # ← technically possible but discouraged!
```

### Double underscore `__` — name mangling:
```python
class Circle:
    def __init__(self, radius):
        self.__radius = radius    # __ = "very private" (name mangled)

    def area(self):
        return 3.14159 * self.__radius ** 2

c = Circle(5)
# print(c.__radius)    # ❌ AttributeError
# print(c._Circle__radius)  # works but you shouldn't!
```

---

## Getters and Setters with `@property`

The Pythonic way to control attribute access:

```python
class Employee:
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary

    @property
    def salary(self):               # getter
        return self._salary

    @salary.setter
    def salary(self, value):        # setter with validation
        if value < 0:
            raise ValueError("Salary cannot be negative")
        self._salary = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Name cannot be empty")
        self._name = value

emp = Employee("Alice", 50000)
print(emp.salary)   # 50000    (calls getter)
emp.salary = 60000  # (calls setter — validates, then sets)
# emp.salary = -100  # ❌ ValueError: Salary cannot be negative
```

---

## `__str__` and `__repr__` — String Representation

```python
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def __str__(self):
        return f"{self.name} ({self.breed})"   # for print()

    def __repr__(self):
        return f"Dog('{self.name}', '{self.breed}')"  # for debugging

d = Dog("Buddy", "Labrador")
print(d)         # Buddy (Labrador)    ← uses __str__
print(repr(d))   # Dog('Buddy', 'Labrador')  ← uses __repr__
```

---

## Key Takeaways

- `class` defines a blueprint; object = instance created from that blueprint
- `__init__(self, ...)` runs automatically when object is created — initializes attributes
- `self` refers to the current object — always first parameter of instance methods
- Class attributes are shared by all instances; instance attributes are unique per object
- `_attribute` = private by convention; `__attribute` = name-mangled (harder to access from outside)
- Use `@property` and `@attribute.setter` for controlled getters/setters
- `__str__` controls `print(obj)` output; `__repr__` controls developer-friendly repr
