import random

# Define a list of predefined responses
responses = {
    "hello": ["Hi!", "Hey there!", "Hello!", "Hi, how can I help you?"],
    "how are you": ["I'm doing well, thank you!", "I'm great, how about you?", "All good!"],
    "bye": ["Goodbye!", "See you later!", "Bye-bye!", "Take care!"],
    "default": ["Interesting!", "Tell me more!", "I see.", "Please go on."],
}

# Function to get a response for user input
def get_response(user_input):
    user_input = user_input.lower()
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    return random.choice(responses["default"])

# Main chat loop
def chat():
    print("Chatbot: Hi there! How can I help you?")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break
        response = get_response(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    chat()
