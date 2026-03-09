import random

print("Simple Chatbot (type 'bye' to exit)")

responses = {
    "hello": ["Hi there!", "Hello!", "Hey!"],
    "how are you": ["I am fine!", "Doing great!", "All good!"],
    "what is your name": ["I am a Python chatbot.", "You can call me ChatBot."],
    "bye": ["Goodbye!", "See you later!"]
}

while True:
    user_input = input("You: ").lower()

    if user_input == "bye":
        print("Bot:", random.choice(responses["bye"]))
        break

    elif user_input in responses:
        print("Bot:", random.choice(responses[user_input]))

    else:
        print("Bot: Sorry, I don't understand that.")