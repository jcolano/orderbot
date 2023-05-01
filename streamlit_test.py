import streamlit as st
import openai 
import os 


with open('../api.key', 'r') as file:
    api_key = file.read().strip()

openai.api_key = api_key

def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature, # this is the degree of randomness of the model's output
    )
#     print(str(response.choices[0].message))
    return response.choices[0].message["content"]


context = [ {'role':'system', 'content':"""
                You are OrderBot, an automated service to collect orders for a pizza restaurant. \
                You first greet the customer, then collects the order, \
                and then asks if it's a pickup or delivery. \
                You wait to collect the entire order, then summarize it and check for a final \
                time if the customer wants to add anything else. \
                If it's a delivery, you ask for an address. \
                Finally you collect the payment.\
                Make sure to clarify all options, extras and sizes to uniquely \
                identify the item from the menu.\
                You respond in a short, very conversational friendly style. \
                The menu includes \
                pepperoni pizza  12.95, 10.00, 7.00 \
                cheese pizza   10.95, 9.25, 6.50 \
                eggplant pizza   11.95, 9.75, 6.75 \
                fries 4.50, 3.50 \
                greek salad 7.25 \
                Toppings: \
                extra cheese 2.00, \
                mushrooms 1.50 \
                sausage 3.00 \
                canadian bacon 3.50 \
                AI sauce 1.50 \
                peppers 1.00 \
                Drinks: \
                coke 3.00, 2.00, 1.00 \
                sprite 3.00, 2.00, 1.00 \
                bottled water 5.00 \
"""} ]  # accumulate messages

def collect_messages(prompt):
    response = get_completion_from_messages(context + [{'role':'user', 'content':f"{prompt}"}]) 
    context.append({'role':'user', 'content':f"{prompt}"})
    context.append({'role':'assistant', 'content':f"{response}"})
    return response

# Function to handle and store chat messages
def handle_message(user_input, response, chat_history):
    # Process the user input (e.g., call your chatbot logic here)
    #_response = f"Your chatbot's response to: {response}"
    
    # Append user input and chatbot response to the chat history
    chat_history.append({'user': user_input, 'chatbot': response})
    return chat_history

# Initialize chat history if not already initialized
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

def submit():
    st.session_state.input_text = ''

# Chat title
st.title("OrderBot")

st.markdown("""
    This is OrderBot, an automated service to collect orders for a pizza restaurant. \
    You can chat with OrderBot and place an order in a conversational style.
""")

# User input text field
user_input = st.text_input("Type your message here", key="input_text") #, on_change=submit

# Handle user input when the user presses Enter
if user_input:
    response = collect_messages(user_input)
    st.session_state.chat_history = handle_message(user_input, response, st.session_state.chat_history)
    st.write("Last OrderBot response:", response)

# Display chat history
for chat in st.session_state.chat_history:
    st.markdown(f"**You:** {chat['user']}")  # Display user message
    st.markdown(f"**Chatbot:** {chat['chatbot']}")  # Display chatbot response

