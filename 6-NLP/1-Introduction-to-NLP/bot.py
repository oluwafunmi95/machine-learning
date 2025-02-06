import random

# Instructions for the user
print("Welcome! You can interact with me by typing something, and I will respond. Type 'exit' to end the conversation.")

# List of possible generic responses
responses = [
    "That's interesting!",
    "Tell me more!",
    "How can I help you further?",
    "That's a good point!",
    "Hmm, I'll think about that."
]

# Start a loop
while True:
    # Accept user input
    user_input = input("You: ")

    # If user asks to exit, break the loop
    if user_input.lower() == "exit":
        print("Goodbye! Have a great day!")
        break

    # Process user input and determine response (random response from the list)
    response = random.choice(responses)

    # Print response
    print(f"Bot: {response}")
