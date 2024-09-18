"""
Program which calculate Grocerie bill
Author = Vraj Prajapati
"""
# item01=30
# item02=20
# item03=10

item1=float(input("Enter the price for item1:-"))
item2=float(input("Enter the price for item2:-"))
item3=float(input("Enter the price for item3:-"))
sub_total = item1 + item2 + item3
sales_tax= sub_total* 0.15
calculate_total= sub_total + sales_tax

print("Calculates_total",calculate_total)
