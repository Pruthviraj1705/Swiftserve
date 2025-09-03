import os
import json
from datetime import datetime

# -------------------------------------------------------
# SwiftServe - Hotel Management System (Beginner Friendly)
# Author: Pruthviraj Vitthal Jagtap (PJ1712)
# Description:
#   Menu → Order → Bill flow for a hotel/restaurant.
#   Now supports multiple orders per customer session!
# -------------------------------------------------------

# ====== CONFIGURABLE CONSTANTS ======
GST_RATE = 0.05                  # 5% GST
PACKING_CHARGE_PER_ITEM = 10     # ₹10 per item (only for Parcel orders)

# ====== FOLDER SETUP ======
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
RECEIPTS_DIR = os.path.join(BASE_DIR, "receipts")

# Create folders if they don't exist
os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(RECEIPTS_DIR, exist_ok=True)

# ====== MENU ======
MENU_FILE = os.path.join(DATA_DIR, "menu.json")

# Default menu if menu.json does not exist
default_menu = {
    1: ["Tea", 15],
    2: ["Coffee", 25],
    3: ["Cold Drink", 40],
    4: ["Poha", 30],
    5: ["Upma", 35],
    6: ["Sandwich", 50],
    7: ["Burger", 80],
    8: ["French Fries", 70],
    9: ["Pizza", 250],
    10: ["Veg Thali", 120],
    11: ["Non-Veg Thali", 180],
    12: ["Biryani", 150],
    13: ["Paneer Butter Masala", 220],
    14: ["Chicken Curry", 240],
    15: ["Roti", 12],
    16: ["Paratha", 25],
    17: ["Idli Sambar", 50],
    18: ["Masala Dosa", 70],
    19: ["Ice Cream", 60],
    20: ["Gulab Jamun", 30]
}

# Create menu.json if not present
if not os.path.exists(MENU_FILE):
    with open(MENU_FILE, "w", encoding="utf-8") as f:
        json.dump(default_menu, f, indent=4, ensure_ascii=False)

# Load menu
with open(MENU_FILE, "r", encoding="utf-8") as f:
    menu = {int(k): v for k, v in json.load(f).items()}

# ====== UTIL FUNCTIONS ======
def line(width=48, ch='-'):
    return ch * width

def show_menu():
    print("\n" + line())
    print("                SWIFTSERVE MENU")
    print(line())
    print(f"{'No.':<5}{'Item':<24}{'Price (₹)':>10}")
    print(line())
    for k, v in menu.items():
        name, price = v
        print(f"{k:<5}{name:<24}{price:>10}")
    print(line())

def get_order_type():
    while True:
        print("\nSelect Order Type:")
        print("1) Dine-In")
        print("2) Parcel (Takeaway)")
        choice = input("Enter 1 or 2: ").strip()
        if choice == '1':
            return "DINE-IN"
        if choice == '2':
            return "PARCEL"
        print("Invalid choice. Please enter 1 or 2.")

def get_integer(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

def take_orders():
    orders = []
    subtotal = 0
    items_count = 0

    while True:
        show_menu()
        choice = get_integer("Enter item number to order (0 to finish): ")

        if choice == 0:
            break

        if choice not in menu:
            print("Invalid item number. Please choose from the menu.")
            continue

        item_name, unit_price = menu[choice]
        qty = get_integer(f"Enter quantity for {item_name}: ")

        if qty <= 0:
            print("Quantity must be at least 1.")
            continue

        line_total = unit_price * qty
        orders.append({
            "name": item_name,
            "qty": qty,
            "unit_price": unit_price,
            "line_total": line_total
        })
        subtotal += line_total
        items_count += qty

        print(f"Added: {qty} x {item_name} → ₹{line_total}")
        print(f"Current Subtotal: ₹{subtotal}")

    return orders, items_count, subtotal

def calculate_totals(order_type, subtotal, items_count):
    gst_amount = round(subtotal * GST_RATE, 2)
    packing = PACKING_CHARGE_PER_ITEM * items_count if order_type == "PARCEL" else 0
    grand_total = round(subtotal + gst_amount + packing, 2)
    return {
        "subtotal": subtotal,
        "gst_rate": GST_RATE,
        "gst_amount": gst_amount,
        "packing_per_item": PACKING_CHARGE_PER_ITEM if order_type == "PARCEL" else 0,
        "packing_total": packing,
        "grand_total": grand_total
    }

def print_bill(project_name, customer_name, order_type, orders, totals, order_number):
    print("\n" + line())
    print(f"         {project_name} - FINAL BILL (Order #{order_number})")
    print(line())
    print(f"Customer : {customer_name}")
    print(f"Order    : {order_type}")
    print(line())
    print(f"{'Item':<22}{'Qty':>5}{'Rate':>9}{'Amount':>12}")
    print(line())

    for it in orders:
        print(f"{it['name']:<22}{it['qty']:>5}{it['unit_price']:>9}{it['line_total']:>12}")

    print(line())
    print(f"{'Subtotal:':<34}{'₹':>2}{totals['subtotal']:>10.2f}")
    print(f"GST @ {int(totals['gst_rate']*100)}%:{'':<24}{'₹':>2}{totals['gst_amount']:>10.2f}")

    if totals['packing_total'] > 0:
        print(f"Packing (₹{totals['packing_per_item']}/item):{'':<11}{'₹':>2}{totals['packing_total']:>10.2f}")

    print(line())
    print(f"{'GRAND TOTAL:':<34}{'₹':>2}{totals['grand_total']:>10.2f}")
    print(line())
    print("Thank you for choosing SwiftServe! Enjoy your meal.")
    print("© 2025 PJ1712 - All Rights Reserved")
    print(line())

    # Save bill to receipts folder
    safe_name = customer_name.strip() or "Guest"
    filename = f"{safe_name.replace(' ', '_')}_Order{order_number}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    filepath = os.path.join(RECEIPTS_DIR, filename)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(f"{project_name} - BILL (Order #{order_number})\n")
        f.write(line() + "\n")
        f.write(f"Customer: {customer_name}\n")
        f.write(f"Order Type: {order_type}\n")
        f.write(line() + "\n")
        for it in orders:
            f.write(f"{it['name']} x {it['qty']} = ₹{it['line_total']}\n")
        f.write(line() + "\n")
        f.write(f"Subtotal: ₹{totals['subtotal']}\n")
        f.write(f"GST: ₹{totals['gst_amount']}\n")
        if totals['packing_total'] > 0:
            f.write(f"Packing Charges: ₹{totals['packing_total']}\n")
        f.write(f"Grand Total: ₹{totals['grand_total']}\n")

    print(f"\nBill saved to: {filepath}")

# ====== MAIN PROGRAM ======
def main():
    print("===== Welcome to SwiftServe - Hotel Management System =====\n")
    customer_name = input("Enter Customer Name: ").strip() or "Guest"

    order_number = 1  # track how many orders this customer has placed

    while True:
        order_type = get_order_type()
        orders, items_count, subtotal = take_orders()

        if not orders:
            print("\nNo items ordered. Skipping bill...")
        else:
            totals = calculate_totals(order_type, subtotal, items_count)
            print_bill("SwiftServe", customer_name, order_type, orders, totals, order_number)
            order_number += 1

        # Ask if they want to place another order
        again = input("\nWould you like to place another order? (y/n): ").strip().lower()
        if again != 'y':
            print("\nThank you for visiting SwiftServe! Have a great day!")
            break

if __name__ == "__main__":
    main()
