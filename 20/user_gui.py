import customtkinter
import sqlite3
import os

my_games_db_path = os.path.join(os.path.dirname(__file__), "my_games.db")

# Create a connection to the SQLite database
conn = sqlite3.connect(my_games_db_path)

# Create table if it doesn't exist
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS games
             (name text, rating real, genre text)''')
conn.commit()
c = conn.cursor()

# GUI functions
def add_game():
    new_game_name = game_entry.get()
    new_game_rating = float(game_rating_entry.get())
    new_game_genre = selected_genre.get()

    # Add new game
    c.execute("INSERT INTO games VALUES (?,?,?)", (new_game_name, new_game_rating, new_game_genre))
    conn.commit()
    print("Game added.")
    show_games()  # Refresh the games list after adding a new game

def show_game_advice():
    # Display game advice based on the user's preferences
    print("Showing game advice...")
    # Here you can implement the logic to display game advice in the advice_frame
    advice_label.config(text="Some game advice goes here.")

def show_games():
    # Clear the current games list
    for widget in games_frame.winfo_children():
        widget.destroy()

    # Fetch games from the database
    c.execute("SELECT name, rating FROM games")
    games = c.fetchall()

    # Display games in the list
    for i, (game_name, game_rating) in enumerate(games):
        game_label = customtkinter.CTkLabel(master=games_frame, text=f"{game_name} - Rating: {game_rating}", font=("Arial", 10))
        game_label.grid(row=i, column=0, padx=10, pady=5, sticky="w")

root = customtkinter.CTk()
root.geometry("800x600")
root.title("User GUI")

# Left side
left_frame = customtkinter.CTkFrame(master=root)
left_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

# Display the list of games
games_label = customtkinter.CTkLabel(master=left_frame, text="My Games", font=("Arial", 12))
games_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

games_frame = customtkinter.CTkFrame(master=left_frame)
games_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

show_games()  # Show games initially

# Right side
right_frame = customtkinter.CTkFrame(master=root)
right_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

# Add games
add_games_label = customtkinter.CTkLabel(master=right_frame, text="Add Games", font=("Arial", 12))
add_games_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

game_entry = customtkinter.CTkEntry(master=right_frame, placeholder_text="Game Name")
game_entry.grid(row=1, column=0, padx=10, pady=10, sticky="w")

game_rating_label = customtkinter.CTkLabel(master=right_frame, text="Rating", font=("Arial", 12))
game_rating_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")

game_rating_options = [str(i) for i in range(1, 6)]
game_rating_entry = customtkinter.CTkOptionMenu(master=right_frame, values=game_rating_options)
game_rating_entry.grid(row=3, column=0, padx=10, pady=10, sticky="w")

genre_label = customtkinter.CTkLabel(master=right_frame, text="Genre", font=("Arial", 12))
genre_label.grid(row=4, column=0, padx=10, pady=10, sticky="w")

selected_genre = customtkinter.StringVar()

for i, genre in enumerate(
    [
        "Action",
        "Adventure",
        "Role-playing",
        "Simulation",
        "Strategy",
        "MMO",
        "Sandbox / open world games",
    ]
):
    genre_radio = customtkinter.CTkRadioButton(master=right_frame, text=genre, variable=selected_genre, value=genre)
    genre_radio.grid(row=i + 5, column=0, padx=10, pady=5, sticky="w")

add_game_button = customtkinter.CTkButton(master=right_frame, text="Add Game", command=add_game)
add_game_button.grid(row=12, column=0, padx=10, pady=10, sticky="w")

# Game advice
game_advice_label = customtkinter.CTkLabel(master=right_frame, text="Game Advice", font=("Arial", 12))
game_advice_label.grid(row=13, column=0, padx=10, pady=10, sticky="w")

advice_frame = customtkinter.CTkFrame(master=right_frame)
advice_frame.grid(row=14, column=0, padx=10, pady=10, sticky="nsew")

advice_label = customtkinter.CTkLabel(master=advice_frame, text="", font=("Arial", 10))
advice_label.pack()

show_advice_button = customtkinter.CTkButton(master=right_frame, text="Show Advice", command=show_game_advice)
show_advice_button.grid(row=15, column=0, padx=10, pady=10, sticky="w")

root.mainloop()
