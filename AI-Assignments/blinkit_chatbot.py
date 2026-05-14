# Blinkit Chatbot

print("================================")
print("   Welcome to Blinkit Chatbot")
print("================================")

while True:

    print("\n------ MENU ------")
    print("1. Order Grocery")
    print("2. Check Product Price")
    print("3. Delivery Time")
    print("4. Cancel Order")
    print("5. Available Offers")
    print("6. Exit")

    choice = input("Enter your choice: ")

    # Order Grocery
    if choice == '1':

        product = input("Enter Product Name: ")
        quantity = int(input("Enter Quantity: "))

        print("\nOrder Placed Successfully")
        print("Product :", product)
        print("Quantity :", quantity)

    # Product Price
    elif choice == '2':

        product = input("Enter Product Name: ")

        print("Price of", product, "is Rs. 100")

    # Delivery Time
    elif choice == '3':

        location = input("Enter Delivery Location: ")

        print("Estimated Delivery Time: 10 Minutes")

    # Cancel Order
    elif choice == '4':

        order_id = input("Enter Order ID: ")

        print("Order", order_id, "Cancelled Successfully")

    # Offers
    elif choice == '5':

        print("\nAvailable Offers:")
        print("1. 20% OFF on Fruits")
        print("2. Buy 1 Get 1 Free on Snacks")
        print("3. Free Delivery on orders above Rs. 500")

    # Exit
    elif choice == '6':

        print("\nThank You for using Blinkit Chatbot")
        break

    # Invalid Choice
    else:

        print("Invalid Choice")