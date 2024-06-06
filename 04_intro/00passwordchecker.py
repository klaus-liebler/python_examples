passwordFile = open("passwort.txt")
secretPassword=passwordFile.read()
typedPassword=input("Geben Sie das Passwort ein: ")
if typedPassword==secretPassword:
    print("Zugang gewährt!")
    receipeFile=open("geheimrezept.txt")
    print(receipeFile.read())
    if typedPassword=="1234":
        print("Sie verwenden ein dämliches Passwort!")
else:
    print("Zugang zum geheimen Rezeptebuch verweigert")