import streamlit as st

# Function to display user messages with rounded rectangle borders
def user_message(message):
    st.markdown(f'<div class="user-message" style="display: flex; justify-content: flex-end; padding: 5px;">'
                f'<div style="background-color: #196b1c; color: white; padding: 10px; border-radius: 10px; font-size:18px; margin-bottom:10px; margin-left:20px;">{message}</div>'
                f'</div>', unsafe_allow_html=True)

# Function to display bot messages with rounded rectangle borders
def bot_message(message):
    st.markdown(f'<div class="bot-message" style="display: flex; padding: 5px;">'
                f'<div style="background-color: #074c85; color: white; padding: 10px; border-radius: 10px; font-size:18px; margin-bottom:10px; margin-right:20px;">{message}</div>'
                f'</div>', unsafe_allow_html=True)

# Define the main Streamlit app
def main(i):
    st.title("Chat UI")
    # Initialize chat history using session state
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # Input field for user to enter a message
    user_input = st.chat_input("Your Message:")
    # Button to send the user's message
    if user_input:
        # Display previous chat messages
        for message, is_bot_response in st.session_state.chat_history:
            if is_bot_response:
                bot_message(message)
            else:
                user_message(message)
        # Add the user's message to the chat history
        st.session_state.chat_history.append((user_input, False))

        # Display the user's message
        user_message(user_input)

        # Bot's static response (you can replace this with a dynamic response generator)
        bot_response = "This is a static bot response."

        # Add the bot's response to the chat history
        st.session_state.chat_history.append((bot_response, True))
        
        # Display the bot's response
        bot_message(bot_response)
    
# Run the app
if __name__ == "__main__":
    main(0)
