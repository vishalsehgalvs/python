# Python Inheritance, super(), Multiple Inheritance

> Source: https://unwiredlearning.com/blog/python

---

## Inheritance

Inheritance lets a **child class** reuse and extend the behavior of a **parent class**.

> 🔁 **Analogy:** A `Dog` IS-A `Animal`. It inherits all animal traits (eat, breathe), and adds its own (`bark`). You don't rewrite `eat()` for every animal.

```
      ┌─────────────────┐
      │     Animal      │  ← Parent (base) class
      │  + name, age    │
      │  + speak()      │
      └─────────────────┘
              ▲
     ┌────────┴────────┐
     │                 │
┌────┴────┐       ┌────┴────┐
│   Dog   │       │   Cat   │  ← Child (derived) classes
│ +bark() │       │ +meow() │
└─────────┘       └─────────┘
```

```python
# Parent class
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print("The animal makes a sound")

# Child class inherits from Animal
class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)   # call parent's __init__
        self.breed = breed

    def speak(self):           # override parent method
        print("The dog barks")

class Cat(Animal):
    def speak(self):           # override
        print("The cat meows")

# Usage
dog = Dog("Buddy", 3, "Golden Retriever")
print(dog.name, dog.age, dog.breed)   # Buddy 3 Golden Retriever
dog.speak()   # The dog barks

cat = Cat("Whiskers", 2)
cat.speak()   # The cat meows

animal = Animal("Generic", 5)
animal.speak()   # The animal makes a sound
```

---

## `super()` — Call the Parent Class

`super()` returns a temporary reference to the parent class, letting you call its methods:

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Employee(Person):
    def __init__(self, name, age, company):
        super().__init__(name, age)    # ← call Person's __init__
        self.company = company

    def display_info(self):
        super().display_info()          # ← call Person's display_info
        print(f"Company: {self.company}")

emp = Employee("John", 30, "Acme Corp")
emp.display_info()
# Name: John, Age: 30
# Company: Acme Corp
```

---

## `isinstance()` and `issubclass()`

```python
dog = Dog("Buddy", 3, "Labrador")

print(isinstance(dog, Dog))     # True — dog is a Dog
print(isinstance(dog, Animal))  # True — dog IS-A Animal (inheritance)
print(isinstance(dog, Cat))     # False

print(issubclass(Dog, Animal))  # True — Dog is a subclass of Animal
print(issubclass(Cat, Dog))     # False
```

---

## Method Resolution Order (MRO)

Python looks for methods in this order: `current class → parent → grandparent → ...`

```python
print(Dog.__mro__)
# (<class 'Dog'>, <class 'Animal'>, <class 'object'>)
# All Python classes implicitly inherit from 'object'
```

---

## Multiple Inheritance

A class can inherit from **more than one** parent:

```python
class Swimmer:
    def swim(self):
        print("The animal swims")

class Walker:
    def walk(self):
        print("The animal walks")

class Flyer:
    def fly(self):
        print("The animal flies")

# Dolphin inherits from Swimmer and Walker
class Dolphin(Swimmer, Walker):
    pass

# Duck inherits from all three
class Duck(Swimmer, Walker, Flyer):
    pass

dolphin = Dolphin()
dolphin.swim()   # The animal swims
dolphin.walk()   # The animal walks

duck = Duck()
duck.swim()      # The animal swims
duck.walk()      # The animal walks
duck.fly()       # The animal flies
```

### The Diamond Problem

```
          Animal
         /      \
      Dog        Cat
         \      /
           Mutt
```

Python resolves this with the **C3 linearization (MRO) algorithm**:

```python
class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    def speak(self):
        print("Woof")

class Cat(Animal):
    def speak(self):
        print("Meow")

class Mutt(Dog, Cat):   # inherits from both Dog and Cat
    pass

mutt = Mutt()
mutt.speak()   # "Woof" — Python uses MRO: Mutt → Dog → Cat → Animal
print(Mutt.__mro__)   # (Mutt, Dog, Cat, Animal, object)
```

---

## Composition vs Inheritance

Inheritance = "IS-A" relationship → `Dog IS-A Animal`  
Composition = "HAS-A" relationship → `Car HAS-A Engine`

```python
# Composition example
class Engine:
    def __init__(self, type):
        self.type = type

    def start(self):
        print(f"The {self.type} engine starts.")

class Car:
    def __init__(self, make, model, engine_type):
        self.make = make
        self.model = model
        self.engine = Engine(engine_type)   # Car HAS-A Engine

    def start_engine(self):
        self.engine.start()    # delegate to Engine

    def display_info(self):
        print(f"{self.make} {self.model}, Engine: {self.engine.type}")

my_car = Car("Toyota", "Corolla", "gasoline")
my_car.start_engine()   # The gasoline engine starts.
my_car.display_info()   # Toyota Corolla, Engine: gasoline
```

### Aggregation — HAS-A with independent lifetime:

```python
class Battery:
    def __init__(self, capacity):
        self.capacity = capacity

class Smartphone:
    def __init__(self, brand, battery):
        self.brand = brand
        self.battery = battery    # Battery is passed in (not created inside)

# Battery can exist without Smartphone
my_battery = Battery(4000)
my_phone = Smartphone("Samsung", my_battery)

# Both can be used independently
print(my_battery.capacity)       # 4000
print(my_phone.battery.capacity) # 4000
```

---

## Key Takeaways

- `class Child(Parent):` — inherit everything from Parent
- `super().__init__(...)` — call parent constructor from child; always call it before setting child's own attributes
- Child can **override** parent methods by defining same method name
- `isinstance(obj, ClassName)` checks if an object is an instance of a class (including parent classes)
- Multiple inheritance: `class C(A, B):` — Python uses MRO to decide method lookup order
- Composition ("HAS-A") is often better than deep inheritance trees — easier to maintain
- Aggregation = composition where contained object can exist independently
