"""
TASK 4:
PROGRAM WHICH IS DISPLAY ALL THE DETAILS BY TASK 1 2 3
AUTHOR : VRAJ PRAJAPATI
"""

def customer_booking(id_counter):
    print("Gathering Information")
    form_id = input("Enter form of ID (Passport or Driver's License): ")
    id_number = input("Enter the ID number: ")
    name = input("Enter the passenger name: ")
    ticket_id = id_counter + 1
    id_counter = ticket_id
    return id_counter, ticket_id, id_number, form_id, name


def ferry_service_total():
    services_list = []
    total_cost = 0

    while True:
        name = input("Enter the service name (or 'done' to end): ")
        if name.lower() == 'done':
            break
        try:
            price = int(input("Enter the price: $"))
            services_list.append((name, price))
            total_cost += price
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    return services_list, total_cost


def booking_approval(total_cost, ticket_id, id_number):
    if total_cost > 0:
        status = "Approved"
    else:
        status = "Pending"

    # Generate the approval reference number
    a_number = id_number[0:3] + str(ticket_id)[-2:]
    ref_num = a_number

    return status, ref_num


def display_booking():
    id_counter = 20000
    id_counter, ticket_id, id_number, form_id, name = customer_booking(id_counter)
    services_list, total_cost = ferry_service_total()
    status, ref_num = booking_approval(total_cost, ticket_id, id_number)

    # Display the results
    print(f"Printing Booking")
    print(f"Form of ID (Passport or Driver's License): {form_id}")
    print(f"ID Number: {id_number}")
    print(f"Passenger Name: {name}")
    print(f"Ticket ID: {ticket_id}")
    print(f"Total: ${total_cost}")
    print(f"Status: {status}")
    print(f"Approval Reference Number: {ref_num}")

    # Print the services list
    print("Services:")
    for service, price in services_list:
        print(f"  {service}: ${price}")


def main():
    display_booking()


if __name__ == "__main__":
    main()