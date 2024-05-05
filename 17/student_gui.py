import customtkinter
import csv
import os

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("800x600")
root.title("Student GUI")

# Create a tabview with four tabs
tabview = customtkinter.CTkTabview(master=root)
tabview.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

lectures_tab = tabview.add("Lectures")
videos_tab = tabview.add("Videos")
ask_question_tab = tabview.add("Ask Question")
answers_tab = tabview.add("Answers")

# Lectures tab
lectures_frame = customtkinter.CTkFrame(master=lectures_tab)
lectures_frame.grid(row=0, column=0, padx=(20, 10), pady=(20, 10), sticky="nsew")

lectures_label = customtkinter.CTkLabel(master=lectures_frame, text="Lectures", font=("Arial", 12))
lectures_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

# Populate the lectures tab with some example lectures
lecture1 = customtkinter.CTkButton(master=lectures_frame, text="Lecture 1")
lecture1.grid(row=1, column=0, padx=10, pady=10, sticky="w")
lecture1.configure(command=lambda: select_lecture(1))

lecture2 = customtkinter.CTkButton(master=lectures_frame, text="Lecture 2")
lecture2.grid(row=2, column=0, padx=10, pady=10, sticky="w")
lecture2.configure(command=lambda: select_lecture(2))

# Videos tab
videos_frame = customtkinter.CTkFrame(master=videos_tab)
videos_frame.grid(row=0, column=0, padx=(20, 10), pady=(20, 10), sticky="nsew")

videos_label = customtkinter.CTkLabel(master=videos_frame, text="Videos", font=("Arial", 12))
videos_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

# Hide the Videos tab initially
videos_tab.forget()

# Function to select a lecture
def select_lecture(lecture_number):
    # Clear the Videos tab
    for widget in videos_frame.winfo_children():
        widget.destroy()

    # Display the Videos tab
    videos_tab.lift()

    # Populate the Videos tab with some example videos for the selected lecture
    if lecture_number == 1:
        video1 = customtkinter.CTkButton(master=videos_frame, text="Video 1")
        video1.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        video2 = customtkinter.CTkButton(master=videos_frame, text="Video 2")
        video2.grid(row=2, column=0, padx=10, pady=10, sticky="w")

# Function to read the student information from the students.csv file
def read_students():
    students = {}
    with open("students.csv", "r") as f:
        reader = csv.reader(f)
        next(reader)  # Skip the header row
        for row in reader:
            student_id, name, password = row
            students[student_id] = {"name": name, "password": password}
    return students

# Function to ask a question
def ask_question():
    global student_id
    question = input_field.get()
    if not question:
        print("Please enter a question")
        return
    if not os.path.exists("questions"):
        os.makedirs("questions")
    with open(f"questions/{student_id}.txt", "a") as f:
        f.write(f"{question}\n")
    print("Question asked successfully")

# Ask Question tab
ask_question_frame = customtkinter.CTkFrame(master=ask_question_tab)
ask_question_frame.grid(row=0, column=0, padx=(20, 10), pady=(20, 10), sticky="nsew")

input_field = customtkinter.CTkEntry(master=ask_question_frame)
input_field.grid(row=0, column=0, padx=10, pady=10, sticky="w")

ask_button = customtkinter.CTkButton(master=ask_question_frame, text="Ask")
ask_button.grid(row=0, column=1, padx=10, pady=10, sticky="e")
ask_button.configure(command=lambda: ask_question(student_id))
# Answers tab
answers_frame = customtkinter.CTkFrame(master=answers_tab)
answers_frame.grid(row=0, column=0, padx=(20, 10), pady=(20, 10), sticky="nsew")

answers_label = customtkinter.CTkLabel(master=answers_frame, text="Answers", font=("Arial", 12))
answers_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

def load_answers(student_id):
    try:
        answers_frame.delete(*answers_frame.winfo_children())
        with open(f"questions/{student_id}.txt", "r") as f:
            for line in f:
                answer = customtkinter.CTkLabel(master=answers_frame, text=line.strip(), font=("Arial", 12))
                answer.grid(row=len(answers), column=0, padx=10, pady=10, sticky="w")
                answers.append(answer)

    except FileNotFoundError:
        os.makedirs("questions", exist_ok=True)
        with open(f"questions/{student_id}.txt", "w") as f:
            pass

    finally:
        answers_tab.after(5000, load_answers, student_id)
# Define the student_id variable when the student logs in


root.mainloop()