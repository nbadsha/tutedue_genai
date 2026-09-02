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
        raise TypeError("You can only add two Product objects.")


class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, name):
        for product in self.products:
            if product.name == name:
                self.products.remove(product)
                return
        print(f"{name} not found in inventory.")

    def get_total_value(self):
        total = 0
        for product in self.products:
            total += product.price
        return total

    def show_all_products(self):
        for product in self.products:
            print(product)


class Store:
    def __init__(self, store_name):
        self.store_name = store_name
        self.inventory = Inventory()

    def add_new_product(self, name, price, category):
        product = Product(name, price, category)
        self.inventory.add_product(product)
        return product

    def show_summary(self):
        print(f"Store Name: {self.store_name}")
        print(f"Total items: {len(self.inventory.products)}")
        print(f"Total value: {self.inventory.get_total_value()}")
        self.inventory.show_all_products()

    def __add__(self, other):
        if isinstance(other, Store):
            return self.inventory.get_total_value() + other.inventory.get_total_value()
        raise TypeError("You can only add two Store objects.")


if __name__ == "__main__":
    store = Store("Tech Store")

    laptop = store.add_new_product("Laptop", 1000, "Electronics")
    smartphone = store.add_new_product("Smartphone", 800, "Electronics")
    headphones = store.add_new_product("Headphones", 150, "Accessories")

    store.show_summary()

    combined_price = laptop + smartphone
    print(f"Combined price of {laptop.name} and {smartphone.name}: {combined_price}")
    print(f"Combined price of {smartphone.name} and {headphones.name}: {smartphone + headphones}")