# Simple Rule-Based Chatbot using if-elif-else statements

def chatbot():
    """
    A rule-based chatbot that responds to simple keywords.
    The conversation runs in a loop until the user types 'quit' or 'exit'.
    """
    print("🤖 Rule-Bot: Hello! I am a simple rule-based chatbot. How can I help you today?")
    print("🤖 Rule-Bot: You can try asking about 'weather', 'name', 'time', or simply type 'quit' to exit.")

    # Start the main input/output loop
    while True:
        # Get user input and convert it to lowercase for case-insensitive matching
        user_input = input("\nYou: ")
        processed_input = user_input.lower().strip()

        # Check for the exit command
        if processed_input in ["quit", "exit", "bye", "goodbye"]:
            print("🤖 Rule-Bot: Goodbye! Have a wonderful day!")
            break  # Exit the while loop

        # Rule 1: Greetings
        elif "hello" in processed_input or "hi" in processed_input:
            print("🤖 Rule-Bot: Hello there! I'm here to chat based on simple rules.")

        # Rule 2: Asking for the bot's name
        elif "your name" in processed_input:
            print("🤖 Rule-Bot: I am Rule-Bot, a helpful digital assistant created with Python if-elif-else logic.")

        # Rule 3: Asking about the weather
        elif "weather" in processed_input:
            # Since this is a rule-based bot, we can't check real weather, so we give a standard response.
            print("🤖 Rule-Bot: I can't check the current weather, but I predict clear skies for logic operations! How is it where you are?")

        # Rule 4: Asking about programming
        elif "python" in processed_input or "code" in processed_input or "programming" in processed_input:
            print("🤖 Rule-Bot: Python is fantastic for building all sorts of applications, including rule-based bots like me!")

        # Rule 5: Acknowledgment/Affirmation
        elif "thanks" in processed_input or "thank you" in processed_input:
            print("🤖 Rule-Bot: You're welcome! I'm glad I could assist.")

        # Rule 6: How are you question
        elif "how are you" in processed_input:
            print("🤖 Rule-Bot: As an algorithm, I'm functioning optimally! How about you?")

        # Default Response (catch-all using else)
        else:
            print("🤖 Rule-Bot: Hmm, I don't have a rule for that yet. Can you ask me about 'weather' or 'python'?")

# Execute the chatbot function when the script is run
if __name__ == "__main__":
    chatbot()
