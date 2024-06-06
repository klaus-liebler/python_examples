import random
secretNumber = random.randint(1, 20)
print("Ich habe mir gerade eine Zahl zwischen 1 und 20 ausgedacht :-)")
guessesTaken=1
while guessesTaken<=6:
    try:
        guess = int(input("Raten Sie mal! "))
        if guess < secretNumber:
            print("Zu klein!")
        elif guess > secretNumber:
            print("Zu groß!")
        else:
            break 
        guessesTaken=guessesTaken+1
    except ValueError:
        print("Bitte geben Sie nur natürliche Zahlen ein.")
if guess == secretNumber:
    print('Gut gemacht. Sie benötigten',guessesTaken,"Versuche.")
else:
    print("Leider verloren! Die geheime Zahl war ", secretNumber, ".")



    