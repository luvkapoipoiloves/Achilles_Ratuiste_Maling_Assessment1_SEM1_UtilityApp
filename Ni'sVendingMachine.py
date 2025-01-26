# Ni's Vending Machine 
from tabulate import tabulate #Reference: https://pypi.org/project/tabulate/
import random #Reference: https://github.com/python/cpython/blob/3.13/Lib/random.py 

Gelo_points = {"user": 0} #Gelo points for customers who use Ni's Vending Machine Daily

admin_password = "admin123@" #password for access on admin mode

    # List of items in the vending machine
items = [
        {"name": "Gelo's Coke", "price": 5.00, "stock": 10, "category": "Drinks"},
        {"name": "Kapoipoi's Pepsi", "price": 5.00, "stock": 8, "category": "Drinks"},
        {"name": "Nyang's Water with ice", "price": 3.00, "stock": 15, "category": "Drinks"},
        {"name": "CooCoo's Orange Juice", "price": 6.50, "stock": 7, "category": "Drinks"},
        {"name": "Nyang's Extra Iced Coffee", "price": 10.00, "stock": 5, "category": "Drinks"},
        {"name": "Ni Chips", "price": 4.00, "stock": 12, "category": "Snacks"},
        {"name": "SNI'sker Chocolate Bar ", "price": 6.00, "stock": 10, "category": "Snacks"},
        {"name": "Ai nd Ni's Crunchy Milk Biscuits", "price": 7.00, "stock": 8, "category": "Snacks"},
        {"name": "Gelo's Footlong Cookies", "price": 8.50, "stock": 6, "category": "Snacks"},
        {"name": "Ai's Protein Bar", "price": 5.50, "stock": 9, "category": "Snacks"},
        {"name": "Ibi Energy Drink", "price": 12.00, "stock": 4, "category": "Drinks"},
        {"name": "Ni's Sandwich (NO KETCHUP)", "price": 15.00, "stock": 3, "category": "Snacks"},
        {"name": "Mapoipoi Tea", "price": 4.00, "stock": 10, "category": "Hot Drinks"},
        {"name": "Ai's Iced Mocha Coffee", "price": 7.50, "stock": 8, "category": "Hot Drinks"},
        {"name": "Hot Ni Chocolate", "price": 9.00, "stock": 5, "category": "Hot Drinks"},
    ] #

def display_categories(categories):
    #This part will display the available categories in which the user will choose from.
    #Reference: Dynamic extraction of unique values: https://stackoverflow.com/questions/12897374/get-unique-values-from-a-list-in-python

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
        print(tabulate(table, headers= ["#", "Item", "Price", "Stock"], tablefmt= "grid")) #Reference: https://pypi.org/project/tabulate/
        print ("\n0. Go Back")
        return category_items

def select_category(categories):
    #This part will allow the user to select a category. 
    #Reference for exception handling: https://realpython.com/python-exceptions/
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

