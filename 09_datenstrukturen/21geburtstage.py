geburtstage = {}
while True:
    name=input('Geben Sie den Namen ein: (Leer lassen zum Beenden): ')
    if name == '':
        break

    if name in geburtstage:
        print(geburtstage[name], ' ist der Geburtstag von ', name)
    else:
        print("Ich habe noch keine Info über", name)
        bday = input('Wann ist der Geburtstag?: ')
        geburtstage[name] = bday
        print('Datenbank aktualisiert!')
for i in geburtstage.items():
    print(i)