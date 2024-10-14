# Python Asyncio & Async Programming Guide

## 1. Async and Await Syntax

In Python, **async** and **await** are used to write asynchronous code. The **async** keyword declares a function as a coroutine, while **await** is used to pause the execution of a coroutine and wait for the result of another coroutine or async function.

Example:

```
import asyncio

async def greet():
    print("Hello")
    await asyncio.sleep(1)  # Simulates a non-blocking delay
    print("World!")

# To run the coroutine
asyncio.run(greet())
```

Key Points:

- **async**: Used before a function definition to make it a coroutine.
- **await**: Suspends the coroutine until the awaited task is completed.


## 2. How to Execute an Async Program with asyncio

To execute an async program, Python's asyncio module provides an event loop that handles the execution of coroutines.

Example:

```
import asyncio

async def main():
    print("Starting the program...")
    await asyncio.sleep(2)
    print("Finished after 2 seconds")

# Execute the program
asyncio.run(main())
```

**Steps:**
- Define a coroutine using async def.
- Use await to pause execution inside the coroutine.
- Call asyncio.run() to execute the coroutine within an event loop.


## 3. How to Run Concurrent Coroutines

Concurrency allows multiple coroutines to be executed at the same time, without blocking each other. The asyncio.gather() function is commonly used to run multiple coroutines concurrently.

Example:

```
import asyncio

async def task1():
    print("Task 1 started")
    await asyncio.sleep(2)
    print("Task 1 completed")

async def task2():
    print("Task 2 started")
    await asyncio.sleep(1)
    print("Task 2 completed")

# Running both coroutines concurrently
async def main():
    await asyncio.gather(task1(), task2())

asyncio.run(main())
```

**Key Function:**

- **asyncio.gather():** Runs multiple coroutines concurrently and waits for all of them to complete.


## 4. How to Create asyncio Tasks

In Python, tasks are used to schedule coroutines for concurrent execution. The asyncio.create_task() function creates a new task and schedules it to run independently of other coroutines.

Example:

```
import asyncio

async def print_after(delay, message):
    await asyncio.sleep(delay)
    print(message)

async def main():
    task1 = asyncio.create_task(print_after(2, "Hello"))
    task2 = asyncio.create_task(print_after(1, "World"))

    # Wait until both tasks are completed
    await task1
    await task2

asyncio.run(main())
```

**Key Function:**
- **asyncio.create_task()**: Schedules a coroutine to run in the background and returns an asyncio.Task object that can be awaited later.


## 5. How to Use the Random Module

The random module in Python provides functions to generate random numbers or choose random elements from sequences. This can be particularly useful when simulating random delays or behaviors in asynchronous programs.

Example:

```
import random

# Generating a random float between 0 and 1
random_float = random.random()
print(f"Random float: {random_float}")

# Generating a random integer between 1 and 10
random_int = random.randint(1, 10)
print(f"Random integer: {random_int}")

# Choosing a random element from a list
choices = ['apple', 'banana', 'cherry']
random_choice = random.choice(choices)
print(f"Random choice: {random_choice}")
```

**Key Functions:**

- **random.random():** Returns a random float between 0.0 and 1.0.
- **random.randint(a, b):** Returns a random integer between a and b (inclusive).
- **random.choice(seq):** Chooses a random element from a non-empty sequence.



## In Summary

This guide covers the essentials of **async** programming in Python, including how to work with coroutines, execute asynchronous programs, run them concurrently, create tasks, and use randomness in your applications. Async programming allows for more efficient code execution, particularly in I/O-bound tasks.


## Learn More

- [Async IO in Python: A Complete Walkthrough](https://realpython.com/async-io-python/#the-asyncio-package-and-asyncawait)
- [asyncio - Asynchronous I/O](https://docs.python.org/3/library/asyncio.html)
- [random.uniform](https://docs.python.org/3/library/random.html#random.uniform)