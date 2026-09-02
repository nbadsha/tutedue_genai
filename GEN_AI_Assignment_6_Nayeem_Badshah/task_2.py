from typing import List


def bill_calculator(prices: List):
    total = 0

    for price in prices:
        try:
            if not isinstance(price, (int, float)):
                raise TypeError(f"{price} is not a number.")

            if price < 0:
                raise ValueError("Negative price not allowed")

            if price <= 0:
                print(f"Skipping {price}: price must be positive.")
                continue

            total += price
            print(f"Running total: {total}")

        except TypeError as e:
            print(f"Skipping {price}: {e}")
        except ValueError as e:
            print(f"Skipping {price}: {e}")

    return total


if __name__ == "__main__":
    prices = [120, 350, 'abc', 500, -200, 800]
    final_total = bill_calculator(prices)
    print(f"Final total: {final_total}")
