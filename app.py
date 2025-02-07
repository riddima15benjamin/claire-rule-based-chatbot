import nltk
import re
from nltk.chat.util import Chat, reflections

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

pairs = [
    [r"hi|hello|hey", ["Hello! How can I assist you today?", "Hi there! How can I help you?"]],
    [r"i need help", ["How can I help you?"]],
    [r"where is my order?|order status", ["Can you please provide your order number?", "I'd be happy to help! Could you provide your order number?"]],
    [r"(\d+)", ["Thank you! An email was sent to you regarding order tracking."]],
    [r"what is your return policy?|i need to return an order", ["Our return policy allows returns within 30 days of purchase."]],
    [r"how do I get a refund?|i need a refund", ["Please contact customer service at +911800301028 or visit the refund section on your account page."]],
    [r"how long does delivery take?", ["Delivery typically takes 3-5 business days."]],
    [r"I have a complaint", ["I'm sorry to hear that. Could you please provide more details?"]],
    [r"thank you|thanks", ["You're welcome! If you need further assistance, feel free to ask."]],
    [r"bye|goodbye", ["Goodbye! Have a great day!", "Bye! I'm here if you need any more help."]]
]

class RuleBasedChatbot:
    def __init__(self, pairs):
        self.chat = Chat(pairs, reflections)
        
    def respond(self, user_input):
        return self.chat.respond(user_input)

chatbot = RuleBasedChatbot(pairs)

def chat_with_bot():
    print("Hi, I'm Claire. How may i help you today? Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("Chatbot: Bye! Have a great day!")
            break
        response = chatbot.respond(user_input)
        print(f"Chatbot: {response}")

chat_with_bot()
