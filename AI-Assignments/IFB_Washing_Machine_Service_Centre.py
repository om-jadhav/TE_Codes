# IFB Washing Machine Service Centre Chatbot

print("========================================")
print(" Welcome to IFB Service Centre Chatbot")
print("========================================")

while True:

    print("\n--------- MENU ---------")
    print("1. Register Complaint")
    print("2. Service Request Status")
    print("3. Washing Machine Price")
    print("4. Service Charges")
    print("5. Customer Support")
    print("6. Exit")

    choice = input("Enter your choice: ")

    # Register Complaint
    if choice == '1':

        name = input("Enter Customer Name: ")
        model = input("Enter Washing Machine Model: ")
        issue = input("Enter Problem: ")

        print("\nComplaint Registered Successfully")
        print("Customer Name :", name)
        print("Model :", model)
        print("Issue :", issue)

    # Service Status
    elif choice == '2':

        request_id = input("Enter Service Request ID: ")

        print("Service Status: Technician Assigned")

    # Washing Machine Price
    elif choice == '3':

        model = input("Enter Washing Machine Model: ")

        print("Price of", model, "is Rs. 25,000")

    # Service Charges
    elif choice == '4':

        print("\nService Charges")
        print("Inspection Charge : Rs. 300")
        print("Repair Charge : Rs. 800")

    # Customer Support
    elif choice == '5':

        print("\nCustomer Care Number : 1800-3000-5678")
        print("Email : support@ifbservice.com")

    # Exit
    elif choice == '6':

        print("\nThank You for using IFB Chatbot")
        break

    # Invalid Choice
    else:

        print("Invalid Choice")