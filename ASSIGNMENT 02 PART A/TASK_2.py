"""
TASK 2:
PROGRAM WHICH IS GENERATE THE TOTAL COST OF THE SERVICE REQUESTED BY THE CUSTOMER.
AUTHOR : VRAJ PRAJAPATI
"""

def ferry_service_total():
    services_list = []   #empty service items
    total_cost = 0       #starting from value of 0 
    
    while  True:
        name = input("Enter the Service name ( or 'done' to end ): ")
        if name.lower() == 'done':  # condition of the end for user list
            break
        try:
            price = int(input("Enter the price : $"))
            services_list.append((name, price))
            total_cost += price
        except ValueError:        # cannot accept other values
            print("Invalid Input.Please enter the numeric value.....!")
            
    return services_list, total_cost

# main function
def main():
    services_list, total_cost = ferry_service_total()
    print("\nServices List")
    if not services_list:
        print("No Services in the list")
    for name, price in services_list:
        print(f"{name} : ${price}")     # output
    print(f"Total Cost : ${total_cost}") # total cost of all services
main()
        
                

    
    
    