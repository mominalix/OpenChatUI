from ChatUI import ChatUI

if __name__ == "__main__":
    app = ChatUI()

    # Start the chat application
    while True:
        user_input = app.wait_for_user_input()

        # Process the user input and send a response when the send button is clicked
        if user_input:
            # Display user input in chat history
            app.display_user_message(user_input)
            
            # Simulate a response from the bot (you can replace this with any logic)
            print("3")
            #response = "First Response"
            #app.display_bot_message(response)
        print("1")