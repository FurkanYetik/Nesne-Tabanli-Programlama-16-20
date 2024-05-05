import customtkinter as ctk
import csv
import os

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()
root.geometry("800x600")
root.title("Teacher GUI")

# Create a tabview with three tabs
tabview = ctk.CTkTabview(master=root)
tabview.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

lectures_tab = tabview.add("Lectures")
questions_tab = tabview.add("Questions")
answers_tab = tabview.add("Answers")

# Lectures tab
lectures_frame = ctk.CTkFrame(master=lectures_tab)
lectures_frame.grid(row=0, column=0, padx=(20, 10), pady=(20, 10), sticky="nsew")

lectures_label = ctk.CTkLabel(master=lectures_frame, text="Add New Videos to Lectures", font=("Arial", 12))
lectures_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

# Function to add new videos to lectures
def add_video_to_lecture(lecture_number):
    video_file = ctk.ask_open_file()
    if video_file:
        # Code to save the video file and associate it with the lecture
        ctk.messagebox.showinfo("Success", "Video added to lecture successfully.")

add_video_button1 = ctk.CTkButton(master=lectures_frame, text="Add Video to Lecture 1", command=lambda: add_video_to_lecture(1))
add_video_button1.grid(row=1, column=0, padx=10, pady=10, sticky="w")

add_video_button2 = ctk.CTkButton(master=lectures_frame, text="Add Video to Lecture 2", command=lambda: add_video_to_lecture(2))
add_video_button2.grid(row=2, column=0, padx=10, pady=10, sticky="w")

# Questions tab
questions_frame = ctk.CTkFrame(master=questions_tab)
questions_frame.grid(row=0, column=0, padx=(20, 10), pady=(20, 10), sticky="nsew")

questions_label = ctk.CTkLabel(master=questions_frame, text="Answer Questions from Students", font=("Arial", 12))
questions_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

# Function to answer questions from students
def answer_question(student_id, question):
    # Save the answer to a file or database
    with open(f"answers/{student_id}.txt", "a") as f:
        f.write(f"Question: {question}\nAnswer: <Your answer>\n\n")
    ctk.messagebox.showinfo("Success", "Question answered successfully.")

def load_questions():
    questions_textbox.configure(state="normal")
    questions_textbox.delete("1.0", "end")
    for question_file in os.listdir("questions"):
        student_id = question_file.split(".")[0]
        with open(os.path.join("questions", question_file), "r") as f:
            question = f.read().strip()
            questions_textbox.insert("end", f"From {student_id}: {question}\n")
    questions_textbox.configure(state="disabled")

# Function to display student questions and answers
def display_questions_and_answers():
    load_questions()

# Answer question button
def on_answer_question():
    selected_text = questions_textbox.get("sel.first", "sel.last")
    if selected_text:
        selected_question = selected_text.split(":")[1].strip()
        student_id = selected_text.split(":")[0].split()[-1]
        answer_question(student_id, selected_question)
        load_questions()

answer_button = ctk.CTkButton(master=questions_frame, text="Answer Selected Question", command=on_answer_question)
answer_button.grid(row=1, column=0, padx=10, pady=10, sticky="w")

# Text widget to display questions
questions_textbox = ctk.CTkTextbox(master=questions_frame, wrap="word", state="disabled")
questions_textbox.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

# Answers tab
answers_frame = ctk.CTkFrame(master=answers_tab)
answers_frame.grid(row=0, column=0, padx=(20, 10), pady=(20, 10), sticky="nsew")

answers_label = ctk.CTkLabel(master=answers_frame, text="Student Questions and Answers", font=("Arial", 12))
answers_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

# Function to display student questions and answers
def display_questions_and_answers():
    answers_textbox.configure(state="normal")
    answers_textbox.delete("1.0", "end")
    for answer_file in os.listdir("answers"):
        with open(os.path.join("answers", answer_file), "r") as f:
            answers_textbox.insert("end", f.read())
            answers_textbox.insert("end", "\n\n")
    answers_textbox.configure(state="disabled")

# Text widget to display answers
answers_textbox = ctk.CTkTextbox(master=answers_frame, wrap="word", state="disabled")
answers_textbox.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

# Call the function to initially load questions and answers
display_questions_and_answers()

root.mainloop()
