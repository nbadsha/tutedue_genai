def check_age(age):
    if age < 1 or age > 120:
        raise ValueError("Age must be between 1 and 120")
    return "Valid age"


if __name__ == "__main__":
    try:
        age = int(input("Enter your age: "))
        result = check_age(age)
        print(result)
    except ValueError as e:
        print(e)
    except Exception:
        print("Please enter a valid integer.")
