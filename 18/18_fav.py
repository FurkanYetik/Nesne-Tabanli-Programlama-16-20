import tkinter as tk
from tkinter import ttk
import json

class HistoricalEventsGUI:
    def __init__(self, master):
        self.master = master
        master.title("Historical Events System")

        # Initialize events and people data
        self.events_data = []
        self.people_data = []

        # Load existing data
        self.load_data()

        # Event Frame
        self.events_frame = ttk.LabelFrame(master, text="Events")
        self.events_frame.grid(column=0, row=0, padx=10, pady=10, sticky="w")

        # treeview to display events
        self.events_tree = ttk.Treeview(self.events_frame)
        self.events_tree['columns'] = ('Name', 'Date', 'Description')
        self.events_tree.heading('Name', text='Name')
        self.events_tree.heading('Date', text='Date')
        self.events_tree.heading('Description', text='Description')
        self.events_tree.grid(column=0, row=0, padx=5, pady=5, sticky="nsew")

        # scrollbar to the treeview
        self.events_scrollbar = ttk.Scrollbar(self.events_frame, orient='vertical', command=self.events_tree.yview)
        self.events_scrollbar.grid(column=1, row=0, sticky='ns')
        self.events_tree.configure(yscrollcommand=self.events_scrollbar.set)

        #frame for the people
        self.people_frame = ttk.LabelFrame(master, text="People")
        self.people_frame.grid(column=0, row=1, padx=10, pady=10, sticky="w")

        #  treeview to display people
        self.people_tree = ttk.Treeview(self.people_frame)
        self.people_tree['columns'] = ('Name', 'Age', 'Description')
        self.people_tree.heading('Name', text='Name')
        self.people_tree.heading('Age', text='Age')
        self.people_tree.heading('Description', text='Description')
        self.people_tree.grid(column=0, row=0, padx=5, pady=5, sticky="nsew")

        #  scrollbar to the treeview
        self.people_scrollbar = ttk.Scrollbar(self.people_frame, orient='vertical', command=self.people_tree.yview)
        self.people_scrollbar.grid(column=1, row=0, sticky='ns')
        self.people_tree.configure(yscrollcommand=self.people_scrollbar.set)

        #  frame for adding events
        self.add_event_frame = ttk.LabelFrame(master, text="Add Event")
        self.add_event_frame.grid(column=1, row=0, padx=10, pady=10, sticky="w")

        #  entry fields for event details
        ttk.Label(self.add_event_frame, text="Name:").grid(column=0, row=0, padx=5, pady=5, sticky="w")
        self.event_name_entry = ttk.Entry(self.add_event_frame)
        self.event_name_entry.grid(column=1, row=0, padx=5, pady=5, sticky="w")

        ttk.Label(self.add_event_frame, text="Date:").grid(column=0, row=1, padx=5, pady=5, sticky="w")
        self.event_date_entry = ttk.Entry(self.add_event_frame)
        self.event_date_entry.grid(column=1, row=1, padx=5, pady=5, sticky="w")

        ttk.Label(self.add_event_frame, text="Description:").grid(column=0, row=2, padx=5, pady=5, sticky="w")
        self.event_description_entry = ttk.Entry(self.add_event_frame)
        self.event_description_entry.grid(column=1, row=2, padx=5, pady=5, sticky="w")

        #  button to add the event
        self.add_event_button = ttk.Button(self.add_event_frame, text="Add Event", command=self.add_event)
        self.add_event_button.grid(column=1, row=3, padx=5, pady=5, sticky="w")

        #  frame for adding people
        self.add_people_frame = ttk.LabelFrame(master, text="Add People")
        self.add_people_frame.grid(column=1, row=1, padx=10, pady=10, sticky="w")

        # entry fields for person details
        ttk.Label(self.add_people_frame, text="Name:").grid(column=0, row=0, padx=5, pady=5, sticky="w")
        self.person_name_entry = ttk.Entry(self.add_people_frame)
        self.person_name_entry.grid(column=1, row=0, padx=5, pady=5, sticky="w")

        ttk.Label(self.add_people_frame, text="Age:").grid(column=0, row=1, padx=5, pady=5, sticky="w")
        self.person_age_entry = ttk.Entry(self.add_people_frame)
        self.person_age_entry.grid(column=1, row=1, padx=5, pady=5, sticky="w")

        ttk.Label(self.add_people_frame, text="Description:").grid(column=0, row=2, padx=5, pady=5, sticky="w")
        self.person_description_entry = ttk.Entry(self.add_people_frame)
        self.person_description_entry.grid(column=1, row=2, padx=5, pady=5, sticky="w")

        #  button to add the person
        self.add_person_button = ttk.Button(self.add_people_frame, text="Add Person", command=self.add_person)
        self.add_person_button.grid(column=1, row=3, padx=5, pady=5, sticky="w")

        # Save data when closing the window
        master.protocol("WM_DELETE_WINDOW", self.save_data)

        # Populate GUI with existing data
        self.populate_gui()

    def add_event(self):
        name = self.event_name_entry.get()
        date = self.event_date_entry.get()
        description = self.event_description_entry.get()
        self.events_data.append({'Name': name, 'Date': date, 'Description': description})
        self.events_tree.insert('', 'end', values=(name, date, description))

    def add_person(self):
        name = self.person_name_entry.get()
        age = self.person_age_entry.get()
        description = self.person_description_entry.get()
        self.people_data.append({'Name': name, 'Age': age, 'Description': description})
        self.people_tree.insert('', 'end', values=(name, age, description))

    def save_data(self):
        with open('events.json', 'w') as events_file:
            json.dump(self.events_data, events_file, indent=4)

        with open('people.json', 'w') as people_file:
            json.dump(self.people_data, people_file, indent=4)

        self.master.destroy()

    def load_data(self):
        try:
            with open('events.json', 'r') as events_file:
                self.events_data = json.load(events_file)
        except FileNotFoundError:
            pass

        try:
            with open('people.json', 'r') as people_file:
                self.people_data = json.load(people_file)
        except FileNotFoundError:
            pass

    def populate_gui(self):
        for event in self.events_data:
            self.events_tree.insert('', 'end', values=(event['Name'], event['Date'], event['Description']))

        for person in self.people_data:
            self.people_tree.insert('', 'end', values=(person['Name'], person['Age'], person['Description']))

root = tk.Tk()
app = HistoricalEventsGUI(root)
root.mainloop()
