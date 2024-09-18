"""
    PROGRAM WHICH IS DETAILS OF REQUEST SYSTEM 
    AUTHOR : VRAJ PRAJAPATI
"""
class RequestSystem:
    def __init__(self):
        self.requests = []
        self.unique_id_counter = 10000

    def user_info(self):
        user_name = input("Enter your name: ")
        user_age = int(input("Enter your age: "))
        user_email = input("Enter your email: ")
        return user_name, user_age, user_email

    def request_details(self):
        items = []
        total_amount = 0
        while True:
            item_name = input("Enter item name (or 'done' to finish): ")
            if item_name.lower() == 'done':
                break
            item_cost = float(input("Enter item cost: "))
            items.append((item_name, item_cost))
            total_amount += item_cost
        return items, total_amount

    def request_approval(self, items, total_amount):
        if total_amount < 150:
            status = "approved"
        else:
            status = "pending"
        self.requests.append({
            "unique_id": self.unique_id_counter,
            "user_name": self.user_name,
            "total_amount": total_amount,
            "items": items,
            "status": status,
            "approval_reference_number": None
        })
        self.unique_id_counter += 1

    def respond_request(self):
        for i, request in enumerate(self.requests):
            if request["status"] == "pending":
                print(f"Request {i+1}: {request['unique_id']}, {request['user_name']}, {request['total_amount']}")
                response = input("Approve or Reject (A/R)? ").upper()
                if response == "A":
                    request["status"] = "approved"
                    request["approval_reference_number"] = input("Enter approval reference number: ")
                elif response == "R":
                    request["status"] = "not approved"

    def display_request(self):
        for request in self.requests:
            print("-"*20)
            print(f"Detailed Report:")
            print(f"User Name: {request['user_name']}")
            print(f"Unique ID: {request['unique_id']}")
            print(f"Total Amount: ${request['total_amount']:.2f}")
            print(f"Category: {request['status']}")
            if request["approval_reference_number"]:
                print(f"Approval Reference Number: {request['approval_reference_number']}")
            print("Request Items:")
            for item_name, item_cost in request["items"]:
                print(f"{item_name}: ${item_cost:.2f}")

    def request_statistic(self):
        approved_count = 0
        pending_count = 0
        not_approved_count = 0
        for request in self.requests:
            if request["status"] == "approved":
                approved_count += 1
            elif request["status"] == "pending":
                pending_count += 1
            else:
                not_approved_count += 1
        print("-"*20)
        print("Statistical Summary:")
        print(f"Total number of requests submitted: {len(self.requests)}")
        print(f"Total number of approved requests: {approved_count}")
        print(f"Total number of pending requests: {pending_count}")
        print(f"Total number of not approved requests: {not_approved_count}")

system = RequestSystem()
system.user_name, system.user_age, system.user_email = system.user_info()
items, total_amount = system.request_details()
system.request_approval(items, total_amount)
system.respond_request()
system.display_request()
system.request_statistic()