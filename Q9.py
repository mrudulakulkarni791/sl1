'''Develop an elementary chatbot for any suitable customer interaction application.'''
# Simple Customer Chatbot

def chatbot():
    print("Chatbot: Hello! Welcome to ABC Store.")
    print("Chatbot: How can I help you today?")
    print("Type 'bye' to exit the chat.\n")

    while True:
        user_input = input("You: ").lower()  # convert to lowercase for easy checking

        if "hi" in user_input or "hello" in user_input:
            print("Chatbot: Hello there! How can I help you today?")

        elif "price" in user_input or "cost" in user_input:
            print("Chatbot: Our prices vary by product. Could you tell me which item you’re interested in?")

        elif "order" in user_input:
            print("Chatbot: You can place an order on our website, or I can help you track an existing one.")

        elif "hours" in user_input or "time" in user_input:
            print("Chatbot: We’re open Monday to Friday, from 9 AM to 6 PM.")

        elif "return" in user_input:
            print("Chatbot: You can return products within 30 days with your receipt.")

        elif "bye" in user_input:
            print("Chatbot: Goodbye! Have a nice day!")
            break  # stop the loop and end the program

        else:
            print("Chatbot: I’m sorry, I didn’t understand that. Could you please rephrase?")

# Run the chatbot
chatbot()
