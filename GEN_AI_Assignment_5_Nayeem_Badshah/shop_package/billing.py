def calculate_total(prices):
    """
    Calculate the total sum of a list of prices.

    :param prices: A list or iterable of numeric price values.
    :return: The sum of all prices as a number. Returns None if the input
        contains non-numeric values or if an unexpected error occurs.
    :raises: This function handles TypeError and other exceptions internally by
        printing an error message and returning None.
    """
    try:
        total = sum(prices)
        return total
    except TypeError:
        print("Error: All items in the prices list must be numbers.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

def apply_tax(amount, tax_rate=0.05):
    """
    Apply tax to the given amount.

    :param amount: The original amount.
    :param tax_rate: The tax rate to apply (default is 5%).
    :return: Amount after applying tax.
    """
    if amount < 0:
        raise ValueError("Amount must be non-negative.")
    
    tax_amount = amount * tax_rate
    total_with_tax = amount + tax_amount
    return total_with_tax