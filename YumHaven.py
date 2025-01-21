# Vending Machine Program in Dirhams (AED)

def display_menu(items):
    """Displays the menu of items."""
    print("\n--- Vending Machine Menu ---")
    for index, item in enumerate(items):
        print(f"{index + 1}. {item['name']} - AED {item['price']} (Stock: {item['stock']})")
    print("0. Exit")

def select_item(items):
    """Allows the user to select an item by entering its number."""
    try:
        choice = int(input("Enter the item number to purchase: "))
        if choice == 0:
            return None
        if 1 <= choice <= len(items):
            item = items[choice - 1]
            if item['stock'] > 0:
                return item
            else:
                print(f"Sorry, {item['name']} is out of stock.")
        else:
            print("Invalid selection. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a number.")
    return None

def insert_money(item):
    """Handles money insertion and returns whether the user can afford the item."""
    while True:
        try:
            money = float(input(f"Insert money to buy {item['name']} (AED {item['price']}): "))
            if money < item['price']:
                print(f"Not enough money. {item['name']} costs AED {item['price']}.")
            else:
                change = money - item['price']
                print(f"Dispensing {item['name']}... Enjoy!")
                if change > 0:
                    print(f"Your change is AED {change:.2f}.")
                item['stock'] -= 1
                return
        except ValueError:
            print("Invalid input. Please insert a valid amount.")

def vending_machine():
    """Main vending machine program."""
    # List of items in the vending machine
    items = [
        {"name": "Coke", "price": 5.00, "stock": 10},
        {"name": "Pepsi", "price": 5.00, "stock": 8},
        {"name": "Water", "price": 3.00, "stock": 15},
        {"name": "Orange Juice", "price": 6.50, "stock": 7},
        {"name": "Chips", "price": 4.00, "stock": 12},
        {"name": "Chocolate", "price": 6.00, "stock": 10},
        {"name": "Biscuits", "price": 7.00, "stock": 8},
        {"name": "Cookies", "price": 8.50, "stock": 6},
    ]

    print("Welcome to the Yum Haven!")
    while True:
        display_menu(items)
        item = select_item(items)
        if item:
            insert_money(item)
        else:
            print("Thank you for using the Yum Haven Vending Machine. Goodbye!")
            break

# Run the program
vending_machine()