import tkinter as tk
import webbrowser
import customtkinter

def add_movie():
    movie_name = movie_name_entry.get()
    movie_link = movie_link_entry.get()
    if movie_name and movie_link:
        movie_listbox.insert(tk.END, f"{movie_name} - {movie_link}")
        movie_name_entry.delete(0, tk.END)
        movie_link_entry.delete(0, tk.END)
        save_movies()
