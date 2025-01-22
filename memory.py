conversation_history = []

def add_to_history(user_input, bot_response):
    conversation_history.append({"user": user_input, "bot": bot_response})

def get_history():
    return conversation_history