def calculate_Gelo_points(price):
    #This will calculate every 5 aed spent, you earn 2 gelo points. 
    #Reference: Integer division and basic arithmetic: https://docs.python.org/3/tutorial/introduction.html#numbers
    return int((price // 5) * 2)

def use_Gelo_points(item):

    #This function will allow the user to use Gelo points to purchase items from Ni's Vending Machine
    if Gelo_points['user'] >= item['price']:
        print(f"You can use {int(item['price'])} Gelo points to purchase {item['name']}.")
        confirm = input("Would you like to use your Gelo points? (yes/no): ").lower()
        if confirm == 'yes':
            Gelo_points['user'] -= int(item['price'])
            item['stock'] -= 1
            print(f"Dispensing {item['name']}... Enjoy!")
            print(f"Points deducted. Your remaining points: {Gelo_points['user']}.")
            return True
        else:
            print("You chose not to use points.")
    else:
        print(f"Not enough points. You need {int(item['price'] - Gelo_points['user'])} more points to buy this item.")
    return False

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

                #This adds a Gelo Point for the user
                points_earned = calculate_Gelo_points(item['price'])
                Gelo_points['user'] += points_earned
                print(f"You earned {points_earned} Gelo points. Total points: {Gelo_points['user']}.")
                return
        except ValueError:
            print("Invalid input. Please insert a valid amount.")

def admin_mode():
    #This feature lets the user access admin mode specifically for employees or restockers for Ni's Vending Machine
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

def suggest_item(items, purchased_item): 
#Reference: https://github.com/python/cpython/blob/3.13/Lib/random.py

    """Suggests a random item from the same category."""
    same_category_items = [
        item for item in items 
        if item['category'] == purchased_item['category'] and item != purchased_item and item['stock'] > 0
    ]
    if same_category_items:
        suggestion = random.choice(same_category_items)
        print(f"Suggestion: How about trying {suggestion['name']} for AED {suggestion['price']:.2f}?")

def vending_machine():
    #This is the main Vending Machine Program

     # Seperates each snacks and drinks to specific categories.
    categories = list(set(item['category'] for item in items))

    print("Welcome to the Ni's Vending Machine!")
    while True:
        print ("\n1. Browse Items")
        print ("2. Check your current Gelo Points")
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
                    if not use_Gelo_points(selected_items):
                        insert_money(selected_items)

                    # This will suggest another item
                    suggest_item(items, selected_items)

            elif main_choice == 2:

                #if the user picks 2, it will allow the user to view their current yum points
                print (f"You currently have: {Gelo_points['user']}")

            elif main_choice == 3:

                #This will let the user be able to access admin mode 
                admin_mode()
            
            elif main_choice == 0:
                print ("Thank you for using the Ni's Vending Machine, Have a good day!")
                
                break
            
            else:
                print ("Invalid Choice, Please try again...")
        except ValueError:
            print ("Invalid User Input, Please enter a number that is valid from above")


# Run the program
vending_machine()

#Updated Display of the Program
""" Welcome to the Ni's Vending Machine!

1. Browse Items
2. Check your current Gelo Points
3. Admin Mode (For Restockers)
0. Exit
Choose an option: 2
You currently have: 0

1. Browse Items
2. Check your current Gelo Points
3. Admin Mode (For Restockers)   
0. Exit
Choose an option: 1

--- Available Categories ---      
1. Snacks
2. Drinks
3. Hot Drinks
0. Exit

Enter the category number to see: 1

--- Items in Snacks ---
+-----+----------------------------------+-----------+---------+
|   # | Item                             | Price     |   Stock |
+=====+==================================+===========+=========+
|   1 | Ni Chips                         | AED 4.00  |      12 |
+-----+----------------------------------+-----------+---------+
|   2 | SNI'sker Chocolate Bar           | AED 6.00  |      10 |
+-----+----------------------------------+-----------+---------+
|   3 | Ai nd Ni's Crunchy Milk Biscuits | AED 7.00  |       8 |
+-----+----------------------------------+-----------+---------+
|   4 | Gelo's Footlong Cookies          | AED 8.50  |       6 |
+-----+----------------------------------+-----------+---------+
|   5 | Ai's Protein Bar                 | AED 5.50  |       9 |
+-----+----------------------------------+-----------+---------+
|   6 | Ni's Sandwich (NO KETCHUP)       | AED 15.00 |       3 |
+-----+----------------------------------+-----------+---------+

0. Go Back
Enter the item number to purchase: 6
Not enough points. You need 15 more points to buy this item.
Insert money to buy Ni's Sandwich (NO KETCHUP) (AED 15.0): 50
Dispensing Ni's Sandwich (NO KETCHUP)... Enjoy!
Your change is AED 35.00.
You earned 6 Gelo points. Total points: 6.
Suggestion: How about trying Gelo's Footlong Cookies for AED 8.50?

1. Browse Items
2. Check your current Gelo Points
3. Admin Mode (For Restockers)
0. Exit
Choose an option: 2
You currently have: 6

1. Browse Items
2. Check your current Gelo Points
3. Admin Mode (For Restockers)
0. Exit
Choose an option: 3
Enter Password: admin123@

--- Admin Mode ---

1. View Item Stock
2. Restock Items
3. Exit Admin Mode
Enter your choice: 3
Exiting Admin Mode.

1. Browse Items
2. Check your current Gelo Points
3. Admin Mode (For Restockers)
0. Exit
Choose an option: 1

--- Available Categories ---
1. Snacks
2. Drinks
3. Hot Drinks
0. Exit

Enter the category number to see: 2

--- Items in Drinks ---
+-----+---------------------------+-----------+---------+
|   # | Item                      | Price     |   Stock |
+=====+===========================+===========+=========+
|   1 | Gelo's Coke               | AED 5.00  |      10 |
+-----+---------------------------+-----------+---------+
|   2 | Kapoipoi's Pepsi          | AED 5.00  |       8 |
+-----+---------------------------+-----------+---------+
|   3 | Nyang's Water with ice    | AED 3.00  |      15 |
+-----+---------------------------+-----------+---------+
|   4 | CooCoo's Orange Juice     | AED 6.50  |       7 |
+-----+---------------------------+-----------+---------+
|   5 | Nyang's Extra Iced Coffee | AED 10.00 |       5 |
+-----+---------------------------+-----------+---------+
|   6 | Ibi Energy Drink          | AED 12.00 |       4 |
+-----+---------------------------+-----------+---------+

0. Go Back
Enter the item number to purchase: 6
Not enough points. You need 6 more points to buy this item.
Insert money to buy Ibi Energy Drink (AED 12.0): 35
Dispensing Ibi Energy Drink... Enjoy!
Your change is AED 23.00.
You earned 4 Gelo points. Total points: 10.
Suggestion: How about trying CooCoo's Orange Juice for AED 6.50?

1. Browse Items
2. Check your current Gelo Points
3. Admin Mode (For Restockers)
0. Exit
Choose an option: 1

--- Available Categories ---
1. Snacks
2. Drinks
3. Hot Drinks
0. Exit

Enter the category number to see: 3

--- Items in Hot Drinks ---
+-----+------------------------+----------+---------+
|   # | Item                   | Price    |   Stock |
+=====+========================+==========+=========+
|   1 | Mapoipoi Tea           | AED 4.00 |      10 |
+-----+------------------------+----------+---------+
|   2 | Ai's Iced Mocha Coffee | AED 7.50 |       8 |
+-----+------------------------+----------+---------+
|   3 | Hot Ni Chocolate       | AED 9.00 |       5 |
+-----+------------------------+----------+---------+

0. Go Back
Enter the item number to purchase: 3
You can use 9 Gelo points to purchase Hot Ni Chocolate.
Would you like to use your Gelo points? (yes/no): yes
Dispensing Hot Ni Chocolate... Enjoy!
Points deducted. Your remaining points: 1.
Suggestion: How about trying Ai's Iced Mocha Coffee for AED 7.50?

1. Browse Items
2. Check your current Gelo Points
3. Admin Mode (For Restockers)
0. Exit
Choose an option: 0
Thank you for using the Ni's Vending Machine, Have a good day!
"""