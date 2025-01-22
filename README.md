# main.py
def chatbot():
    history = []  # To store conversation history

    while True:
        user_input = input()  # No prompts, directly taking user input
        if user_input.lower() in ["exit", "bye"]:
            break

        history.append(f"You: {user_input}")
        response = generate_response(user_input, history)
        print(response)

        history.append(f"Bot: {response}")

def generate_response(user_input, history):
    # Example using basic context
    if "remember" in user_input:
        return f"I remember this: {', '.join(history[-4:])}"  # Show recent history
    elif "how are you" in user_input:
        return "I'm a bot. How can I help you today?"
    else:
        return "I'm learning from you. Let's continue."

if __name__ == "__main__":
    chatbot()
