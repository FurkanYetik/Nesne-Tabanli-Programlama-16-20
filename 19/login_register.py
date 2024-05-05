import customtkinter
import json
import os

data_file_path = os.path.join(os.path.dirname(__file__), "data.json")

# Check if data file exists, if not create an empty one
if not os.path.exists(data_file_path):
    with open(data_file_path, "w") as file:
        json.dump({"customers": [], "restaurants": []}, file)

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("320x490")
root.title("Login System")

tabview = customtkinter.CTkTabview(master=root)
tabview.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

customer_tab = tabview.add("Customers")
restaurant_tab = tabview.add("Restaurants")

def customer_login():
    username = customer_entry1.get()
    password = customer_entry2.get()

    # Load the data from the JSON file
    with open('data.json') as f:
        data = json.load(f)

    # Authenticate the user
    for user in data['customers']:
        if user['username'] == username and user['password'] == password:
            # Open the customer GUI
            import customer_gui
            customer_gui.root.mainloop()
            return

    # If authentication fails, print an error message
    customer_button.configure(fg_color=("red", "red"))
    print("Invalid username or password")
def restaurant_login():
    username = restaurant_entry1.get()
    password = restaurant_entry2.get()
    with open(data_file_path, "r") as file:
        data = json.load(file)
        restaurants = data.get("restaurants", [])
        for restaurant in restaurants:
            if restaurant["username"] == username and restaurant["password"] == password:
                # Open the restaurant GUI
                import restaurant_gui
                restaurant_gui.root.mainloop()
                return
    restaurant_button.configure(fg_color=("red", "red"))
    print("Invalid username or password")

def register_customer():
    new_username = register_entry1.get()
    new_password = register_entry2.get()
    with open(data_file_path, "r+") as file:
        data = json.load(file)
        customers = data.get("customers", [])
        # Check if username already exists
        for customer in customers:
            if customer["username"] == new_username:
                print("Username already exists.")
                return
        # Add new customer
        customers.append({"username": new_username, "password": new_password})
        file.seek(0)
        json.dump(data, file)
        print("Registration successful.")

# Customer tab
customer_frame = customtkinter.CTkFrame(master=customer_tab)
customer_frame.grid(row=0, column=0, padx=(20, 10), pady=(20, 10), sticky="nsew")

customer_label = customtkinter.CTkLabel(master=customer_frame, text="Customer Login", font=("Arial", 12))
customer_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

customer_entry1 = customtkinter.CTkEntry(master=customer_frame, placeholder_text="User Name")
customer_entry1.grid(row=1, column=0, padx=10, pady=10, sticky="w")

customer_entry2 = customtkinter.CTkEntry(master=customer_frame, placeholder_text="Password", show="*")
customer_entry2.grid(row=2, column=0, padx=10, pady=10, sticky="w")

customer_button = customtkinter.CTkButton(master=customer_frame, text="Login", command=customer_login)
customer_button.grid(row=3, column=0, padx=10, pady=10, sticky="w")

# Customer registration
register_label1 = customtkinter.CTkLabel(master=customer_frame, text="New User Registration", font=("Arial", 12))
register_label1.grid(row=4, column=0, padx=10, pady=(20, 10), sticky="w")

register_entry1 = customtkinter.CTkEntry(master=customer_frame, placeholder_text="New User Name")
register_entry1.grid(row=5, column=0, padx=10, pady=10, sticky="w")

register_entry2 = customtkinter.CTkEntry(master=customer_frame, placeholder_text="New Password", show="*")
register_entry2.grid(row=6, column=0, padx=10, pady=10, sticky="w")

register_button = customtkinter.CTkButton(master=customer_frame, text="Register", command=register_customer)
register_button.grid(row=7, column=0, padx=10, pady=10, sticky="w")

# Restaurant tab
restaurant_frame = customtkinter.CTkFrame(master=restaurant_tab)
restaurant_frame.grid(row=0, column=0, padx=(20, 10), pady=(20, 10), sticky="nsew")

restaurant_label = customtkinter.CTkLabel(master=restaurant_frame, text="Restaurant Login", font=("Arial", 12))
restaurant_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

restaurant_entry1 = customtkinter.CTkEntry(master=restaurant_frame, placeholder_text="User Name")
restaurant_entry1.grid(row=1, column=0, padx=10, pady=10, sticky="w")

restaurant_entry2 = customtkinter.CTkEntry(master=restaurant_frame, placeholder_text="Password", show="*")
restaurant_entry2.grid(row=2, column=0, padx=10, pady=10, sticky="w")

restaurant_button = customtkinter.CTkButton(master=restaurant_frame, text="Login", command=restaurant_login)
restaurant_button.grid(row=3, column=0, padx=10, pady=10, sticky="w")

root.mainloop()
