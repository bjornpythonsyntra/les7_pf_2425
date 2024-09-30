import tkinter as tk
from tkinter import ttk

# Gegeven data
data = [["Jan", 8, 7, 5], ["Piet", 9, 7, 4], ["Joris", 7, 8, 6]]


# Functie om de GUI op te zetten
def create_gui():
    # Hoofdvenster
    root = tk.Tk()
    root.title("Overzicht van Personen en Punten")

    # Tabel aanmaken met ttk.Treeview
    tree = ttk.Treeview(root, columns=("Naam", "Punt 1", "Punt 2", "Punt 3"), show="headings")

    # Kolomnamen instellen
    tree.heading("Naam", text="Naam")
    tree.heading("Punt 1", text="Punt 1")
    tree.heading("Punt 2", text="Punt 2")
    tree.heading("Punt 3", text="Punt 3")

    # Kolombreedtes instellen
    tree.column("Naam", width=100)
    tree.column("Punt 1", width=50)
    tree.column("Punt 2", width=50)
    tree.column("Punt 3", width=50)

    # Voeg de gegevens toe aan de tabel
    for persoon in data:
        tree.insert("", tk.END, values=persoon)

    # Plaats de tabel in het venster
    tree.pack(expand=True, fill='both')

    # Start de GUI
    root.mainloop()


# Roep de functie aan om de GUI te starten
create_gui()
