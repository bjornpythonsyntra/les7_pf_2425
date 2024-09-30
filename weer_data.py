temp = [[12, 9, 6, 3, 3], [16, 16, 16, 14, 16]]

# Voeg het gemiddelde toe als een nieuwe kolom
for row in temp:
    #print(temp.index(row)) geeft index van rij
    average = sum(row) / len(row)  # Berekent het gemiddelde van de rij
    row.append(average)            # Voeg het gemiddelde toe aan de rij

print(temp)