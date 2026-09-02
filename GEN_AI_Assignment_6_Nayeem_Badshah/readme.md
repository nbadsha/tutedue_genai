# GEN_AI_Assignment_6_Nayeem_Badshah

This assignment focuses on Python exception handling and input validation. It includes multiple mini-programs that demonstrate how to handle invalid user input, division errors, file access issues, age validation, and shopping cart calculations using `try`, `except`, `raise`, and `finally`.

## Project Overview

The project contains several Python scripts, each solving a different exception-handling task:

- `main.py` - Division function with error handling
- `task_2.py` - Bill calculator that ignores invalid prices and continues processing
- `task_3.py` - Age validation using a custom exception
- `task_4.py` - File reader that handles missing and permission errors
- `task_5.py` - Shopping cart program that validates entered prices

## Task 1: Division with Error Handling

The `divide(numerator, denominator)` function:

- returns the result of division for valid values
- raises `ValueError("Cannot divide by zero.")` if the denominator is zero
- raises `ValueError("Numerator and denominator must be numbers.")` for invalid types
- uses a `finally` block to print `Operation Complete`

## Task 2: Bill Calculator with Error Handling

The bill calculator:

- iterates through a list of prices
- checks whether each value is numeric
- skips non-numeric values with a message
- raises a `ValueError` for negative prices
- prints the running total as it processes valid values

## Task 3: Age Validator

The `check_age(age)` function:

- raises `ValueError("Age must be between 1 and 120")` when the age is out of range
- is used in a main program that reads user input and catches the exception

## Task 4: File Reader with Exception Handling

The file reader program:

- asks the user for a filename
- tries to open and read the file
- catches `FileNotFoundError` and `PermissionError`
- prints the first 3 lines of the file if it opens successfully
- uses `finally` to print `File operation attempted.`

## Task 5: Safe Shopping Cart

The shopping cart program:

- starts with an empty list: `cart = []`
- keeps asking the user for prices until they enter `q`
- converts each entry to a float
- handles `ValueError` for invalid input
- raises a custom error for negative prices
- prints:
  - total number of items
  - total bill

## How to Run

Open the project folder in a terminal and run any task file individually, for example:

```bash
python task_1.py
python task_2.py
python task_3.py
python task_4.py
python task_5.py
```

## Learning Objective

This assignment helps practice:

- `try` / `except` / `finally` blocks
- custom exception handling
- file input/output error handling
- input validation
- safe program design in real-world scenarios
