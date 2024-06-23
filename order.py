from Exceptions import InsufficientQuantityError, InvalidMenuItemError
class Order:
    def __init__(self, menu):
        self.menu = menu
        self.items = []

    def add_item(self, name, quantity):
        menu_item = next((item for item in self.menu.items if item.name == name), None)
        if not menu_item:
            raise InvalidMenuItemError(f"Item '{name}' not found in the menu.")
        if menu_item.quantity < quantity:
            raise InsufficientQuantityError(f"Not enough quantity for item '{name}'. Available: {menu_item.quantity}")
        self.items.append((menu_item, quantity))
        menu_item.quantity -= quantity

    def calculate_total(self, discount = 0):
        total = sum(item.price * quantity for item, quantity in self.items)
        total -= total * (discount / 100)
        return total

    def generate_receipt(self):
        receipt = "Receipt:\n"
        receipt += "\n".join([f"{item.name} x {quantity}: {item.price * quantity}" for item, quantity in self.items])
        receipt += f"\nTotal: {self.calculate_total()}"
        return receipt

    def save_order_to_file(self, filename):
        with open(filename, 'a') as file:
            for item, quantity in self.items:
                file.write(f"{item.name},{item.price},{quantity}\n")