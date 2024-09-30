data = [
    ["Jan", 8, 7, 5],
    ["Piet", 9, 7, 4],
    ["Joris", 7, 8, 6]
]

# Voeg de som van de punten toe als een nieuwe kolom
for row in data:
    total = sum(row[1:])  # Bereken de som van de punten van kolom 2 t/m 4
    row.append(total)      # Voeg de som toe als nieuwe kolom

# Bekijk het resultaat
for rij in data:
    for item in rij:
        print(item,end="\t")
    print("")
print("")