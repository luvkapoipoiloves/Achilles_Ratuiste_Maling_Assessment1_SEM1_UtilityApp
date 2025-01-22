# Yum Haven Vending Machine 
import random

def display_menu(items, categories):
    """Displays the menu of items, grouped by categories."""
    print("\n--- Yum Haven Vending Machine Menu ---")
    for category in categories:
        print(f"\nCategory: {category}")
        for index, item in enumerate(items):
            if item['category'] == category:
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

def suggest_item(items, current_item):
    """Suggests a random item from the same category."""
    same_category_items = [item for item in items if item['category'] == current_item['category'] and item != current_item and item['stock'] > 0]
    if same_category_items:
        suggestion = random.choice(same_category_items)
        print(f"Suggestion: How about trying {suggestion['name']} for AED {suggestion['price']:.2f}?")

def vending_machine():
    """Main vending machine program."""
    # List of items in the vending machine
    items = [
        {"name": "Coke", "price": 5.00, "stock": 10, "category": "Drinks"},
        {"name": "Pepsi", "price": 5.00, "stock": 8, "category": "Drinks"},
        {"name": "Water", "price": 3.00, "stock": 15, "category": "Drinks"},
        {"name": "Orange Juice", "price": 6.50, "stock": 7, "category": "Drinks"},
        {"name": "Iced Coffee", "price": 10.00, "stock": 5, "category": "Drinks"},
        {"name": "Chips", "price": 4.00, "stock": 12, "category": "Snacks"},
        {"name": "Chocolate Bar", "price": 6.00, "stock": 10, "category": "Snacks"},
        {"name": "Biscuits", "price": 7.00, "stock": 8, "category": "Snacks"},
        {"name": "Cookies", "price": 8.50, "stock": 6, "category": "Snacks"},
        {"name": "Granola Bar", "price": 5.50, "stock": 9, "category": "Snacks"},
        {"name": "Energy Drink", "price": 12.00, "stock": 4, "category": "Drinks"},
        {"name": "Sandwich", "price": 15.00, "stock": 3, "category": "Snacks"},
        {"name": "Tea", "price": 4.00, "stock": 10, "category": "Hot Drinks"},
        {"name": "Coffee", "price": 7.50, "stock": 8, "category": "Hot Drinks"},
        {"name": "Hot Chocolate", "price": 9.00, "stock": 5, "category": "Hot Drinks"},
    ]

     # Seperates each snacks and drinks to specific categories.
    categories = list(set(item['category'] for item in items))

    print("Welcome to the Yum Haven Vending Machine!")
    while True:
        display_menu(items, categories)
        item = select_item(items)
        if item:
            insert_money(item)
            suggest_item(items, item)
        else:
            print("Thank you for using Yum Haven Vending MAchine. Have a good day!")
            break

# Run the program
vending_machine()

#Updated Display
#--- Yum Haven Vending Machine Menu ---

#Category: Drinks
#1. Coke - AED 5.0 (Stock: 10)
#2. Pepsi - AED 5.0 (Stock: 8)
#3. Water - AED 3.0 (Stock: 15)
#4. Orange Juice - AED 6.5 (Stock: 7)
#5. Iced Coffee - AED 10.0 (Stock: 5)
#11. Energy Drink - AED 12.0 (Stock: 4)

#Category: Snacks
#6. Chips - AED 4.0 (Stock: 12)
#7. Chocolate Bar - AED 6.0 (Stock: 10)
#8. Biscuits - AED 7.0 (Stock: 8)
#9. Cookies - AED 8.5 (Stock: 6)
#10. Granola Bar - AED 5.5 (Stock: 9)
#12. Sandwich - AED 15.0 (Stock: 3)

#Category: Hot Drinks
#13. Tea - AED 4.0 (Stock: 10)
#14. Coffee - AED 7.5 (Stock: 8)
#15. Hot Chocolate - AED 9.0 (Stock: 5)
#0. Exit
#Enter the item number to purchase: