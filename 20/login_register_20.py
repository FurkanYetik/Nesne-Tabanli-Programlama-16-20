import customtkinter
import sqlite3
import os

data_base_path = os.path.join(os.path.dirname(__file__), "data.db")

# Create a connection to the SQLite database
conn = sqlite3.connect(data_base_path)
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS users
             (username text, password text)''')
conn.commit()

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("320x490")
root.title("Login System")

tabview = customtkinter.CTkTabview(master=root)
tabview.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

login_tab = tabview.add("Login")
register_tab = tabview.add("Register")

def login_user():
    username = login_entry1.get()
    password = login_entry2.get()


    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    if c.fetchone():
        # Open the user GUI
        import user_gui
        user_gui.root.mainloop()
        return

    login_button.configure(fg_color=("red", "red"))
    print("Invalid username or password")

def register_user():
    new_username = register_entry1.get()
    new_password = register_entry2.get()

    # Check if username already exists
    c.execute("SELECT * FROM users WHERE username=?", (new_username,))
    if c.fetchone():
        print("Username already exists.")
        return

    # Add new user
    c.execute("INSERT INTO users VALUES (?,?)", (new_username, new_password))
    conn.commit()
    print("Registration successful.")

# Login tab
login_frame = customtkinter.CTkFrame(master=login_tab)
login_frame.grid(row=0, column=0, padx=(20, 10), pady=(20, 10), sticky="nsew")

login_label = customtkinter.CTkLabel(master=login_frame, text="User Login", font=("Arial", 12))
login_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

login_entry1 = customtkinter.CTkEntry(master=login_frame, placeholder_text="User Name")
login_entry1.grid(row=1, column=0, padx=10, pady=10, sticky="w")

login_entry2 = customtkinter.CTkEntry(master=login_frame, placeholder_text="Password", show="*")
login_entry2.grid(row=2, column=0, padx=10, pady=10, sticky="w")

login_button = customtkinter.CTkButton(master=login_frame, text="Login", command=login_user)
login_button.grid(row=3, column=0, padx=10, pady=10, sticky="w")

# Register tab
register_frame = customtkinter.CTkFrame(master=register_tab)
register_frame.grid(row=0, column=0, padx=(20, 10), pady=(20, 10), sticky="nsew")

register_label1 = customtkinter.CTkLabel(master=register_frame, text="New User Registration", font=("Arial", 12))
register_label1.grid(row=0, column=0, padx=10, pady=(20, 10), sticky="w")

register_entry1 = customtkinter.CTkEntry(master=register_frame, placeholder_text="New User Name")
register_entry1.grid(row=1, column=0, padx=10, pady=10, sticky="w")

register_entry2 = customtkinter.CTkEntry(master=register_frame, placeholder_text="New Password", show="*")
register_entry2.grid(row=2, column=0, padx=10, pady=10, sticky="w")

register_button = customtkinter.CTkButton(master=register_frame, text="Register", command=register_user)
register_button.grid(row=3, column=0, padx=10, pady=10, sticky="w")

root.mainloop()