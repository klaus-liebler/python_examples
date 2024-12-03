# Dies ist ein Nummern-Rate-Spiel
import random
secretNumber = random.randint(1, 20)
print("Ich habe mir gerade eine Zahl zwischen 1 und 20 ausgedacht :-)")

# Der Spieler darf sechsmal raten (range = exklusive dem Ende)
for guessesTaken in range(1, 7):
    guess = int(input("Raten Sie mal! "))
    if guess < secretNumber:
        print("Zu klein!")
    elif guess > secretNumber:
        print("Zu groß!")
    else:
        break    # Hier geht es rein, wenn weder zu groß, noch zu klein, also richtig!
if guess == secretNumber:
    print('Gut gemacht. Sie haben die richtige Zahl nach', guessesTaken, " Versuchen erraten.")
else:
    print('Leider haben Sie es nicht geschafft! Meine geheime Zahl war', secretNumber, '.')