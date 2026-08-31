# GEN AI Assignment 4

This assignment practices Python file handling, reading and writing text files, appending records, basic calculations, and simple error-safe file access.

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

Running the notebook creates `sales_data.txt`, `products.txt`, and `discount_report.txt` in the notebook's working directory.

Tasks 5 and 7 require user input while their cells are running.

## Implemented Tasks

### Task 1: Write Sales Records to a File

Creates `sales = [1200, 450, 980, 1500, 3000]`, writes each value on a separate line to `sales_data.txt`, then reopens and prints the file.

### Task 2: Read File in Different Ways

Demonstrates `.read()` for the entire file, `.readline()` for the first line, and `.readlines()` for all lines. Newline characters are removed and the sales values are converted to integers.

### Task 3: Append New Sales

Appends `5000`, `2500`, and `1700` to `sales_data.txt`, prints the updated file, and displays the total number of lines.

### Task 4: Generate Summary Report from File

Reads the sales values from `sales_data.txt` and calculates:

- Total Sales
- Highest Sale
- Lowest Sale
- Average Sale

### Task 5: Create Product Info File

Asks the user for three product names and prices, writes them to `products.txt` using the format `ProductName | Price`, and reads the file back line by line.

### Task 6: Read File Safely

Asks the user for a filename and uses `os.path.exists()` before opening it. Existing files are printed; missing files display:

```text
File not found. Please check the filename.
```

### Task 7: Export Discounted Prices

Uses a product-price dictionary and asks for a discount percentage. It writes each product's original and discounted price to `discount_report.txt` with this format:

```text
Product | Original Price | Discounted Price
```

The report also includes the total number of products and the average discounted price, then prints the completed file.

## Note

Run the cells in order because later tasks use files created by earlier tasks.
