# redbus_chatbot.py

print("Welcome to RedBus Chatbot")
print("Type 'exit' to quit\n")

while True:
    user_input = input("You: ").lower()

    # Exit
    if user_input == "exit":
        print("Bot: Thank you for using RedBus Chatbot!")
        break

    # Greetings
    elif any(word in user_input for word in ["hello", "hi", "hey"]):
        print("Bot: Hello! How can I help you with your bus booking?")

    # Booking buses
    elif any(word in user_input for word in ["book", "ticket", "bus"]):
        source = input("Bot: Enter source city: ")
        destination = input("Bot: Enter destination city: ")
        date = input("Bot: Enter travel date: ")

        print(f"\nBot: Searching buses from {source} to {destination} on {date}...")
        print("Bot: Found 5 available buses.")
        print("Bot: Ticket booking successful!\n")

    # Cancel ticket
    elif "cancel" in user_input:
        booking_id = input("Bot: Enter booking ID: ")
        print(f"Bot: Booking {booking_id} has been cancelled.")

    # Check ticket status
    elif any(word in user_input for word in ["status", "pnr"]):
        booking_id = input("Bot: Enter booking ID: ")
        print(f"Bot: Booking {booking_id} is confirmed.")

    # Help
    elif "help" in user_input:
        print("""
Bot Commands:
- book bus
- cancel ticket
- check status
- exit
""")

    # Unknown message
    else:
        print("Bot: Sorry, I didn't understand that.")