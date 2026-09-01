import math_utils
import string_utils
import shop_package.discount as disc
from shop_package.billing import calculate_total, apply_tax

def main():
    # Test the math_utils module functions
    # test the add function
    result = math_utils.add(5, 3)
    print(f"5 + 3 = {result}")
    # test the subtract function
    result = math_utils.subtract(5, 3)
    print(f"5 - 3 = {result}")
    # test the square function
    result = math_utils.square(5)
    print(f"5^2 = {result}")

    # Test the string_utils module functions
    # test the capitalize_words function
    input_string = "hello world"
    result = string_utils.capitalize_words(input_string)
    print(f"Capitalized: {result}")
    # test the reverse_string function
    input_string = "hello"
    result = string_utils.reverse_string(input_string)
    print(f"Reversed: {result}")
    # test the word_count function
    input_string = "hello world"
    result = string_utils.word_count(input_string)
    print(f"Word count: {result}")

    # Test the shop_package.discount module functions
    # test the apply_discount function
    original_price = 100
    discount_percentage = 20
    discounted_price = disc.apply_discount(original_price, discount_percentage)
    print(f"Original price: {original_price}, Discounted price: {discounted_price}")
    # test the flat_discount function
    flat_discount_amount = 15
    discounted_price = disc.flat_discount(original_price, flat_discount_amount)
    print(f"Original price: {original_price}, Flat discounted price: {discounted_price}")
    # Test the shop_package.billing module functions
    # test the calculate_total function
    prices = [10, 20, 30]
    total = calculate_total(prices)
    print(f"Total: {total}")
    # test the apply_tax function
    tax_rate = 0.05
    total_with_tax = apply_tax(total, tax_rate)
    print(f"Total with tax: {total_with_tax}")

if __name__ == "__main__":
    main()