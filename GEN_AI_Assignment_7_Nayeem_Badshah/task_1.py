class Product:

    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def get_info(self):
        return f"Product Name: {self.name}, Price: {self.price}, Category: {self.category}"

    def apply_discount(self, discount_percentage):
        if discount_percentage < 0 or discount_percentage > 100:
            raise ValueError("Discount percentage must be between 0 and 100.")
        discount_amount = (discount_percentage / 100) * self.price
        return self.price - discount_amount

if __name__ == "__main__":
    # Example usage
    product = Product("Laptop", 1000, "Electronics")
    print(product.get_info())
    discounted_price = product.apply_discount(10)
    print(f"Discounted Price: {discounted_price}")