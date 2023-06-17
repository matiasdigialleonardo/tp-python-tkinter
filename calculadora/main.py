import tkinter as tk

def add_number(entry, num):
    current_value = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current_value + str(num))

def add_operation(entry, operation):
    current_value = entry.get()
    print(current_value[-1])
    if current_value and current_value[-1].isdigit():
        entry.insert(tk.END, operation)

def calculate(entry, result_label):
    try:
        expression = entry.get()
        result = eval(expression)
        result_label.config(text="Result: " + str(result))
    except (SyntaxError, ZeroDivisionError):
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")
        result_label.config(text="Error")

# Create the main window
window = tk.Tk()
window.title("Calculator")

# Create input field and label
entry = tk.Entry(window, width=20, justify=tk.RIGHT)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

result_label = tk.Label(window, text="Result:")
result_label.grid(row=1, column=0, columnspan=4, padx=10)

# Create the calculator buttons
buttons = [
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
]

for button_text, row, column in buttons:
    if button_text.isdigit():
        button = tk.Button(window, text=button_text, width=5,
                            command=lambda num=button_text: add_number(entry, num))
    elif button_text == "C":
        button = tk.Button(window, text=button_text, width=5,
                            command=lambda: entry.delete(0, tk.END))
    elif button_text == "=":
        button = tk.Button(window, text=button_text, width=5,
                            command=lambda: calculate(entry, result_label))
    else:
        button = tk.Button(window, text=button_text, width=5,
                            command=lambda op=button_text: add_operation(entry, op))
    button.grid(row=row+2, column=column, padx=5, pady=5)

# Start the main event loop
window.mainloop()

