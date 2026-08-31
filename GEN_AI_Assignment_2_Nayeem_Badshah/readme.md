# GEN AI Assignment 2

This assignment demonstrates Python conditionals, loops, user input, and loop-control statements through order-processing and sales examples.

## Notebook

- [Nayeem_GEN_AI_task_1-5.ipynb](Nayeem_GEN_AI_task_1-5.ipynb)

## Requirements

- Python 3.8 or later
- Jupyter Notebook or JupyterLab

Install Jupyter if needed:

```bash
pip install jupyterlab
```

## How to Run

Open the assignment folder in VS Code or start JupyterLab:

```bash
jupyter lab
```

Open `Nayeem_GEN_AI_task_1-5.ipynb` and run the cells from top to bottom.

## Implemented Tasks

### Task 1: Discount Rules

Reads an integer order amount and applies the following discounts:

| Order amount | Discount |
| --- | ---: |
| 2000 or more | 15% |
| 1500 to 1999 | 10% |
| 1000 to 1499 | 7% |
| Less than 1000 | 0% |

The program prints an error message when the input is not a whole number.

### Task 2: Process Multiple Orders

Processes the list `[1200, 2500, 800, 1750, 3000]` with a `for` loop. It prints each order, its discount percentage, and its final amount, then calculates:

- Total revenue after discounts: `8166.00`
- Orders that received a discount: `4`

### Task 3: User Menu

Uses a `while` loop to provide these menu options:

1. Add an order amount to a running list.
2. Show all orders and totals after discounts.
3. Quit with `q`.

Invalid choices use `continue` to display the menu again, while `q` uses `break` to exit.

### Task 5: Loop Control with Conditions

Processes daily sales using `daily = [200, 150, 0, 400, 50, -1, 300]`:

- `0` is skipped with `continue`.
- `-1` is treated as corrupted data and stops processing with `break`.
- Positive sales are added to a running total.

The final total before the corrupted entry is `800`.

## Note

The notebook currently includes Tasks 1, 2, 3, and 5. No Task 4 section is present in the current notebook.
