# GEN_AI_Assignment_7_Nayeem_Badshah

This assignment demonstrates the use of Object-Oriented Programming (OOP) in Python to model a simple retail store system. The project focuses on classes, object relationships, and basic inventory management without using any file handling, exception handling, or external packages.

## Project Overview

The system includes three main classes:

- `Product`: represents a product with a name, price, and category
- `Inventory`: manages a list of product objects
- `Store`: contains the store name and inventory and provides summary operations

## Class Structure

### `Product`

Attributes:
- `name`
- `price`
- `category`

Methods:
- `__str__()` - returns product details in a readable format
- `__add__()` - combines the prices of two product objects

### `Inventory`

Attributes:
- `products` - a list used to store all product objects

Methods:
- `add_product(product)` - adds a product to the inventory
- `remove_product(name)` - removes a product by matching its name
- `get_total_value()` - calculates the total price of all products in the inventory
- `show_all_products()` - prints each product in the inventory

### `Store`

Attributes:
- `store_name`
- `inventory`

Methods:
- `add_new_product(name, price, category)` - creates and adds a new product
- `show_summary()` - prints the store name, total items, total inventory value, and list of products
- `__add__()` - sums the total values of two store objects

## Example Workflow

The program creates a `Store` object, adds three products, shows the inventory summary, and then combines the prices of two products using the `+` operator.

Example:

```python
store = Store("Tech Store")

laptop = store.add_new_product("Laptop", 1000, "Electronics")
smartphone = store.add_new_product("Smartphone", 800, "Electronics")
headphones = store.add_new_product("Headphones", 150, "Accessories")

store.show_summary()
print(laptop + smartphone)
```

## Expected Output

```python
Store Name: Tech Store
Total items: 3
Total value: 1950
Product Name: Laptop, Price: 1000, Category: Electronics
Product Name: Smartphone, Price: 800, Category: Electronics
Product Name: Headphones, Price: 150, Category: Accessories
Combined price of Laptop and Smartphone: 1800
```

## Learning Objective

This project helps practice:

- class creation and object instantiation
- encapsulation through attributes and methods
- object interaction and aggregation
- method overloading using `__add__()`
- basic inventory management in an OOP style

## Files

- `task_7.py` - contains the complete OOP implementation
- `readme.md` - project documentation
