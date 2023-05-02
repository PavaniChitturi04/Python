import random

# Define a dictionary of responses
responses = {
    "hi": ["Hello!", "Hi there!", "Hi!"],
    "how are you": ["I'm doing well, thanks for asking.", "I'm fine, how about you?"],
    "what's your name": ["My name is Chatbot.", "You can call me Chatbot."],
    "bye": ["Goodbye!", "See you later!"],
    "default": ["Sorry, I didn't understand what you said.", "Can you please rephrase that?", "I'm not sure I understand."],
}

# Define a function to get a response from the dictionary
def get_response(message):
    message = message.lower()
    if message in responses:
        return random.choice(responses[message])
    else:
        return random.choice(responses["default"])

# Start the chatbot loop
print("Chatbot: Hi, I'm a chatbot. How can I help you today?")
while True:
    message = input("You: ")
    if message.lower() == "bye":
        print("Chatbot: Goodbye!")
        break
    else:
        response = get_response(message)
        print("Chatbot:", response)