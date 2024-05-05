import tkinter as tk
import webbrowser
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

movie_links = {}
movie_directors = {}
tv_links = {}
tv_directors = {}
movie_genres = {}
tv_genres = {}
def add_movie():
    movie_name = movie_name_entry.get()
    movie_link = movie_link_entry.get()
    movie_director = movie_director_entry.get()
    movie_genre = movie_genre_entry.get()
    if movie_name and movie_link and movie_director and movie_genre:
        movie_listbox.insert(tk.END, f"{movie_name} - {movie_genre} - Director: {movie_director}")
        movie_links[movie_name] = movie_link
        movie_directors[movie_name] = movie_director
        movie_genres[movie_name] = movie_genre
        movie_name_entry.delete(0, tk.END)
        movie_link_entry.delete(0, tk.END)
        movie_director_entry.delete(0, tk.END)
        movie_genre_entry.delete(0, tk.END)
        save_movies()

def delete_movie():
    selected_index = movie_listbox.curselection()
    if selected_index:
        selected_item = movie_listbox.get(selected_index)
        movie_name = selected_item.split(" - Director: ")[0]
        movie_listbox.delete(selected_index)
        del movie_links[movie_name]
        save_movies()

def on_movie_double_click(event):
    selected_index = movie_listbox.curselection()
    if selected_index:
        selected_item = movie_listbox.get(selected_index)
        movie_name = selected_item.split(" - ")[0]
        webbrowser.open(movie_links[movie_name])
        add_to_watching_history(selected_item)


def add_tv_series():
    tv_name = tv_name_entry.get()
    tv_link = tv_link_entry.get()
    tv_director = tv_director_entry.get()
    tv_genre = tv_genre_entry.get()
    if tv_name and tv_link and tv_director and tv_genre:
        tv_listbox.insert(tk.END, f"{tv_name} - {tv_genre} - Director: {tv_director}")
        tv_links[tv_name] = tv_link
        tv_directors[tv_name] = tv_director
        tv_genres[tv_name] = tv_genre
        tv_name_entry.delete(0, tk.END)
        tv_link_entry.delete(0, tk.END)
        tv_director_entry.delete(0, tk.END)
        tv_genre_entry.delete(0, tk.END)
        save_tv_series()


def delete_tv_series():
    selected_index = tv_listbox.curselection()
    if selected_index:
        selected_item = tv_listbox.get(selected_index)
        tv_name = selected_item.split(" - Director: ")[0]
        tv_listbox.delete(selected_index)
        del tv_links[tv_name]
        save_tv_series()

def on_tv_double_click(event):
    selected_index = tv_listbox.curselection()
    if selected_index:
        selected_item = tv_listbox.get(selected_index)
        tv_name = selected_item.split(" - Director: ")[0]
        if tv_name in tv_links:
            webbrowser.open(tv_links[tv_name])
            add_to_watching_history(selected_item)
        else:
            print(f"No link found for {tv_name}")

def add_to_watching_list():
    item_name = watching_list_entry.get()
    if item_name:
        watching_listbox.insert(tk.END, item_name)
        watching_list_entry.delete(0, tk.END)
        save_watching_list()


def on_watching_list_double_click(event):
    selected_index = watching_listbox.curselection()
    if selected_index:
        selected_item = watching_listbox.get(selected_index)

        # Try to find a match in Movies
        for index, movie_item in enumerate(movie_listbox.get(0, tk.END)):
            movie_name = movie_item.split(" - Director: ")[0]
            if selected_item.lower() == movie_name.lower():
                _, movie_link = movie_item.split(" - ")
                webbrowser.open(movie_link)
                return

        # Try to find a match in TV Series
        for index, tv_item in enumerate(tv_listbox.get(0, tk.END)):
            tv_name = tv_item.split(" - Director: ")[0]
            if selected_item.lower() == tv_name.lower():
                _, tv_link = tv_item.split(" - ")
                webbrowser.open(tv_link)
                return

        print(f"No match found for {selected_item}")

def save_movies():
    with open("movies.txt", "w") as file:
        for movie_item in movie_listbox.get(0, tk.END):
            movie_name, movie_genre, movie_director = movie_item.split(" - ")
            movie_link = movie_links[movie_name]
            movie_genres[movie_name] = movie_genre
            file.write(f"{movie_name} - Genre: {movie_genre} - Director: {movie_director} - Link: {movie_link}\n")

def load_movies():
    try:
        with open("movies.txt", "r") as file:
            movie_listbox.delete(0, tk.END)
            for line in file:
                movie_name, movie_genre, movie_director, movie_link = line.strip().split(" - ")
                movie_listbox.insert(tk.END, f"{movie_name} - {movie_genre} - Director: {movie_director}")
                movie_links[movie_name] = movie_link
                movie_directors[movie_name] = movie_director
                movie_genres[movie_name] = movie_genre
    except FileNotFoundError:
        pass
