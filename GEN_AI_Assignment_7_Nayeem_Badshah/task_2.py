class Product:

    def __init__(self, name, price, category):
        self.name = name
        self.__price = price
        self.category = category

    def get_price(self):
        return self.__price

    def set_price(self, new_price):
        if new_price < 0:
            raise ValueError("Price cannot be negative.")
        self.__price = new_price

if __name__ == "__main__":
    # Example usage
    product = Product("Smartphone", 500, "Electronics")
    print(f"Product Name: {product.name}, Price: {product.get_price()}, Category: {product.category}")
    
    # Update price
    product.set_price(450)
    print(f"Updated Price: {product.get_price()}")