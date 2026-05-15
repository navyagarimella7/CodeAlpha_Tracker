
RULES = {
    "hello":          "Hi there!  How can I help you?",
    "hi":             "Hey! Great to see you. ",
    "hey":            "Hey! What's up?",
    "how are you":    "I'm doing great, thanks for asking! ",
    "what is your name": "I'm ChatBot, your friendly assistant!",
    "what can you do":   "I can have a basic conversation with you. Try saying hello!",
    "tell me a joke":    "Why don't scientists trust atoms? Because they make up everything! ",
    "bye":            "Goodbye! Have a wonderful day! ",
    "goodbye":        "See you later! Take care! ",
    "thanks":         "You're welcome! ",
    "thank you":      "Happy to help! ",
}

def get_response(user_message):
    """
    Match the user's message against the rules dictionary.

    Args:
        user_message (str): Raw text typed by the user.

    Returns:
        str: The bot's reply.
    """
    cleaned = user_message.strip().lower()

    if cleaned in RULES:
        return RULES[cleaned]
    elif cleaned == "":
        return "Oops! You didn't type anything. Try saying 'hello'."
    else:
        return "🤔 Hmm, I don't understand that yet. Try: hello, how are you, bye."

def run_chatbot():
    """
    Main loop: reads user input, gets a response, prints it.
    Exits when the user types 'bye' or 'goodbye'.
    """
    print("=" * 50)
    print("       Welcome to Navya's ChatBot! 🤖")
    print("  Type 'bye' or 'goodbye' to exit the chat.")
    print("=" * 50)
    print()

    
    while True:
        
        user_input = input("You: ")
        response = get_response(user_input)

        print(f"Bot: {response}")
        print()  # Blank line for readability

        if user_input.strip().lower() in ("bye", "goodbye"):
            break  # Exit the while loop

if __name__ == "__main__":
    run_chatbot()