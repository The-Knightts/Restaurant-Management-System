# restaurant.py
from menu import Menu
from order import Order
from Exceptions import CustomException

menu = Menu()

while True:
    print("\nRestaurant Management System")
    print("1. Add a menu item")
    print("2. Update a menu item")
    print("3. Delete a menu item")
    print("4. Display the menu")
    print("5. Take an order")
    print("6. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            name = input("Enter item name: ")
            price = float(input("Enter item price: "))
            quantity = int(input("Enter item quantity: "))
            menu.add_item(name, price, quantity)
            print("Item added successfully!")

        elif choice == 2:
            name = input("Enter item name: ")
            price = float(input("Enter item price: "))
            quantity = int(input("Enter item quantity: "))
            menu.update_item(name, price, quantity)
            print("Item updated successfully!")

        elif choice == 3:
            name = input("Enter item name to delete: ")
            menu.delete_item(name)
            print("Item deleted successfully!")

        elif choice == 4:
            menu.display_menu()

        elif choice == 5:
            order = Order(menu)
            while True:
                item_name = input("Enter item name to order (or 'done' to finish): ")
                if item_name.lower() == 'done':
                    break
                item_quantity = int(input("Enter quantity: "))
                order.add_item(item_name, item_quantity)
            print(order.generate_receipt())
            order.save_order_to_file('orders.txt')
            print("Order saved successfully!")

        elif choice == 6:
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

    except CustomException as e:
        print(f"Error: {e}")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
