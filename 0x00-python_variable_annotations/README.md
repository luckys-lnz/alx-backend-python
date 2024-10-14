# Type Annotations in Python 3

## Introduction

Python is a dynamically typed language, which means variables don’t have a predefined type. However, starting from Python 3.5, Type Annotations were introduced to provide an optional way to specify types for variables and functions. This helps improve code readability and allows for better type-checking.

In this guide, we will cover how to use type annotations, discuss the concept of Duck Typing, and explain how to validate your Python code using Mypy.

## Why Use Type Annotations?

Type annotations offer several advantages:

-Code Readability: It becomes easier to understand what types a function expects and what it returns.

- Error Prevention: Static type checkers can catch type-related errors early during development.
- IDE Support: Improved autocompletion and inline error detection in modern IDEs.
- Documentation: Acts as in-code documentation, making it easier to maintain.

## Basic Type Annotations

### Variable Type Annotations

You can specify the type of a variable using the colon : followed by the type.

```
age: int = 25
name: str = "John"
height: float = 5.9
```

In the above example:

- age is an integer.
- name is a string.
- height is a float.

## Function Signatures

For functions, type annotations are used to define the expected types of parameters and the return type.

```
def greet(name: str) -> str:
    return f"Hello, {name}!"
```

Here:

- The parameter name is expected to be a string (str).
- The function returns a string (str).

You can also annotate multiple parameters:

```
def add(x: int, y: int) -> int:
    return x + y
```

## Complex Types

Python also supports type annotations for more complex data structures like lists, dictionaries, tuples, and optional values.

### Lists and Dictionaries:

```
from typing import List, Dict

names: List[str] = ["Alice", "Bob", "Charlie"]
ages: Dict[str, int] = {"Alice": 30, "Bob": 25}
```

### Tuples:

```
from typing import Tuple

coordinates: Tuple[int, int] = (10, 20)
```

### Optional Types:

Sometimes, a value can either be of a specific type or None. You can use Optional to indicate this.

```
from typing import Optional

def get_user(id: int) -> Optional[str]:
    if id == 1:
        return "Alice"
    return None
```

# Duck Typing in Python

## What is Duck Typing?

**Duck Typing** is a concept in dynamic languages like Python that relies on the idea of "if it walks like a duck and quacks like a duck, it must be a duck." It means that an object’s suitability is determined by the presence of certain methods and properties, rather than the object's actual type.

### How it Works in Python

In Python, **duck typing** allows you to use any object in a function as long as it has the required methods or attributes, without needing to explicitly check its type.

```
class Duck:
    def quack(self):
        return "Quack!"

class Dog:
    def quack(self):
        return "Woof!"

def make_it_quack(thing):
    print(thing.quack())

duck = Duck()
dog = Dog()

make_it_quack(duck)  # Output: Quack!
make_it_quack(dog)   # Output: Woof!
```

Even though **Duck** and **Dog** are different types, the **make_it_quack** function works for both because they both have a **quack()** method.

# Validating Code with Mypy

## Installing Mypy

**Mypy** is a static type checker for Python that checks type annotations and ensures your code adheres to them.

To install Mypy:
```
pip install mypy
```

## Checking Type Annotations with Mypy
Once installed, you can run Mypy on your Python files to check for type-related issues.

```
mypy script.py
```

**NB:** If the script contains type errors, Mypy will report them. For example:

```
def add(a: int, b: int) -> int:
    return a + b

result = add(2, "three")  # Error: Incompatible types

```

Running **Mypy** on this code will produce an error because the function **add** expects both **a** and **b** to be integers, but **"three"** is a string.

### Handling Errors and Issues
If **Mypy** detects type issues, it will point to the lines where type mismatches or violations occur. For example:
```
script.py:4: error: Argument 2 to "add" has incompatible type "str"; expected "int"
```

You can fix the issues by ensuring the arguments passed to the function conform to the expected types.

For large projects, you may not want to enforce strict type checking on every line. In such cases, you can use **# type: ignore** to skip certain lines from Mypy’s checking:

```
result = add(2, "three")  # type: ignore
```


# In Summary

Type annotations in Python 3 allow you to add static typing to a dynamically typed language, enhancing code clarity, safety, and IDE support. With tools like Mypy, you can validate these type annotations and catch type-related issues early in the development process. Despite the advantages of static typing, Python's flexibility in dynamic typing, including features like Duck Typing, remains intact.

# Learn More:-
- [PEP 484](https://peps.python.org/pep-0484/)
- [mypy documentation](https://mypy.readthedocs.io/en/stable/)
