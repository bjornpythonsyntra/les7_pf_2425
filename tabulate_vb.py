from tabulate import tabulate

# Gegeven data
data = [["Jan", 8, 7, 5], ["Piet", 9, 7, 4], ["Joris", 7, 8, 6]]

# Kolomnamen
kolomnamen = ["Naam", "Punt 1", "Punt 2", "Punt 3"]

# Maak de tabel aan
tabel = tabulate(data, headers=kolomnamen, tablefmt="fancy-grid")

# Print de tabel
print(tabel)
