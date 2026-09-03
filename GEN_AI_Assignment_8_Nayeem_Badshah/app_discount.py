import streamlit as st

def calculate_discounted_price(original_price, discount_percentage):
    """
    Calculate the discounted price based on the original price and discount percentage.

    Parameters:
    original_price (float): The original price of the item.
    discount_percentage (float): The discount percentage to be applied.

    Returns:
    float: The discounted price after applying the discount.
    """
    if original_price < 0 or discount_percentage < 0:
        raise ValueError("Original price and discount percentage must be non-negative.")
    
    discount_amount = (discount_percentage / 100) * original_price
    discounted_price = original_price - discount_amount
    return discounted_price


st.title("Discount Calculator")

original_price = st.number_input("Enter the original price:", min_value=0.0, step=0.01)
discount_percentage = st.slider("Select the discount percentage:", min_value=0, max_value=50, value=0)

if st.button("Calculate Discounted Price"):
    try:
        discounted_price = calculate_discounted_price(original_price, discount_percentage)
        st.success(f"The discounted price is: {discounted_price:.2f}")
    except ValueError as e:
        st.error(str(e))