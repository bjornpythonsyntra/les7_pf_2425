from tabulate import tabulate

# Startlijst met bestaande gegevens
data = [["Jan", 8, 7, 5], ["Piet", 9, 7, 4], ["Joris", 7, 8, 6]]


# Functie om een persoon toe te voegen aan de lijst
def voeg_persoon_toe():
    # Vraag de gebruiker om invoer
    naam = input("Geef de naam van de persoon: ")
    punten1 = int(input("Geef het punt van opdracht 1: "))
    punten2 = int(input("Geef het punt van opdracht 2: "))
    punten3 = int(input("Geef het punt van opdracht 3: "))

    # Voeg de nieuwe gegevens zonder de som toe aan de lijst
    data.append([naam, punten1, punten2, punten3])
    print(f"{naam} is toegevoegd met de punten: {punten1}, {punten2}, {punten3}.")


# Functie om de lijst met gegevens weer te geven en de som te berekenen
def toon_data():
    print("\nOverzicht van alle personen en hun punten:")
    tabel_data = []  # Maak een nieuwe lijst voor de tabel

    for persoon in data:
        # Controleer of er al een 4e kolom is, zo ja, overschrijf deze
        if len(persoon) == 5:
            persoon.pop()  # Verwijder de bestaande som

        # Bereken de som van de 2e, 3e en 4e kolom (punten)
        totaal_punten = sum(persoon[1:4])

        # Voeg de berekende som toe als nieuwe kolom
        persoon.append(totaal_punten)

        # Voeg de persoon toe aan de tabel_data lijst
        tabel_data.append(persoon)

    # Kolomnamen voor de tabel
    kolomnamen = ["Naam", "Punt 1", "Punt 2", "Punt 3", "Totaal_punten"]

    # Maak de tabel aan met tabulate
    print(tabulate(tabel_data, headers=kolomnamen, tablefmt="grid"))


# Functie om een persoon uit de lijst te verwijderen
def verwijder_persoon():
    naam = input("Geef de naam van de persoon die je wilt verwijderen: ")
    for persoon in data:
        if persoon[0] == naam:  # Controleer of de naam overeenkomt
            data.remove(persoon)  # Verwijder de persoon uit de lijst
            print(f"{naam} is verwijderd.")
            return
    print(f"Persoon met de naam {naam} is niet gevonden.")


# Voorbeeld van het gebruik van de functies
voeg_persoon_toe()
toon_data()
verwijder_persoon()
toon_data()
