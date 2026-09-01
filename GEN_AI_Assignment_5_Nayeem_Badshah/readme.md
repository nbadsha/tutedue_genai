# GEN_AI_Assignment_5_Nayeem_Badshah

This project is a Python practice assignment focused on modular programming, utility functions, and basic retail calculations. It demonstrates how to organize code into separate modules and import them into a main script for execution.

## Project Overview

The assignment contains a set of reusable functions for:

- basic arithmetic operations
- string processing
- discount and billing logic for a simple shop application

## Folder Structure

- `main.py` - Runs test cases for all utility modules.
- `math_utils.py` - Contains arithmetic helper functions.
- `string_utils.py` - Contains string manipulation functions.
- `shop_package/__init__.py` - Package initialization file.
- `shop_package/discount.py` - Includes discount-related calculations.
- `shop_package/billing.py` - Includes total and tax calculations.

## Included Functions

### Math Utilities
- `add(a, b)` - Adds two numbers.
- `subtract(a, b)` - Subtracts the second number from the first.
- `square(a)` - Returns the square of a number.

### String Utilities
- `capitalize_words(input_string)` - Capitalizes the first letter of each word.
- `reverse_string(input_string)` - Reverses the input string.
- `word_count(input_string)` - Counts the number of words in a string.

### Shop Package: Discounts
- `apply_discount(price, discount_percentage)` - Applies percentage-based discount.
- `flat_discount(price, discount_amount)` - Applies a fixed discount amount.

### Shop Package: Billing
- `calculate_total(prices)` - Sums all item prices and returns `None` if invalid values are passed.
- `apply_tax(amount, tax_rate=0.05)` - Adds tax to a given amount.

## How to Run

Open a terminal in the project directory and run:

```bash
python main.py
```

This will print sample outputs demonstrating the behavior of each function.

## Example Output

```python
5 + 3 = 8
5 - 3 = 2
5^2 = 25
Capitalized: Hello World
Reversed: olleh
Word count: 2
Original price: 100, Discounted price: 80.0
Original price: 100, Flat discounted price: 85
Total: 60
Total with tax: 63.0
```

## Purpose

This assignment helps practice:

- Python function creation
- modular code organization
- importing modules across packages
- simple business logic implementation
- basic debugging and error handling

