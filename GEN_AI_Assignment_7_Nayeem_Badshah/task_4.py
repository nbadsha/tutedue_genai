class Product:

    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def get_info(self):
        return f"Product Name: {self.name}, Price: {self.price}, Category: {self.category}"
    
class Laptop(Product):

    def __init__(self, name, price, category, ram_size):
        super().__init__(name, price, category)
        self.ram_size = ram_size

    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}, RAM Size: {self.ram_size} GB"

class Mobile(Product):

    def __init__(self, name, price, category, battery_capacity):
        super().__init__(name, price, category)
        self.battery_capacity = battery_capacity

    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}, Battery Capacity: {self.battery_capacity} mAh"

if __name__ == "__main__":
    # Example usage
    laptop = Laptop("Gaming Laptop", 1500, "Electronics", 16)
    print(laptop.get_info())

    mobile = Mobile("Smartphone", 800, "Electronics", 4000)
    print(mobile.get_info())