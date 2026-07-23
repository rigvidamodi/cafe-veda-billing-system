# Define the menu of restaurant
menu = {
    'Veda Signature Latte': 249,
    'Cheese Croissant': 249,
    'Pink Sauce Pasta': 349,
    'Blueberry Cheesecake': 289,
    'Strawberry Mojito': 189,
    'Spanish Latte': 259,
    'Date Delight Combo (Veda Signature Latte + Blueberry Cheesecake)': 449,
    'Study Break Combo (Spanish Latte + Cheese Croissant)': 449,
    'Pasta & Sip Combo (Pink Sauce Pasta + Strawberry Mojito)': 449,
    'Besties Combo (Pink Sauce Pasta + 2 Strawberry Mojitos)': 669
}

# Greet
print("********** WELCOME TO CAFÉ VÈDA **********")
print("------------------------------------------")

for item, price in menu.items():
    print(f"{item} : ₹{price}")

print("------------------------------------------")

order_total = 0
ordered_items = []

# First Order
item_1 = input("Enter the name of item you want to order: ")

if item_1 in menu:
    order_total += menu[item_1]
    ordered_items.append(item_1)
    print(f"{item_1} has been added to your order.")
else:
    print(f"Ordered item '{item_1}' is not available.")

# Second Order
another_order = input("Do you want to add another item? (Yes/No): ").lower()

if another_order == "yes":
    item_2 = input("Enter the name of second item you want to order: ")

    if item_2 in menu:
        order_total += menu[item_2]
        ordered_items.append(item_2)
        print(f"{item_2} has been added to your order.")
    else:
        print(f"Ordered item '{item_2}' is not available.")

# Final Bill
print("\n========== FINAL BILL ==========")

for item in ordered_items:
    print(f"{item:<55} ₹{menu[item]}")

print("--------------------------------")
print(f"Total Amount to Pay : ₹{order_total}")
print("Thank You for Visiting Café Vèda!")
