lijst_namen = ["Ben","Bart","Bert","Bent","Bart"]
lijst_namen.append("Bjorn")
lijst_namen.extend(["pieter","Peter"])
lijst_namen.insert(1,"Henk")
#lijst_namen.remove()#value based
#lijst_namen.pop()#index based
#lijst_namen.sort(reverse=True)#sorteren van z-a
#naam wijzigen
oude_naam = input("geef naam")
if oude_naam in lijst_namen:
    nieuwe_naam = input("geef nieuwe naam")
    plaats = lijst_namen.index(oude_naam)
    lijst_namen[plaats] = nieuwe_naam
else:
    print("De naam is niet in lijst")
print(lijst_namen)