def save_tv_series():
    with open("tv_series.txt", "w") as file:
        for tv_item in tv_listbox.get(0, tk.END):
            tv_name, _, tv_genre, _, tv_director, _ = tv_item.split(" - ")
            tv_link = tv_links[tv_name]
            tv_genres[tv_name] = tv_genre
            file.write(f"{tv_name} - Genre: {tv_genre} - Director: {tv_director} - Link: {tv_link}\n")


def load_tv_series():
    try:
        with open("tv_series.txt", "r") as file:
            tv_listbox.delete(0, tk.END)
            for line in file:
                tv_name, _, tv_genre, _, tv_director, _, tv_link = line.strip().split(" - ")
                tv_listbox.insert(tk.END, f"{tv_name} - {tv_genre} - Director: {tv_director}")
                tv_links[tv_name] = tv_link
                tv_directors[tv_name] = tv_director
                tv_genres[tv_name] = tv_genre
    except FileNotFoundError:
        pass
def save_watching_list():
    with open("watching_list.txt", "w") as file:
        file.write("\n".join(watching_listbox.get(0, tk.END)) + "\n")

def load_watching_list():
    try:
        with open("watching_list.txt", "r") as file:
            watching_listbox.delete(0, tk.END)
            watching_listbox.insert(tk.END, *file.readlines())
    except FileNotFoundError:
        pass

def delete_watching_item():
    selected_index = watching_listbox.curselection()
    if selected_index:
        watching_listbox.delete(selected_index)
        save_watching_list()

def add_to_watching_history(item):
    watching_history_listbox.insert(tk.END, item)
    save_watching_history()

def check_in_watching_history(item):
    for i in watching_history_listbox.get(0, tk.END):
        if item in i:
            return True
    return False

def remove_from_watching_history(item):
    for index, i in enumerate(watching_history_listbox.get(0, tk.END)):
        if item in i:
            watching_history_listbox.delete(index)
            save_watching_history()
            break

def save_watching_history():
    with open("watching_history.txt", "w") as file:
        file.write("\n".join(watching_history_listbox.get(0, tk.END)) + "\n")

def load_watching_history():
    try:
        with open("watching_history.txt", "r") as file:
            history = file.readlines()
        watching_history_listbox.delete(0, tk.END)
        watching_history_listbox.insert(tk.END, *history)
    except FileNotFoundError:
        pass

def clear_watching_history():
    watching_history_listbox.delete(0, tk.END)
    open("watching_history.txt", "w").close()

root = customtkinter.CTk()
root.geometry("1900x750")
root.configure(bg=root.cget('bg'))  # Set background color of root window

# Watching History Column
watching_history_frame = customtkinter.CTkFrame(master=root)
watching_history_frame.pack(pady=20, padx=20, fill="both", expand=True, side=tk.RIGHT)

watching_history_label = customtkinter.CTkLabel(master=watching_history_frame, text="Watching History", font=("Arial", 24))
watching_history_label.grid(row=0, column=0, columnspan=2, pady=10, padx=10)

watching_history_listbox = tk.Listbox(master=watching_history_frame, height=15, bg=root.cget('bg'))  # Set background color of listbox
watching_history_listbox.grid(row=1, column=0, rowspan=2, padx=10)

clear_history_button = customtkinter.CTkButton(master=watching_history_frame, text="Clear History", command=clear_watching_history)
clear_history_button.grid(row=1, column=1, pady=10, padx=10)

load_watching_history()

# Movies Column
movie_frame = customtkinter.CTkFrame(master=root)
movie_frame.pack(pady=20, padx=20, fill="both", expand=True, side=tk.LEFT)

movie_label = customtkinter.CTkLabel(master=movie_frame, text="Movies", font=("Arial", 24))
movie_label.grid(row=0, column=0, columnspan=4, pady=10, padx=10)

movie_listbox = tk.Listbox(master=movie_frame, height=15, bg=root.cget('bg'))  # Set background color of listbox
movie_listbox.grid(row=1, column=0, rowspan=5, padx=10)
movie_listbox.bind("<Double-Button-1>", on_movie_double_click)

movie_name_label = customtkinter.CTkLabel(master=movie_frame, text="Movie Name:")
movie_name_label.grid(row=1, column=1, pady=10, padx=10, sticky="w")

movie_name_entry = customtkinter.CTkEntry(master=movie_frame, placeholder_text="Enter Movie Name")
movie_name_entry.grid(row=1, column=2, columnspan=2, pady=10, padx=10, sticky="ew")

movie_link_label = customtkinter.CTkLabel(master=movie_frame, text="Movie Link:")
movie_link_label.grid(row=2, column=1, pady=10, padx=10, sticky="w")

movie_link_entry = customtkinter.CTkEntry(master=movie_frame, placeholder_text="Enter Movie Link")
movie_link_entry.grid(row=2, column=2, columnspan=2, pady=10, padx=10, sticky="ew")

movie_director_label = customtkinter.CTkLabel(master=movie_frame, text="Director:")
movie_director_label.grid(row=3, column=1, pady=10, padx=10, sticky="w")

movie_director_entry = customtkinter.CTkEntry(master=movie_frame, placeholder_text="Enter Director Name")
movie_director_entry.grid(row=3, column=2, columnspan=2, pady=10, padx=10, sticky="ew")

