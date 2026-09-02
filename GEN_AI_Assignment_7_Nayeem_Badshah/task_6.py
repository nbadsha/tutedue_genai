class Product:

    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def __str__(self):
        return f"Product Name: {self.name}, Price: {self.price}, Category: {self.category}"

    def __add__(self, other):
        if isinstance(other, Product):
            return self.price + other.price
        return NotImplemented

if __name__ == "__main__":
    # Example usage
    product1 = Product("Laptop", 1000, "Electronics")
    product2 = Product("Smartphone", 800, "Electronics")

    print(product1)
    print(product2)

    total_price = product1 + product2
    print(f"Total Price of both products: {total_price}")