# Yum Haven Vending Machine 
from tabulate import tabulate
import random

Yum_points = {"user": 0} #Yum points for customers who use Yum Haven Daily

admin_password = "admin123@" #password for access on admin mode

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
        choice = int(input("\nEnter the category number to see: "))
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

                #This adds a Yum point for the user
                Yum_points['user'] += int(item['price'])
                print(f"You have earned {int(item['price'])} Yum points. Total Yum points: {Yum_points['user']}.")
                return
        except ValueError:
            print("Invalid input. Please insert a valid amount.")

def admin_mode():
    #This feature lets the user access admin mode specifically for employees or restockers for Yum Haven
    password = input("Enter Password: ")
    if password == admin_password:
        print ("\n--- Admin Mode ---")
        while True:
            print ("\n1. View Item Stock")
            print ("2. Restock Items")
            print ("3. Exit Admin Mode")
            try:
                choice = int(input("Enter your choice: "))
                if choice == 1:

                    #This will display the current stock of each item
                    print("\n--- Current Stock ---")
                    table = [[item['name'], item['category'], f"AED {item['price']:.2f}", item['stock']] 
                             for item in items]
                    print(tabulate(table, headers=["Item", "Category", "Price", "Stock"], tablefmt="fancy_grid"))\
                    
                elif choice == 2:
                    # This will allow the user to restock the items
                    for item in items:
                        restock = int(input(f"Enter new stock quantity for {item['name']} (current stock: {item['stock']}): "))
                        item['stock'] += restock
                    print("Items restocked successfully.")
                elif choice == 3:
                    print("Exiting Admin Mode.")
                    break
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")
    else:
        print("Incorrect password. Access denied.")

def suggest_item(items, current_item):
    """Suggests a random item from the same category."""
    same_category_items = [item for item in items if item['category'] == current_item['category'] and item != current_item and item['stock'] > 0]
    if same_category_items:
        suggestion = random.choice(same_category_items)
        print(f"Suggestion: How about trying {suggestion['name']} for AED {suggestion['price']:.2f}?")

def vending_machine():
    #This is the main Vending Machine Program

     # Seperates each snacks and drinks to specific categories.
    categories = list(set(item['category'] for item in items))

    print("Welcome to the Yum Haven Vending Machine!")
    while True:
        print ("\n1. Browse Items")
        print ("2. Check your current Yum Points")
        print ("3. Admin Mode (For Restockers)")
        print ("0. Exit")
        try:
            main_choice = int(input("Choose an option: "))
            if main_choice == 1:

                #This will allow the user to browse the items given
                display_categories (categories)
                selected_categories = select_category(categories)
                if not selected_categories:
                    continue
                category_items = display_items_in_each_category(items, selected_categories)
                selected_items = select_item_from_category(category_items)
                if selected_items:
                    insert_money(selected_items)

            elif main_choice == 2:

                #if the user picks 2, it will allow the user to view their current yum points
                print (f"You currently have: {Yum_points['user']}")

            elif main_choice == 3:

                #This will let the user be able to access admin mode 
                admin_mode()
            
            elif main_choice == 0:
                print ("Thank you for using the Yum Haven Vending Machine, Have a good day!")
                
                break
            
            else:
                print ("Invalid Choice, Please try again...")
        except ValueError:
            print ("Invalid User Input, Please enter a number that is valid from above")


# Run the program
vending_machine()

#Updated Display of the Program
""" Welcome to the Yum Haven Vending Machine!

1. Browse Items
2. Check your current Yum Points
3. Admin Mode (For Restockers)
0. Exit

Choose an option: 

Choose an option: 1

--- Available Categories ---
1. Hot Drinks
2. Snacks
3. Drinks
0. Exit

Enter the category number to see:

Enter the category number to see: 1

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
Enter the item number to purchase: 

Enter the item number to purchase: 6

Insert money to buy Sandwich (AED 15.0):

Insert money to buy Sandwich (AED 15.0): 20
Dispensing Sandwich... Enjoy!
Your change is AED 5.00.
You have earned 15 Yum points. Total Yum points: 15.

1. Browse Items
2. Check your current Yum Points
3. Admin Mode (For Restockers)
0. Exit

Choose an option: 

Choose an option: 3
Enter Password: admin123@

--- Admin Mode --- 

1. View Item Stock 
2. Restock Items   
3. Exit Admin Mode 
Enter your choice: 1

--- Current Stock ---
╒═══════════════╤════════════╤═══════════╤═════════╕
│ Item          │ Category   │ Price     │   Stock │
╞═══════════════╪════════════╪═══════════╪═════════╡
│ Coke          │ Drinks     │ AED 5.00  │      10 │
├───────────────┼────────────┼───────────┼─────────┤
│ Pepsi         │ Drinks     │ AED 5.00  │       8 │
├───────────────┼────────────┼───────────┼─────────┤
│ Water         │ Drinks     │ AED 3.00  │      15 │
├───────────────┼────────────┼───────────┼─────────┤
│ Orange Juice  │ Drinks     │ AED 6.50  │       7 │
├───────────────┼────────────┼───────────┼─────────┤
│ Iced Coffee   │ Drinks     │ AED 10.00 │       5 │
├───────────────┼────────────┼───────────┼─────────┤
│ Chips         │ Snacks     │ AED 4.00  │      12 │
├───────────────┼────────────┼───────────┼─────────┤
│ Chocolate Bar │ Snacks     │ AED 6.00  │      10 │
├───────────────┼────────────┼───────────┼─────────┤
│ Biscuits      │ Snacks     │ AED 7.00  │       8 │
├───────────────┼────────────┼───────────┼─────────┤
│ Cookies       │ Snacks     │ AED 8.50  │       6 │
├───────────────┼────────────┼───────────┼─────────┤
│ Granola Bar   │ Snacks     │ AED 5.50  │       9 │
├───────────────┼────────────┼───────────┼─────────┤
│ Energy Drink  │ Drinks     │ AED 12.00 │       4 │
├───────────────┼────────────┼───────────┼─────────┤
│ Sandwich      │ Snacks     │ AED 15.00 │       3 │
├───────────────┼────────────┼───────────┼─────────┤
│ Tea           │ Hot Drinks │ AED 4.00  │      10 │
├───────────────┼────────────┼───────────┼─────────┤
│ Coffee        │ Hot Drinks │ AED 7.50  │       8 │
├───────────────┼────────────┼───────────┼─────────┤
│ Hot Chocolate │ Hot Drinks │ AED 9.00  │       5 │
╘═══════════════╧════════════╧═══════════╧═════════╛

1. View Item Stock
2. Restock Items
3. Exit Admin Mode
Enter your choice: 2
Enter new stock quantity for Coke (current stock: 10): 11
Enter new stock quantity for Pepsi (current stock: 8): 12
Enter new stock quantity for Water (current stock: 15): 16
Enter new stock quantity for Orange Juice (current stock: 7): 17
Enter new stock quantity for Iced Coffee (current stock: 5): 6
Enter new stock quantity for Chips (current stock: 12): 13
Enter new stock quantity for Chocolate Bar (current stock: 10): 11
Enter new stock quantity for Biscuits (current stock: 8): 9
Enter new stock quantity for Cookies (current stock: 6): 7
Enter new stock quantity for Granola Bar (current stock: 9): 10
Enter new stock quantity for Energy Drink (current stock: 4): 5
Enter new stock quantity for Sandwich (current stock: 3): 4
Enter new stock quantity for Tea (current stock: 10): 11
Enter new stock quantity for Coffee (current stock: 8): 8
Enter new stock quantity for Hot Chocolate (current stock: 5): 6
Items restocked successfully.
"""