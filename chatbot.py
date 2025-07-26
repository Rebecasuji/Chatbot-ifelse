# chatbot.py

def chatbot():
    print("🤖 Hello! I am RuleBot, your chatbot assistant.")
    print("Ask me anything like greetings, my name, how I feel, or your own name. Say 'bye' to exit.")

    while True:
        user_input = input("You: ").lower().strip()

        if user_input in ['hi', 'hello', 'hey']:
            print("RuleBot: Hello there! How can I assist you today?")

        elif "your name" in user_input:
            print("RuleBot: I am RuleBot, your friendly chatbot!")

        elif "help" in user_input:
            print("RuleBot: I can respond to greetings, tell my name, respond to 'how are you', or exit when you say 'bye'.")

        elif user_input in ['bye', 'exit', 'quit']:
            print("RuleBot: Goodbye! Have a nice day 😊")
            break

        elif "how are you" in user_input:
            print("RuleBot: I'm just code, but I'm functioning perfectly! Thanks for asking.")

        elif "my name is" in user_input:
            name = user_input.replace("my name is", "").strip().capitalize()
            print(f"RuleBot: Nice to meet you, {name}! How can I help you today?")

        elif "time" in user_input:
            print("RuleBot: I can't read the clock yet 🕒, but you can check your device's time!")

        else:
            print("RuleBot: Sorry, I didn't understand that. Type 'help' to see what you can ask me.")

if __name__ == "__main__":
    chatbot()
