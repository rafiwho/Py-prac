class Cart:
    def __init__(self):
        self.items = {}

    def add_item(self, name, quantity, price):
        if name in self.items:
            self.items[name][0] += quantity
        else:
            self.items[name] = [quantity, price]

    def remove_item(self, name):
        if name in self.items:
            del self.items[name]

    def remove_quantity(self, name, quantity):
        if name in self.items:
            self.items[name][0] -= quantity
            if self.items[name][0] <= 0:
                del self.items[name]

    def total_quantity(self):
        return sum(quantity for quantity, _ in self.items.values())

    def total_price(self):
        return sum(quantity * price for quantity, price in self.items.values())

class Checkout(Cart):
    def __init__(self):
        super().__init__()
    
    def show_items(self):
        print("Current Items in Cart:")
        for name, (quantity, price) in self.items.items():
            print(f"{name} - {quantity} * ${price}= ${quantity*price}")
        print(f"Total Quantity: {self.total_quantity()}")
        print(f"Total Price: ${self.total_price()}")

    def confirm_checkout(self,confirm):
        if confirm == 1:
            print("\nConfirm to checkout:")
            self.show_items()
            print(f"Total Price: ${self.total_price()}")
        else:
            print("\nNot Confirmed")


cart = Checkout()
cart.add_item("Laptop", 1, 1000)
cart.add_item("Mouse", 1, 8)
cart.add_item("Keyboard", 2, 5)

cart.show_items()

cart.remove_quantity("Keyboard", 1)
print("\nRemoved 1 Keyboard from Cart:")
cart.show_items()

cart.remove_item("Mouse")
print("\nRemoved Mouse from Cart:")
cart.show_items()

cart.confirm_checkout(1)

