import tkinter as tk
from tkinter import ttk
from src.entities import client, techincian, technical_problem


class RepairCenter():
    def __init__(self):
        root = tk.Tk()
        root.title("Client Management System")
        self.client1 = client.Client()
        self.technician1 = techincian.Technician()
        self.technicalProblem1 = technical_problem.TechnicalProblem()
        
        self.client1.createClientsTable()
        self.technician1.createTechniciansTable()
        self.technicalProblem1.createTechnicalProblemsTable()


        # Create a notebook widget
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(pady=10, padx=10)

        self.create_client_page()
        self.create_technical_problem_page()
        self.create_appointment_page()
        
        self.technician1.add("Juan", "Gimenez")
        self.technician1.add("Eduardo", "Perez")

        root.mainloop()
        
    def create_client_page(self):
        # First Page - Client Information
        self.page1 = ttk.Frame(self.notebook)
        self.notebook.add(self.page1, text="Client Info")

        # Labels and entry fields for client information
        self.first_name_label = ttk.Label(self.page1, text="First Name:")
        self.first_name_label.grid(row=0, column=0, padx=5, pady=5)
        self.first_name_entry = ttk.Entry(self.page1)
        self.first_name_entry.grid(row=0, column=1, padx=5, pady=5)

        self.last_name_label = ttk.Label(self.page1, text="Last Name:")
        self.last_name_label.grid(row=1, column=0, padx=5, pady=5)
        self.last_name_entry = ttk.Entry(self.page1)
        self.last_name_entry.grid(row=1, column=1, padx=5, pady=5)

        self.street_label = ttk.Label(self.page1, text="Street Name:")
        self.street_label.grid(row=2, column=0, padx=5, pady=5)
        self.street_entry = ttk.Entry(self.page1)
        self.street_entry.grid(row=2, column=1, padx=5, pady=5)

        self.number_label = ttk.Label(self.page1, text="Number:")
        self.number_label.grid(row=3, column=0, padx=5, pady=5)
        self.number_entry = ttk.Entry(self.page1)
        self.number_entry.grid(row=3, column=1, padx=5, pady=5)

        self.save_client_button = ttk.Button(self.page1, text="Save Client Info", command=self.save_client_info)
        self.save_client_button.grid(row=5, columnspan=2, pady=10)
        
    def create_technical_problem_page(self):
        # Second Page - Technical Problem
        self.page2 = ttk.Frame(self.notebook)
        self.notebook.add(self.page2, text="Technical Problem")

        # Text field for problem description
        self.problem_label = ttk.Label(self.page2, text="Problem Description:")
        self.problem_label.grid(row=0, column=0, padx=5, pady=5)
        self.problem_text = tk.Text(self.page2, height=5, width=30)
        self.problem_text.grid(row=0, column=1, padx=5, pady=5)

        # Dropdown for selecting client
        self.client_label = ttk.Label(self.page2, text="Client:")
        self.client_label.grid(row=1, column=0, padx=5, pady=5)
        # Get all clients last names for the dropdown
        self.client_options = self.client1.get_clients()
        self.client_dropdown_var = tk.StringVar()
        self.client_dropdown = ttk.Combobox(self.page2, textvariable=self.client_dropdown_var, values=self.client_options)
        self.client_dropdown.grid(row=1, column=1, padx=5, pady=5)

        self.save_problem_button = ttk.Button(self.page2, text="Save Problem", command=self.save_problem_info)
        self.save_problem_button.grid(row=2, columnspan=2, pady=10)
        
    def create_appointment_page(self):
        # Third Page - Technician Assignment
        self.page3 = ttk.Frame(self.notebook)
        self.notebook.add(self.page3, text="Appointment")

        # Label and entry to select the client
        self.technician_label = ttk.Label(self.page3, text="Technician:")
        self.technician_label.grid(row=0, column=0, padx=5, pady=5)
        self.technician_options = self.technician1.get_technicians()
        self.technician_dropdown_var = tk.StringVar()
        self.technician_dropdown = ttk.Combobox(self.page3, textvariable=self.technician_dropdown_var, values=self.technician_options)
        self.technician_dropdown.grid(row=0, column=1, padx=5, pady=5)

        # Entry field to enter client for technician assignment
        self.client_label = ttk.Label(self.page3, text="Client:")
        self.client_label.grid(row=1, column=0, padx=5, pady=5)
        self.client_options = self.client1.get_clients()
        self.client_dropdown_var = tk.StringVar()
        self.client_dropdown = ttk.Combobox(self.page3, textvariable=self.client_dropdown_var, values=self.client_options)
        self.client_dropdown.grid(row=1, column=1, padx=5, pady=5)

        # Dropdown for selecting technical problem
        self.problem_label = ttk.Label(self.page3, text="Technical Problem:")
        self.problem_label.grid(row=2, column=0, padx=5, pady=5)
        self.problem_options = self.technicalProblem1.get_problems_id()
        self.problem_dropdown_var = tk.StringVar()
        self.problem_dropdown = ttk.Combobox(self.page3, textvariable=self.problem_dropdown_var, values=self.problem_options)
        self.problem_dropdown.bind("<<ComboboxSelected>>", self.update_description)
        self.problem_dropdown.grid(row=2, column=1, padx=5, pady=5)
        # Create a label to display the problem description
        self.description_label = ttk.Label(self.page3, text="Problem Description:")
        self.description_label.grid(row=3, column=0, padx=5, pady=5)

        # Create a label to show the selected problem description
        self.selected_description_text_var = tk.StringVar()
        self.selected_description_text = tk.Text(self.page3, height=5, width=30)
        self.selected_description_text.grid(row=3, column=1, padx=5, pady=5)
        
        # Date and time entry fields for technician visit
        self.date_label = ttk.Label(self.page3, text="Date:")
        self.date_label.grid(row=4, column=0, padx=5, pady=5)
        self.date_entry = ttk.Entry(self.page3)
        self.date_entry.grid(row=4, column=1, padx=5, pady=5)

        self.hour_label = ttk.Label(self.page3, text="Hour:")
        self.hour_label.grid(row=5, column=0, padx=5, pady=5)
        self.hour_entry = ttk.Entry(self.page3)
        self.hour_entry.grid(row=5, column=1, padx=5, pady=5)

        self.save_appointment_button = ttk.Button(self.page3, text="Save Appointment", command=self.save_appointment)
        self.save_appointment_button.grid(row=6, columnspan=2, pady=10)

    def save_client_info(self):
        # Function to save the client information entered in the GUI
        data = (
            self.first_name_entry.get(),
            self.last_name_entry.get(),
            self.street_entry.get(),
            self.number_entry.get()
        )
        self.client1.add(data)
        [entry.delete(0, tk.END) for entry in [self.first_name_entry, self.last_name_entry, self.street_entry, self.number_entry]]

    def save_problem_info(self):
        clientId = self.client1.get_client_id(self.client_dropdown_var.get())
        data = (self.problem_text.get("1.0", "end-1c"), clientId)
        self.technicalProblem1.add(data)
        self.problem_text.delete("1.0", "end")
        
    def save_appointment(self):
        data = (
            self.date_entry.get(),
            self.hour_entry.get(),
            self.technician1.get_technician_id(self.technician_dropdown_var.get()),
            self.problem_dropdown_var.get()
        )
        self.technicalProblem1.add_appointment(data)
        [entry.delete(0, tk.END) for entry in [self.date_entry, self.hour_entry, self.street_entry]]
        self.technician_dropdown_var.set("")
        
        
    def update_description(self, event=None):
        selected_item = self.problem_dropdown_var.get()
        current_problem = self.technicalProblem1.get_problem(selected_item)
        self.selected_description_text.delete("1.0", "end")
        self.selected_description_text.insert(tk.END, current_problem)
    