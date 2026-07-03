import tkinter as tk
from tkinter import ttk

# Recommendation Function
def recommend():
    genre = genre_var.get()

    recommendations = {
        "Action": "🎬 John Wick\n🎬 The Dark Knight\n🎬 Mad Max: Fury Road \n🎬 Die Hard\n🎬 Terminator 2: Judgment Day\n🎬 The Matrix\n🎬 Gladiator\n🎬 Mission: Impossible-Fallout\n🎬 Top Gun:Maverick\n🎬 The Raid(also known as The Raid: Redemption\n                    ",
        "Comedy": "😂 The Hangover\n😂 Superbad\n😂 Home Alone\n😂 3 Idiots\n😂 Monty Python and Holy Grail\n😂 Airplane\n😂 Groundhog Day\n😂 The Grand Budapest Hotel\n😂 Hot Fuzz\n😂 Borat",
        "Horror": "👻 The Exorcist\n👻 The Shining\n👻 Sinister\n👻 The Conjuring\n👻 Hereditary\n👻 The Texas Chain Saw Massacre\n👻 Alien\n👻 Halloween\n👻 Annabelle\n👻 The Ring",
        "Romance": "❤️ Titanic\n❤️ The Vow\n❤️ Pride & Prejudice\n❤️ Before Sunrise\n❤️ The Notebook\n❤️ A Walk to Remember\n❤️ Me Before You\n❤️ The Fault in Our Stars\n❤️ Your Name\n❤️ Eternal Sunshine of the Spotless Mind",
        "Sci-Fi": "🚀 Interstellar\n🚀 The Martian\n🚀 Arrival\n🚀 The Theory of Everything\n🚀 A Beautiful Mind\n🚀 2001: A Space Odyssey\n🚀 Contact\n🚀 Gravity\n🚀 Apollo 13\n🚀 Oppenheimer"
    }

    result_box.config(state="normal")
    result_box.delete("1.0", tk.END)
    result_box.insert(tk.END, recommendations.get(genre, "No recommendation available."))
    result_box.config(state="disabled")


def clear():
    genre_combo.set("Select Genre")
    result_box.config(state="normal")
    result_box.delete("1.0", tk.END)
    result_box.config(state="disabled")


# Main Window
root = tk.Tk()
root.title("Movie Recommendation System")
root.geometry("900x700")
root.config(bg="#BE63B0")
root.resizable(False, False)

# Title
title = tk.Label(
    root,
    text="🎥 Movie Recommendation System",
    font=("Segoe UI", 27, "bold"),
    bg="#1E293B",
    fg="white"
)
title.pack(pady=20)

# Select Genre
label = tk.Label(
    root,
    text="Choose Your Favourite Genre",
    font=("Arial", 18),
    bg="#1E293B",
    fg="white"
)
label.pack()

genre_var = tk.StringVar()

genre_combo = ttk.Combobox(
    root,
    textvariable=genre_var,
    values=["Action", "Comedy", "Horror", "Romance", "Sci-Fi"],
    state="readonly",
    font=("Arial", 15),
    width=35
)

genre_combo.set("Select Genre")
genre_combo.pack(pady=10)

# Buttons
frame = tk.Frame(root, bg="#1E293B")
frame.pack()

recommend_btn = tk.Button(
    frame,
    text="Recommend",
    font=("Arial", 16, "bold"),
    bg="#4F46E5",
    activebackground="#3730A3",
    fg="white",
    width=15,
    command=recommend
)

recommend_btn.grid(row=0, column=0, padx=10)

clear_btn = tk.Button(
    frame,
    text="Clear",
    font=("Arial", 12, "bold"),
    bg="#EF4444",
    activebackground="#B91C1C",
    fg="white",
    width=15,
    command=clear
)

clear_btn.grid(row=0, column=1, padx=10)

# Result
result_label = tk.Label(
    root,
    text="Recommended Movies",
    font=("Arial", 14, "bold"),
    bg="#1E293B",
    fg="white"
)
result_label.pack(pady=15)

result_box = tk.Text(
    root,
    width=45,
    height=10,
    font=("Calibri", 16),
    bg="#F8FAFC",
    fg="black",
    relief="solid",
    state="disabled"
)

result_box.pack()

root.mainloop()