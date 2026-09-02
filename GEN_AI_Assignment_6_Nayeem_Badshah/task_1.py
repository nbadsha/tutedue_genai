def divide(numerator, denominator):
    try:
        return numerator / denominator
    except ValueError:
        raise ValueError("Numerator and denominator must be numbers.")
    except ZeroDivisionError:
        raise ValueError("Cannot divide by zero.")
    finally:
        print("Operation Complete")

if __name__ == "__main__":
    # Example usage
    try:
        result = divide(10, 2)
        print(f"Result: {result}")
    except Exception as e:
        print(e)

    try:
        result = divide(10, 0)
        print(f"Result: {result}")
    except Exception as e:
        print(e)

    try:
        result = divide(10, "a")
        print(f"Result: {result}")
    except Exception as e:
        print(e)

    try:
        result = divide("a", 2)
        print(f"Result: {result}")
    except Exception as e:
        print(e)

    