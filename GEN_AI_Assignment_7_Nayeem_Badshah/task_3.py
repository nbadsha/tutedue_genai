class Product:

    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def get_info(self):
        return f"Product Name: {self.name}, Price: {self.price}, Category: {self.category}"

class ElectronicProduct(Product):

    def __init__(self, name, price, category, warranty_period):
        super().__init__(name, price, category)
        self.warranty_period = warranty_period

    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}, Warranty Period: {self.warranty_period} months"

if __name__ == "__main__":
    # Example usage
    product = Product("Laptop", 1000, "Electronics")
    print(product.get_info())

    electronic_product = ElectronicProduct("Smartphone", 800, "Electronics", 24)
    print(electronic_product.get_info())