# IT5016_0661

def customer_booking(id_counter):
    print("Gathering Information")
    passengers = []
    while True:
        form_id = input("Enter form of ID (Passport or Driver's License) for passenger {}: ".format(len(passengers) + 1))
        id_number = input("Enter the ID number for passenger {}: ".format(len(passengers) + 1))
        name = input("Enter the passenger name for passenger {}: ".format(len(passengers) + 1)) #The format() method formats the specified value(s) and insert them inside the string's placeholder.
        ticket_id = id_counter + 1
        id_counter = ticket_id
        passengers.append((ticket_id, id_number, form_id, name))
        response = input("Add another passenger? (yes/no): ") # if the user want add another passenger details then ..
        if response.lower() != 'yes':
            break 
    return id_counter, passengers


def ferry_service_total():
    services_list = [] # stores empty list
    total_cost = 0   # start with 0 value

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


def booking_approval(total_cost, passengers):
    if total_cost > 0:
        status = "Approved"
    else:
        status = "Pending"

    # Generate the approval reference number
    ref_num = ""
    for passenger in passengers:
        ref_num += passenger[1][0:3] + str(passenger[0])[-2:]
    ref_num = ref_num

    return status, ref_num


def display_booking(passengers, services_list, total_cost, status, ref_num):
    # Display the results
    print(f"Printing Booking")
    for passenger in passengers:
        print(f"Form of ID (Passport or Driver's License) for passenger {passengers.index(passenger) + 1}: {passenger[2]}")
        print(f"ID Number for passenger {passengers.index(passenger) + 1}: {passenger[1]}")
        print(f"Passenger Name for passenger {passengers.index(passenger) + 1}: {passenger[3]}")
        print(f"Ticket ID for passenger {passengers.index(passenger) + 1}: {passenger[0]}")
    print(f"Total: ${total_cost}")
    print(f"Status: {status}")
    print(f"Approval Reference Number: {ref_num}")

    # Print the services list
    print("Services:")
    for service, price in services_list:
        print(f"  {service}: ${price}")


def main():
    id_counter = 20000
    id_counter, passengers = customer_booking(id_counter)
    services_list, total_cost = ferry_service_total()
    status, ref_num = booking_approval(total_cost, passengers)
    display_booking(passengers, services_list, total_cost, status, ref_num)


if __name__ == "__main__":
    main()
    
    
# Index :- It returns the position of the first occurrence of that element in the list. If the item is not found in the list, index() function raises a “ValueError” error.

"""
AUTHOR : VRAJ PRAJAPATI
"""

PROGRAM WHICH CREATE ABOUT THE PASSENGER DETAILS AND ITEMS LIST WITH TOTAL PRICE.

IN THE PROGRAM, FIRST EXECUTE THE PASSENGER DEATAILS, AFTER THAT IF USER WANTS ADD ONE PASSENGER DETAILS THEN TYPE 'YES' 
THEN ADD TO DETAILS ABOUT THE PASSENGER DETAILS.

SOFTWARE DESIGN PRINCILES:

- Software design is the process of organizing or modifying software requirements into the actions required to build a software system. 
- The elements of software design are arranged and structured according to a number of principles.
- Developing software systems that are simple to use, maintain, and alter is the primary objective of software design.

PRINCIPLES :
1. SOC ( Separation of Concerns )
2. KISS ( Keep it Simple and Stupid )
3. YAGNI ( You Ain't Gonna Need It )
4. DRY ( Don't Repeat Yourself )
5. SRP ( Single Responsibility Principle )
6. CQS (Command-Query Separation )
7. OCP ( Open-Closed Principle )


1.SOC :-

customer_booking: handles customer information gathering
ferry_service_total: handles service selection and total cost calculation
booking_approval: determines the booking status and generates an approval reference number
display_booking: displays the booking details
main: Operate the entire process

2.KISS :-

The program is simple and easy to understand.The program is easy to use.The program is easy to modify.

3.YAGNI :-

The code does not include unnecessary features or complexity.

4.DRY :-

The code avoids duplicated logic by using functions to perform repetitive tasks.

5.SRP :-

The code follows the Single Responsibility Principle by separating the concerns of each function.
customer_booking only gathers customer information and does not perform any calculations or display any results.
ferry_service_total only calculates the total cost and does not gather any information or display any results.
booking_approval only determines the booking status and generates an approval reference number and does not gather any information or display any results.

6.CQS :-

The code follows the Command-Query Separation principle by separating the concerns of each function.
customer_booking modifies the id_counter and passengers variables, while display_booking only displays information without modifying any state.

7.OCP :-

The code follows the Open-Closed Principle by allowing new types of ferries to be added without modifying the existing code.


SOLID :- 

S - Single Responsibility Principle (SRP)
O - Open-Closed Principle (OCP)
L - Liskov Substitution Principle (LSP)
I - Interface Segregation Principle (ISP)
D - Dependency Inversion Principle (DIP)

SRP :- 

customer_booking is responsible for gathering passenger information, ferry_service_total handles service selection and pricing, and booking_approval determines the booking status.


OCP :-

we can simply add a new input option in ferry_service_total without modifying the existing code.
if we want to add a new type of ferry service, we can create a new function that calculates the cost of that service without modifying the existing ferry_service_total function.

LSP :-

booking_approval takes the total cost and passenger list as inputs, without knowing how they were generated.


ISP :-

we can add new methods to the interface without affecting the existing code.display_booking takes five inputs (passengers, services list, total cost, status, and ref num) and displays the booking information in a structured format.
the customer_booking function provides a service to gather passenger information, and the ferry_service_total function provides a service to calculate the total cost of ferry services.

DIP :-

we can easily switch to a different payment method without modifying the existing code.
booking_approval depends on the output of ferry_service_total and customer_booking.
