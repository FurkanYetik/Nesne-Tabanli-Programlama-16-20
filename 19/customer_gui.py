import customtkinter
import json
import os
import tkinter.messagebox as messagebox

# Path to the JSON files storing menu data and order data
menu_data_file_path = os.path.join(os.path.dirname(__file__), "menu_data.json")
order_data_file_path = os.path.join(os.path.dirname(__file__), "order_data.json")

# Check if menu data file exists, if not create an empty one
if not os.path.exists(menu_data_file_path):
    with open(menu_data_file_path, "w") as file:
        json.dump([], file)

# Check if order data file exists, if not create an empty one
if not os.path.exists(order_data_file_path):
    with open(order_data_file_path, "w") as file:
        json.dump([], file)

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500x500")
root.title("Customer Panel")

frame = customtkinter.CTkFrame(master=root)
frame.pack(fill="both", expand=True)

menu_label = customtkinter.CTkLabel(master=frame, text="Menu", font=("Arial", 12))
menu_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

# Load menu data from JSON file
with open(menu_data_file_path, "r") as file:
    menu_data = json.load(file)

# Entry widgets to input quantities and address
quantity_entries = []
for index, item in enumerate(menu_data):
    item_label = customtkinter.CTkLabel(master=frame, text=f"{item['menu_item']}: ${item['price']}")
    item_label.grid(row=index + 1, column=0, padx=10, pady=5, sticky="w")

    quantity_label = customtkinter.CTkLabel(master=frame, text="Quantity:")
    quantity_label.grid(row=index + 1, column=1, padx=10, pady=5, sticky="e")

    quantity_entry = customtkinter.CTkEntry(master=frame)
    quantity_entry.grid(row=index + 1, column=2, padx=10, pady=5, sticky="w")

    quantity_entries.append(quantity_entry)

address_entry_label = customtkinter.CTkLabel(master=frame, text="Delivery Address:", font=("Arial", 10))
address_entry_label.grid(row=len(menu_data) + 2, column=0, padx=10, pady=5, sticky="w")
address_entry = customtkinter.CTkEntry(master=frame)
address_entry.grid(row=len(menu_data) + 2, column=1, padx=10, pady=5, sticky="w")

name_entry_label = customtkinter.CTkLabel(master=frame, text="Name:", font=("Arial", 10))
name_entry_label.grid(row=len(menu_data) + 3, column=0, padx=10, pady=5, sticky="w")
name_entry = customtkinter.CTkEntry(master=frame)
name_entry.grid(row=len(menu_data) + 3, column=1, padx=10, pady=5, sticky="w")

# Function to place an order
def place_order():
    # Get address from the entry widget
    address = address_entry.get()
    if not address:
        messagebox.showinfo("Error", "Please enter your delivery address.")
        return

    # Get name from the entry widget
    name = name_entry.get()
    if not name:
        messagebox.showinfo("Error", "Please enter your name.")
        return

    # Initialize the order summary
    order_summary = ""
    total_price = 0

    # Iterate over each menu item and corresponding quantity entry
    for index, item in enumerate(menu_data):
        # Get quantity from the corresponding entry widget
        quantity = quantity_entries[index].get()
        if not quantity:
            messagebox.showinfo("Error", f"Please enter the quantity for {item['menu_item']}.")
            return
        try:
            quantity = int(quantity)
            if quantity <= 0:
                raise ValueError
        except ValueError:
            messagebox.showinfo("Error", f"Invalid quantity for {item['menu_item']}.")
            return

        # Calculate subtotal for the item
        subtotal = quantity * item["price"]

        # Update the order summary
        order_summary += f"{item['menu_item']}: {quantity} x ${item['price']} = ${subtotal}\n"
        total_price += subtotal

    # Add the total price and delivery address to the order summary
    order_summary += f"\nTotal Price: ${total_price}\nDelivery Address: {address}\nName: {name}"

    # Display the order summary
    order_summary_label = customtkinter.CTkLabel(master=frame, text=order_summary, font=("Arial", 10))
    order_summary_label.grid(row=len(menu_data) + 2, column=0, columnspan=3, padx=10, pady=10, sticky="w")

    # Save the order to the order data file
    order_data = {
        "name": name,
        "address": address,
        "items": [{"menu_item": item["menu_item"], "quantity": quantity, "price": item["price"]} for index, item in enumerate(menu_data)],
        "total_price": total_price
    }
    with open(order_data_file_path, "r+") as file:
        order_data_list = json.load(file)
        order_data_list.append(order_data)
        file.seek(0)
        json.dump(order_data_list, file, indent=4)
        file.truncate()

    # Display a message box indicating the order was placed successfully
    messagebox.showinfo("Order Placed", "Your order has been placed successfully!")

# Place order button
place_order_button = customtkinter.CTkButton(master=frame, text="Place Order", command=place_order)
place_order_button.grid(row=len(menu_data) + 2, column=2, padx=10, pady=10, sticky="e")

root.mainloop()
