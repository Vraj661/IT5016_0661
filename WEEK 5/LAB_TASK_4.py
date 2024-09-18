"""
    PROGRAM WHICH IS Detailed Report
    author : Vraj Prajapati
"""
def create_detailed_report(id_counter):
    print(f"Enter the User Information")
    name = input("Enter the User name: ")
    age = int(input("Enter the User age: "))
    email = input("Enter the User Email: ")

    u_id = id_counter + 1
    id_counter = u_id

    print(f"User Information")
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Email Address: {email}")
    print(f"Unique ID: {u_id}")

    return u_id, name, age, email

def calculate_total_amount():
    items_list = []
    total_price = 0

    while True:
        item_name = input("Enter item name (or 'finish' to end): ")
        if item_name.lower() == 'finish':
            break
        try:
            item_price = float(input("Enter item price: $"))
            items_list.append((item_name, item_price))
            total_price += item_price
        except ValueError:
            print("Invalid Input. Please enter a numeric value")

    return total_price, items_list

def categorize_request(total_price):
    if total_price < 150:
        category = "Low"
        recommendation = "Proceed with standard processing."
    else:
        category = "High"
        recommendation = "Review for potential discounts."

    return category, recommendation

def main():
    id_counter = 5000
    u_id, name, age, email = create_detailed_report(id_counter)
    total_price, items_list = calculate_total_amount()
    category, recommendation = categorize_request(total_price)

    print(f"Detailed Report:")
    print(f"Unique ID: {u_id}")
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Email Address: {email}")
    print(f"Total Amount: ${total_price:.2f}")
    print(f"Category: {category}")
    print(f"Recommendation: {recommendation}")

if __name__ == "__main__":
    main()