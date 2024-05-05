import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500x350")
root.title("Login System")

def login():
    username = entry1.get()
    password = entry2.get()
    with open("../as.txt", "r") as file:
        lines = file.readlines()
    for line in lines:
        fields = line.strip().split(",")
        if len(fields) == 2:
            if fields[0] == username and fields[1] == password:
                # Open the movie and TV series watching service GUI
                import movie_and_tv_series_gui
                movie_and_tv_series_gui.root.mainloop()
                return
    button.configure(fg_color=("red", "red"))
    print("Invalid username or password")
def sign_up():
    username = entry3.get()
    password = entry4.get()
    with open("../as.txt", "a") as file:

        file.write(f"{username},{password}\n")
    print("Sign-up successful")

frame  = customtkinter.CTkFrame(master = root)
frame.grid(row=0, column=0, padx=(20, 10), pady=(20, 10), sticky="nsew")

label = customtkinter.CTkLabel(master=frame,text="Login", font=("Arial",12))
label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

entry1 = customtkinter.CTkEntry(master = frame , placeholder_text="User Name")
entry1.grid(row=1, column=0, padx=10, pady=10, sticky="w")

entry2 = customtkinter.CTkEntry(master = frame , placeholder_text="Password", show="*")
entry2.grid(row=2, column=0, padx=10, pady=10, sticky="w")

button = customtkinter.CTkButton(master=frame , text="Login", command=login)
button.grid(row=3, column=0, padx=10, pady=10, sticky="w")

frame2 = customtkinter.CTkFrame(master = root)
frame2.grid(row=0, column=1, padx=(10, 20), pady=(20, 10), sticky="nsew")

label2 = customtkinter.CTkLabel(master=frame2,text="Sign Up", font=("Arial",12))
label2.grid(row=0, column=1, padx=10, pady=10, sticky="w")

entry3 = customtkinter.CTkEntry(master = frame2 , placeholder_text="User Name")
entry3.grid(row=1, column=1, padx=10, pady=10, sticky="w")

entry4 = customtkinter.CTkEntry(master = frame2 , placeholder_text="Password", show="*")
entry4.grid(row=2, column=1, padx=10, pady=10, sticky="w")

button2 = customtkinter.CTkButton(master=frame2 , text="Sign Up", command=sign_up)
button2.grid(row=3, column=1, padx=10, pady=10, sticky="w")

checkbox = customtkinter.CTkCheckBox(master=frame, text="Checkbox")
checkbox.grid(row=4, column=0, padx=10, pady=10, sticky="w")

root.mainloop()