"""
TASK 3:
PROGRAM WHICH IS GENERATE STATUS BY PREVIOUS TASK 2 AND GENERATE THE APPROVAL REFERENCE NUMBER
AUTHOR : VRAJ PRAJAPATI
"""
# TASK 1: Customer Booking
def customer_booking(id_counter):

    print("Gathering Information")
    id_number = input("Enter the ID NUMBER: ")
    # Generate the unique ID
    ticket_id = id_counter + 1
    id_counter = ticket_id
    
    return id_counter, ticket_id, id_number

# TASK 2: Ferry Service Total
def ferry_service_total():
 
    services_list = []  # Empty service items
    total_cost = 0  # Starting from value of 0
    
    while True:
        name = input("Enter the Service name (or 'done' to end): ")
        if name.lower() == 'done':  # Condition to end user input
            break
        try:
            price = int(input("Enter the price: $"))
            services_list.append((name, price))
            total_cost += price
        except ValueError:  # Handle non-numeric input
            print("Invalid Input. Please enter a numeric value.")
            
    return services_list, total_cost

# TASK 3 LOGIC: Booking Approval
def booking_approval(total_cost, ticket_id, id_number):
   
    if total_cost > 0:
        status = "Approved"
    else:
        status = "Pending"
        
    # Generate the approval reference number    
    a_number = id_number[0:3] + str(ticket_id)[-2:]
    ref_num = a_number
    
    return status, ref_num

# MAIN Function
def main():
    id_counter = 20000
    id_counter, ticket_id, id_number = customer_booking(id_counter)
    services_list, total_cost = ferry_service_total()
    status, ref_num = booking_approval(total_cost, ticket_id, id_number)
    
    # Display the output
    print(f"Total: ${total_cost}")
    print(f"Status: {status}")
    print(f"Approval Reference Number: {ref_num}")
    
    # Print the services list
    print("Services:")
    for service, price in services_list:
        print(f"  {service}: ${price}")

if __name__ == "__main__":
    main()