import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog, messagebox

# Beginlijst met gegevens
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

    # Voeg een knop toe om een persoon toe te voegen
    add_button = tk.Button(root, text="Voeg Persoon Toe", command=lambda: voeg_persoon(tree))
    add_button.pack(pady=10)

    # Start de GUI
    root.mainloop()


# Functie om een nieuw persoon toe te voegen aan de lijst en de tabel
def voeg_persoon(tree):
    # Vraag om gegevens
    naam = simpledialog.askstring("Naam", "Geef de naam van de persoon:")
    if naam is None:
        return  # Geen invoer, dus functie beëindigen

    try:
        punt1 = int(simpledialog.askinteger("Punt 1", "Geef het punt van opdracht 1:"))
        punt2 = int(simpledialog.askinteger("Punt 2", "Geef het punt van opdracht 2:"))
        punt3 = int(simpledialog.askinteger("Punt 3", "Geef het punt van opdracht 3:"))
    except TypeError:
        messagebox.showwarning("Ongeldige invoer", "Zorg ervoor dat je een geldig getal invoert.")
        return

    # Voeg de nieuwe gegevens toe aan de lijst
    new_person = [naam, punt1, punt2, punt3]
    data.append(new_person)

    # Voeg de nieuwe persoon toe aan de tabel
    tree.insert("", tk.END, values=new_person)

    # Bevestiging tonen
    messagebox.showinfo("Persoon Toegevoegd", f"{naam} is toegevoegd met de punten: {punt1}, {punt2}, {punt3}.")


# Roep de functie aan om de GUI te starten
create_gui()
