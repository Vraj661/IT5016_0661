"""
TASK 1
PROGRAM WHICH IS GENERATE THE SOFTWARE SYSTEM ABOUT THE BOOKINGS
AUTHOR : VRAJ PRAJAPATI
"""
# CREATE THE CLASS    
class BookingSystem:
    id_counter = 20000  # to generate unique booking IDs
    ticket_id_counter = 0  # to generate unique ticket IDs

# DEFINE THE INIT FUNCTION 
    def __init__(self, name):
        self.id = BookingSystem.id_counter
        BookingSystem.id_counter += 1 
        BookingSystem.ticket_id_counter += 1
        self.ticket_id = BookingSystem.ticket_id_counter
        self.name = name
        self.service_requests = [] # EMPTY LISTS
        self.approval_ref = None  
        
# FIRST METHOD 
    def customer_info(self, name):
        self.name = name
# SECOND METHOD
    def ferry_service_details(self, service_name, price):
        self.service_requests.append({"service_name": service_name, "price": price})
# THIRD METHOD
    def booking_approval(self, approval_status):
        if approval_status.lower() == "approved":
            self.status = "approved"
        elif approval_status.lower() == "not approved":
            self.status = "not approved"
        else:
            print("pending")
        
        # generate the approval refference number 
        self.approval_ref = f"{self.id[0:3]}{self.ticket_id}"
# FOURTH METHOD WHICH IS DISPLAYING THE DETAILS
    def display_booking_info(self):
        print("Printing Booking : ")
        print(f"ID Number: {self.id}")
        print(f"Passenger Name: {self.name}")
        total_cost = sum(request["price"] for request in self.service_requests)
        print(f"Ticket ID: {self.ticket_id}")
        print(f"Total: {total_cost}")
        print(f"Status: {self.status}")
        print(f"Approval Reference Number: {self.approval_ref}")

# FIFTH METHOD TO THE CONTAIN INFORMATION    
    def booking_statistic(cls, bookings):
        total_bookings = len(bookings)
        total_pending = sum(1 for booking in bookings if booking.status == "pending")
        total_not_approved = sum(1 for booking in bookings if booking.status == "not approved")
        total_approved = sum(1 for booking in bookings if booking.status == "approved")
        return {
            "Total number of Bookings submitted": total_bookings,
            "Total number of Approved Bookings": total_approved,
            "Total number of Pending Bookings": total_pending,
            "Total number of Not approved Bookings": total_not_approved,
        }
# MAIN FUNCTION
def main():
    bookings = []
    while True:
        print("1. Submit Request")
        print("2. Respond to Request")
        print("3. Display Requests")
        print("4. Request Statistics")
        print("5. Exit")
        # give the number from upper operation which you want.
        choice = input("Enter your choice: ")

        if choice == "1":
            form = input("Enter between (Passport and Driver's License): ")
            Id = input("Enter the ID NUMBER: ")
            Name = input("Enter the Passenger name: ")
            items = []
            while True:
                item_name = input("Enter item name (or 'done' to finish): ")
                if item_name.lower() == "done":
                    break
                item_cost = int(input("Enter item cost: "))  # stores the only integer values
                items.append({"name": item_name, "cost": item_cost})
                
            booking_system = BookingSystem(Name)
            for item in items:
                booking_system.ferry_service_details(item["name"], item["cost"])
            booking_system.approval_ref = None  
            bookings.append(booking_system)
            print("Request submitted successfully!")
        
        
        elif choice == "2":
            request_id = int(input("Enter request ID: "))
            for booking in bookings:
                if booking.id == request_id:
                    status = input("Enter response (approved/not approved): ")
                    booking.booking_approval(status)
                    print("Request responded successfully!")
                    break
            else:
                print("Request ID not found, Please Try again")
            
        elif choice == "3":
            for booking in bookings:
                booking.display_booking_info()
                print()
            
        elif choice == "4":
            BookingSystem.booking_statistic(bookings)
            
        elif choice == "5":
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
    
