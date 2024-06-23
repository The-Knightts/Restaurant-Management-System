from Exceptions import InvalidMenuItemError

class MenuItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class Menu:
    def __init__(self):
        self.items = []
        self.read_menu_from_file('menu.txt')

    def add_item(self, name, price, quantity):
        for item in self.items:
            if item.name == name:
                raise InvalidMenuItemError(f"Item '{name}' already exists in the menu.")
        self.items.append(MenuItem(name, price, quantity))
        self.write_menu_to_file('menu.txt')

    def update_item(self, name, price, quantity):
        for item in self.items:
            if item.name == name:
                item.price = price
                item.quantity = quantity
                self.write_menu_to_file('menu.txt')
                return
        raise InvalidMenuItemError(f"Item '{name}' not found in the menu.")

    def delete_item(self, name):
        found = False
        for item in self.items:
            if item.name == name:
                self.items.remove(item)
                found = True
                self.write_menu_to_file('menu.txt')
                break
        if not found:
            raise InvalidMenuItemError(f"Item '{name}' not found in the menu.")

    def display_menu(self):
        if not self.items:
            print("Menu is empty.")
        else:
            for item in self.items:
                print(f"Name: {item.name}, Price: {item.price}, Quantity: {item.quantity}")

    def read_menu_from_file(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                name, price, quantity = line.strip().split(',')
                self.items.append(MenuItem(name, float(price), int(quantity)))

    def write_menu_to_file(self, filename):
        with open(filename, 'w') as file:
            for item in self.items:
                file.write(f"{item.name},{item.price},{item.quantity}\n")
