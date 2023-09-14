import customtkinter as ctk
import tkinter as tk

class ChatUI(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Chat UI")
        self.geometry("400x400")
        
        # Create a frame to hold the chat history
        self.chat_frame = ctk.CTkFrame(self)
        self.chat_frame.pack(fill="both", expand=True)
        
        # # Create a scrollbar for the chat history
        self.scrollbar = ctk.CTkScrollbar(self.chat_frame)
        self.scrollbar.pack(side="right", fill="y")
        
        # Create a textbox to display the chat history
        self.chat_history = ctk.CTkTextbox(self.chat_frame, yscrollcommand=self.scrollbar.set)
        self.chat_history.pack(fill="both", expand=True)
        self.scrollbar.configure(command=self.chat_history.yview)
        
        # Create an input field for typing messages
        self.message_entry = ctk.CTkEntry(self)
        self.message_entry.pack(fill="x")
        
        # Create a button to send messages
        self.send_button = ctk.CTkButton(self, text="Send", command=self.send_message)
        self.send_button.pack()
        self.is_sending = False

    def send_message(self):
        if not self.is_sending:
            message = self.message_entry.get()
            if message:
                # Display the user's message in the chat history
                self.display_user_message(message)

                # Clear the message entry field
                self.message_entry.delete(0, "end")
                
                # Simulate a response from the bot (you can replace this with any logic)
                response = "Third Response"
                self.display_bot_message(response)

                #self.is_sending = True


    def display_user_message(self, message):
        self.display_message("You", message)

    def display_bot_message(self, message):
        self.display_message("Bot", message)

    def display_message(self, sender, message):
        formatted_message = f"{sender}: {message}\n"
        self.chat_history.insert("end", formatted_message)

    def process_bot_response(self, user_message):
        # Simulate a response from the bot (you can replace this with any logic)
        response = "Second Response"
        self.display_bot_message(response)
        self.is_sending = False
        self.update()

    def wait_for_user_input(self):
        # Wait for the user to send a message and return it
        self.send_button.configure(state="normal")
        self.message_entry.configure(state="normal")
        self.update()

        if True:
            self.update()
            if self.is_sending:
                print("2")
                return self.message_entry.get()
                
