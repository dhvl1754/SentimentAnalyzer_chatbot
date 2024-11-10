from textblob import TextBlob as tb

intents = {
    "hours":{
        "keywords" : ["hours", "open", "close"],
        "response" : "We are open from Monday to Friday, 9 AM to 5 PM."
    },
    "return":{
        "keywords" : ["refund", "money back", "return"],
        "response" : "I'd be happy to help you with the return process. Let me transfer you to a live agent."
    }
}

def get_response(message):
    message = message.lower()

    for intent_name, intent_data in intents.items():
        if any(word in message for word in intent_data["keywords"]):
            return intent_data["response"]
            
    s = tb(message).sentiment.polarity
    return ("That's so great to hear" if s > 0 else
            "I am so sorry to hear that. How can I help?" if s<0 else
            "I see. Can you tell me more about that?")

def chat():
    print("Chatbot: Hi, how can I help you today?")

    while(user_message:= input("You: ").strip().lower()) not in ['exit', 'quit', 'bye']:
        print(f"\nChatbot: {get_response(user_message)}")

if __name__ == "__main__":
    chat()
        
