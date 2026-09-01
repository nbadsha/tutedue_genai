def apply_discount(price, discount_percentage):
    """
    Apply a discount to the given price.

    :param price: Original price of the item.
    :param discount_percentage: Discount percentage to apply.
    :return: Price after applying the discount.
    """
    if discount_percentage < 0 or discount_percentage > 100:
        raise ValueError("Discount percentage must be between 0 and 100.")
    
    discount_amount = (discount_percentage / 100) * price
    discounted_price = price - discount_amount
    return discounted_price

def flat_discount(price, discount_amount):
    """
    Apply a flat discount to the given price.

    :param price: Original price of the item.
    :param discount_amount: Flat discount amount to apply.
    :return: Price after applying the flat discount.
    """
    if discount_amount < 0:
        raise ValueError("Discount amount must be non-negative.")
    
    discounted_price = price - discount_amount
    return max(discounted_price, 0)  # Ensure price doesn't go below 0