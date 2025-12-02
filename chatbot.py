# Basic Chatbot

def chatbot():
    print("🤖 Simple Python Chatbot")
    print("Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ").lower()

        if "hello" in user_input:
            print("Bot: Hi! How can I help you?")
        elif "how are you" in user_input:
            print("Bot: I'm doing great! Thanks for asking.")
        elif "name" in user_input:
            print("Bot: I'm a simple chatbot created by Nitin!")
        elif "bye" in user_input:
            print("Bot: Goodbye! Have a great day 😊")
            break
        else:
            print("Bot: Sorry, I don't understand that.")

chatbot()

