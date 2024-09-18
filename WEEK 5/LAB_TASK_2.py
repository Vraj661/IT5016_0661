"""
PROGRAM WHICH IS TO INPUT ITEM PRICES AND CALCULATE TOTAL AMOUNT.
AUTHOR : VRAJ PRAJAPATI
"""

def calculate_total_amount():
    items_list = []
    total_price = 0.0
    
    while True:
        item_input = input("Enter item name and price (e.g., 'Apple $1.99') or 'finish' to end: ").strip()
        if item_input.lower() == 'finish':
            break
        try:
            item_name, item_price = item_input.split('$')
            item_name = item_name.strip()
            item_price = float(item_price.strip())
            items_list.append((item_name, item_price))
            total_price += item_price
        except ValueError:
            print("Invalid Input. Please enter the item name and price separated by '$'")
            
    return total_price, items_list

def main():
    total_price, items_list = calculate_total_amount()
    print("\nItems List:")
    if not items_list:
        print("No items added.")
    for item_name, item_price in items_list:
        print(f"{item_name}: ${item_price:.2f}")
    print(f"Total Price : ${total_price:.2f}")
    
main()