from app.bot import ChatBot
from modules.memory import add_to_history, get_history

def main():
    print("Smarty.bot is running! Type 'exit' to quit.")

    bot = ChatBot()  # Create an instance of your chatbot

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Smarty.bot: Goodbye!")
            break

        # Process user input through the bot
        response = bot.process_input(user_input)

        # Add to memory (conversation history)
        add_to_history(user_input, response)

        # Display bot's response
        print(f"Smarty.bot: {response}")

if __name__ == "__main__":
    main()
