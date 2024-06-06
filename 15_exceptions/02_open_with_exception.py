try:
    f = open("ich_existiere_nicht.txt")
    print(f.read())
except FileNotFoundError as e:
    print("Es gab einen FileNotFoundError mit der Meldung ", e.strerror)
print("Das Programm läuft weiter!")