import customtkinter
import json
import os

# Path to the JSON file storing menu data
menu_data_file_path = os.path.join(os.path.dirname(__file__), "menu_data.json")

# Check if menu data file exists, if not create an empty one
if not os.path.exists(menu_data_file_path):
    with open(menu_data_file_path, "w") as file:
        json.dump([], file)

# Path to the JSON file storing order data
order_data_file_path = os.path.join(os.path.dirname(__file__), "order_data.json")

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

restaurant_root = customtkinter.CTk()
restaurant_root.geometry("500x350")
restaurant_root.title("Restaurant Panel")

restaurant_frame = customtkinter.CTkFrame(master=restaurant_root)
restaurant_frame.pack(fill="both", expand=True)

menu_label = customtkinter.CTkLabel(master=restaurant_frame, text="Menu Management", font=("Arial", 12))
menu_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

menu_entry_label = customtkinter.CTkLabel(master=restaurant_frame, text="Menu Item:", font=("Arial", 10))
menu_entry_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")

menu_entry = customtkinter.CTkEntry(master=restaurant_frame)
menu_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

price_entry_label = customtkinter.CTkLabel(master=restaurant_frame, text="Price:", font=("Arial", 10))
price_entry_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")

price_entry = customtkinter.CTkEntry(master=restaurant_frame)
price_entry.grid(row=2, column=1, padx=10, pady=5, sticky="w")


def add_menu_item():
    menu_item = menu_entry.get()
    price = price_entry.get()
    # Validate price (check if it's a valid float)
    try:
        price = float(price)
        if price <= 0:
            raise ValueError("Price must be a positive number")
    except ValueError as e:
        print(f"Error: {e}")
        return

    # Load existing menu data from JSON file
    if os.path.exists(menu_data_file_path) and os.path.getsize(menu_data_file_path) > 0:
        with open(menu_data_file_path, "r") as file:
            menu_data = json.load(file)
    else:
        menu_data = []  # Default empty list if the file is empty or does not exist

    # Append new menu item to the menu data
    menu_data.append({"menu_item": menu_item, "price": price})

    # Write updated menu data back to JSON file
    with open(menu_data_file_path, "w") as file:
        json.dump(menu_data, file, indent=4)

    print("Menu item added successfully!")
    # You can also update the menu display or perform other actions as needed


add_button = customtkinter.CTkButton(master=restaurant_frame, text="Add Menu Item", command=add_menu_item)
add_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="w")


# Function to display orders
def display_orders():
    # Check if order data file exists
    if os.path.exists(order_data_file_path) and os.path.getsize(order_data_file_path) > 0:
        with open(order_data_file_path, "r") as file:
            orders = json.load(file)
            order_text = "\n\n".join(["Name: {}\nAddress: {}\nItems: {}\nTotal Price: ${}".format(order['name'],
                                                                                                   order['address'],
                                                                                                   ", ".join(["({}) {} x ${}".format(item['menu_item'], item['quantity'], item['price']) for item in order['items']]),
                                                                                                   order['total_price']) for order in orders])
            order_label.configure(text=order_text)
    else:
        order_label.configure(text="No orders yet")

order_label = customtkinter.CTkLabel(master=restaurant_frame, text="Orders:", font=("Arial", 12))
order_label.grid(row=4, column=0, padx=10, pady=10, sticky="w")

display_orders_button = customtkinter.CTkButton(master=restaurant_frame, text="Display Orders", command=display_orders)
display_orders_button.grid(row=4, column=1, padx=10, pady=10, sticky="e")

restaurant_root.mainloop()
