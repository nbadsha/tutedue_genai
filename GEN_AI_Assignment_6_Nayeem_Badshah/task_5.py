cart = []

while True:
    price_input = input("Enter price (or 'q' to quit): ")

    if price_input.lower() == 'q':
        break

    try:
        price = float(price_input)
        if price < 0:
            raise ValueError("Negative price not allowed")
        cart.append(price)
    except ValueError as e:
        print(f"Invalid input: {e}")

print(f"Total items: {len(cart)}")
print(f"Total bill: {sum(cart)}")
