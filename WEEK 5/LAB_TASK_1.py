"""
    PROGRAM WHICH IS TO GET USER INFORMATION
    AUTHOR : VRAJ PRAJAPATI
"""

def collect_user_data(id_counter):
    
    print(f"Enter the User Information")
    name = input("Enter the User name : ")
    age = int(input("Enter the User age : "))
    Email = input("Enter the User Email : ")
    
    u_id = id_counter + 1
    id_counter = u_id
    
    print(f"User Information")
    print(f"Name : {name}")
    print(f"Age : {age}")
    print(f"Email Address : {Email}")
    print(f"Unique ID : {u_id}")
    

def main():
    id_counter = 5000
    collect_user_data(id_counter)
main()
    
    
    