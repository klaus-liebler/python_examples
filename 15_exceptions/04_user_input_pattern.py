zahl=0
while True:
    try:
        zahl = int(input("Bitte geben Sie eine Ganzzahl ein! "))
        break
    except ValueError:
        print("Uuups, nochmal probieren!")
print("Gute gemacht! Der Nachfolger der Zahl ist", zahl+1)