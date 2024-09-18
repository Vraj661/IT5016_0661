"""
TASK 1:
PROGRAM WHICH IS GENERATE THE UNIQUE ID.
AUTHOR : VRAJ PRAJAPATI
"""

def CustumerBooking(id_counter):
    # get the information from the user
    print("Gathering Information")
    Form_id = input("Enter between ( Passport and Driver's Licenece ): ")
    Id_number = input("Enter the ID NUMBER : ")
    Name = input("Enter the Passenger name ")
    # generate the unique id 
    Ticket_id = id_counter + 1
    id_counter = Ticket_id
    # for the printing all details as on the paper
    print("\nPrinting Booking Information : ")
    print(f"Form of ID(Passport, Driver's Licenece): {Form_id}")
    print(f"ID Number : {Id_number}")
    print(f"Passenger Name : {Name}")
    print(f"Ticket ID : {Ticket_id}")
# main function which is starting part of code  
def main():
    id_counter = 20000
    CustumerBooking(id_counter)
main()
# end of the code