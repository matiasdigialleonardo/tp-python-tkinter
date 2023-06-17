import tkinter as tk
from tkinter import ttk, messagebox
from main_tp_tkinter import RepairCenter


class LoginWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        # Set the window title
        self.title("Login")

        # Create a frame for the login elements with padding
        login_frame = ttk.Frame(self, padding=20)
        login_frame.pack()

        # Username label and entry
        self.username_label = ttk.Label(login_frame, text="Username:")
        self.username_label.grid(row=0, column=0)
        self.username_entry = ttk.Entry(login_frame)
        self.username_entry.grid(row=0, column=1)

        # Password label and entry
        self.password_label = ttk.Label(login_frame, text="Password:")
        self.password_label.grid(row=1, column=0)
        self.password_entry = ttk.Entry(login_frame, show="*")
        self.password_entry.grid(row=1, column=1)

        # Login button
        self.login_button = ttk.Button(login_frame, text="Login", command=self.login)
        self.login_button.grid(row=2, column=0, columnspan=2, padx=20, pady=20)
        
        self.mainloop()
        
    def login(self):
        # Retrieve the entered username and password
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Validate the username and password (replace this with your own authentication logic)
        if username == "admin" and password == "admin":
            # If login is successful, close the login window and open the Client management system window
            self.destroy()
            RepairCenter()
        else:
            # If login is unsuccessful, show an error message
            messagebox.showerror("Login Failed", "Invalid username or password.")

loginWindow = LoginWindow()