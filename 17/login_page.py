import customtkinter
import csv
import os

students_csv_path = os.path.join(os.path.dirname(__file__), "students.csv")



customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500x350")
root.title("Login System")

tabview = customtkinter.CTkTabview(master=root)
tabview.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

student_tab = tabview.add("Students")
teacher_tab = tabview.add("Teachers")

def student_login():
    username = student_entry1.get()
    password = student_entry2.get()
    with open(students_csv_path, "r") as file:
        reader = csv.reader(file)
        students = list(reader)  # Read the entire CSV file into a list
        for row in students:
            if len(row) == 3:  # Check if the row has 3 columns (student_id, username, password)
                if row[1] == username and row[2] == password:
                    student_id = row[0]  # Store the student_id
                    # Open the student GUI
                    import student_gui
                    student_gui.student_id = student_id  # Pass the student_id to the student_gui module
                    student_gui.root.mainloop()
                    return
    student_button.configure(fg_color=("red", "red"))
    print("Invalid username or password")
def teacher_login():
    username = teacher_entry1.get()
    password = teacher_entry2.get()
    with open("../teachers.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) == 2:
                if row[0] == username and row[1] == password:
                    # Open the teacher GUI
                    import teacher_gui
                    teacher_gui.root.mainloop()
                    return
    teacher_button.configure(fg_color=("red", "red"))
    print("Invalid username or password")

# Student tab
student_frame = customtkinter.CTkFrame(master=student_tab)
student_frame.grid(row=0, column=0, padx=(20, 10), pady=(20, 10), sticky="nsew")

student_label = customtkinter.CTkLabel(master=student_frame, text="Student Login", font=("Arial", 12))
student_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

student_entry1 = customtkinter.CTkEntry(master=student_frame, placeholder_text="User Name")
student_entry1.grid(row=1, column=0, padx=10, pady=10, sticky="w")

student_entry2 = customtkinter.CTkEntry(master=student_frame, placeholder_text="Password", show="*")
student_entry2.grid(row=2, column=0, padx=10, pady=10, sticky="w")

student_button = customtkinter.CTkButton(master=student_frame, text="Login", command=student_login)
student_button.grid(row=3, column=0, padx=10, pady=10, sticky="w")

# Teacher tab
teacher_frame = customtkinter.CTkFrame(master=teacher_tab)
teacher_frame.grid(row=0, column=0, padx=(20, 10), pady=(20, 10), sticky="nsew")

teacher_label = customtkinter.CTkLabel(master=teacher_frame, text="Teacher Login", font=("Arial", 12))
teacher_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

teacher_entry1 = customtkinter.CTkEntry(master=teacher_frame, placeholder_text="User Name")
teacher_entry1.grid(row=1, column=0, padx=10, pady=10, sticky="w")

teacher_entry2 = customtkinter.CTkEntry(master=teacher_frame, placeholder_text="Password", show="*")
teacher_entry2.grid(row=2, column=0, padx=10, pady=10, sticky="w")

teacher_button = customtkinter.CTkButton(master=teacher_frame, text="Login", command=teacher_login)
teacher_button.grid(row=3, column=0, padx=10, pady=10, sticky="w")

root.mainloop()