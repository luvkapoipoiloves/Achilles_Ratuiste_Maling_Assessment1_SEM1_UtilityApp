# Yum Haven Vending Machine 
from tabulate import tabulate
import random

def display_categories(categories):
    #This part will display the available categories in which the user will choose from.
    print("\n--- Available Categories ---")
    for index, category in enumerate(categories, start=1):
        print(f"{index}. {category}")
    print("0. Exit")

def display_items_in_each_category(items, category):
        #This Filters the items by category
        category_items =[item for item in items if item['category'] == category]

        #This create seperate tables to make it simpler for the users experience.
        table =[[index + 1, item['name'], f"AED {item['price']:.2f}", item['stock']]
                for index, item in enumerate(category_items)]
        print(f"\n--- Items in {category} ---")

        #This Prints the table 
        print(tabulate(table, headers= ["#", "Item", "Price", "Stock"], tablefmt= "grid"))
        print ("\n0. Go Back")
        return category_items

def select_category(categories):
    #This part will allow the user to select a category.
    try:
        choice = int(input("n\Enter the category number to see: "))
        if choice == 0:
            return None
        if 1 <= choice <= len(categories):
            return categories [choice - 1]
        else:
            print ("Invalid Number, Please Try Again. ")
    except ValueError:
        print ("Invalid Input. Please try again. ")
    return None

def select_item_from_category(category_items):
    #This will allow the user to select an item from the category they choose.
    try:
        choice = int(input("Enter the item number to purchase: "))
        if choice == 0:
            return None
        if 1 <= choice <= len(category_items):
            item = category_items[choice - 1]
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
                print(f"Not enough money. {item['name']} costs AED {item['price']:.2f}.")
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
        display_categories(categories)
        selected_category = select_category(categories)
        if not selected_category:
            print("Thank you for using Yum Haven. Have a nice day!")
            break
        # This will show the items in the selected category by the user
        category_items = display_items_in_each_category(items, selected_category)
        selected_item = select_item_from_category(category_items)
        if selected_item:
            insert_money(selected_item)
            suggest_item(items, selected_item)

# Run the program
vending_machine()

#Updated Display
""" Welcome to the Yum Haven Vending Machine!

--- Available Categories ---
1. Hot Drinks
2. Snacks
3. Drinks
0. Exit
n\Enter the category number to see: 2

--- Items in Snacks ---
+-----+---------------+-----------+---------+
|   # | Item          | Price     |   Stock |
+=====+===============+===========+=========+
|   1 | Chips         | AED 4.00  |      12 |
+-----+---------------+-----------+---------+
|   2 | Chocolate Bar | AED 6.00  |      10 |
+-----+---------------+-----------+---------+
|   3 | Biscuits      | AED 7.00  |       8 |
+-----+---------------+-----------+---------+
|   4 | Cookies       | AED 8.50  |       6 |
+-----+---------------+-----------+---------+
|   5 | Granola Bar   | AED 5.50  |       9 |
+-----+---------------+-----------+---------+
|   6 | Sandwich      | AED 15.00 |       3 |
+-----+---------------+-----------+---------+

0. Go Back
Enter the item number to purchase: """