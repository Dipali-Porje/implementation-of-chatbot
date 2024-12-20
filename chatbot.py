# Advanced rule-based chatbot
import re
import random

# Define patterns and responses
responses = [
    (r"hello|hi|hey", ["Hello! How can I help you?", "Hi there! What can I assist you with?", "Hey! What's up?"]),
    (r"how are you(.*)", ["I'm just a program, but I'm functioning perfectly!", "I'm here to assist you. How can I help?"]),
    (r"(.*) your name?", ["I'm Chatbot! Your virtual assistant.", "My name is Chatbot, and I'm here to help you."]),
    (r"what (.*) do you (.*)", ["I can assist with answering questions, providing information, or just chatting!", "I'm here to help with anything you need, within my capabilities."]),
    (r"(.*) weather (.*)", ["I recommend checking a weather website or app for accurate information.", "I'm unable to provide real-time weather updates."]),
    (r"tell me a joke", ["Why don’t scientists trust atoms? Because they make up everything!", "Why did the math book look sad? Because it had too many problems."]),
    (r"(.*) created you?", ["I was created by a team of developers using Python!", "Some amazing developers brought me to life."]),
    (r"(.*) help (.*)", ["Sure, I'd love to help. Please elaborate on your question.", "I'm here to assist. Could you provide more details?"]),
    (r"(.*) (movie|book) (.*) recommend", ["I recommend 'Inception' if you like mind-bending movies.", "'To Kill a Mockingbird' is a great book to read."]),
    (r"bye|goodbye", ["Goodbye! Have a great day!", "Bye! Feel free to reach out anytime."]),
    (r"(.*)", ["I'm not sure I understand. Can you elaborate?", "Sorry, I didn't catch that. Could you rephrase?"]),
]

# Function to generate chatbot responses
def chatbot_response(message):
    message = message.lower()
    for pattern, replies in responses:
        if re.search(pattern, message):
            return random.choice(replies)
    return "I'm sorry, I didn't understand that."

# Interactive chatbot
print("Chatbot: Hi there! Type 'exit' to end the chat.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye! Have a great day!")
        break
    print(f"Chatbot: {chatbot_response(user_input)}")