movie_genre_label = customtkinter.CTkLabel(master=movie_frame, text="Genre:")
movie_genre_label.grid(row=4, column=1, pady=10, padx=10, sticky="w")

movie_genre_entry = customtkinter.CTkEntry(master=movie_frame, placeholder_text="Enter Genre")
movie_genre_entry.grid(row=4, column=2, columnspan=2, pady=10, padx=10, sticky="ew")

add_movie_button = customtkinter.CTkButton(master=movie_frame, text="Add Movie", command=add_movie)
add_movie_button.grid(row=5, column=1, pady=10, padx=10, sticky="w")

delete_movie_button = customtkinter.CTkButton(master=movie_frame, text="Delete Movie", command=delete_movie)
delete_movie_button.grid(row=5, column=2, pady=10, padx=10, sticky="w")

tv_frame = customtkinter.CTkFrame(master=root)
tv_frame.pack(pady=20, padx=20, fill="both", expand=True, side=tk.LEFT)

tv_label = customtkinter.CTkLabel(master=tv_frame, text="TV Series", font=("Arial", 24))
tv_label.grid(row=0, column=0, columnspan=4, pady=10, padx=10)

tv_listbox = tk.Listbox(master=tv_frame, height=15, bg=root.cget('bg'))  # Set background color of listbox
tv_listbox.grid(row=1, column=0, rowspan=5, padx=10)
tv_listbox.bind("<Double-Button-1>", on_tv_double_click)

tv_name_label = customtkinter.CTkLabel(master=tv_frame, text="TV Series Name:")
tv_name_label.grid(row=1, column=1, pady=10, padx=10, sticky="w")

tv_name_entry = customtkinter.CTkEntry(master=tv_frame, placeholder_text="Enter TV Series Name")
tv_name_entry.grid(row=1, column=2, columnspan=2, pady=10, padx=10, sticky="ew")

tv_link_label = customtkinter.CTkLabel(master=tv_frame, text="TV Series Link:")
tv_link_label.grid(row=2, column=1, pady=10, padx=10, sticky="w")

tv_link_entry = customtkinter.CTkEntry(master=tv_frame, placeholder_text="Enter TV Series Link")
tv_link_entry.grid(row=2, column=2, columnspan=2, pady=10, padx=10, sticky="ew")

tv_director_label = customtkinter.CTkLabel(master=tv_frame, text="Director:")
tv_director_label.grid(row=3, column=1, pady=10, padx=10, sticky="w")

tv_director_entry = customtkinter.CTkEntry(master=tv_frame, placeholder_text="Enter Director Name")
tv_director_entry.grid(row=3, column=2, columnspan=2, pady=10, padx=10, sticky="ew")

tv_genre_label = customtkinter.CTkLabel(master=tv_frame, text="Genre:")
tv_genre_label.grid(row=4, column=1, pady=10, padx=10, sticky="w")

tv_genre_entry = customtkinter.CTkEntry(master=tv_frame, placeholder_text="Enter Genre")
tv_genre_entry.grid(row=4, column=2, columnspan=2, pady=10, padx=10, sticky="ew")

add_tv_button = customtkinter.CTkButton(master=tv_frame, text="Add TV Series", command=add_tv_series)
add_tv_button.grid(row=5, column=1, pady=10, padx=10, sticky="w")

delete_tv_series_button = customtkinter.CTkButton(master=tv_frame, text="Delete TV Series", command=delete_tv_series)
delete_tv_series_button.grid(row=5, column=2, pady=10, padx=10, sticky="w")

# Watching List Column
watching_list_frame = customtkinter.CTkFrame(master=root)
watching_list_frame.pack(pady=20, padx=20, fill="both", expand=True, side=tk.LEFT)

watching_list_label = customtkinter.CTkLabel(master=watching_list_frame, text="Watching List", font=("Arial", 24))
watching_list_label.grid(row=0, column=0, columnspan=4, pady=10, padx=10)

watching_listbox = tk.Listbox(master=watching_list_frame, height=15, bg=root.cget('bg'))  # Set background color of listbox
watching_listbox.grid(row=1, column=0, rowspan=5, padx=10)
watching_listbox.bind("<Double-Button-1>", on_watching_list_double_click)

watching_list_label = customtkinter.CTkLabel(master=watching_list_frame, text="Enter Item Name:")
watching_list_label.grid(row=1, column=1, pady=10, padx=10, sticky="w")

watching_list_entry = customtkinter.CTkEntry(master=watching_list_frame, placeholder_text="Enter Item Name")
watching_list_entry.grid(row=1, column=2, columnspan=2, pady=10, padx=10, sticky="ew")

add_watching_list_button = customtkinter.CTkButton(master=watching_list_frame, text="Add to Watching List", command=add_to_watching_list)
add_watching_list_button.grid(row=2, column=1, pady=10, padx=10, sticky="w")

delete_watching_item_button = customtkinter.CTkButton(master=watching_list_frame, text="Delete Watching Item", command=delete_watching_item)
delete_watching_item_button.grid(row=2, column=2, pady=10, padx=10, sticky="w")

load_watching_list()


root.mainloop()
