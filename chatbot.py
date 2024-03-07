#Project Name: Basic ChatBot
#Programming Language: Python
import nltk
import random

# Download NLTK data for tokenization
nltk.download('punkt')

# Some responses of chatbot
responses = {
    "hello": ["Hi there! How can I help you today?", "Hello! How can I help you?", "Greeting, How can I help you today?"],
    "hii": ["Hi there! How can I help you today?", "Hello! How can I help you?"],
    "how are you": ["I'm just a computer program, but thanks for asking! How can I assist you?"],
    "what is your name": ["I'm a chatbot. You can call me ROBO-CHITTI.", "Myself Robo, ROBO- CHITTI", "CHITTI - The chatterbox "],
    "hii chitti": ["Hello dear!!", "Hii, nice to meet you...", "Whatsup bro!!"],
    "bye": ["Goodbye! If you have more questions, feel free to ask anytime.", "See you next time", "Bye Bye.\n Have a good day!!"],
    "goodbye": ["Goodbye! If you have more questions, feel free to ask anytime.", "See you next time", "Bye Bye.\n Have a good day!!"],
    "tell me a joke": ["Why don't scientists trust atoms? Because they make up everything!", "Why did the math book look sad? Because it had too many problems.", "Why did the bicycle fall over? Because it was two-tired!"],
    "help me": ["Sure, I can help you with information or answer questions. What do you need assistance with?", "Yes, I am always ready to help you!", "Of course, tell me how can I help you?"],
}

# Function to reply to the user
def chatbot_response(user_input):
    # Tokenize user input for better processing
    user_input_tokens = nltk.word_tokenize(user_input.lower())

    # Iterate through response keys
    for key in responses:
        # Check if the key is present in the user's input
        if key in user_input.lower():
            # Return a random response from the corresponding key
            return random.choice(responses[key])

    # If no matching key is found, provide a default response
    return "I am sorry, I didn't understand your question."

# Loop to keep the chatbot in conversational mode until the user says bye
while True:
    # Get user input
    user_input = input("You: ")
    
    # Get chatbot response
    response = chatbot_response(user_input)
    
    # Display chatbot response
    print("Chatbot: ", response)
    
    # Check if the user wants to exit the conversation
    if user_input.lower() == "bye" or user_input.lower() == "goodbye":
        break