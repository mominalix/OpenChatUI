import customtkinter as ctk
import tkinter as tk
from datetime import datetime

class ChatUI(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Chat UI")
        self.geometry("400x400")
        
        # Create a frame to hold the chat history
        self.chat_frame = ctk.CTkFrame(self)
        self.chat_frame.pack(fill="both", expand=True)
        
        # Create a scrollbar for the chat history
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
        
        # Simulate a chat conversation
        self.simulate_chat()

    def send_message(self):
        message = self.message_entry.get()
        if message:
            current_time = datetime.now().strftime("%H:%M:%S")
            formatted_message = f"[{current_time}] You: {message}\n"
            self.chat_history.insert("end", formatted_message)
            self.message_entry.delete(0, "end")
            # Simulate receiving a response
            self.receive_message("Bot", "I received your message.")

    def receive_message(self, sender, message):
        current_time = datetime.now().strftime("%H:%M:%S")
        formatted_message = f"[{current_time}] {sender}: {message}\n"
        self.chat_history.insert("end", formatted_message)

    def simulate_chat(self):
        # Simulate a chat conversation for demonstration purposes
        conversation = [
            ("User", "Hello!"),
            ("Bot", "Hi there! How can I assist you today?"),
            ("User", "I have a question about your product."),
            ("Bot", "Sure, feel free to ask any questions you have."),
            ("User", "What are the features of your product?"),
            ("Bot", "Our product offers a wide range of features including..."),
        ]
        
        for sender, message in conversation:
            self.receive_message(sender, message)
            self.update()
            self.after(1000)  # Simulate a delay between messages

if __name__ == "__main__":
    app = ChatUI()
    app.mainloop()
