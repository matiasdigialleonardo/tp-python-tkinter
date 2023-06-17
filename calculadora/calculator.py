import tkinter as tk
from tkinter import ttk

# Create the calculator buttons
BUTTONS = (
    ("7", 0, 0),
    ("8", 0, 1),
    ("9", 0, 2),
    ("/", 0, 3),
    ("4", 1, 0),
    ("5", 1, 1),
    ("6", 1, 2),
    ("*", 1, 3),
    ("1", 2, 0),
    ("2", 2, 1),
    ("3", 2, 2),
    ("-", 2, 3),
    ("0", 3, 0),
    ("C", 3, 1),
    ("=", 3, 2),
    ("+", 3, 3)
)


class Calculator(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.grid()
        
        parent.grid_columnconfigure(0, weight=1)  # Column 0 expands horizontally
        parent.grid_rowconfigure(0, weight=1) 
        
        entry = ttk.Entry(self)
        entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, )
        
        label = ttk.Label(self, text="Result:")
        label.grid(row=1, column=0, columnspan=4, padx=5, pady=5, )
        
        for button_value, row, column in BUTTONS:
            button = ttk.Button(self, text=button_value, width=5, command=lambda num = button_value: self.add_number(entry, num))
            button.grid(row=row+2, column=column, padx=5, pady=5)
            
    def add_number(self, entry, num):
        entry.insert(0, num)
        


        
        
root = tk.Tk()
root.title("Calculator")
root.grid_columnconfigure(0, weight=1)  # Column 0 expands horizontally
root.grid_rowconfigure(0, weight=1)   
calculator = Calculator(root)
root.mainloop()