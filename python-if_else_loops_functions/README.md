# Python - If/Else, Loops, Functions

## Table of Contents
- [Introduction](#introduction)
- [Learning Objectives](#learning-objectives)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Concepts Covered](#concepts-covered)
- [Examples](#examples)
- [Resources](#resources)

## Introduction
This project focuses on the essential Python concepts of control flow using `if/else` statements, loops, and functions. These are fundamental building blocks in programming, allowing you to create dynamic programs that can make decisions, repeat actions, and modularize your code into reusable functions.

Through this project, you will learn how to:
- Make decisions in code using `if/else` statements.
- Perform repetitive tasks using loops (`for` and `while`).
- Create and use functions to encapsulate logic.

## Learning Objectives
By the end of this project, you should be able to:
- Understand and apply conditional statements (`if`, `else if`, `else`).
- Use `for` and `while` loops for iteration.
- Define and call Python functions, and understand the importance of functions in structuring programs.
- Use built-in functions and create custom ones.
- Understand the basics of return values and function arguments.

## Project Structure
The project consists of several Python scripts, each tackling specific tasks related to `if/else`, loops, and functions. Below is the structure of the project:

```
.
├── 0-positive_or_negative.py
├── 1-loop.py
├── 2-functions.py
├── 3-advanced_conditions.py
└── README.md
```

- **`0-positive_or_negative.py`**: Determines if a random number is positive, negative, or zero.
- **`1-loop.py`**: Demonstrates basic looping constructs.
- **`2-functions.py`**: Includes examples of user-defined functions.
- **`3-advanced_conditions.py`**: Explores more advanced condition handling.

## Usage
To run the programs, simply execute the Python files in your terminal. For example, to run the script that determines if a number is positive or negative:

```bash
$ python3 0-positive_or_negative.py
```

Each script is self-contained and can be run independently.

## Concepts Covered

### 1. **If/Else Statements**
Conditional statements allow you to execute different pieces of code based on specific conditions.

```python
if condition:
    # code block if condition is True
elif another_condition:
    # code block if another condition is True
else:
    # code block if none of the above conditions are True
```

### 2. **Loops**
Loops are used to repeat a block of code multiple times.

- **`for` loops**: Used to iterate over a sequence (like lists, tuples, or strings).

    ```python
    for i in range(5):
        print(i)
    ```

- **`while` loops**: Repeats as long as a condition is true.

    ```python
    while condition:
        # code block
    ```

### 3. **Functions**
Functions allow you to encapsulate code into reusable blocks.

```python
def function_name(parameters):
    # code block
    return result
```

Functions can take arguments, return values, and help keep your code organized.

## Examples
Here are some examples of code you might encounter in this project:

- **Positive or Negative Number Example**:
    ```python
    import random
    number = random.randint(-10, 10)

    if number > 0:
        print(f"{number} is positive")
    elif number == 0:
        print(f"{number} is zero")
    else:
        print(f"{number} is negative")
    ```

- **Looping Example**:
    ```python
    for i in range(1, 11):
        print(i)
    ```

- **Simple Function Example**:
    ```python
    def greet(name):
        return f"Hello, {name}!"

    print(greet("Alice"))
    ```

## Resources
To learn more about Python and the concepts covered in this project, you can refer to the following resources:
- [Python Official Documentation](https://docs.python.org/3/)
- [Python Loops](https://docs.python.org/3/tutorial/controlflow.html#for-statements)
- [Python Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
- [Python If/Else Statements](https://docs.python.org/3/tutorial/controlflow.html#if-statements)

---

This **README** provides a clear overview of the project and what it covers, making it easy for someone new to the project to understand its purpose and how to get started.
