lieblingstiere = ["Giraffe", "Elefant", "Frosch"]
liebingszahlen = [4, 64, 256]

print("Mein absolutes Lieblingstier ist ", lieblingstiere[0])
print("Mein Nicht-Lieblingstier ist ", lieblingstiere[len(lieblingstiere)-1])
print("Meine drittliebste Zahl ist ", liebingszahlen[2])

lieblingstiere = ["Giraffe", "Elefant", "Frosch"]
print("Mein zwanzigliebstes Tier ist ", lieblingstiere[19])

tiere_und_zahlen = [["Katze", "Hund"], [10,20,30,40]]
print(tiere_und_zahlen[0]) #["Katze", "Hund"]
print(tiere_und_zahlen[0][1]) #Hund

lieblingstiere = ["Giraffe", "Elefant", "Frosch"]
print(lieblingstiere[-1]) #Frosch
print(lieblingstiere[-2]) #Elefant

lieblingstiere = ["Giraffe", "Elefant", "Frosch"]
lieblingstiere[0] = "Krokodil"
print(lieblingstiere)