'''
PROGRAM WHICH IS SHOPPING LIST
NAME VRAJ PRAJAPATI
'''
def shopping_list():

  total_cost = 0
  shopping_list = {}

    
  while True:
    item_name = input("Enter the name of the item (or type 'done' to finish): ")
    if item_name == "done":
      break

    item_price = float(input(f"Enter the price of '{item_name}': "))
    shopping_list[item_name] = item_price
    total_cost += item_price

  print("\nShopping List:")
  for item, price in shopping_list.items():
    print(f"{item}: ${price:.2f}")

  print(f"\nTotal Price: ${total_cost:.2f}")

shopping_list()

