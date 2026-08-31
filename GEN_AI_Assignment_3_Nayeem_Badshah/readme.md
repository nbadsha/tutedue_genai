# GEN AI Assignment 3

This assignment practices Python functions, recursion, lambda expressions, and the `map()` and `filter()` functions.

## Notebook

- [Nayeem_GEN_AI_task_1-7.ipynb](Nayeem_GEN_AI_task_1-7.ipynb)

## Requirements

- Python 3.8 or later
- Jupyter Notebook, JupyterLab, or VS Code with the Jupyter extension

Install JupyterLab if needed:

```bash
pip install jupyterlab
```

## How to Run

Open the notebook and run the cells from top to bottom:

```bash
jupyter lab
```

Task 7 is interactive and waits for menu input. Use `q` to exit its menu.

## Implemented Tasks

### Task 1: Basic Function - Price After Discount

Defines `apply_discount(price, discount_percent=5)`, which returns the price after discount. The function also limits discounts to a maximum of 60%. It is tested with a 10% discount and the default 5% discount.

### Task 2: Recursive Function - Factorial Utility

Defines a recursive `factorial(n)` function with base cases for `0` and `1`. Negative values display an error message and return `None`.

### Task 3: Lambda Function - GST Calculator

Defines `gst`, a lambda function that adds 18% GST to a price. It also demonstrates calculating a price after applying a discount and GST.

### Task 4: Using `map()` - Apply GST to a List of Prices

Uses `map(gst, prices)` to create `prices_with_gst` from a list of prices and prints both lists.

### Task 5: Using `filter()` - Filter Expensive Products

Uses `filter()` to separate prices greater than 500 from prices less than or equal to 500.

### Task 6: Combined Utility Function

Defines `process_prices(prices)`, which uses `map()` to apply a 10% discount and `filter()` to keep discounted prices above 300. The function returns both lists.

### Task 7: Mini Problem - Menu Using Functions

Defines three helper functions:

- `add_price(prices_list, price)` adds a price to a list.
- `get_average_price(prices_list)` returns the average price.
- `get_max_price(prices_list)` returns the highest price.

These functions are used in a loop-driven menu with options to add a price, show the average, show the highest price, or quit.
